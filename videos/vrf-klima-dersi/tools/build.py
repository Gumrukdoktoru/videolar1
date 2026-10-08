"""Generate compositions/sNN.html and index.html from timing.json + scene definitions."""
import json, re, sys, html
from lib import ROOT, TIMING, SCENES, scene, icon

sys.path.insert(0, str(ROOT / "tools"))
ALL = {}
for mod in ("scenes_a", "scenes_b", "scenes_c"):
    try:
        ALL.update(__import__(mod).S)
    except ModuleNotFoundError:
        pass

(ROOT / "compositions").mkdir(exist_ok=True)
for sid, d in ALL.items():
    (ROOT / "compositions" / f"{sid}.html").write_text(scene(sid, d["body"], d["css"], d["js"], d["keys"], d.get("exit", True)))

TOTAL = round(TIMING["total"], 2)
HERO = {"s01", "s15"}

CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORUN & SÜREÇ", ["s02", "s03"]), ("ORTAK NOKTA & TUZAK", ["s04"]),
    ("KARŞILAŞTIRMA", ["s05"]), ("ÖNEMLİ SONUÇ", ["s06"]), ("4 TEKNİK KRİTER", ["s07", "s08", "s09", "s10", "s11"]),
    ("ESKİ BTB'LER", ["s12"]), ("KOÇUN TAVSİYESİ", ["s13"]), ("MİNİ QUIZ", ["s14"]), ("ÖZET", ["s15"]),
]

