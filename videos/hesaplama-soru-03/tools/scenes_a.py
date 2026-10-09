"""Scenes 01-06: giriş, soru, şıklar, üç anahtar, adım 1 (zamanaşımı), adım 2 (kıymet + vergiler)."""
from lib import T, D, SCENES, icon, badge

S = {}


def steps(active):
    names = ["ZAMANAŞIMI", "KIYMET & VERGİ", "CEZA & İNDİRİM", "SONUÇ"]
    out = []
    for i, n in enumerate(names, 1):
        st = "done" if i < active else "on" if i == active else ""
        mark = icon("check", 26) if i < active else f"<b>{i}</b>"
        out.append(f'<div class="stp {st}"><span class="dot">{mark}</span>{n}</div>')
        if i < len(names):
            out.append('<i class="bar"></i>')
    return f'<div class="steps">{"".join(out)}</div>'


STEPS_CSS = r"""
.steps { position:absolute; left:600px; top:128px; width:1220px; display:flex; align-items:center; gap:0; }
.steps .stp { display:flex; align-items:center; gap:12px; font:900 22px Montserrat; letter-spacing:.06em; color:#7E8DBA; white-space:nowrap; }
.steps .stp .dot { width:44px; height:44px; border-radius:50%; display:flex; align-items:center; justify-content:center; border:3px solid #3A5296; font:700 22px 'JetBrains Mono'; color:#7E8DBA; }
.steps .stp.done { color:#AEBBE3; } .steps .stp.done .dot { background:var(--teal); border-color:var(--teal); color:#03221a; }
.steps .stp.on { color:var(--fg); } .steps .stp.on .dot { background:var(--gold); border-color:var(--gold); color:#2a1d00; box-shadow:0 0 0 8px rgba(255,197,61,.18); }
.steps .bar { flex:1; height:4px; margin:0 16px; background:#2B4C9E; border-radius:2px; }
"""


def ledger(lines, tag="ZAMANAŞIMI"):
    """Notebook 'çözüm defteri': list of (label, value, cls). Rows get classes r0, r1, ... for timed writing.
    cls 'out' = struck row (with a small tag); 'pen' = penalty row (red value)."""
    rows = []
    for i, (lab, val, cls) in enumerate(lines):
        extra = f'<i class="sk"></i><em class="tg">{tag}</em>' if "out" in cls else ""
        rows.append(f'<div class="ln r{i} {cls}"><span class="lb">{lab}</span><span class="dots"></span><span class="vl">{val}</span>{extra}</div>')
    empty = "".join('<div class="ln blank"></div>' for _ in range(max(0, 4 - len(lines))))
    return f'<div class="ledger"><div class="lh">{icon("pen", 30)}ÇÖZÜM DEFTERİ<small>TL</small></div>{"".join(rows)}{empty}</div>'


LEDGER_CSS = r"""
.ledger { position:absolute; left:1330px; top:250px; width:490px; height:560px; background:#FBF8EE; border-radius:16px; padding:22px 26px 0 64px;
  box-shadow:0 26px 60px rgba(0,0,0,.4); color:#1B2A57; overflow:hidden;
  background-image:linear-gradient(90deg, transparent 46px, #F2A0A0 46px, #F2A0A0 49px, transparent 49px), repeating-linear-gradient(#FBF8EE 0 89px, #C9D6EE 89px 91px); }
.ledger .lh { display:flex; align-items:center; gap:12px; font:900 22px Montserrat; letter-spacing:.1em; color:#2B47A8; height:70px; margin-top:-6px; }
.ledger .lh small { margin-left:auto; font:700 18px 'JetBrains Mono'; color:#5A6AA0; }
.ledger .ln { position:relative; display:flex; align-items:baseline; gap:10px; height:91px; padding-top:36px; font:700 26px 'JetBrains Mono'; }
.ledger .ln .lb { font:800 25px Montserrat; white-space:nowrap; }
.ledger .ln .dots { flex:1; border-bottom:3px dotted #8C9BC4; transform:translateY(-6px); }
.ledger .ln .vl { font:700 27px 'JetBrains Mono'; color:#0B6B4F; white-space:nowrap; }
.ledger .ln.pen .vl { color:#B4231B; }
.ledger .ln.out .lb, .ledger .ln.out .vl { color:#7D88A8; }
.ledger .ln.out .sk { position:absolute; right:-6px; top:52px; width:118px; height:4px; background:#B4231B; border-radius:2px; transform-origin:left center; }
.ledger .ln.out .tg { position:absolute; right:0; top:8px; font:900 15px Montserrat; font-style:normal; letter-spacing:.08em; color:#B4231B;
  border:2px solid #B4231B; border-radius:6px; padding:1px 8px; }
"""


