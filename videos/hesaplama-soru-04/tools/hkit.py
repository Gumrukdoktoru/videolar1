"""Reusable scene templates for the one-question tax-calculation lessons (Gümrük Koçu · Vergi Hesaplama Dersleri).

Every template takes a scene id + content + word anchors; an anchor is a script word ("Cevap"), a (word, n) tuple for
the n-th occurrence, a "prefix*" word, or a number (scene-local seconds). Templates register into S[sid].
"""
from lib import T, D, SCENES, icon, badge

S = {}
STEP_NAMES = ["ADIM 1", "ADIM 2", "ADIM 3", "SONUÇ"]  # set per video

CHAR = {  # cutout file, display name, natural aspect (w/h)
    "stajyer": ("stajyer-cut", "STAJYER", 403 / 1150),
    "yardimci": ("yardimci-cut", "YARDIMCI", 565 / 1150),
    "baba": ("baba-crop", "GÜMRÜKÇÜ BABA", 759 / 1882),
    "cano": ("cano-cut", "CANO", 523 / 1143),
}


def A(sid, a, off=0.0):
    if a is None:
        return None
    if isinstance(a, (int, float)):
        return round(a + off, 2)
    if isinstance(a, tuple):
        return T(sid, a[0], a[1], off)
    return T(sid, a, 1, off)


def aud_end(sid):
    s = SCENES[sid]
    return round(s["audio_local"] + s["audio_dur"], 2)


def scoped(sid, css):
    return css.replace("#S ", f"#{sid} ")


def fmt(v, dec=0):
    s = f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s


COMMON_CSS = r"""
#S .top { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:24px; }
#S .top .kicker { font-size:26px; }
#S .chr { position:absolute; filter:drop-shadow(0 18px 30px rgba(0,0,0,.45)); }
#S .ctag { position:absolute; font:900 19px Montserrat; letter-spacing:.08em; color:#071A45; background:var(--accent2);
  padding:6px 14px; border-radius:10px; box-shadow:0 8px 20px rgba(0,0,0,.35); white-space:nowrap; transform:translateX(-50%); }
#S .bub { position:absolute; padding:14px 18px; background:#F4F7FF; color:#0B1A44; border-radius:20px; font:900 23px/1.25 Montserrat;
  box-shadow:0 16px 36px rgba(0,0,0,.35); }
#S .bub:after { content:""; position:absolute; left:var(--tail, 120px); bottom:-22px; border:12px solid transparent; border-top:14px solid #F4F7FF; }
#S .bub em { font-style:normal; color:#B4231B; }
#S .bub i { font-style:normal; color:#0B8A47; }
#S .hayir { position:absolute; padding:8px 20px; border:6px solid var(--uyari); border-radius:14px; color:var(--uyari);
  font-family:'Archivo Black'; font-size:44px; line-height:1; background:rgba(7,26,69,.92); transform:rotate(-8deg); white-space:nowrap; }
"""


def person(ch, h, cx, bottom, bubble=None, bub_left=None, bub_top=None, bub_w=290, tail=120, cls="p1"):
    """Character cutout centred at cx with its feet at `bottom`, a name tag and an optional speech bubble."""
    f, name, ar = CHAR[ch]
    w = round(ar * h)
    out = (f'<img class="chr {cls}" src="assets/img/{f}.png" alt="{name}" style="height:{h}px; left:{cx - w // 2}px; top:{bottom - h}px" />'
           f'<span class="ctag {cls}t" style="left:{cx}px; top:{bottom + 6}px">{name}</span>')
    if bubble:
        out += (f'<div class="bub {cls}b" style="left:{bub_left if bub_left is not None else cx - 150}px; top:{bub_top if bub_top is not None else bottom - h - 130}px;'
                f' width:{bub_w}px; --tail:{tail}px">{bubble}</div>')
    return out


PERSON_JS = r"""
function personIn(cls, at, bubAt) {
  tl.fromTo(q(".chr." + cls), { x: 260, opacity: 0 }, { x: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }, at);
  rise("." + cls + "t", at + 0.45, 0, 16);
  if (bubAt != null) tl.fromTo(q(".bub." + cls + "b"), { scale: 0.3, opacity: 0, transformOrigin: "40% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, bubAt);
}
"""


# ------------------------------------------------------------------ step tracker + ledger
def steps(active):
    out = []
    for i, n in enumerate(STEP_NAMES, 1):
        st = "done" if i < active else "on" if i == active else ""
        mark = icon("check", 26) if i < active else f"<b>{i}</b>"
        out.append(f'<div class="stp {st}"><span class="dot">{mark}</span>{n}</div>')
        if i < len(STEP_NAMES):
            out.append('<i class="bar"></i>')
    return f'<div class="steps">{"".join(out)}</div>'


STEPS_CSS = r"""
#S .steps { position:absolute; left:600px; top:128px; width:1220px; display:flex; align-items:center; gap:0; }
#S .steps .stp { display:flex; align-items:center; gap:12px; font:900 22px Montserrat; letter-spacing:.06em; color:#7E8DBA; white-space:nowrap; }
#S .steps .stp .dot { width:44px; height:44px; border-radius:50%; display:flex; align-items:center; justify-content:center; border:3px solid #3A5296; font:700 22px 'JetBrains Mono'; color:#7E8DBA; }
#S .steps .stp.done { color:#AEBBE3; } #S .steps .stp.done .dot { background:var(--teal); border-color:var(--teal); color:#03221a; }
#S .steps .stp.on { color:var(--fg); } #S .steps .stp.on .dot { background:var(--gold); border-color:var(--gold); color:#2a1d00; box-shadow:0 0 0 8px rgba(255,197,61,.18); }
#S .steps .bar { flex:1; height:4px; margin:0 16px; background:#2B4C9E; border-radius:2px; }
"""

LEDGER_CSS = r"""
#S .ledger { position:absolute; left:1380px; top:236px; width:440px; height:640px; background:#FBF8EE; border-radius:16px; padding:22px 26px 0 64px;
  box-shadow:0 26px 60px rgba(0,0,0,.4); color:#1B2A57; overflow:hidden;
  background-image:linear-gradient(90deg, transparent 46px, #F2A0A0 46px, #F2A0A0 49px, transparent 49px), repeating-linear-gradient(#FBF8EE 0 89px, #C9D6EE 89px 91px); }
#S .ledger .lh { display:flex; align-items:center; gap:12px; font:900 22px Montserrat; letter-spacing:.1em; color:#2B47A8; height:70px; margin-top:-6px; }
#S .ledger .lh small { margin-left:auto; font:700 18px 'JetBrains Mono'; color:#5A6AA0; }
#S .ledger .ln { position:relative; display:flex; align-items:baseline; gap:10px; height:91px; padding-top:36px; }
#S .ledger .ln .lb { font:800 24px Montserrat; white-space:nowrap; }
#S .ledger .ln .dots { flex:1; border-bottom:3px dotted #8C9BC4; transform:translateY(-6px); }
#S .ledger .ln .vl { font:700 27px 'JetBrains Mono'; color:#0B6B4F; white-space:nowrap; }
#S .ledger .ln.pen .vl { color:#B4231B; }
#S .ledger .ln.q .vl { color:#B47A00; }
#S .ledger .ln.out .lb, #S .ledger .ln.out .vl { color:#7D88A8; text-decoration:line-through; text-decoration-color:#B4231B; text-decoration-thickness:3px; }
#S .ledger .ln.tot { border-top:4px solid #1B2A57; }
#S .ledger .ln.tot .lb { color:#B4231B; } #S .ledger .ln.tot .vl { color:#B4231B; font-size:30px; }
"""


def ledger(lines, unit="TL"):
    rows = "".join(f'<div class="ln r{i} {cls}"><span class="lb">{lab}</span><span class="dots"></span><span class="vl">{val}</span></div>'
                   for i, (lab, val, cls) in enumerate(lines))
    return f'<div class="ledger"><div class="lh">{icon("pen", 30)}ÇÖZÜM DEFTERİ<small>{unit}</small></div>{rows}</div>'