SHARED_CSS = r"""
:root {
  --bg:#071A45; --bg2:#0B2257; --panel:rgba(13,36,92,.92); --line:#2B4C9E; --fg:#EEF2FF; --muted:#AEBBE3;
  --accent:#3F6BFF; --accent2:#8FB2FF; --ms:#8FB2FF; --vrf:#33D9B2; --hot:#FF7A45; --cold:#4FC3F7;
  --onemli:#FFC53D; --dikkat:#FF9F43; --uyari:#FF4D5E; --ok:#2ED47A;
}
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:1920px; height:1080px; overflow:hidden; background:var(--bg); }
#root { position:relative; width:100%; height:100%; overflow:hidden; background:var(--bg); font-family:Montserrat, sans-serif; color:var(--fg); }
.kicker { font:700 24px 'JetBrains Mono', monospace; letter-spacing:.18em; color:var(--accent2); text-transform:uppercase; }
.h1 { font-family:'Archivo Black', sans-serif; font-size:66px; line-height:1.04; color:var(--fg); letter-spacing:-0.005em; margin-top:10px; }
.card { background:var(--panel); border:3px solid var(--line); border-radius:22px; box-shadow:0 26px 60px rgba(0,0,0,.38); }
.chip { display:inline-flex; align-items:center; gap:14px; font:700 26px Montserrat; color:var(--fg); background:rgba(63,107,255,.18);
  border:2px solid rgba(143,178,255,.55); border-radius:999px; padding:10px 24px; }
.chip .ico { color:var(--accent2); }
.ico { display:block; flex:none; }
.badge { display:inline-flex; align-items:center; gap:12px; padding:10px 24px 10px 14px; border-radius:14px; font:900 32px Montserrat;
  letter-spacing:.08em; box-shadow:0 10px 0 rgba(0,0,0,.28), 0 18px 40px rgba(0,0,0,.35); }
.badge .bi { display:flex; }
.badge-big { font-size:58px; padding:16px 40px 16px 24px; border-radius:20px; gap:18px; }
.b-onemli { background:var(--onemli); color:#2a1d00; }
.b-dikkat { background:var(--dikkat); color:#2b1300; }
.b-uyari { background:var(--uyari); color:#2a0a0e; }
.b-uyari .ico path:first-child { fill:#2a0a0e; }
.b-uyari .ico path:nth-child(2) { stroke:var(--uyari); }
.b-uyari .ico circle { fill:var(--uyari); }
.b-ipucu { background:#FFE27A; color:#2a2200; }
.b-soru { background:var(--accent); color:#fff; }
.b-tuzak { background:#14141A; color:#FFD400; border:6px solid transparent;
  background-image:linear-gradient(#14141A,#14141A), repeating-linear-gradient(-45deg,#FFD400 0 14px,#14141A 14px 28px);
  background-origin:border-box; background-clip:padding-box, border-box; }
svg text.svgl { font:700 22px Montserrat; fill:#AEBBE3; }
svg text.svgt { font:700 20px 'JetBrains Mono'; fill:#FFC53D; }
svg text.svgs { font:700 18px Montserrat; }
svg text.svga { font:700 18px 'JetBrains Mono'; fill:#021410; }

/* persistent chrome */
#bg { position:absolute; inset:0; overflow:hidden; }
#bg .grid { position:absolute; left:-200px; top:-200px; width:2320px; height:1480px; opacity:.55;
  background-image: linear-gradient(rgba(120,160,255,.10) 2px, transparent 2px), linear-gradient(90deg, rgba(120,160,255,.10) 2px, transparent 2px),
  linear-gradient(rgba(120,160,255,.05) 1px, transparent 1px), linear-gradient(90deg, rgba(120,160,255,.05) 1px, transparent 1px);
  background-size: 200px 200px, 200px 200px, 40px 40px, 40px 40px; }
#bg .glow { position:absolute; border-radius:50%; }
#bg .g1 { left:900px; top:-260px; width:1300px; height:1000px; background:radial-gradient(closest-side, rgba(63,107,255,.32), rgba(63,107,255,0)); }
#bg .g2 { left:-300px; top:420px; width:1100px; height:900px; background:radial-gradient(closest-side, rgba(51,217,178,.18), rgba(51,217,178,0)); }
#bg .ghost { position:absolute; left:1180px; top:560px; width:820px; height:560px; opacity:.09; }
#bg .vign { position:absolute; inset:0; background:radial-gradient(ellipse at 60% 45%, rgba(0,0,0,0) 55%, rgba(2,8,26,.55) 100%); }

#presenter-fig { position:absolute; left:-330px; top:300px; width:1100px; height:1100px; }
#presenter-fig .pwrap { position:absolute; inset:0; transform-origin:50% 100%; }
#presenter-fig img { position:absolute; inset:0; width:100%; height:100%; }
#presenter-fig .halo { position:absolute; left:250px; top:120px; width:660px; height:660px; border-radius:50%;
  background:radial-gradient(closest-side, rgba(63,107,255,.35), rgba(63,107,255,0)); }
#nameplate { position:absolute; left:96px; top:944px; display:flex; align-items:center; gap:16px; padding:12px 22px 12px 16px;
  background:rgba(4,14,40,.86); border:2px solid rgba(143,178,255,.5); border-radius:16px; }
#nameplate .nm { font:900 26px Montserrat; letter-spacing:.06em; color:var(--fg); }
#nameplate .rl { font:400 18px 'JetBrains Mono'; color:var(--accent2); letter-spacing:.1em; }
#nameplate .bars { display:flex; align-items:center; gap:5px; height:40px; }
#nameplate .bars i { display:block; width:7px; height:40px; border-radius:4px; background:var(--vrf); transform-origin:50% 50%; transform:scaleY(.15); }

#topbar { position:absolute; left:0; top:0; width:1920px; height:104px; }
#topbar .logo { position:absolute; left:96px; top:44px; height:58px; padding:8px 18px; background:#F4F7FF; border-radius:14px; display:flex; align-items:center; }
#topbar .logo img { height:40px; }
#topbar .meta { position:absolute; left:460px; top:58px; font:700 22px 'JetBrains Mono'; color:var(--muted); letter-spacing:.08em; }
#topbar .meta b { color:var(--fg); }
.chap { position:absolute; right:96px; top:47px; height:52px; }
.chap .cp { display:flex; align-items:center; gap:14px; height:52px; padding:0 22px; border-radius:999px; background:rgba(63,107,255,.22);
  border:2px solid rgba(143,178,255,.6); font:900 22px Montserrat; letter-spacing:.08em; color:var(--fg); white-space:nowrap; }
.chap .cp b { font:700 20px 'JetBrains Mono'; color:var(--vrf); }
#progress { position:absolute; left:0; top:0; width:1920px; height:8px; background:rgba(143,178,255,.15); }
#progress .fill { position:absolute; left:0; top:0; width:1920px; height:8px; background:linear-gradient(90deg,var(--accent),var(--vrf)); transform-origin:0 50%; transform:scaleX(0); }
#progress .tick { position:absolute; top:0; width:3px; height:8px; background:var(--bg); }
#sweep { position:absolute; left:0; top:120px; width:240px; height:800px; opacity:0;
  background:linear-gradient(90deg, rgba(63,107,255,0), rgba(143,178,255,.35), rgba(51,217,178,.0)); }

.cap { position:absolute; left:580px; top:930px; width:1240px; height:92px; display:flex; align-items:center; justify-content:center; }
.cap span { display:inline-block; max-width:1240px; text-align:center; font:700 34px/1.25 Montserrat; color:#F6F8FF; padding:10px 26px;
  background:rgba(3,11,34,.82); border-radius:14px; }
.cap span b { color:var(--vrf); font-weight:900; }
"""

