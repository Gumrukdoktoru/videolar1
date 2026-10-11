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
# spoken phrase -> on-screen form; common phrases + per-video list in narration/display.json
DISPLAY = [
    ("üç saniye", "3 saniye"), ("üç soru", "3 soru"), ("üç soruyla", "3 soruyla"), ("üç kuralı", "3 kuralı"),
    ("de ge ö", "DGÖ"), ("de te ö", "DTÖ"),
]
if (N / "display.json").exists():
    DISPLAY += [tuple(x) for x in json.load(open(N / "display.json"))]
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
            if seg[0]["w"][:1].isupper() and val[:1].islower():
                val = ("İ" if val[0] == "i" else val[0].upper()) + val[1:]
            merged.append({"w": val + (tail.group(0) if tail else ""), "s": seg[0]["s"], "e": seg[-1]["e"], "tail": bool(tail)})
            i += n
            break
    else:
        merged.append(words_all[i]); i += 1

# spoken Turkish numbers -> digits ("on iki bin üç yüz yirmi" -> 12.320, "yüzde yirmi" -> %20, "bir virgül beş" -> 1,5)
NUMW = {"sıfır": 0, "bir": 1, "iki": 2, "üç": 3, "dört": 4, "dörd": 4, "beş": 5, "altı": 6, "yedi": 7, "sekiz": 8, "dokuz": 9,
        "on": 10, "yirmi": 20, "otuz": 30, "kırk": 40, "elli": 50, "altmış": 60, "yetmiş": 70, "seksen": 80, "doksan": 90,
        "yüz": 100, "bin": 1000, "milyon": 1000000}
SUFFIX = {"e", "a", "ye", "ya", "de", "da", "te", "ta", "den", "dan", "ten", "tan", "i", "ı", "u", "ü", "yi", "yı", "yu", "yü",
          "si", "sı", "su", "sü", "in", "ın", "un", "ün", "nin", "nın", "nun", "nün", "le", "la", "yle", "yla", "dir", "dır", "dur", "dür",
          "tir", "tır", "tur", "tür", "lik", "lık", "luk", "lük", "lık", "dı", "di", "du", "dü", "tı", "ti", "tu", "tü"}
OPW = {"çarpı": "×", "artı": "+", "bölü": "÷"}


def numtok(w, first):
    """(value_word, suffix) if token w is a number word (optionally with a case suffix), else None."""
    b = bare(w)
    if b in ("yüzde", "binde"):
        return None
    if b in NUMW:
        return b, ""
    for k in sorted(NUMW, key=len, reverse=True):
        if b.startswith(k) and b[len(k):] in SUFFIX and (not first or NUMW[k] >= 20):
            return k, b[len(k):]
    return None


def numval(ws):
    total = cur = 0
    for x in ws:
        v = NUMW[x]
        if v == 100:
            cur = (cur or 1) * 100
        elif v >= 1000:
            total += (cur or 1) * v
            cur = 0
        else:
            cur += v
    return total + cur


def grp(n):
    return f"{n:,}".replace(",", ".")


out, i = [], 0
while i < len(merged):
    w = merged[i]
    b = bare(w["w"])
    if b in OPW and not re.search(r"[^\wçğıöşüâîû']$", w["w"].rstrip(".,!?:;")):
        out.append(dict(w, w=OPW[b] + w["w"][len(w["w"].rstrip(".,!?:;")):])); i += 1; continue
    pct = b == "yüzde" and i + 1 < len(merged) and numtok(merged[i + 1]["w"], False) is not None and not re.search(r"[.,!?:;]$", w["w"])
    j = i + 1 if pct else i
    words, suf, dec, k = [], "", None, j
    while k < len(merged):
        nt = numtok(merged[k]["w"], first=not words and not pct)
        if nt is None:
            break
        words.append(nt[0]); suf = nt[1]; k += 1
        if suf or re.search(r"[.,!?:;]$", merged[k - 1]["w"]):
            break
    if words and not suf and k < len(merged) - 1 and bare(merged[k]["w"]) == "virgül" and not re.search(r"[.,!?:;]$", merged[k - 1]["w"]):
        fw, k2 = [], k + 1
        while k2 < len(merged):
            nt = numtok(merged[k2]["w"], False)
            if nt is None:
                break
            fw.append(nt[0]); suf = nt[1]; k2 += 1
            if suf or re.search(r"[.,!?:;]$", merged[k2 - 1]["w"]):
                break
        if fw:
            dec = str(numval(fw)); k = k2
    if not words or (not pct and dec is None and len(words) == 1 and NUMW[words[0]] < 10):
        out.append(w); i += 1; continue
    v = numval(words)
    txt = (str(v) if 2000 < v < 2100 and words[:2] == ["iki", "bin"] and len(words) > 2 else grp(v)) + ("," + dec if dec else "")
    if pct:
        txt = "%" + txt
    if suf:
        txt += "'" + suf
    last = merged[k - 1]["w"]
    tail = re.search(r"[.,!?:;]+$", last)
    out.append({"w": txt + (tail.group(0) if tail else ""), "s": merged[i]["s"], "e": merged[k - 1]["e"], "tail": bool(tail)})
    i = k
merged = out

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
    brk = (re.search(r"[.!?:;]$", w["w"]) and (w.get("tail") or not re.search(r"(^|\s)\d+\.$", w["w"]))) or (re.search(r",$", w["w"]) and len(txt) > 22) or len(txt) > 44
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