# ------------------------------------------------------------------ s01 intro
def intro(sid, num, ordinal, kicker, title_html, chips, qq_html, *, art="calc", at_bugun="Bugünün", at_qq, at_tz=None):
    """chips: [(text, anchor)] up to 4."""
    k = dict(hello=A(sid, "Merhaba"), iki=A(sid, ordinal), bugun=A(sid, at_bugun), ch=[A(sid, c[1]) for c in chips], qq=A(sid, at_qq),
             tz=A(sid, at_tz), kagit=A(sid, "Kâğıt"))
    S[sid] = dict(
        sfx=[("pop", 0.15, 0.35), ("whoosh-short", k["bugun"] - 0.2, 0.3)] + [("pop", t, 0.25) for t in k["ch"]]
            + [("ping", k["qq"], 0.3), ("pop", k["kagit"], 0.3)] + ([("impact-bass-1", k["tz"], 0.3)] if at_tz else []),
        keys=k,
        css=scoped(sid, r"""
#S .sting { position:absolute; left:1060px; top:420px; width:640px; height:150px; display:flex; align-items:center; justify-content:center;
  background:#F4F7FF; border-radius:26px; box-shadow:0 30px 80px rgba(0,0,0,.45); }
#S .sting img { width:520px; }
#S .right { position:absolute; left:860px; top:150px; width:960px; }
#S .t1 { font-family:'Archivo Black'; font-size:80px; white-space:nowrap; line-height:1; color:var(--fg); margin-top:16px; }
#S .t2 { display:flex; align-items:baseline; gap:22px; margin-top:8px; white-space:nowrap; }
#S .t2 .w { font-family:'Archivo Black'; font-size:128px; line-height:1; color:var(--gold); text-shadow:0 10px 40px rgba(255,197,61,.35); }
#S .t2 .s { font:800 30px Montserrat; color:var(--muted); }
#S .topic { position:absolute; left:860px; top:560px; width:960px; height:300px; display:flex; align-items:center; gap:30px; padding:0 34px; }
#S .topic .art { flex:none; width:170px; height:170px; border-radius:40px; display:flex; align-items:center; justify-content:center;
  background:rgba(255,197,61,.12); border:3px solid rgba(255,197,61,.6); color:var(--gold); }
#S .topic .tx small { display:block; font:700 22px 'JetBrains Mono'; color:var(--accent2); letter-spacing:.14em; }
#S .topic .tx > b { display:block; font:900 42px/1.1 Montserrat; color:var(--fg); margin-top:6px; white-space:nowrap; }
#S .topic .tx > b em { font-style:normal; color:var(--teal); }
#S .chips { display:flex; gap:12px; margin-top:16px; }
#S .chips span { font:800 22px Montserrat; padding:6px 14px; border-radius:12px; white-space:nowrap; }
#S .chips .c0 { background:rgba(51,217,178,.14); border:2px solid var(--teal); color:#C9FFF0; }
#S .chips .c1 { background:rgba(255,197,61,.16); border:2px solid var(--gold); color:var(--gold); }
#S .chips .c2 { background:rgba(255,77,94,.14); border:2px solid var(--uyari); color:#FFC9CF; }
#S .chips .c3 { background:rgba(46,212,122,.14); border:2px solid var(--ok); color:#CFFFE5; }
#S .qq { margin-top:16px; font:800 26px Montserrat; color:var(--muted); white-space:nowrap; }
#S .qq b { color:var(--gold); display:inline-block; }
#S .tz { position:absolute; right:-18px; top:-30px; }
#S .ready { position:absolute; left:1250px; top:876px; }
"""),
        body=f'''
<div class="sting"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div>
<div class="right">
  <div class="kicker k1">GÜMRÜK KOÇU · HESAPLAMA DERSLERİ</div>
  <div class="t1">VERGİ HESAPLAMA</div>
  <div class="t2"><span class="w">DERS #{num}</span><span class="s">örnek soru · adım adım</span></div>
</div>
<div class="topic card">
  <div class="art">{icon(art, 110)}</div>
  <div class="tx"><small>{kicker}</small><b>{title_html}</b>
    <div class="chips">{"".join(f'<span class="c{i}">{c[0]}</span>' for i, c in enumerate(chips))}</div>
    <div class="qq">{qq_html}</div></div>
  {f'<div class="tz">{badge("tuzak")}</div>' if at_tz else ''}
</div>
<div class="ready chip">{icon("pen", 32)} Kâğıt + kalem hazır mı? {icon("calc", 32)}</div>
''',
        js=r"""
tl.fromTo(q(".sting"), { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.6, ease: "back.out(1.8)" }, 0.15);
tl.to(q(".sting"), { scale: 0.85, opacity: 0, y: -40, duration: 0.45, ease: "power2.in" }, K.hello - 0.35);
rise(".right .k1", K.hello, 0, 20);
tl.fromTo(q(".t1"), { y: 70, opacity: 0, skewY: 4 }, { y: 0, opacity: 1, skewY: 0, duration: 0.7, ease: "expo.out" }, K.hello + 0.2);
tl.fromTo(q(".t2 .w"), { scale: 2.4, opacity: 0, transformOrigin: "0% 60%" }, { scale: 1, opacity: 1, duration: 0.5, ease: "expo.in" }, K.iki);
rise(".t2 .s", K.iki + 0.5, 0, 20);
tl.fromTo(q(".topic"), { y: 220, opacity: 0, rotation: 2 }, { y: 0, opacity: 1, rotation: 0, duration: 0.8, ease: "expo.out" }, K.bugun);
breathe(".topic .art", K.bugun + 0.8, D - 0.6, 0.05, 2.4);
K.ch.forEach((t, i) => pop(".chips .c" + i, t, 0, "back.out(2.6)"));
rise(".topic .qq", K.qq, 0, 20);
pulse(".topic .qq b", K.qq + 0.7, 1.1);
if (K.tz != null) slam(".topic .tz", K.tz);
tl.fromTo(q(".ready"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "back.out(2)" }, K.kagit);
tl.fromTo(q(".ready .ico"), { rotation: 0 }, { rotation: 14, duration: 0.2, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 50%" }, K.kagit + 0.5);
""")


# ------------------------------------------------------------------ s02 question + data
RATE_COL = {"gv": "var(--gold)", "kdv": "var(--teal)", "igv": "var(--uyari)", "ok": "var(--ok)", "acc": "var(--accent2)", "usd": "var(--usd)"}


def question(sid, title, det, cards, rates, who, ask, *, at_once="Önce"):
    """det: dict(icon, head, sub, stamp, at, at_stamp); cards: [(kicker, value_html, sub_html, icon, anchor)] (≤4);
    rates: [(label, value, colour_key, anchor)] (≤5); who: dict(char, tag, bubble, at, at_bub); ask: (html, anchor)."""
    k = dict(once=A(sid, at_once), det=A(sid, det["at"]), stamp=A(sid, det.get("at_stamp")), cards=[A(sid, c[4]) for c in cards],
             rates=[A(sid, r[3]) for r in rates], who=A(sid, who["at"]), bub=A(sid, who["at_bub"]), ask=A(sid, ask[1]))
    ch = who["char"]
    f, name, ar = CHAR[ch]
    h = 440
    w = round(ar * h)
    cx = 1690
    sfx = [("whoosh-short", k["det"] - 0.1, 0.3)] + [("pop", t, 0.28) for t in k["cards"]] + [("pop", t, 0.25) for t in k["rates"]] \
        + [("ping", k["bub"], 0.3), ("notification", k["ask"], 0.35)]
    if k["stamp"] is not None:
        sfx.append(("error", k["stamp"], 0.25))
    S[sid] = dict(
        sfx=sfx, keys=k,
        css=scoped(sid, COMMON_CSS + r"""
#S .hdr { position:absolute; left:600px; top:132px; }
#S .hdr .h1 { font-size:58px; white-space:nowrap; }
#S .det { position:absolute; left:600px; top:268px; width:900px; height:140px; display:flex; align-items:center; gap:22px; padding:0 26px; }
#S .det .ico { color:var(--accent2); flex:none; }
#S .det > div > b { display:block; font:900 30px Montserrat; white-space:nowrap; }
#S .det .sub { display:block; font:400 21px 'JetBrains Mono'; color:var(--muted); margin-top:6px; white-space:nowrap; }
#S .det .sub em { font-style:normal; font-weight:700; color:var(--gold); }
#S .det .stp { margin-left:auto; padding:10px 16px; border:5px solid var(--uyari); border-radius:12px; color:#FF8A96; font:900 20px/1.15 Montserrat;
  text-align:center; transform:rotate(-4deg); background:rgba(255,77,94,.08); white-space:nowrap; }
#S .cards { position:absolute; left:600px; top:426px; width:900px; display:flex; gap:16px; }
#S .dc { flex:1; height:178px; padding:16px 20px; position:relative; min-width:0; }
#S .dc small { display:block; font:900 17px Montserrat; letter-spacing:.06em; color:var(--accent2); white-space:nowrap; }
#S .dc .v { font:700 38px 'JetBrains Mono'; color:var(--usd); margin-top:14px; white-space:nowrap; }
#S .dc .s { font:800 20px/1.25 Montserrat; color:var(--muted); margin-top:6px; }
#S .dc .s b { color:var(--fg); }
#S .dc .ico { position:absolute; right:14px; top:14px; color:var(--gold); }
#S .rates { position:absolute; left:600px; top:622px; width:900px; display:flex; gap:14px; }
#S .rate { flex:1; height:150px; border-radius:20px; display:flex; flex-direction:column; align-items:center; justify-content:center; border:3px solid; min-width:0; }
#S .rate small { font:900 16px Montserrat; letter-spacing:.04em; white-space:nowrap; }
#S .rate b { font-family:'Archivo Black'; font-size:46px; line-height:1; margin-top:10px; white-space:nowrap; }
#S .rate b.sm { font-size:30px; }
#S .ask { position:absolute; left:600px; top:790px; width:1220px; height:110px; display:flex; align-items:center; gap:26px; padding:0 30px;
  background:rgba(63,107,255,.18); border:3px solid var(--accent); border-radius:20px; }
#S .ask .t { font:800 32px Montserrat; color:var(--fg); white-space:nowrap; }
#S .ask .t b { color:var(--gold); display:inline-block; }
#S .ask .t em { font-style:normal; color:var(--teal); }
"""),
        body=f'''
<div class="hdr"><div class="kicker">ÖRNEK SORU · VERİLER</div><div class="h1">{title}</div></div>
<div class="det card">{icon(det["icon"], 60)}<div><b>{det["head"]}</b><span class="sub">{det["sub"]}</span></div>
  {f'<div class="stp">{det["stamp"]}</div>' if det.get("stamp") else ''}</div>
<div class="cards">{"".join(f'<div class="dc card c{i}"><span>{icon(c[3], 32)}</span><small>{c[0]}</small><div class="v">{c[1]}</div><div class="s">{c[2]}</div></div>' for i, c in enumerate(cards))}</div>
<div class="rates">{"".join(f'<div class="rate r{i}" style="border-color:{RATE_COL[r[2]]}; color:{RATE_COL[r[2]]}; background:color-mix(in srgb, {RATE_COL[r[2]]} 13%, transparent)"><small>{r[0]}</small><b class="{"sm" if len(r[1]) > 5 else ""}">{r[1]}</b></div>' for i, r in enumerate(rates))}</div>
{person(ch, h, cx, 736, who["bubble"], bub_left=1530, bub_top=150, bub_w=290, tail=130)}
<div class="ask">{badge("soru")}<div class="t">{ask[0]}</div></div>
''',
        js=PERSON_JS + r"""
rise(".hdr", K.once, 0, 30);
slideX(".det", K.det - 0.4, -60);
if (K.stamp != null) slam(".det .stp", K.stamp);
K.cards.forEach((t, i) => pop(".cards .c" + i, t - 0.3));
K.rates.forEach((t, i) => pop(".rates .r" + i, t - 0.1));
personIn("p1", K.who, K.bub);
tl.fromTo(q(".ask"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "back.out(1.6)" }, K.ask);
pulse(".ask .t b", K.ask + 1.0, 1.1);
""")