KW = [r"VRF'yi", r"VRF'lerde", r"VRF", r"multi split", r"BTB'ler", r"BTB", r"tuzak", r"Elektronik Genleşme Vanası", r"inverter",
      r"dört", r"Dört", r"Hayır!", r"önemli", r"iptal", r"İsme değil, tekniğe bakın."]


def cap_html(text):
    t = html.escape(text)
    for k in KW:
        t = re.sub(r"(?<![\wçğıöşü])(" + re.escape(k) + r")(?![\wçğıöşü])", r"<b>\1</b>", t)
    t = re.sub(r"<b><b>(.*?)</b></b>", r"<b>\1</b>", t)
    return t


def sub(cid, inner_html, css, js, dur):
    return f"""<!doctype html>
<html lang="tr">
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>
        #{cid} {{ position:absolute; inset:0; pointer-events:none; }}
{css}
      </style>
      <div id="{cid}" data-composition-id="{cid}" data-width="1920" data-height="1080" data-duration="{dur}">
{inner_html}
      </div>
      <script>
(() => {{
  const tl = gsap.timeline({{ paused: true }});
{js}
  window.__timelines["{cid}"] = tl;
}})();
      </script>
    </template>
  </body>
</html>
"""


def rep(total, period):
    return f"Math.max(0, Math.floor({total} / {period}) - 1)"


# ---- captions sub-composition
caps = [
    f'<div id="cap-{i + 1:03d}" class="cap clip" data-start="{c["s"]}" data-duration="{round(max(0.3, c["e"] - c["s"]), 3)}" data-track-index="0"><span>{cap_html(c["text"])}</span></div>'
    for i, c in enumerate(TIMING["captions"])
]
CAP_JS = """
  document.querySelectorAll("#captions .cap span").forEach((c) => {
    const at = parseFloat(c.parentElement.dataset.start);
    tl.fromTo(c, { y: 14, opacity: 0 }, { y: 0, opacity: 1, duration: 0.18, ease: "power2.out" }, at);
  });
"""
(ROOT / "compositions" / "captions.html").write_text(sub("captions", "\n".join(caps), "", CAP_JS, TOTAL))

# ---- chrome sub-composition: top bar, chapter pills, progress, scene sweep
chap_html, ticks, chap_times = [], [], []
for i, (name, ids) in enumerate(CHAPTERS):
    st = SCENES[ids[0]]["start"]
    en = SCENES[ids[-1]]["start"] + SCENES[ids[-1]]["dur"]
    chap_times.append((name, st))
    chap_html.append(
        f'<div id="chap-{i + 1:02d}" class="chap clip" data-start="{st}" data-duration="{round(en - st, 3)}" data-track-index="1">'
        f'<div class="cp"><b>{i + 1:02d}/{len(CHAPTERS)}</b>{name}</div></div>'
    )
    if i:
        ticks.append(f'<i class="tick" style="left:{round(1920 * st / TOTAL, 1)}px"></i>')