def hourglass(cls="hg", w=200):
    return f'''<svg class="{cls}" viewBox="0 0 200 240" width="{w}" height="{round(w * 1.2)}" aria-hidden="true">
  <rect x="34" y="8" width="132" height="16" rx="6" fill="#8FB2FF"/><rect x="34" y="216" width="132" height="16" rx="6" fill="#8FB2FF"/>
  <path d="M48 24 C48 86 98 98 98 120 C98 142 48 154 48 216 M152 24 C152 86 102 98 102 120 C102 142 152 154 152 216" fill="none" stroke="#EEF2FF" stroke-width="7" stroke-linecap="round"/>
  <path class="sandTop" d="M60 44 H140 C134 80 104 96 100 112 C96 96 66 80 60 44 Z" fill="#FFC53D"/>
  <path class="sandBot" d="M100 140 C88 160 60 178 56 206 H144 C140 178 112 160 100 140 Z" fill="#FFC53D"/>
  <path class="stream" d="M100 112 V206" stroke="#FFC53D" stroke-width="4" stroke-dasharray="6 8"/>
</svg>'''


# ---------------------------------------------------------------- s01 Giriş
_lis = T("s01", "lisans")
S["s01"] = dict(
    sfx=[("pop", 0.15, 0.35), ("whoosh-short", _lis - 0.2, 0.3), ("pop", _lis, 0.25), ("pop", T("s01", "Zamanaşımı"), 0.25),
         ("pop", T("s01", "üç"), 0.25), ("pop", T("s01", "peşin"), 0.25), ("ping", T("s01", "arada"), 0.3), ("pop", T("s01", "Kâğıt"), 0.3)],
    keys=dict(hello=T("s01", "Merhaba"), iki=T("s01", "üçüncüsüne"), bugun=T("s01", "Bugün"), sev=T("s01", "sevilen"), lis=_lis,
              zam=T("s01", "Zamanaşımı"), uc=T("s01", "üç"), pes=T("s01", "peşin"), arada=T("s01", "arada"), kagit=T("s01", "Kâğıt")),
    css=r"""
#s01 .sting { position:absolute; left:1060px; top:420px; width:640px; height:150px; display:flex; align-items:center; justify-content:center;
  background:#F4F7FF; border-radius:26px; box-shadow:0 30px 80px rgba(0,0,0,.45); }
#s01 .sting img { width:520px; }
#s01 .right { position:absolute; left:860px; top:150px; width:960px; }
#s01 .t1 { font-family:'Archivo Black'; font-size:80px; white-space:nowrap; line-height:1; color:var(--fg); margin-top:16px; }
#s01 .t2 { display:flex; align-items:baseline; gap:22px; margin-top:8px; white-space:nowrap; }
#s01 .t2 .w { font-family:'Archivo Black'; font-size:128px; line-height:1; color:var(--gold); text-shadow:0 10px 40px rgba(255,197,61,.35); }
#s01 .t2 .s { font:800 30px Montserrat; color:var(--muted); }
#s01 .topic { position:absolute; left:860px; top:560px; width:960px; height:300px; display:flex; align-items:center; gap:30px; padding:0 34px; }
#s01 .topic .hg { flex:none; }
#s01 .topic .tx small { display:block; font:700 22px 'JetBrains Mono'; color:var(--accent2); letter-spacing:.14em; }
#s01 .topic .tx > b { display:block; font:900 44px/1.1 Montserrat; color:var(--fg); margin-top:6px; white-space:nowrap; }
#s01 .topic .tx > b em { font-style:normal; color:var(--teal); }
#s01 .chips { display:flex; gap:12px; margin-top:16px; }
#s01 .chips span { font:800 22px Montserrat; padding:6px 14px; border-radius:12px; white-space:nowrap; }
#s01 .chips .c1 { background:rgba(51,217,178,.14); border:2px solid var(--teal); color:#C9FFF0; }
#s01 .chips .c2 { background:rgba(255,197,61,.16); border:2px solid var(--gold); color:var(--gold); }
#s01 .chips .c3 { background:rgba(255,77,94,.14); border:2px solid var(--uyari); color:#FFC9CF; }
#s01 .chips .c4 { background:rgba(46,212,122,.14); border:2px solid var(--ok); color:#CFFFE5; }
#s01 .qq { margin-top:16px; font:800 26px Montserrat; color:var(--muted); white-space:nowrap; }
#s01 .qq b { color:var(--gold); display:inline-block; }
#s01 .tz { position:absolute; right:-18px; top:-30px; }
#s01 .ready { position:absolute; left:1250px; top:876px; }
""",
    body=f'''
<div class="sting"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div>
<div class="right">
  <div class="kicker k1">GÜMRÜK KOÇU · HESAPLAMA DERSLERİ</div>
  <div class="t1">VERGİ HESAPLAMA</div>
  <div class="t2"><span class="w">DERS #3</span><span class="s">örnek soru · adım adım</span></div>
</div>
<div class="topic card">
  {hourglass("hg", 170)}
  <div class="tx"><small>KONU · SONRADAN KONTROL</small><b>Lisans ücreti &amp; <em>zamanaşımı</em></b>
    <div class="chips"><span class="c1">Lisans ücreti</span><span class="c2">Zamanaşımı</span><span class="c3">3 kat ceza</span><span class="c4">Peşin ödeme</span></div>
    <div class="qq">Hangi yıllar <b>hesaba girer?</b></div></div>
  <div class="tz">{badge("tuzak")}</div>
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
tl.fromTo(q(".hg .sandTop"), { scaleY: 1 }, { scaleY: 0.12, duration: D - K.bugun, ease: "none", transformOrigin: "50% 100%" }, K.bugun);
tl.fromTo(q(".hg .sandBot"), { scaleY: 0.12 }, { scaleY: 1, duration: D - K.bugun, ease: "none", transformOrigin: "50% 100%" }, K.bugun);
tl.fromTo(q(".hg .stream"), { strokeDashoffset: 0 }, { strokeDashoffset: -14 * (D - K.bugun) * 3, duration: D - K.bugun, ease: "none" }, K.bugun);
slam(".topic .tz", K.sev);
pop(".chips .c1", K.lis, 0, "back.out(2.6)");
pop(".chips .c2", K.zam, 0, "back.out(2.6)");
pop(".chips .c3", K.uc, 0, "back.out(2.6)");
pop(".chips .c4", K.pes, 0, "back.out(2.6)");
rise(".topic .qq", K.arada, 0, 20);
pulse(".topic .qq b", K.arada + 0.7, 1.1);
tl.fromTo(q(".ready"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "back.out(2)" }, K.kagit);
tl.fromTo(q(".ready .ico"), { rotation: 0 }, { rotation: 14, duration: 0.2, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 50%" }, K.kagit + 0.5);
"""
)

# ---------------------------------------------------------------- s02 Soru
YEARS = [("2021", "8.000", "8"), ("2022", "15.000", "15"), ("2023", "20.000", "20")]
S["s02"] = dict(
    sfx=[("whoosh-short", T("s02", "firmasının") - 0.1, 0.3), ("error", T("s02", "etmediği"), 0.25), ("pop", T("s02", "yılında", 1), 0.3),
         ("pop", T("s02", "yılında", 2), 0.3), ("pop", T("s02", "yılında", 3), 0.3), ("pop", T("s02", "Gümrük"), 0.25), ("pop", T("s02", "KDV"), 0.25),
         ("ping", T("s02", "Firma"), 0.3), ("notification", T("s02", "Soru"), 0.35)],
    keys=dict(once=T("s02", "Önce"), haz=T("s02", "haziran"), firma=T("s02", "firmasının"), etm=T("s02", "etmediği"), ilgili=T("s02", "ilgili"),
              mart=T("s02", "mart"), y1=T("s02", "yılında", 1), y2=T("s02", "yılında", 2), y3=T("s02", "yılında", 3),
              gv=T("s02", "Gümrük"), kdv=T("s02", "KDV"), firma2=T("s02", "Firma"), gun=T("s02", "gün"), soru=T("s02", "Soru")),
    css=r"""
#s02 .hdr { position:absolute; left:600px; top:132px; }
#s02 .hdr .h1 { font-size:60px; }
#s02 .det { position:absolute; left:600px; top:268px; width:900px; height:140px; display:flex; align-items:center; gap:22px; padding:0 26px; }
#s02 .det .ico { color:var(--accent2); }
#s02 .det > div > b { display:block; font:900 30px Montserrat; }
#s02 .det .sub { display:block; font:400 21px 'JetBrains Mono'; color:var(--muted); margin-top:6px; white-space:nowrap; }
#s02 .det .sub em { font-style:normal; font-weight:700; color:var(--gold); }
#s02 .det .stp { margin-left:auto; padding:10px 16px; border:5px solid var(--uyari); border-radius:12px; color:#FF8A96; font:900 21px/1.15 Montserrat;
  text-align:center; transform:rotate(-4deg); background:rgba(255,77,94,.08); white-space:nowrap; }
#s02 .yrs { position:absolute; left:600px; top:426px; width:900px; display:flex; gap:16px; }
#s02 .yr { flex:1; height:178px; padding:16px 20px; position:relative; }
#s02 .yr .y { display:flex; align-items:baseline; gap:10px; font-family:'Archivo Black'; font-size:40px; color:var(--fg); line-height:1; }
#s02 .yr .y small { font:800 18px 'JetBrains Mono'; color:var(--accent2); letter-spacing:.1em; }
#s02 .yr .usd { font:700 40px 'JetBrains Mono'; color:var(--usd); margin-top:14px; white-space:nowrap; }
#s02 .yr .kur { font:800 21px Montserrat; color:var(--muted); margin-top:6px; }
#s02 .yr .kur b { color:var(--fg); }
#s02 .yr .lic { position:absolute; right:16px; top:16px; color:var(--gold); }
#s02 .rates { position:absolute; left:600px; top:622px; width:900px; display:flex; gap:14px; }
#s02 .rate { flex:1; height:150px; border-radius:20px; display:flex; flex-direction:column; align-items:center; justify-content:center; }
#s02 .rate small { font:900 16px Montserrat; letter-spacing:.04em; white-space:nowrap; }
#s02 .rate b { font-family:'Archivo Black'; font-size:58px; line-height:1; margin-top:8px; white-space:nowrap; }
#s02 .rate b.sm { font-size:36px; margin-top:12px; }
#s02 .g-gv { background:rgba(255,197,61,.14); border:3px solid var(--gold); color:var(--gold); }
#s02 .g-kdv { background:rgba(51,217,178,.12); border:3px solid var(--teal); color:var(--teal); }
#s02 .g-pes { flex:1.4; background:rgba(46,212,122,.12); border:3px solid var(--ok); color:var(--ok); }
#s02 .cano { position:absolute; left:1556px; top:300px; height:470px; filter:drop-shadow(0 18px 30px rgba(0,0,0,.45)); }
#s02 .ctag { position:absolute; left:1572px; top:720px; font:900 20px Montserrat; letter-spacing:.08em; color:#071A45; background:var(--accent2);
  padding:6px 14px; border-radius:10px; box-shadow:0 8px 20px rgba(0,0,0,.35); }
#s02 .bub { position:absolute; left:1530px; top:168px; width:290px; padding:14px 18px; background:#F4F7FF; color:#0B1A44; border-radius:20px; font:900 24px/1.25 Montserrat; }
#s02 .bub:after { content:""; position:absolute; left:120px; bottom:-22px; border:12px solid transparent; border-top:14px solid #F4F7FF; }
#s02 .bub em { font-style:normal; color:#0B8A47; }
#s02 .ask { position:absolute; left:600px; top:790px; width:1220px; height:110px; display:flex; align-items:center; gap:26px; padding:0 30px;
  background:rgba(63,107,255,.18); border:3px solid var(--accent); border-radius:20px; }
#s02 .ask .t { font:800 34px Montserrat; color:var(--fg); }
#s02 .ask .t b { color:var(--gold); display:inline-block; }
#s02 .ask .t em { font-style:normal; color:var(--teal); }
""",
    body=f'''
<div class="hdr"><div class="kicker">ÖRNEK SORU · VERİLER</div><div class="h1">Unutulan lisans ücreti</div></div>
<div class="det card">{icon("search", 60)}<div><b>M firması · sonradan kontrol</b><span class="sub">kontrol: <em>Haziran 2024</em> · ödeme + ithalat: her yıl <em>mart</em></span></div>
  <div class="stp">LİSANS ÜCRETİ<br/>BEYAN EDİLMEMİŞ</div></div>
<div class="yrs">{"".join(f'<div class="yr card y{i}"><span class="lic">{icon("doc", 34)}</span><div class="y">{y}<small>MART</small></div><div class="usd">{u} $</div><div class="kur">kur: 1 $ = <b>{k} TL</b></div></div>' for i, (y, u, k) in enumerate(YEARS, 1))}</div>
<div class="rates">
  <div class="rate g-gv"><small>GÜMRÜK VERGİSİ</small><b>%8</b></div>
  <div class="rate g-kdv"><small>KDV</small><b>%20</b></div>
  <div class="rate g-pes"><small>CEZA · PEŞİN ÖDEME</small><b class="sm">15 GÜN</b></div>
</div>
<img class="cano" src="assets/img/cano-cut.png" alt="M firması temsilcisi" />
<div class="ctag">M FİRMASI</div>
<div class="bub">Vergi ve cezayı <em>15 günde peşin</em> ödeyelim!</div>
<div class="ask">{badge("soru")}<div class="t">İstenen: <b>vergi + ceza</b> toplam ödeme = ? <em>TL</em></div></div>
''',
    js=r"""
rise(".hdr", K.once, 0, 30);
slideX(".det", K.haz - 0.6, -60);
tl.fromTo(q(".cano"), { x: 300, opacity: 0 }, { x: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }, K.firma);
rise(".ctag", K.firma + 0.5, 0, 20);
slam(".det .stp", K.etm);
pulse(".det .sub", K.mart, 1.05);
pop(".yrs .y1", K.y1 - 0.4);
pop(".yrs .y2", K.y2 - 0.4);
pop(".yrs .y3", K.y3 - 0.4);
pop(".rates .g-gv", K.gv);
pop(".rates .g-kdv", K.kdv);
pop(".rates .g-pes", K.gun - 0.3);
tl.fromTo(q(".bub"), { scale: 0.3, opacity: 0, transformOrigin: "40% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.firma2);
tl.fromTo(q(".ask"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "back.out(1.6)" }, K.soru);
pulse(".ask .t b", K.soru + 1.0, 1.1);
"""
)

# ---------------------------------------------------------------- s03 Şıklar + geri sayım
_s03 = SCENES["s03"]
_end = round(_s03["audio_local"] + _s03["audio_dur"], 2)
OPTS = [("A", "185.000"), ("B", "568.750"), ("C", "601.250"), ("D", "662.818"), ("E", "740.000")]
S["s03"] = dict(
    sfx=[("pop", T("s03", L), 0.28) for L, _ in OPTS] + [("notification", T("s03", "Videoyu"), 0.35)]
        + [("click-soft", _end + 0.2 + i, 0.4) for i in range(5)] + [("chime", _end + 5.15, 0.35)],
    keys=dict(sik=T("s03", "Şıklarımız"), A=T("s03", "A"), B=T("s03", "B"), C=T("s03", "C"), Dk=T("s03", "D"), E=T("s03", "E"),
              vid=T("s03", "Videoyu"), end=_end),
    css=r"""
#s03 .hdr { position:absolute; left:600px; top:132px; }
#s03 .opts { position:absolute; left:600px; top:290px; width:760px; }
#s03 .opt { display:flex; align-items:center; gap:26px; height:104px; margin-bottom:16px; padding:0 30px 0 18px; }
#s03 .opt .L { width:72px; height:72px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black';
  font-size:38px; color:#071A45; background:var(--accent2); flex:none; }
#s03 .opt .v { font:700 56px 'JetBrains Mono'; color:var(--fg); }
#s03 .opt .u { font:800 28px Montserrat; color:var(--muted); margin-left:auto; }
#s03 .stop { position:absolute; left:1420px; top:270px; width:400px; height:620px; display:flex; flex-direction:column; align-items:center; padding-top:34px; }
#s03 .stop .pz { width:150px; height:150px; border-radius:50%; background:var(--uyari); color:#fff; display:flex; align-items:center; justify-content:center;
  box-shadow:0 0 0 14px rgba(255,77,94,.18), 0 20px 50px rgba(0,0,0,.4); }
#s03 .stop .pt { font:900 34px/1.15 Montserrat; text-align:center; margin-top:28px; color:var(--fg); }
#s03 .stop .ps { font:700 22px 'JetBrains Mono'; color:var(--muted); margin-top:10px; letter-spacing:.08em; }
#s03 .ring { position:relative; width:200px; height:200px; margin-top:26px; }
#s03 .ring svg { position:absolute; inset:0; transform:rotate(-90deg); }
#s03 .ring .n { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:96px; color:var(--gold); opacity:0; }
""",
    body=f'''
<div class="hdr">{badge("soru")}<div class="h1">Hangisi doğru?</div></div>
<div class="opts">{"".join(f'<div class="opt card o{L}"><span class="L">{L}</span><span class="v">{v}</span><span class="u">TL</span></div>' for L, v in OPTS)}</div>
<div class="stop card"><div class="pz">{icon("pause", 84)}</div><div class="pt">Videoyu durdur,<br/>önce sen çöz!</div><div class="ps">SÜRE BAŞLIYOR</div>
  <div class="ring"><svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="86" fill="none" stroke="#2B4C9E" stroke-width="14"/>
    <circle class="arc" cx="100" cy="100" r="86" fill="none" stroke="#FFC53D" stroke-width="14" stroke-linecap="round"/></svg>
    {"".join(f'<div class="n n{k}">{k}</div>' for k in (5, 4, 3, 2, 1))}</div></div>
''',
    js=r"""
rise(".hdr", K.sik, 0, 30);
["A", "B", "C", "Dk", "E"].forEach((k, i) => slideX(".o" + "ABCDE"[i], K[k], -90));
["A", "B", "C", "Dk", "E"].forEach((k, i) => pulse(".o" + "ABCDE"[i] + " .L", K[k] + 0.45, 1.18));
tl.fromTo(q(".stop"), { x: 120, opacity: 0 }, { x: 0, opacity: 1, duration: 0.65, ease: "expo.out" }, K.vid);
tl.fromTo(q(".stop .pz"), { scale: 0.4 }, { scale: 1, duration: 0.6, ease: "back.out(2.4)" }, K.vid + 0.15);
breathe(".stop .pz", K.vid + 0.8, D - 0.5, 0.06, 1.0);
q(".ring .arc").forEach((p) => { p.setAttribute("pathLength", "1"); p.style.strokeDasharray = "1 1"; });
tl.fromTo(q(".ring .arc"), { strokeDashoffset: 0 }, { strokeDashoffset: 1, duration: 5.0, ease: "none" }, K.end + 0.15);
[5, 4, 3, 2, 1].forEach((k, i) => {
  const at = K.end + 0.15 + i;
  tl.fromTo(q(".ring .n" + k), { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2)" }, at);
  tl.to(q(".ring .n" + k), { opacity: 0, duration: 0.15 }, at + 0.85);
});
"""
)

# ---------------------------------------------------------------- s04 Üç anahtar
KEYCARDS = [("k1", "1", "doc", "Kıymete ekle", "Eşyayla ilgili ve <b>satış koşulu</b> olarak ödenen lisans ücreti → <b>gümrük kıymetine eklenir</b>", "GK md. 27/1-c", "var(--teal)"),
            ("k2", "2", "clock", "Zamanaşımı: 3 yıl", "Eksik vergiler, yükümlülüğün <b>doğduğu tarihten itibaren 3 yıl</b> içinde tebliğ edilmeli", "GK md. 197/2", "var(--gold)"),
            ("k3", "3", "check", "Peşin ödeme: ¾", "Ceza kararı <b>tebliğden itibaren 15 gün</b> içinde peşin ödenirse cezanın <b>dörtte üçü</b> tahsil edilir", "Kabahatler K. md. 17/6", "var(--ok)")]
S["s04"] = dict(
    sfx=[("impact-bass-1", T("s04", "anahtarı"), 0.35), ("whoosh-short", T("s04", "Bir") - 0.2, 0.3), ("whoosh-short", T("s04", "İki") - 0.2, 0.3),
         ("whoosh-short", T("s04", "üç", 3) - 0.2, 0.3), ("ping", T("s04", "eklenir"), 0.3), ("ping", T("s04", "edilmelidir"), 0.3), ("chime", T("s04", "tahsil"), 0.35)],
    keys=dict(anah=T("s04", "anahtarı"), bir=T("s04", "Bir"), kiy=T("s04", "kıymetine"), iki=T("s04", "İki"), yil=T("s04", "üç", 2),
              uc=T("s04", "üç", 3), dort=T("s04", "dörtte")),
    css=r"""
#s04 .top { position:absolute; left:600px; top:132px; display:flex; align-items:center; gap:26px; }
#s04 .top .kicker { font-size:26px; }
#s04 .kc { position:absolute; left:600px; width:1220px; height:166px; display:flex; align-items:center; gap:26px; padding:0 30px 0 22px; }
#s04 .k1 { top:262px; } #s04 .k2 { top:446px; } #s04 .k3 { top:630px; }
#s04 .kc .num { width:92px; height:92px; border-radius:24px; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:52px;
  color:#071A45; flex:none; }
#s04 .kc .ib { width:72px; height:72px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:rgba(143,178,255,.14); color:var(--accent2); flex:none; }
#s04 .kc .tx { flex:1; }
#s04 .kc .tx b.t { display:block; font:900 34px Montserrat; color:var(--fg); }
#s04 .kc .tx p { font:600 25px/1.3 Montserrat; color:#C9D3F2; margin-top:6px; }
#s04 .kc .tx p b { color:var(--fg); font-weight:900; }
#s04 .kc .ref { flex:none; font:700 19px 'JetBrains Mono'; color:#071A45; background:var(--accent2); padding:6px 12px; border-radius:9px; white-space:nowrap; }
#s04 .order { position:absolute; left:600px; top:822px; display:flex; align-items:center; gap:14px; font:800 22px Montserrat; color:var(--muted); }
#s04 .order span { padding:6px 12px; border-radius:10px; background:rgba(255,255,255,.07); border:2px solid rgba(255,255,255,.2); color:var(--fg); }
""",
    body=f'''
<div class="top">{badge("onemli", big=True)}<div class="kicker">SORUNUN 3 ANAHTARI</div></div>
{"".join(f'<div class="kc card {k}" style="border-color:{c}"><span class="num" style="background:{c}">{n}</span><span class="ib">{icon(ic, 40)}</span><div class="tx"><b class="t">{t}</b><p>{p}</p></div><span class="ref">{r}</span></div>' for k, n, ic, t, p, r, c in KEYCARDS)}
<div class="order">SIRA: <span>süre</span>{icon("arrow", 26)}<span>kıymet</span>{icon("arrow", 26)}<span>vergi</span>{icon("arrow", 26)}<span>ceza</span>{icon("arrow", 26)}<span>indirim</span></div>
''',
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 2.4, opacity: 0, rotation: -8 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.anah);
rise(".top .kicker", K.anah + 0.4, 0, 20);
slideX(".k1", K.bir - 0.2, -100);
pulse(".k1 .ref", K.kiy + 0.4, 1.12);
slideX(".k2", K.iki - 0.2, -100);
pulse(".k2 .ref", K.yil + 0.4, 1.12);
slideX(".k3", K.uc - 0.2, -100);
pulse(".k3 .ref", K.dort + 0.4, 1.12);
rise(".order", K.dort + 1.2, 0, 20);
"""
)

# ---------------------------------------------------------------- s05 Adım 1: zamanaşımı çizelgesi
X0, PX = 690, 270            # Jan 2021 at x=690, 270 px per year
def _x(y, m):
    return round(X0 + (y - 2021 + (m - 1) / 12) * PX, 1)
_kx = _x(2024, 6)
_rows = [(2021, 404, "#FF4D5E"), (2022, 494, "#2ED47A"), (2023, 584, "#2ED47A")]
_bars = []
for y, yy, col in _rows:
    sx, ex = _x(y, 3), min(_x(y + 3, 3), 1800)
    _bars.append(f'<g class="row b{y}"><circle cx="{sx}" cy="{yy}" r="13" fill="{col}"/>'
                 f'<rect class="bar" x="{sx}" y="{yy - 11}" width="{round(ex - sx, 1)}" height="22" rx="11" fill="{col}" opacity=".85"/>'
                 f'<text x="{sx - 24}" y="{yy + 8}" text-anchor="end" class="yl">{y}</text></g>')
_ticks = "".join(f'<path d="M{_x(y, 1)} 330 V650" stroke="#2B4C9E" stroke-width="2"/><text x="{_x(y, 1) + 8}" y="676" class="tk">{y}</text>' for y in range(2021, 2026))
S["s05"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("pop", T("s05", "haziranında"), 0.3), ("click-soft", T("s05", "mart"), 0.4), ("error", T("s05", "doldu"), 0.3),
         ("pop", T("s05", "iki", 4), 0.3), ("pop", T("s05", "iki", 6), 0.3), ("chime", T("s05", "içinde"), 0.35)],
    keys=dict(bir=T("s05", "Birinci"), kon=T("s05", "Kontrol"), haz=T("s05", "haziranında"), mart=T("s05", "mart"), sure=T("s05", "süresi"),
              doldu=T("s05", "doldu"), ist=T("s05", "istenemez"), y22=T("s05", "iki", 4), y23=T("s05", "iki", 6), ic=T("s05", "içinde")),
    css=STEPS_CSS + r"""
#s05 .tlc { position:absolute; left:600px; top:236px; width:1220px; height:500px; padding:22px 30px; }
#s05 .tlc .kicker { color:var(--gold); }
#s05 svg.tl { position:absolute; left:0; top:0; width:1920px; height:1080px; overflow:visible; }
#s05 svg.tl .yl { font:900 26px 'JetBrains Mono'; fill:#EEF2FF; }
#s05 svg.tl .tk { font:700 18px 'JetBrains Mono'; fill:#7E8DBA; }
#s05 svg.tl .kl { font:900 20px Montserrat; fill:#FF8A96; letter-spacing:.06em; }
#s05 .exp { position:absolute; left:1330px; top:386px; padding:8px 16px; border:5px solid var(--uyari); border-radius:12px; color:#FF8A96;
  font-family:'Archivo Black'; font-size:30px; line-height:1; background:rgba(7,26,69,.92); transform:rotate(-6deg); }
#s05 .okk { position:absolute; display:flex; align-items:center; gap:8px; font:900 20px Montserrat; color:#03221a; background:var(--ok); padding:6px 12px; border-radius:10px; }
#s05 .o22 { left:1650px; top:436px; } #s05 .o23 { left:1650px; top:526px; }
#s05 .res { position:absolute; left:600px; top:760px; width:1220px; height:120px; display:flex; align-items:center; gap:24px; padding:0 30px; }
#s05 .res .yy { display:flex; gap:14px; }
#s05 .res .yy span { font-family:'Archivo Black'; font-size:40px; padding:6px 18px; border-radius:14px; }
#s05 .res .yy .no { color:#7D88A8; background:rgba(255,77,94,.12); text-decoration:line-through; text-decoration-color:var(--uyari); text-decoration-thickness:5px; }
#s05 .res .yy .ok { color:#DFFFEF; background:rgba(46,212,122,.18); border:3px solid var(--ok); }
#s05 .res .t { font:800 27px/1.25 Montserrat; color:var(--fg); }
#s05 .res .t small { display:block; font:700 19px 'JetBrains Mono'; color:var(--muted); margin-top:4px; }
""",
    body=f'''
{steps(1)}
<div class="tlc card"><div class="kicker">ADIM 1 · ZAMANAŞIMI ÇİZELGESİ · GK 197/2</div></div>
<svg class="tl" viewBox="0 0 1920 1080">
  {_ticks}
  <path class="kline" d="M{_kx} 318 V662" stroke="#FF4D5E" stroke-width="5" stroke-dasharray="12 8"/>
  <text class="kl klab" x="{_kx - 12}" y="336" text-anchor="end">KONTROL · HAZİRAN 2024</text>
  {"".join(_bars)}
</svg>
<div class="exp">SÜRE DOLDU</div>
<div class="okk o22">{icon("check", 22)} SÜRE İÇİNDE</div><div class="okk o23">{icon("check", 22)} SÜRE İÇİNDE</div>
<div class="res card"><div class="yy"><span class="no">2021</span><span class="ok">2022</span><span class="ok">2023</span></div>
  <div class="t">Hesaba yalnızca 2022 ve 2023 girer<small>2021: vergi ve ceza istenemez</small></div></div>
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
pulse(".steps .stp.on .dot", K.bir, 1.25);
tl.fromTo(q(".tlc"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.bir);
fadeIn("svg.tl path:not(.kline), svg.tl .tk", K.bir + 0.3, 0.5);
fadeTo("svg.tl .row, .exp, .okk, .res, svg.tl .kline, svg.tl .klab", 0.01, 0, 0.01);
fadeIn("svg.tl .kline, svg.tl .klab", K.haz - 0.2, 0.3);
draw("svg.tl .kline", K.haz - 0.2, 0.6);
fadeIn("svg.tl .b2021", K.mart - 0.1, 0.2);
tl.fromTo(q("svg.tl .b2021 .bar"), { scaleX: 0 }, { scaleX: 1, duration: 1.2, ease: "power2.out", transformOrigin: "0% 50%" }, K.sure - 0.3);
slam(".exp", K.doldu);
fadeTo("svg.tl .b2021", K.ist, 0.45, 0.4);
fadeIn("svg.tl .b2022", K.y22 - 0.1, 0.2);
tl.fromTo(q("svg.tl .b2022 .bar"), { scaleX: 0 }, { scaleX: 1, duration: 0.9, ease: "power2.out", transformOrigin: "0% 50%" }, K.y22);
fadeIn("svg.tl .b2023", K.y23 - 0.1, 0.2);
tl.fromTo(q("svg.tl .b2023 .bar"), { scaleX: 0 }, { scaleX: 1, duration: 0.9, ease: "power2.out", transformOrigin: "0% 50%" }, K.y23);
pop(".okk.o22", K.y22 + 0.9, 0, "back.out(3)");
pop(".okk.o23", K.y23 + 0.9, 0, "back.out(3)");
tl.fromTo(q(".res"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "back.out(1.6)" }, K.ic - 0.6);
"""
)

# ---------------------------------------------------------------- s06 Adım 2: kıymet + vergiler
S["s06"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("click-soft", T("s06", "On"), 0.4), ("click-soft", T("s06", "yirmi", 2), 0.4), ("ping", T("s06", "Toplam") + 0.4, 0.3),
         ("click-soft", T("s06", "Gümrük"), 0.4), ("notification", T("s06", "dikkat"), 0.3), ("click-soft", T("s06", "Bunun"), 0.4), ("chime", T("s06", "seksen") + 0.3, 0.35)],
    keys=dict(ik=T("s06", "İkinci"), on=T("s06", "On"), iki=T("s06", "iki"), y2=T("s06", "yirmi", 2), dort=T("s06", "dört"), top=T("s06", "Toplam"),
              gv=T("s06", "Gümrük"), elli=T("s06", "elli"), dik=T("s06", "dikkat"), kdv=T("s06", "KDV"), yet=T("s06", "yetmiş"),
              bunun=T("s06", "Bunun"), otuz=T("s06", "otuz"), eks=T("s06", "Eksik"), sek=T("s06", "seksen")),
    css=STEPS_CSS + LEDGER_CSS + r"""
#s06 .main { position:absolute; left:600px; top:236px; width:700px; height:640px; padding:22px 30px; }
#s06 .main .kicker { color:var(--teal); }
#s06 .dk { position:absolute; left:1080px; top:212px; }
#s06 .rw { display:flex; align-items:baseline; gap:12px; margin-top:12px; font:700 31px 'JetBrains Mono'; color:var(--fg); white-space:nowrap; }
#s06 .rw small { font:800 15px Montserrat; letter-spacing:.04em; color:var(--muted); width:112px; flex:none; }
#s06 .rw .op { color:var(--muted); }
#s06 .rw .v { display:inline-block; }
#s06 .rw.k .v { color:var(--usd); } #s06 .rw.g .v { color:var(--gold); } #s06 .rw.m .v { color:var(--accent2); } #s06 .rw.d .v { color:var(--teal); }
#s06 .rw.tot { margin-top:14px; padding-top:10px; border-top:3px solid rgba(255,255,255,.25); }
#s06 .rw.tot .v { color:#DFFFEF; font-size:36px; }
#s06 .sum { display:flex; align-items:baseline; gap:16px; margin-top:16px; padding-top:12px; border-top:5px solid var(--fg); white-space:nowrap; }
#s06 .sum small { font:900 24px Montserrat; letter-spacing:.06em; color:var(--teal); }
#s06 .sum b { font-family:'Archivo Black'; font-size:58px; line-height:1; color:#DFFFF6; display:inline-block; }
#s06 .sum em { font-style:normal; font:800 28px Montserrat; color:var(--teal); }
#s06 .ledger { top:236px; }
""",
    body=f'''
{steps(2)}
<div class="main card"><div class="kicker">ADIM 2 · KIYMET VE VERGİLER</div>
  <div class="rw k r1"><small>2022</small><span>15.000 $ × 15</span><span class="op">=</span><span class="v c1">0</span></div>
  <div class="rw k r2"><small>2023</small><span>20.000 $ × 20</span><span class="op">=</span><span class="v c2">0</span></div>
  <div class="rw tot r3"><small>KIYMET</small><span class="op">Σ =</span><span class="v c3">0</span><span class="op">TL</span></div>
  <div class="rw g r4"><small>GV</small><span>625.000 × %8</span><span class="op">=</span><span class="v c4">0</span></div>
  <div class="rw m r5"><small>KDV MATR.</small><span>625.000 + 50.000</span><span class="op">=</span><span class="v c5">0</span></div>
  <div class="rw d r6"><small>KDV</small><span>675.000 × %20</span><span class="op">=</span><span class="v c6">0</span></div>
  <div class="sum"><small>EKSİK VERGİ</small><b class="c7">0</b><em>TL</em></div>
</div>
<div class="dk">{badge("dikkat")}</div>
{ledger([("2021", "—", "out"), ("Eksik GV", "50.000", ""), ("Eksik KDV", "135.000", "")])}
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".main"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.ik);
tl.fromTo(q(".ledger"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.ik + 0.2);
rise(".r1", K.on, 0, 20);
count(".r1 .c1", K.iki - 0.2, 0, 225000, 0.7, 0);
rise(".r2", K.y2, 0, 20);
count(".r2 .c2", K.dort - 0.2, 0, 400000, 0.7, 0);
rise(".r3", K.top, 0, 20);
count(".r3 .c3", K.top + 0.3, 0, 625000, 0.8, 0);
pulse(".r3 .v", K.top + 1.2, 1.15);
rise(".r4", K.gv, 0, 20);
count(".r4 .c4", K.elli - 0.2, 0, 50000, 0.6, 0);
write(".ledger .r1", K.elli + 0.4, 0.6);
slam(".dk", K.dik);
rise(".r5", K.kdv, 0, 20);
count(".r5 .c5", K.yet - 0.4, 0, 675000, 0.7, 0);
pulse(".r5 .v", K.yet + 0.5, 1.15);
rise(".r6", K.bunun, 0, 20);
count(".r6 .c6", K.otuz - 0.4, 0, 135000, 0.7, 0);
write(".ledger .r2", K.otuz + 0.5, 0.6);
rise(".sum", K.eks, 0, 20);
count(".sum .c7", K.sek - 0.4, 0, 185000, 0.8, 0);
pulse(".sum b", K.sek + 0.6, 1.12);
"""
)