# ------------------------------------------------------------------ s03 options + 5 s countdown
def options(sid, opts, unit):
    end = aud_end(sid)
    k = dict(sik=A(sid, "Şıklarımız"), L=[A(sid, L) for L, _ in opts], vid=A(sid, "Videoyu"), end=end)
    S[sid] = dict(
        sfx=[("pop", t, 0.28) for t in k["L"]] + [("notification", k["vid"], 0.35)] + [("click-soft", end + 0.2 + i, 0.4) for i in range(5)]
            + [("chime", end + 5.15, 0.35)],
        keys=k,
        css=scoped(sid, r"""
#S .hdr { position:absolute; left:600px; top:132px; display:flex; align-items:center; gap:22px; }
#S .opts { position:absolute; left:600px; top:290px; width:760px; }
#S .opt { display:flex; align-items:center; gap:26px; height:104px; margin-bottom:16px; padding:0 30px 0 18px; }
#S .opt .L { width:72px; height:72px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black';
  font-size:38px; color:#071A45; background:var(--accent2); flex:none; }
#S .opt .v { font:700 56px 'JetBrains Mono'; color:var(--fg); white-space:nowrap; }
#S .opt .u { font:800 28px Montserrat; color:var(--muted); margin-left:auto; }
#S .stop { position:absolute; left:1420px; top:270px; width:400px; height:620px; display:flex; flex-direction:column; align-items:center; padding-top:34px; }
#S .stop .pz { width:150px; height:150px; border-radius:50%; background:var(--uyari); color:#fff; display:flex; align-items:center; justify-content:center;
  box-shadow:0 0 0 14px rgba(255,77,94,.18), 0 20px 50px rgba(0,0,0,.4); }
#S .stop .pt { font:900 34px/1.15 Montserrat; text-align:center; margin-top:28px; color:var(--fg); }
#S .stop .ps { font:700 22px 'JetBrains Mono'; color:var(--muted); margin-top:10px; letter-spacing:.08em; }
#S .ring { position:relative; width:200px; height:200px; margin-top:26px; }
#S .ring svg { position:absolute; inset:0; transform:rotate(-90deg); }
#S .ring .n { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:96px; color:var(--gold); opacity:0; }
"""),
        body=f'''
<div class="hdr">{badge("soru")}<div class="h1">Hangisi doğru?</div></div>
<div class="opts">{"".join(f'<div class="opt card o{L}"><span class="L">{L}</span><span class="v">{v}</span><span class="u">{unit}</span></div>' for L, v in opts)}</div>
<div class="stop card"><div class="pz">{icon("pause", 84)}</div><div class="pt">Videoyu durdur,<br/>önce sen çöz!</div><div class="ps">SÜRE BAŞLIYOR</div>
  <div class="ring"><svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="86" fill="none" stroke="#2B4C9E" stroke-width="14"/>
    <circle class="arc" cx="100" cy="100" r="86" fill="none" stroke="#FFC53D" stroke-width="14" stroke-linecap="round"/></svg>
    {"".join(f'<div class="n n{j}">{j}</div>' for j in (5, 4, 3, 2, 1))}</div></div>
''',
        js=r"""
rise(".hdr", K.sik, 0, 30);
K.L.forEach((t, i) => { slideX(".o" + "ABCDE"[i], t, -90); pulse(".o" + "ABCDE"[i] + " .L", t + 0.45, 1.18); });
tl.fromTo(q(".stop"), { x: 120, opacity: 0 }, { x: 0, opacity: 1, duration: 0.65, ease: "expo.out" }, K.vid);
tl.fromTo(q(".stop .pz"), { scale: 0.4 }, { scale: 1, duration: 0.6, ease: "back.out(2.4)" }, K.vid + 0.15);
breathe(".stop .pz", K.vid + 0.8, D - 0.5, 0.06, 1.0);
q(".ring .arc").forEach((p) => { p.setAttribute("pathLength", "1"); p.style.strokeDasharray = "1 1"; });
tl.fromTo(q(".ring .arc"), { strokeDashoffset: 0 }, { strokeDashoffset: 1, duration: 5.0, ease: "none" }, K.end + 0.15);
[5, 4, 3, 2, 1].forEach((n, i) => {
  const at = K.end + 0.15 + i;
  tl.fromTo(q(".ring .n" + n), { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2)" }, at);
  tl.to(q(".ring .n" + n), { opacity: 0, duration: 0.15 }, at + 0.85);
});
""")


# ------------------------------------------------------------------ s04 three keys
KEY_COL = ["var(--teal)", "var(--gold)", "var(--ok)"]


def keys(sid, cards, order, *, at_head="anahtarı", at_order=None):
    """cards: [(icon, title, text_html, ref, at_card, at_ref)] x3; order: [text] chain shown at the bottom."""
    k = dict(head=A(sid, at_head), card=[A(sid, c[4]) for c in cards], ref=[A(sid, c[5]) for c in cards], order=A(sid, at_order))
    S[sid] = dict(
        sfx=[("impact-bass-1", k["head"], 0.35)] + [("whoosh-short", t - 0.2, 0.3) for t in k["card"]] + [("ping", t, 0.3) for t in k["ref"]],
        keys=k,
        css=scoped(sid, COMMON_CSS + r"""
#S .kc { position:absolute; left:600px; width:1220px; height:166px; display:flex; align-items:center; gap:26px; padding:0 30px 0 22px; }
#S .k0 { top:262px; } #S .k1 { top:446px; } #S .k2 { top:630px; }
#S .kc .num { width:92px; height:92px; border-radius:24px; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:52px;
  color:#071A45; flex:none; }
#S .kc .ib { width:72px; height:72px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:rgba(143,178,255,.14); color:var(--accent2); flex:none; }
#S .kc .tx { flex:1; }
#S .kc .tx b.t { display:block; font:900 32px Montserrat; color:var(--fg); }
#S .kc .tx p { font:600 24px/1.3 Montserrat; color:#C9D3F2; margin-top:6px; }
#S .kc .tx p b { color:var(--fg); font-weight:900; }
#S .kc .ref { flex:none; font:700 19px 'JetBrains Mono'; color:#071A45; background:var(--accent2); padding:6px 12px; border-radius:9px; white-space:nowrap; }
#S .order { position:absolute; left:600px; top:822px; display:flex; align-items:center; gap:14px; font:800 22px Montserrat; color:var(--muted); white-space:nowrap; }
#S .order span { padding:6px 12px; border-radius:10px; background:rgba(255,255,255,.07); border:2px solid rgba(255,255,255,.2); color:var(--fg); }
"""),
        body=f'''
<div class="top">{badge("onemli", big=True)}<div class="kicker">SORUNUN 3 ANAHTARI</div></div>
{"".join(f'<div class="kc card k{i}" style="border-color:{KEY_COL[i]}"><span class="num" style="background:{KEY_COL[i]}">{i + 1}</span><span class="ib">{icon(c[0], 40)}</span><div class="tx"><b class="t">{c[1]}</b><p>{c[2]}</p></div><span class="ref">{c[3]}</span></div>' for i, c in enumerate(cards))}
<div class="order">SIRA: {f' {icon("arrow", 26)} '.join(f'<span>{o}</span>' for o in order)}</div>
''',
        js=r"""
tl.fromTo(q(".top .badge"), { scale: 2.4, opacity: 0, rotation: -8 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.head);
rise(".top .kicker", K.head + 0.4, 0, 20);
K.card.forEach((t, i) => { slideX(".k" + i, t - 0.2, -100); pulse(".k" + i + " .ref", K.ref[i] + 0.3, 1.12); });
rise(".order", K.order != null ? K.order : K.ref[2] + 1.0, 0, 20);
""")