seg_times = [s["start"] for s in TIMING["scenes"]][1:]
CHROME_HTML = f"""
<div id="sweep"></div>
<div id="topbar"><div class="logo"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div>
  <div class="meta">DERS · <b>VRF KLİMALAR</b> · GGM 01.10.2026</div></div>
{chr(10).join(chap_html)}
<div id="progress"><div class="fill"></div>{''.join(ticks)}</div>
"""
CHROME_JS = f"""
  const TOTAL = {TOTAL};
  tl.fromTo("#topbar .logo", {{ y: -90 }}, {{ y: 0, duration: 0.6, ease: "back.out(1.5)" }}, 0.4);
  tl.fromTo("#topbar .meta", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power2.out" }}, 0.7);
  tl.fromTo("#progress .fill", {{ scaleX: 0 }}, {{ scaleX: 1, duration: TOTAL, ease: "none" }}, 0);
  const CH = {json.dumps([t for _, t in chap_times])};
  document.querySelectorAll("#chrome .chap .cp").forEach((c, i) => {{
    tl.fromTo(c, {{ y: -70, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "back.out(1.7)" }}, CH[i] + 0.15);
  }});
  {json.dumps(seg_times)}.forEach((t) => {{
    tl.fromTo("#sweep", {{ x: 420 }}, {{ x: 1760, duration: 0.55, ease: "power2.inOut", immediateRender: false }}, t - 0.3);
    tl.fromTo("#sweep", {{ opacity: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.22 }}, {{ opacity: 0, duration: 0.33 }}], immediateRender: false }}, t - 0.3);
  }});
"""
(ROOT / "compositions" / "chrome.html").write_text(sub("chrome", CHROME_HTML, "", CHROME_JS, TOTAL))

# ---- presenter sub-composition
flat = []
for s in TIMING["scenes"]:
    ws = s["words"]
    for i, w in enumerate(ws):
        st = s["start"] + w["t"]
        en = s["start"] + (ws[i + 1]["t"] if i + 1 < len(ws) else s["audio_local"] + s["audio_dur"])
        flat.append([round(st, 3), round(min(en, st + 0.9), 3)])
