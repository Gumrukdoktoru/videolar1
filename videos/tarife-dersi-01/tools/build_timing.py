"""Build timing.json: scene slots, script-aligned word timings, caption phrases (number words shown as digits)."""
import json, re, subprocess, difflib, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
N = ROOT / "narration"
script = json.load(open(N / "script.json"))

PRE_FIRST = 1.6   # intro sting before first line
PRE = 0.45        # silence before each line
POST = 0.55       # breath after each line
OUTRO_HOLD = 3.0  # end card hold

def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)]).decode().strip())

def norm(w):
    w = w.lower().replace("’", "'")
    w = re.sub(r"[^\wçğıöşüâîû']", "", w)
    return w

NUM = {"1": "bir", "2": "iki", "3": "üç", "4": "dört", "5": "beş"}

scenes, words_all, t = [], [], 0.0
for i, s in enumerate(script):
    d = dur(N / f"{s['id']}.mp3")
    pre = PRE_FIRST if i == 0 else PRE
    post = (OUTRO_HOLD if i == len(script) - 1 else POST) + s.get("hold", 0)
    start = round(t, 3)
    audio_at = round(start + pre, 3)
    slot = round(pre + d + post, 3)
    text = re.sub(r"\[[^\]]+\]\s*", "", s["text"]).strip()
    swords = text.split()
    tx = json.load(open(N / "tx" / f"{s['id']}.json"))
    tw = [w for w in tx if w.get("text", "").strip()]
    a = [norm(w) for w in swords]
    b = [norm(NUM.get(w["text"].strip(".,!?"), w["text"])) for w in tw]
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    times = [None] * len(swords)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                times[i1 + k] = (tw[j1 + k]["start"], tw[j1 + k]["end"])
        elif j2 > j1:
            st, en = tw[j1]["start"], tw[j2 - 1]["end"]
            n = i2 - i1
            for k in range(n):
                times[i1 + k] = (st + (en - st) * k / n, st + (en - st) * (k + 1) / n)
    # fill gaps by interpolation
    for k in range(len(times)):
        if times[k] is None:
            prev = next((times[j] for j in range(k - 1, -1, -1) if times[j]), (0, 0))
            nxt = next((times[j] for j in range(k + 1, len(times)) if times[j]), (d, d))
            times[k] = (prev[1], max(prev[1], nxt[0]))
    sw = []
    for w, (st, en) in zip(swords, times):
        st = min(st, d); en = min(max(en, st + 0.05), d)
        sw.append({"w": w, "s": round(audio_at + st, 3), "e": round(audio_at + en, 3), "ls": round(pre + st, 3)})
    words_all.extend(sw)
    scenes.append({"id": s["id"], "title": s["title"], "start": start, "dur": slot,
                   "audio": f"narration/{s['id']}.mp3", "audio_at": audio_at, "audio_local": round(pre, 3),
                   "audio_dur": round(d, 3), "words": [{"w": x["w"], "t": x["ls"]} for x in sw]})
    t += slot

# spoken number phrases -> digits for on-screen captions (longest match first)
DISPLAY = [
    ("seksen dört ve seksen beşinci", "84 ve 85."), ("yetmiş iki ile seksen üç", "72 ile 83"), ("altmış sekiz ile yetmiş", "68 ile 70"),
    ("seksen altı ile seksen dokuz", "86 ile 89"), ("seksen dört ile doksan altı", "84 ile 96"), ("bir ile seksen üç", "1 ile 83"),
    ("yetmiş birinci", "71."), ("yetmiş yedinci", "77."), ("on dördüncü", "14."), ("on altıncı", "16."), ("on beşinci", "15."),
    ("on üçüncü", "13."), ("on yedinci", "17."), ("üçüncü genel kural", "3. genel kural"),
    ("ilk altı hanesi", "ilk 6 hanesi"), ("on iki haneli", "12 haneli"), ("yedi ve sekizinci", "7 ve 8."), ("dokuz ve onuncu", "9 ve 10."),
    ("son iki hane", "son 2 hane"), ("de ge ö", "DGÖ"), ("de te ö", "DTÖ"),
    ("ce e bölü e le", "ce/el"), ("ce te bölü le", "ct/l"), ("pe bölü se te", "p/st"), ("ce bölü ke", "c/k"),
    ("pe bölü a'yı", "p/a'yı"), ("pe bölü a", "p/a"), ("te je", "TJ"),
    ("sıfır virgül iki gramdır", "0,2 gramdır"), ("üç saniye", "3 saniye"), ("dört ifade", "4 ifade"),
    ("üç soru", "3 soru"), ("üç soruyla", "3 soruyla"),
]
DISPLAY.sort(key=lambda kv: -len(kv[0].split()))
DISPLAY = [(k.split(), v) for k, v in DISPLAY]
def bare(w):
    return re.sub(r"[^\wçğıöşüâîû']", "", w.replace("İ", "i").replace("I", "ı").lower())
merged, i = [], 0
while i < len(words_all):
    for key, val in DISPLAY:
        n = len(key)
        seg = words_all[i:i + n]
        if len(seg) == n and [bare(x["w"]) for x in seg] == key:
            tail = re.search(r"[.,!?:;]+$", seg[-1]["w"])
            merged.append({"w": val + (tail.group(0) if tail else ""), "s": seg[0]["s"], "e": seg[-1]["e"]})
            i += n
            break
    else:
        merged.append(words_all[i]); i += 1

# caption phrases: break on punctuation or ~40 chars
caps, cur = [], []
def flush():
    if cur:
        caps.append({"text": " ".join(x["w"] for x in cur), "s": cur[0]["s"], "e": cur[-1]["e"]})
        cur.clear()
scene_ends = {round(s["audio_at"] + s["audio_dur"], 3) for s in scenes}
for i, w in enumerate(merged):
    cur.append(w)
    txt = " ".join(x["w"] for x in cur)
    nxt = merged[i + 1] if i + 1 < len(merged) else None
    brk = (re.search(r"[.!?:;]$", w["w"]) and not re.search(r"(^|\s)\d+\.$", w["w"])) or (re.search(r",$", w["w"]) and len(txt) > 22) or len(txt) > 44
    if nxt and nxt["s"] - w["e"] > 0.6:
        brk = True
    if brk or nxt is None:
        flush()
for c in caps:
    c["e"] = round(c["e"] + 0.25, 3)
for a, b in zip(caps, caps[1:]):
    if a["e"] > b["s"]:
        a["e"] = b["s"]

out = {"total": round(t, 3), "scenes": scenes, "captions": caps}
json.dump(out, open(ROOT / "timing.json", "w"), ensure_ascii=False, indent=1)
print("total", round(t, 2))
for s in scenes:
    print(s["id"], s["start"], s["dur"], s["title"])
print("captions", len(caps))