# ------------------------------------------------------------------ s05–s07 calculation steps
ROW_COL = {"k": "var(--usd)", "g": "var(--gold)", "m": "var(--accent2)", "d": "var(--teal)", "r": "#FF8A96", "o": "var(--ok)"}


def side_ledger(lines, anchors, unit):
    return ledger(lines, unit), [A_ for A_ in anchors]


def calc(sid, active, kicker, rows, *, sum_row=None, side=None, dik=None, at_start=None, color="var(--teal)", note=None):
    """rows: [(small, expr, value, colour_key, at_row, at_count, dec)]; sum_row: (label, value, unit, at_row, at_count, dec);
    side: ('ledger', lines, anchors, unit) | ('minmax', dict) | ('law', head, ref, html, anchor) | None; dik: (badge_kind, anchor)."""
    k = dict(start=A(sid, at_start) if at_start else 0.3, row=[A(sid, r[4]) for r in rows], cnt=[A(sid, r[5]) for r in rows],
             sum=A(sid, sum_row[3]) if sum_row else None, sumc=A(sid, sum_row[4]) if sum_row else None, dik=A(sid, dik[1]) if dik else None,
             note=A(sid, note[1]) if note else None)
    sfx = [("whoosh-short", 0.3, 0.25)] + [("click-soft", t, 0.4) for t in k["cnt"]]
    if sum_row:
        sfx.append(("chime", k["sumc"] + 0.6, 0.35))
    if dik:
        sfx.append(("notification", k["dik"], 0.3))
    main_w = 1220 if side is None else 760
    side_html, side_css, side_js = "", "", ""
    if side and side[0] == "ledger":
        _, lines, anchors, unit = side
        k["led"] = [A(sid, a) for a in anchors]
        side_html = ledger(lines, unit)
        side_css = LEDGER_CSS
        side_js = r"""
tl.fromTo(q(".ledger"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.start + 0.2);
q(".ledger .ln").forEach((e, i) => { if (K.led[i] != null) write(".ledger .r" + i, K.led[i], 0.6); else tl.set(e, { clipPath: "inset(0 0% 0 0)" }, 0); });
"""
    elif side and side[0] == "minmax":
        d = side[1]
        k["mm"] = [A(sid, a) for a in d["at"]]  # min, max, nispi, pick
        vmax = max(v for _, v, _ in d["bars"])
        bars = "".join(f'<div class="mb b{i} {cls}"><span class="lb">{lab}</span><div class="tr"><i style="width:{round(v / vmax * 100, 1)}%"></i></div>'
                       f'<b>{fmt(v, d.get("dec", 0))}</b></div>' for i, (lab, v, cls) in enumerate(d["bars"]))
        side_html = (f'<div class="mm card"><div class="mh">{icon("ruler", 28)} {d["head"]}</div>{bars}'
                     f'<div class="pick">{icon("arrow", 30)}<span>{d["pick"]}</span></div><div class="why">{d["why"]}</div></div>')
        sfx += [("pop", t, 0.28) for t in k["mm"][:3]] + [("impact-bass-1", k["mm"][3], 0.35)]
        side_css = r"""
#S .mm { position:absolute; left:1380px; top:236px; width:440px; height:640px; padding:22px 26px; }
#S .mm .mh { display:flex; align-items:center; gap:12px; font:900 22px Montserrat; letter-spacing:.06em; color:var(--gold); }
#S .mb { margin-top:26px; }
#S .mb .lb { font:900 20px Montserrat; letter-spacing:.06em; color:var(--muted); }
#S .mb .tr { height:30px; margin-top:8px; border-radius:15px; background:rgba(255,255,255,.08); overflow:hidden; }
#S .mb .tr i { display:block; height:100%; border-radius:15px; background:var(--accent2); transform-origin:left center; }
#S .mb b { display:block; font:700 34px 'JetBrains Mono'; color:var(--fg); margin-top:6px; }
#S .mb.lo .tr i { background:var(--teal); } #S .mb.hi .tr i { background:var(--uyari); } #S .mb.ni .tr i { background:var(--gold); }
#S .mb.win { padding:10px 12px; margin-left:-12px; margin-right:-12px; border-radius:14px; border:3px solid var(--ok); background:rgba(46,212,122,.10); }
#S .pick { display:flex; align-items:center; gap:12px; margin-top:24px; padding:12px 16px; border-radius:14px; background:var(--ok); color:#03221a; font:900 26px Montserrat; }
#S .mm .why { font:700 20px/1.3 Montserrat; color:#C9D3F2; margin-top:12px; }
"""
        side_js = r"""
tl.fromTo(q(".mm"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.start + 0.2);
fadeTo(".mm .mb, .mm .pick, .mm .why", 0.01, 0, 0.01);
[0, 1, 2].forEach((i) => { fadeIn(".mm .b" + i, K.mm[i] - 0.1, 0.3); tl.fromTo(q(".mm .b" + i + " .tr i"), { scaleX: 0 }, { scaleX: 1, duration: 0.8, ease: "power2.out" }, K.mm[i]); });
tl.to(q(".mm .mb.win"), { scale: 1.04, duration: 0.3, ease: "back.out(2)", transformOrigin: "50% 50%" }, K.mm[3]);
pop(".mm .pick", K.mm[3], 0, "back.out(2.4)");
fadeIn(".mm .why", K.mm[3] + 0.6, 0.4);
"""
    elif side and side[0] == "law":
        _, head, ref, html_, anchor = side
        k["law"] = A(sid, anchor)
        side_html = f'<div class="lawc"><div class="lh">{icon("doc", 30)} {head}</div><div class="no">{ref}</div><div class="lt">{html_}</div></div>'
        sfx.append(("pop", k["law"], 0.3))
        side_css = r"""
#S .lawc { position:absolute; left:1380px; top:236px; width:440px; height:640px; background:#F3F6FF; color:#0B1A44; border-radius:20px; padding:24px 28px;
  box-shadow:0 30px 70px rgba(0,0,0,.45); }
#S .lawc .lh { display:flex; align-items:center; gap:12px; font:900 22px Montserrat; letter-spacing:.06em; color:#1E3FBF; }
#S .lawc .no { display:inline-block; margin-top:10px; font:700 19px 'JetBrains Mono'; color:#fff; background:#1E3FBF; padding:3px 10px; border-radius:8px; }
#S .lawc .lt { font:600 27px/1.4 Montserrat; margin-top:18px; }
#S .lawc .lt b { font-weight:900; background:linear-gradient(transparent 55%, #FFC53D 55%); }
"""
        side_js = r"""
tl.fromTo(q(".lawc"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.law - 0.3);
"""
    row_html = "".join(
        f'<div class="rw r{i}{" long" if len(r[1]) + len(fmt(r[2], r[6] if len(r) > 6 else 0)) > 24 else ""}" style="--c:{ROW_COL[r[3]]}"><small>{r[0]}</small><span class="ex">{r[1]}</span><span class="op">=</span>'
        f'<span class="v c{i}">0</span></div>' for i, r in enumerate(rows))
    sum_html = (f'<div class="sum"><small>{sum_row[0]}</small><b class="cs">0</b><em>{sum_row[2]}</em></div>' if sum_row else "")
    S[sid] = dict(
        sfx=sfx, keys=dict(k, vals=[r[2] for r in rows], decs=[r[6] if len(r) > 6 else 0 for r in rows],
                           sv=sum_row[1] if sum_row else 0, sd=(sum_row[5] if sum_row and len(sum_row) > 5 else 0)),
        css=scoped(sid, STEPS_CSS + COMMON_CSS + side_css + r"""
#S .main { position:absolute; left:600px; top:236px; width:__W__px; height:640px; padding:22px 30px; }
#S .main .kicker { color:__C__; }
#S .dk { position:absolute; left:__DK__px; top:180px; }
#S .rw { display:flex; align-items:baseline; gap:12px; margin-top:24px; font:700 34px 'JetBrains Mono'; color:var(--fg); white-space:nowrap; }
#S .rw small { font:800 17px Montserrat; letter-spacing:.04em; color:var(--muted); width:124px; flex:none; white-space:normal; line-height:1.15; }
#S .rw .op { color:var(--muted); }
#S .rw.long { font-size:28px; gap:10px; }
#S .mnote { position:absolute; left:30px; right:30px; bottom:26px; display:flex; align-items:center; gap:16px; padding:16px 20px; border-radius:16px;
  border:2px dashed var(--gold); background:rgba(255,197,61,.10); font:800 24px/1.3 Montserrat; color:#FFE9B0; }
#S .mnote .ico { color:var(--gold); flex:none; }
#S .mnote em { font-style:normal; color:#FF8A96; }
#S .mnote b { color:var(--teal); }
#S .rw .v { display:inline-block; color:var(--c); }
#S .sum { display:flex; align-items:baseline; gap:16px; margin-top:20px; padding-top:14px; border-top:5px solid var(--fg); white-space:nowrap; }
#S .sum small { font:900 24px Montserrat; letter-spacing:.06em; color:var(--teal); }
#S .sum b { font-family:'Archivo Black'; font-size:58px; line-height:1; color:#DFFFF6; display:inline-block; }
#S .sum em { font-style:normal; font:800 28px Montserrat; color:var(--teal); }
""").replace("__W__", str(main_w)).replace("__C__", color).replace("__DK__", str(600 + main_w - 220)),
        body=f'''
{steps(active)}
<div class="main card"><div class="kicker">{kicker}</div>{row_html}{sum_html}{f'<div class="mnote">{icon("bulb", 34)}<span>{note[0]}</span></div>' if note else ""}</div>
{f'<div class="dk">{badge(dik[0])}</div>' if dik else ''}
{side_html}
''',
        js=r"""
rise(".steps", 0.15, 0, -30);
pulse(".steps .stp.on .dot", K.start, 1.25);
tl.fromTo(q(".main"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.start);
K.row.forEach((t, i) => { rise(".r" + i, t, 0, 20); count(".r" + i + " .c" + i, K.cnt[i] - 0.2, 0, K.vals[i], 0.7, K.decs[i]); pulse(".r" + i + " .v", K.cnt[i] + 0.6, 1.12); });
if (K.sum != null) { rise(".sum", K.sum, 0, 20); count(".sum .cs", K.sumc - 0.3, 0, K.sv, 0.8, K.sd); pulse(".sum b", K.sumc + 0.6, 1.12); }
if (K.dik != null) slam(".dk", K.dik);
if (K.note != null) tl.fromTo(q(".mnote"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }, K.note);
""" + side_js)