seg = [[s["start"], "hero" if s["id"] in HERO else "corner"] for s in TIMING["scenes"]]
PRES_HTML = """
<div id="presenter-fig"><div class="halo"></div><div class="pwrap"><img src="assets/img/koc-cutout.png" alt="Gümrük Koçu" /></div></div>
<div id="nameplate"><div class="bars"><i></i><i></i><i></i><i></i><i></i></div><div><div class="nm">GÜMRÜK KOÇU</div><div class="rl">ANLATICI · DERS</div></div></div>
"""
PRES_JS = f"""
  const TOTAL = {TOTAL};
  const W = {json.dumps(flat)};
  const SEG = {json.dumps(seg)};
  const P = document.getElementById("presenter-fig");
  const PW = P.querySelector(".pwrap");
  const BARS = document.querySelectorAll("#nameplate .bars i");
  const HERO = {{ x: 135, y: 0, scale: 1.15 }};
  const CORNER = {{ x: 0, y: 0, scale: 1 }};
  tl.fromTo(P, {{ x: -700, y: 0, scale: 1.15, transformOrigin: "50% 100%" }}, {{ x: HERO.x, scale: HERO.scale, duration: 1.0, ease: "expo.out" }}, 0.2);
  for (let i = 1; i < SEG.length; i++) {{
    if (SEG[i][1] !== SEG[i - 1][1]) {{
      const tgt = SEG[i][1] === "hero" ? HERO : CORNER;
      tl.to(P, {{ x: tgt.x, y: tgt.y, scale: tgt.scale, duration: 0.9, ease: "power3.inOut" }}, SEG[i][0] - 0.35);
    }}
  }}
  tl.fromTo("#nameplate", {{ y: 120, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }}, 0.9);
  tl.fromTo("#presenter-fig .halo", {{ scale: 0.9, opacity: 0.6 }}, {{ scale: 1.08, opacity: 1, duration: 2.6, ease: "sine.inOut", yoyo: true, repeat: {rep('TOTAL', 2.6)} }}, 0);
  const st = {{ t: 0 }};
  tl.fromTo(st, {{ t: 0 }}, {{ t: TOTAL, duration: TOTAL, ease: "none", onUpdate: () => {{
    const t = st.t;
    let lo = 0, hi = W.length - 1, last = -1;
    while (lo <= hi) {{ const m = (lo + hi) >> 1; if (W[m][0] <= t) {{ last = m; lo = m + 1; }} else hi = m - 1; }}
    const speaking = last >= 0 && t < W[last][1] + 0.08;
    const since = last >= 0 ? t - W[last][0] : 9;
    const bob = speaking ? -6 * Math.max(0, 1 - since / 0.24) : 0;
    const env = speaking ? 1 : 0;
    const rot = 0.5 * Math.sin(t * 1.7) * (0.4 + 0.6 * env);
    const sy = 1 + 0.006 * Math.sin(t * 2 * Math.PI / 3.4) + 0.004 * env * Math.max(0, 1 - since / 0.3);
    PW.style.transform = `translateY(${{bob.toFixed(2)}}px) rotate(${{rot.toFixed(3)}}deg) scaleY(${{sy.toFixed(4)}})`;
    BARS.forEach((b, i) => {{
      const v = speaking ? 0.3 + 0.7 * Math.abs(Math.sin(t * (9 + i * 2.3) + i * 1.3)) * Math.max(0.35, 1 - since / 0.5) : 0.15;
      b.style.transform = `scaleY(${{v.toFixed(3)}})`;
    }});
  }} }}, 0);
"""
(ROOT / "compositions" / "presenter.html").write_text(sub("presenter", PRES_HTML, "", PRES_JS, TOTAL))

# ---- audio
audio = [
    f'<audio id="vo-{s["id"]}" src="{s["audio"]}" data-start="{s["audio_at"]}" data-duration="{round(s["audio_dur"] - 0.06, 3)}" data-track-index="10" data-volume="1"></audio>'
    for s in TIMING["scenes"]
]
sfx = []
for n, s in enumerate(TIMING["scenes"][1:], 1):
    sfx.append([f"sfx-w{n:02d}", "whoosh-short", round(s["start"] - 0.15, 3), None, 0.22])
import subprocess
SFX_DUR = {}
for f in (ROOT / "assets" / "sfx").glob("*.mp3"):
    SFX_DUR[f.stem] = round(min({"riser": 3.0}.get(f.stem, 99), float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]).decode()) - 0.02), 3)
for sid, d in ALL.items():
    for j, (name, t, vol) in enumerate(d.get("sfx", [])):
        sfx.append([f"sfx-{sid}-{j}", name, round(SCENES[sid]["start"] + t, 3), None, vol])
for x in sfx:
    x[3] = SFX_DUR[x[1]]
sfx.sort(key=lambda x: x[2])
lanes = []  # greedy lane assignment so no two sfx overlap on a track
for x in sfx:
    for li, end in enumerate(lanes):
        if end <= x[2]:
            lanes[li] = x[2] + x[3]; x.append(12 + li); break
    else:
        lanes.append(x[2] + x[3]); x.append(12 + len(lanes) - 1)
sfx_html = [
    f'<audio id="{i}" src="assets/sfx/{f}.mp3" data-start="{st}" data-duration="{du}" data-track-index="{tr}" data-volume="{v}"></audio>'
    for i, f, st, du, v, tr in sfx
]

BG_JS = f"""
  const TOTAL = {TOTAL};
  tl.fromTo("#bg .grid", {{ x: 0, y: 0 }}, {{ x: -200, y: -120, duration: TOTAL, ease: "none" }}, 0);
  tl.fromTo("#bg .g1", {{ scale: 1, opacity: 0.8 }}, {{ scale: 1.18, opacity: 1, duration: 4.2, ease: "sine.inOut", yoyo: true, repeat: {rep('TOTAL', 4.2)} }}, 0);
  tl.fromTo("#bg .g2", {{ scale: 1.1, x: 0 }}, {{ scale: 0.9, x: 120, duration: 6.4, ease: "sine.inOut", yoyo: true, repeat: {rep('TOTAL', 6.4)} }}, 0);
  tl.fromTo("#bg .ghost", {{ x: 0 }}, {{ x: -160, duration: TOTAL, ease: "none" }}, 0);
"""
(ROOT / "compositions" / "background.html").write_text(sub("background", '<div id="bg"><div class="grid"></div><div class="glow g1"></div><div class="glow g2"></div><svg class="ghost" viewBox="0 0 820 560" aria-hidden="true"><g fill="none" stroke="#8FB2FF" stroke-width="10"><rect x="10" y="10" width="800" height="540" rx="40"/><circle cx="290" cy="280" r="190"/><circle cx="290" cy="280" r="30"/><path d="M290 280 Q 420 210 440 280 Q 380 320 290 280z M290 280 Q 230 400 170 360 Q 200 300 290 280z M290 280 Q 220 160 280 120 Q 320 190 290 280z"/><path d="M580 80 V 480 M640 80 V 480 M700 80 V 480 M760 80 V 480"/></g></svg><div class="vign"></div></div>', "", BG_JS, TOTAL))

parts = [f'<div id="host-background" class="clip" data-composition-id="background" data-composition-src="compositions/background.html" data-start="0" data-duration="{TOTAL}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>']
for s in TIMING["scenes"]:
    if s["id"] not in ALL:
        continue
    parts.append(
        f'<div id="host-{s["id"]}" class="clip" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html" '
        f'data-start="{s["start"]}" data-duration="{s["dur"]}" data-track-index="2" data-track-kind="graphics" data-width="1920" data-height="1080"></div>'
    )
for cid, tr in (("presenter", 3), ("chrome", 4), ("captions", 5)):
    parts.append(
        f'<div id="host-{cid}" class="clip" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" '
        f'data-start="0" data-duration="{TOTAL}" data-track-index="{tr}" data-track-kind="{"captions" if cid == "captions" else "graphics"}" data-width="1920" data-height="1080"></div>'
    )
hosts = "\n    ".join(parts)

INDEX = f"""<!doctype html>
<html lang="tr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>VRF Klimalar — Gümrük Koçu Ders</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>{SHARED_CSS}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
    {hosts}
    {chr(10).join("    " + a for a in audio)}
    {chr(10).join("    " + a for a in sfx_html)}
    </div>
    <script>
(() => {{
  const TOTAL = {TOTAL};
  const tl = gsap.timeline({{ paused: true }});
  window.__timelines["main"] = tl;
}})();
    </script>
  </body>
</html>
"""
(ROOT / "index.html").write_text(INDEX)


# YouTube chapters + SRT
def ts(t):
    m, s = divmod(int(t), 60)
    return f"{m}:{s:02d}"
YT = ["Giriş", "Sorun ve süreç", "Ortak nokta ve tuzak", "Multi-split ve VRF karşılaştırması", "Önemli sonuç",
      "4 teknik kriter", "Eski BTB'ler", "Koçun tavsiyesi", "Mini quiz", "Özet"]
yt = "\n".join(f"{ts(t)} {YT[i]}" for i, (name, t) in enumerate(chap_times))
(ROOT / "youtube-bolumler.txt").write_text(yt + "\n")

def srt_t(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"
srt = "\n".join(f"{i + 1}\n{srt_t(c['s'])} --> {srt_t(c['e'])}\n{c['text']}\n" for i, c in enumerate(TIMING["captions"]))
(ROOT / "altyazi.srt").write_text(srt)
print("built", len(ALL), "scenes; total", TOTAL)