# ------------------------------------------------------------------ sorter: which costs enter the value / the VAT base
VERDICT = {"gk": ("GK'YA EKLE", "var(--teal)", "check"), "kdv": ("YALNIZ KDV MATRAHI", "var(--gold)", "arrow"),
           "no": ("EKLENMEZ", "var(--uyari)", "x"), "in": ("FİYATTA", "var(--accent2)", "check")}


def sorter(sid, active, kicker, items, *, total=None, at_start=None, dik=None):
    """items: [(name_html, amount, verdict, at_item, at_verdict, note)] (≤6); total: (label_html, value, unit, at, at_count)."""
    k = dict(start=A(sid, at_start) if at_start else 0.3, it=[A(sid, x[3]) for x in items], vd=[A(sid, x[4]) for x in items],
             tot=A(sid, total[3]) if total else None, totc=A(sid, total[4]) if total else None, tv=total[1] if total else 0,
             dik=A(sid, dik[1]) if dik else None)
    rows = "".join(
        f'<div class="it i{i} v-{v}"><span class="nm">{nm}<small>{note}</small></span><span class="am">{am}</span>'
        f'<span class="vd" style="--c:{VERDICT[v][1]}">{icon(VERDICT[v][2], 24)}{VERDICT[v][0]}</span></div>'
        for i, (nm, am, v, _, _, note) in enumerate(items))
    sfx = [("whoosh-short", 0.3, 0.25)] + [("pop", t, 0.25) for t in k["it"]] + [("ping" if items[i][2] != "no" else "error", t, 0.28) for i, t in enumerate(k["vd"])]
    if total:
        sfx.append(("chime", k["totc"] + 0.6, 0.35))
    if dik:
        sfx.append(("notification", k["dik"], 0.3))
    S[sid] = dict(
        sfx=sfx, keys=k,
        css=scoped(sid, STEPS_CSS + COMMON_CSS + r"""
#S .main { position:absolute; left:600px; top:226px; width:1220px; height:660px; padding:20px 28px; }
#S .main .kicker { color:var(--teal); }
#S .dk { position:absolute; left:1600px; top:172px; }
#S .it { display:flex; align-items:center; gap:18px; height:72px; margin-top:12px; padding:0 18px; border-radius:16px; background:rgba(255,255,255,.05);
  border:2px solid rgba(255,255,255,.12); }
#S .it .nm { flex:1; font:800 25px Montserrat; color:var(--fg); white-space:nowrap; }
#S .it .nm small { display:block; font:700 16px 'JetBrains Mono'; color:var(--muted); margin-top:2px; }
#S .it .am { font:700 28px 'JetBrains Mono'; color:var(--usd); white-space:nowrap; }
#S .it .vd { flex:none; width:300px; display:flex; align-items:center; justify-content:center; gap:8px; height:46px; border-radius:12px; font:900 18px Montserrat;
  letter-spacing:.04em; color:#071A45; background:var(--c); white-space:nowrap; }
#S .it.v-no .nm, #S .it.v-no .am { color:#8C97B8; text-decoration:line-through; text-decoration-color:var(--uyari); text-decoration-thickness:3px; }
#S .it.v-gk { border-color:rgba(51,217,178,.55); } #S .it.v-kdv { border-color:rgba(255,197,61,.55); }
#S .tot { display:flex; align-items:baseline; gap:16px; margin-top:18px; padding-top:12px; border-top:5px solid var(--fg); white-space:nowrap; }
#S .tot small { font:900 22px Montserrat; letter-spacing:.04em; color:var(--teal); }
#S .tot small b { color:var(--fg); }
#S .tot b.cs { font-family:'Archivo Black'; font-size:54px; line-height:1; color:#DFFFF6; display:inline-block; margin-left:auto; }
#S .tot em { font-style:normal; font:800 26px Montserrat; color:var(--teal); }
"""),
        body=f'''
{steps(active)}
<div class="main card"><div class="kicker">{kicker}</div>{rows}
{f'<div class="tot"><small>{total[0]}</small><b class="cs">0</b><em>{total[2]}</em></div>' if total else ''}</div>
{f'<div class="dk">{badge(dik[0])}</div>' if dik else ''}
''',
        js=r"""
rise(".steps", 0.15, 0, -30);
pulse(".steps .stp.on .dot", K.start, 1.25);
tl.fromTo(q(".main"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.start);
fadeTo(".it .vd", 0.01, 0, 0.01);
K.it.forEach((t, i) => { slideX(".it.i" + i, t - 0.2, -70); pop(".it.i" + i + " .vd", K.vd[i], 0, "back.out(2.6)"); });
if (K.tot != null) { rise(".tot", K.tot, 0, 20); count(".tot .cs", K.totc - 0.3, 0, K.tv, 0.9, 0); pulse(".tot b.cs", K.totc + 0.7, 1.1); }
if (K.dik != null) slam(".dk", K.dik);
""")


# ------------------------------------------------------------------ s08 result: receipt + options
def result(sid, lines, total, unit, opts, letter, *, sub="", at, total_label="TOPLAM"):
    """lines: [(label, small, value_html, anchor)]; at: dict(son, od, cnt, dogru, L)."""
    k = dict(son=A(sid, at["son"]), ln=[A(sid, x[3]) for x in lines], od=A(sid, at["od"]), cnt=A(sid, at["cnt"]), dogru=A(sid, at["dogru"]),
             L=A(sid, at["L"]), tv=total[0], td=total[1] if len(total) > 1 else 0)
    S[sid] = dict(
        sfx=[("whoosh-short", 0.3, 0.25)] + [("click-soft", t, 0.4) for t in k["ln"]] + [("riser", k["od"] - 0.6, 0.3),
             ("impact-bass-1", k["cnt"] + 0.9, 0.4), ("chime", k["L"], 0.45)],
        keys=k,
        css=scoped(sid, STEPS_CSS + r"""
#S .rcp { position:absolute; left:600px; top:236px; width:620px; height:620px; background:#FBF8EE; color:#1B2A57; padding:26px 38px;
  box-shadow:0 30px 70px rgba(0,0,0,.45); clip-path:polygon(0 0,100% 0,100% 96%,95% 100%,90% 96%,85% 100%,80% 96%,75% 100%,70% 96%,65% 100%,60% 96%,55% 100%,50% 96%,45% 100%,40% 96%,35% 100%,30% 96%,25% 100%,20% 96%,15% 100%,10% 96%,5% 100%,0 96%); }
#S .rcp .rh { text-align:center; font-family:'Archivo Black'; font-size:36px; letter-spacing:.04em; }
#S .rcp .rs { text-align:center; font:700 18px 'JetBrains Mono'; color:#5A6AA0; letter-spacing:.14em; margin-top:4px; padding-bottom:12px; border-bottom:3px dashed #9BA8CC; }
#S .rcp .ln { display:flex; justify-content:space-between; align-items:baseline; margin-top:16px; font:800 27px Montserrat; }
#S .rcp .ln b { font:700 34px 'JetBrains Mono'; white-space:nowrap; }
#S .rcp .ln small { display:block; font:600 18px 'JetBrains Mono'; color:#5A6AA0; }
#S .rcp .eq { border-top:4px solid #1B2A57; margin-top:20px; padding-top:14px; }
#S .rcp .tot { display:flex; justify-content:space-between; align-items:center; font:900 26px Montserrat; color:#B4231B; }
#S .rcp .tot b { font:700 54px 'JetBrains Mono'; }
#S .rcp .usd { text-align:right; font:800 22px Montserrat; color:#B4231B; }
#S .ans { position:absolute; left:1270px; top:250px; width:550px; }
#S .ao { display:flex; align-items:center; gap:22px; height:88px; margin-bottom:14px; padding:0 24px 0 14px; position:relative; }
#S .ao .L { width:62px; height:62px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:32px;
  color:#071A45; background:var(--accent2); flex:none; }
#S .ao .v { font:700 42px 'JetBrains Mono'; color:var(--fg); white-space:nowrap; }
#S .ao .ck { margin-left:auto; width:56px; height:56px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center; opacity:0; }
#S .stamp { position:absolute; left:1340px; top:762px; padding:14px 26px; border:7px solid var(--ok); color:var(--ok); border-radius:16px;
  font-family:'Archivo Black'; font-size:52px; line-height:1; background:rgba(7,26,69,.9); transform:rotate(-7deg); }
#S .burst { position:absolute; left:1300px; top:452px; width:1px; height:1px; }
#S .burst i { position:absolute; left:0; top:0; width:14px; height:14px; border-radius:3px; opacity:0; }
"""),
        body=f'''
{steps(4)}
<div class="rcp"><div class="rh">ÖDEME HESABI</div><div class="rs">{sub}</div>
  {"".join(f'<div class="ln l{i}"><span>{a}<small>{b}</small></span><b>{c}</b></div>' for i, (a, b, c, _) in enumerate(lines))}
  <div class="eq"><div class="tot"><span>{total_label}</span><b class="cnt">0</b></div><div class="usd">{unit}</div></div>
</div>
<div class="ans">{"".join(f'<div class="ao card a{L}"><span class="L">{L}</span><span class="v">{v}</span><span class="ck">{icon("check", 34)}</span></div>' for L, v in opts)}</div>
<div class="stamp">CEVAP: {letter}</div>
<div class="burst">{"".join(f'<i style="background:{c}"></i>' for c in ["#FFC53D", "#33D9B2", "#8FB2FF", "#FF4D5E", "#2ED47A"] * 4)}</div>
''',
        js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".rcp"), { y: -200, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, ease: "expo.out" }, K.son);
fadeTo(".rcp .ln, .rcp .eq", 0.01, 0, 0.01);
K.ln.forEach((t, i) => rise(".rcp .l" + i, t, 0, 20));
rise(".rcp .eq", K.od, 0, 20);
count(".rcp .cnt", K.cnt - 0.1, 0, K.tv, 1.1, K.td);
pulse(".rcp .tot b", K.cnt + 1.1, 1.12);
slideX(".ans .ao", K.od + 0.3, 80, 0.08);
fadeTo(".ans .ao:not(.a__L__)", K.dogru, 0.3, 0.4);
tl.to(q(".ans .a__L__"), { borderColor: "#2ED47A", backgroundColor: "rgba(46,212,122,.18)", scale: 1.06, duration: 0.35, ease: "back.out(2)", transformOrigin: "0% 50%" }, K.dogru);
tl.fromTo(q(".ans .a__L__ .ck"), { opacity: 0, scale: 0.2 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(3)" }, K.L - 0.2);
slam(".stamp", K.L);
q(".burst i").forEach((p, i) => {
  const a = (i / 20) * Math.PI * 2, r = 160 + (i % 5) * 34;
  tl.fromTo(p, { x: 0, y: 44, opacity: 1, rotation: 0, scale: 1 }, { x: Math.cos(a) * r, y: 44 + Math.sin(a) * r, opacity: 0, rotation: 260 + i * 17, scale: 0.6, duration: 1.1, ease: "power2.out", immediateRender: false }, K.L + 0.05);
});
""".replace("__L__", letter))


# ------------------------------------------------------------------ s09 traps
def traps(sid, cards, unit, baba_bubble, *, at_tz="tuzaklara", at):
    """cards: [(L, value, why, lines[(label, value, cls)], sum_value)] x4; at: [(card_anchor, sum_anchor)] x4."""
    k = dict(tz=A(sid, at_tz), c=[A(sid, a[0]) for a in at], s=[A(sid, a[1]) for a in at])
    pos = [(600, 254), (1100, 254), (600, 582), (1100, 582)]
    html_cards = ""
    for i, (L, v, why, lines, sv) in enumerate(cards):
        x, y = pos[i]
        lns = "".join(f'<div class="ln {cls}"><span>{a}</span><b>{b}</b></div>' for a, b, cls in lines)
        html_cards += (f'<div class="tc t{i} card" style="left:{x}px; top:{y}px"><div class="x">{icon("x", 32)}</div>'
                       f'<div class="th"><span class="L">{L}</span><b>{v} {unit}</b></div><div class="why">{why}</div>{lns}'
                       f'<div class="sum"><span>Toplam</span><b>{sv}</b></div></div>')
    S[sid] = dict(
        sfx=[("impact-bass-1", k["tz"], 0.4)] + [("error", t, 0.25) for t in k["s"]] + [("pop", k["s"][3] + 1.6, 0.3)],
        keys=k,
        css=scoped(sid, COMMON_CSS + r"""
#S .top .kicker { font-size:24px; color:#FFD400; }
#S .tc { position:absolute; width:480px; height:312px; padding:14px 22px; }
#S .tc .th { display:flex; align-items:center; gap:14px; }
#S .tc .th .L { width:52px; height:52px; border-radius:50%; background:var(--uyari); color:#fff; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:28px; flex:none; }
#S .tc .th b { font:700 36px 'JetBrains Mono'; color:#FFB3BB; white-space:nowrap; }
#S .tc .why { margin-top:10px; font:800 20px/1.25 Montserrat; color:var(--fg); padding:8px 12px; background:rgba(255,77,94,.12); border-left:5px solid var(--uyari); border-radius:8px; }
#S .tc .ln { display:flex; justify-content:space-between; align-items:baseline; margin-top:10px; font:700 20px Montserrat; color:var(--muted); white-space:nowrap; gap:10px; }
#S .tc .ln b { font:700 24px 'JetBrains Mono'; color:#FF8A96; }
#S .tc .ln.miss b { color:var(--gold); }
#S .tc .sum { margin-top:10px; padding-top:8px; border-top:3px solid #3B5296; display:flex; justify-content:space-between; align-items:center; font:900 22px Montserrat; color:#FF8A96; }
#S .tc .sum b { font:700 30px 'JetBrains Mono'; }
#S .tc .x { position:absolute; right:-14px; top:-14px; width:52px; height:52px; border-radius:50%; background:var(--uyari); color:#2a0a0e;
  display:flex; align-items:center; justify-content:center; box-shadow:0 8px 20px rgba(0,0,0,.4); }
"""),
        body=f'''
<div class="top">{badge("tuzak", big=True)}<div class="kicker">HER YANLIŞ ŞIK = BİR HATA</div></div>
{html_cards}
{person("baba", 520, 1716, 888, baba_bubble, bub_left=1608, bub_top=176, bub_w=270, tail=150)}
''',
        js=PERSON_JS + r"""
tl.fromTo(q(".top .badge"), { scale: 2.6, opacity: 0, rotation: -10 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.tz);
rise(".top .kicker", K.tz + 0.5, 0, 20);
personIn("p1", K.tz + 0.8, K.s[3] + 1.6);
fadeTo(".tc .why, .tc .ln, .tc .sum, .tc .x", 0.01, 0, 0.01);
K.c.forEach((at, i) => {
  const c = ".t" + i;
  tl.fromTo(q(c), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "expo.out" }, at);
  fadeIn(c + " .why", at + 0.3, 0.3);
  fadeIn(c + " .ln", Math.min(at + 1.2, K.s[i] - 0.3), 0.3);
  fadeIn(c + " .sum", K.s[i], 0.3);
  pop(c + " .x", K.s[i], 0, "back.out(3)");
});
""")


# ------------------------------------------------------------------ s10 warning
def warn(sid, kicker, law, panel, who, *, at_uy="uyarı", hayir=None):
    """law: dict(head, ref, conds[(html, anchor)], res, at, at_res); panel: dict(head, items[(cls pv|pc, k, tag, v, anchor)], at);
    who: dict(char, bubble, at, at_bub)."""
    k = dict(uy=A(sid, at_uy), law=A(sid, law["at"]), cond=[A(sid, c[1]) for c in law["conds"]], res=A(sid, law["at_res"]),
             pan=A(sid, panel["at"]), pi=[A(sid, x[4]) for x in panel["items"]], who=A(sid, who["at"]), bub=A(sid, who["at_bub"]),
             hayir=A(sid, hayir))
    sfx = [("notification", k["uy"], 0.35)] + [("pop", t, 0.3) for t in k["cond"]] + ([("chime", k["res"], 0.3)] if law["res"] else []) + [("whoosh-short", k["pan"] - 0.1, 0.3)] \
        + [("pop", t, 0.25) for t in k["pi"]]
    if hayir:
        sfx.append(("impact-bass-1", k["hayir"], 0.35))
    S[sid] = dict(
        sfx=sfx, keys=k,
        css=scoped(sid, COMMON_CSS + r"""
#S .top .kicker { color:#FF8A96; }
#S .law { position:absolute; left:600px; top:254px; width:900px; height:330px; padding:20px 26px; }
#S .law .lh { display:flex; align-items:center; gap:14px; font:900 22px Montserrat; letter-spacing:.06em; color:var(--accent2); white-space:nowrap; }
#S .law .lh .no { font:700 19px 'JetBrains Mono'; color:#071A45; background:var(--accent2); padding:3px 10px; border-radius:8px; }
#S .cond { display:flex; align-items:center; gap:16px; margin-top:14px; padding:12px 18px; border-radius:16px; background:rgba(46,212,122,.10); border:2px solid rgba(46,212,122,.55); }
#S .cond .n { width:44px; height:44px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center; flex:none; }
#S .cond span { font:800 24px/1.2 Montserrat; color:var(--fg); }
#S .cond span b { color:var(--gold); }
#S .res { display:flex; align-items:center; gap:14px; margin-top:14px; font:900 24px Montserrat; color:var(--teal); }
#S .res b { color:#03221a; background:var(--teal); padding:6px 14px; border-radius:10px; white-space:nowrap; }
#S .ind { position:absolute; left:600px; top:604px; width:1220px; height:280px; padding:20px 26px; }
#S .ind .lh { font:900 22px Montserrat; letter-spacing:.06em; color:var(--ok); display:flex; align-items:center; gap:12px; }
#S .ind .two { display:flex; gap:20px; margin-top:16px; }
#S .ind .pl { flex:1; display:flex; align-items:center; gap:16px; padding:18px 22px; border-radius:18px; min-width:0; }
#S .ind .pl .k { font:900 26px Montserrat; white-space:nowrap; }
#S .ind .pl .v { font:700 30px 'JetBrains Mono'; margin-left:auto; white-space:nowrap; }
#S .ind .pv { background:rgba(255,77,94,.12); border:3px solid var(--uyari); color:#FFE3E6; }
#S .ind .pv .tg { font:900 17px Montserrat; color:#2a0a0e; background:var(--uyari); padding:4px 10px; border-radius:8px; white-space:nowrap; }
#S .ind .pc { background:rgba(46,212,122,.12); border:3px solid var(--ok); color:#DFFFEF; }
#S .ind .pc .tg { font:900 17px Montserrat; color:#03221a; background:var(--ok); padding:4px 10px; border-radius:8px; white-space:nowrap; }
"""),
        body=f'''
<div class="top">{badge("uyari", big=True)}<div class="kicker">{kicker}</div></div>
<div class="law card"><div class="lh">{icon("doc", 32)} {law["head"]} <span class="no">{law["ref"]}</span></div>
  {"".join(f'<div class="cond c{i}"><span class="n">{icon("check", 26)}</span><span>{c[0]}</span></div>' for i, c in enumerate(law["conds"]))}
  {f'<div class="res">{icon("arrow", 30)} <b>{law["res"]}</b></div>' if law["res"] else ''}</div>
<div class="ind card"><div class="lh">{icon("check", 26)} {panel["head"]}</div>
  <div class="two">{"".join(f'<div class="pl {c} p{i}"><span class="k">{a}</span><span class="tg">{b}</span><span class="v">{v}</span></div>' for i, (c, a, b, v, _) in enumerate(panel["items"]))}</div></div>
{person(who["char"], 320, 1696, 556, who["bubble"], bub_left=1530, bub_top=120, bub_w=290, tail=150)}
{f'<div class="hayir" style="left:1560px; top:430px">HAYIR!</div>' if hayir else ''}
''',
        js=PERSON_JS + r"""
tl.fromTo(q(".top .badge"), { scale: 2.4, opacity: 0, rotation: -8 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.uy);
rise(".top .kicker", K.uy + 0.45, 0, 20);
tl.fromTo(q(".law"), { x: -80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.law);
K.cond.forEach((t, i) => slideX(".cond.c" + i, t - 0.3, -50));
if (K.res != null) { fadeTo(".law .res", 0.01, 0, 0.01); pop(".law .res", K.res, 0, "back.out(2.4)"); }
personIn("p1", K.who, K.bub);
tl.fromTo(q(".ind"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }, K.pan);
fadeTo(".ind .pl", 0.01, 0, 0.01);
K.pi.forEach((t, i) => pop(".ind .p" + i, t - 0.2));
if (K.hayir != null) slam(".hayir", K.hayir);
""")


# ------------------------------------------------------------------ s11 coach note
def coach(sid, st, it, chain, *, at_koc="Koçun", at_form="Formülü"):
    """st: dict(head, icon, opts[(ok|no, text, small, anchor)], at); it: dict(head, big, p, ref, at, at_pulse); chain: [(text, icon, anchor)] x5."""
    k = dict(koc=A(sid, at_koc), st=A(sid, st["at"]), o=[A(sid, x[3]) for x in st["opts"]], it=A(sid, it["at"]), itp=A(sid, it["at_pulse"]),
             form=A(sid, at_form), c=[A(sid, x[2]) for x in chain])
    S[sid] = dict(
        sfx=[("pop", k["koc"], 0.35)] + [("ping" if st["opts"][i][0] == "ok" else "error", t, 0.25) for i, t in enumerate(k["o"])]
            + [("pop", k["it"], 0.3), ("whoosh-short", k["form"] - 0.2, 0.3)] + [("pop", t, 0.25) for t in k["c"][:-1]] + [("chime", k["c"][-1], 0.3)],
        keys=k,
        css=scoped(sid, COMMON_CSS + r"""
#S .top .kicker { color:#FFE27A; }
#S .st { position:absolute; left:600px; top:250px; width:780px; height:330px; padding:20px 26px; }
#S .st .lh { font:900 22px Montserrat; letter-spacing:.06em; color:var(--gold); display:flex; align-items:center; gap:12px; }
#S .opt { display:flex; align-items:center; gap:16px; margin-top:14px; padding:12px 18px; border-radius:16px; }
#S .opt .m { width:44px; height:44px; border-radius:50%; display:flex; align-items:center; justify-content:center; flex:none; }
#S .opt b { font:900 25px Montserrat; white-space:nowrap; }
#S .opt small { margin-left:auto; font:700 17px 'JetBrains Mono'; letter-spacing:.06em; white-space:nowrap; }
#S .opt.ok { background:rgba(46,212,122,.14); border:3px solid var(--ok); color:#DFFFEF; } #S .opt.ok .m { background:var(--ok); color:#03221a; } #S .opt.ok small { color:var(--ok); }
#S .opt.no { background:rgba(255,77,94,.10); border:2px solid rgba(255,77,94,.5); color:#C9D3F2; } #S .opt.no .m { background:var(--uyari); color:#2a0a0e; } #S .opt.no small { color:#FF8A96; }
#S .it { position:absolute; left:1400px; top:250px; width:420px; height:330px; padding:22px 24px; display:flex; flex-direction:column; }
#S .it .lh { font:900 22px Montserrat; letter-spacing:.06em; color:var(--accent2); }
#S .it .big { font-family:'Archivo Black'; font-size:40px; line-height:1.1; color:var(--fg); margin-top:14px; }
#S .it .big em { font-style:normal; color:var(--teal); }
#S .it p { font:700 20px/1.3 Montserrat; color:#C9D3F2; margin-top:10px; }
#S .it .ref { margin-top:auto; font:700 17px 'JetBrains Mono'; color:var(--muted); }
#S .fm { position:absolute; left:600px; top:604px; width:1220px; height:270px; padding:24px 30px; border-radius:24px;
  background:linear-gradient(180deg, rgba(255,197,61,.14), rgba(255,197,61,.04)); border:4px solid var(--gold); }
#S .fm .kicker { color:var(--gold); }
#S .chain { display:flex; align-items:center; gap:10px; margin-top:26px; }
#S .ch { flex:1; height:132px; border-radius:18px; background:rgba(255,255,255,.07); border:2px solid rgba(255,255,255,.25); display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:10px; text-align:center; padding:0 6px; min-width:0; }
#S .ch .n { width:44px; height:44px; border-radius:50%; background:var(--gold); color:#2a1d00; display:flex; align-items:center; justify-content:center; }
#S .ch b { font:900 21px/1.15 Montserrat; color:var(--fg); }
#S .ar { color:var(--gold); flex:none; }
"""),
        body=f'''
<div class="top">{badge("ipucu", big=True)}<div class="kicker">KOÇUN NOTU</div></div>
<div class="st card"><div class="lh">{icon(st["icon"], 28)} {st["head"]}</div>
  {"".join(f'<div class="opt {c} o{i}"><span class="m">{icon("check" if c == "ok" else "x", 26)}</span><b>{t}</b><small>{s}</small></div>' for i, (c, t, s, _) in enumerate(st["opts"]))}</div>
<div class="it card"><div class="lh">{it["head"]}</div><div class="big">{it["big"]}</div><p>{it["p"]}</p><div class="ref">{it["ref"]}</div></div>
<div class="fm"><div class="kicker">AKILDA TUT · 5 ADIMLI FORMÜL</div>
  <div class="chain">{f'<span class="ar">{icon("arrow", 34)}</span>'.join(f'<div class="ch c{j}"><span class="n">{icon(ic, 24)}</span><b>{t}</b></div>' for j, (t, ic, _) in enumerate(chain))}</div></div>
''',
        js=r"""
tl.fromTo(q(".top .badge"), { scale: 0.3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.5, ease: "back.out(2.4)" }, K.koc);
rise(".top .kicker", K.koc + 0.3, 0, 20);
tl.fromTo(q(".st"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.st);
fadeTo(".st .opt", 0.01, 0, 0.01);
K.o.forEach((t, i) => pop(".st .o" + i, t - 0.2));
tl.fromTo(q(".it"), { x: 60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.it);
pulse(".it .big em", K.itp + 0.3, 1.15);
tl.fromTo(q(".fm"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }, K.form);
fadeTo(".chain .ch, .chain .ar", 0.01, 0, 0.01);
K.c.forEach((t, i) => { pop(".chain .c" + i, t - 0.1); if (i) fadeIn(".chain .ar:nth-of-type(" + i + ")", t - 0.2, 0.2); });
""")


# ------------------------------------------------------------------ s12 closing
def closing(sid, kicker, rows, ans, note, *, at_oz="Özetle", L_anchor=None):
    """rows: [(title, line, anchor)] x2; ans: (letter, value, unit); note: (icon, html, anchor)."""
    k = dict(oz=A(sid, at_oz), r=[A(sid, x[2]) for x in rows], C=A(sid, L_anchor or ans[0]), note=A(sid, note[2]),
             abone=A(sid, "abone"), pay=A(sid, "paylaşmayı"), bir=A(sid, "sonraki"))
    S[sid] = dict(
        exit=False,
        sfx=[("whoosh-short", 0.3, 0.25), ("impact-bass-1", k["C"], 0.4), ("pop", k["abone"], 0.35), ("pop", k["pay"], 0.35), ("chime", k["bir"], 0.35)],
        keys=k,
        css=scoped(sid, r"""
#S .right { position:absolute; left:860px; top:140px; width:960px; }
#S .sum { margin-top:18px; }
#S .row { display:flex; align-items:center; gap:22px; height:118px; padding:0 26px; margin-bottom:16px; }
#S .row .n { width:58px; height:58px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:28px; flex:none; }
#S .row .n0 { background:var(--teal); color:#03221a; } #S .row .n1 { background:var(--gold); color:#2a1d00; }
#S .row b { display:block; font:900 29px Montserrat; color:var(--fg); white-space:nowrap; }
#S .row span.l { display:block; font:700 25px 'JetBrains Mono'; color:var(--muted); margin-top:4px; white-space:nowrap; }
#S .arow { display:flex; align-items:center; gap:24px; margin-top:12px; }
#S .ans { display:flex; align-items:center; gap:26px; padding:22px 30px; border-radius:24px; background:rgba(46,212,122,.14); border:4px solid var(--ok);
  box-shadow:0 0 60px rgba(46,212,122,.25); width:max-content; flex:none; }
#S .ans .L { width:96px; height:96px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:56px; }
#S .ans b { font-family:'Archivo Black'; font-size:72px; line-height:1; color:#DFFFEF; white-space:nowrap; }
#S .ans small { font:800 30px Montserrat; color:var(--ok); margin-left:6px; }
#S .note { display:flex; align-items:center; gap:14px; padding:14px 18px; border-radius:16px; background:rgba(255,197,61,.12); border:2px dashed var(--gold);
  font:800 22px/1.25 Montserrat; color:#FFE9B0; }
#S .note .ico { color:var(--gold); flex:none; }
#S .note em { font-style:normal; color:#FF8A96; }
#S .cta { display:flex; gap:20px; margin-top:30px; }
#S .btn { display:flex; align-items:center; gap:14px; padding:18px 30px; border-radius:16px; font:900 30px Montserrat; }
#S .sub { background:#FF0033; color:#fff; box-shadow:0 10px 0 #9c0020; }
#S .shr { background:#F4F7FF; color:#0B1A44; box-shadow:0 10px 0 #9aa8d0; }
#S .bye { position:absolute; left:860px; top:790px; display:flex; align-items:center; gap:20px; }
#S .bye .lg { background:#F4F7FF; border-radius:14px; padding:10px 18px; }
#S .bye .lg img { height:46px; display:block; }
#S .bye span { font:800 28px/1.25 Montserrat; color:var(--fg); max-width:520px; }
"""),
        body=f'''
<div class="right">
  <div class="kicker">{kicker}</div>
  <div class="sum">{"".join(f'<div class="row card r{i}"><span class="n n{i}">{i + 1}</span><div><b>{t}</b><span class="l">{l}</span></div></div>' for i, (t, l, _) in enumerate(rows))}</div>
  <div class="arow"><div class="ans"><span class="L">{ans[0]}</span><b{' style="font-size:56px"' if len(ans[1]) > 7 else ""}>{ans[1]}</b><small>{ans[2]}</small></div>
    <div class="note">{icon(note[0], 40)}<div>{note[1]}</div></div></div>
  <div class="cta"><div class="btn sub">{icon("bell", 34)} ABONE OL</div><div class="btn shr">{icon("share", 34)} PAYLAŞ</div></div>
</div>
<div class="bye"><div class="lg"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div><span>Bir sonraki hesaplama dersinde görüşmek üzere!</span></div>
''',
        js=r"""
rise(".right .kicker", K.oz, 0, 20);
K.r.forEach((t, i) => slideX(".sum .r" + i, t, 80));
slideX(".arow .note", K.note, 60);
tl.fromTo(q(".ans"), { scale: 2.2, opacity: 0, transformOrigin: "0% 50%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "expo.in" }, K.C - 0.3);
tl.fromTo(q(".ans"), { boxShadow: "0 0 20px rgba(46,212,122,.15)" }, { boxShadow: "0 0 80px rgba(46,212,122,.55)", duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 3 }, K.C + 0.5);
pop(".cta .sub", K.abone, 0, "back.out(2.6)");
pop(".cta .shr", K.pay, 0, "back.out(2.6)");
tl.fromTo(q(".cta .sub .ico"), { rotation: 0 }, { rotation: 18, duration: 0.12, yoyo: true, repeat: 7, ease: "sine.inOut", transformOrigin: "50% 10%" }, K.abone + 0.4);
tl.fromTo(q(".bye"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }, K.bir);
""")
