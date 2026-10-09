"""Scenes 01-06: giriş, soru, şıklar, anahtar kural, adım 1-2."""
from lib import T, D, SCENES, icon, badge

S = {}


def disc(uid, size=300, cls="disc"):
    """Spinning CD: rainbow sheen group carries class sheen (rotate with svgOrigin 150 150)."""
    return f'''<svg class="{cls}" viewBox="0 0 300 300" width="{size}" height="{size}" aria-hidden="true">
  <defs>
    <radialGradient id="{uid}-g" cx="50%" cy="50%" r="50%"><stop offset=".18" stop-color="#E9EEFF"/><stop offset=".7" stop-color="#B8C6EC"/><stop offset="1" stop-color="#8FA3D6"/></radialGradient>
    <linearGradient id="{uid}-r" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF7AD9"/><stop offset=".3" stop-color="#FFD84D"/><stop offset=".55" stop-color="#5CFFB0"/><stop offset=".8" stop-color="#57B8FF"/><stop offset="1" stop-color="#A47BFF"/></linearGradient>
  </defs>
  <circle cx="150" cy="150" r="142" fill="url(#{uid}-g)" stroke="#DCE7FF" stroke-width="4"/>
  <g class="sheen"><path d="M150 150 L150 8 A142 142 0 0 1 273 79 Z" fill="url(#{uid}-r)" opacity=".6"/><path d="M150 150 L150 292 A142 142 0 0 1 27 221 Z" fill="url(#{uid}-r)" opacity=".45"/></g>
  <circle cx="150" cy="150" r="100" fill="none" stroke="#FFFFFF" stroke-width="2" opacity=".5"/>
  <circle cx="150" cy="150" r="46" fill="#0B2257" stroke="#8FB2FF" stroke-width="5"/><circle cx="150" cy="150" r="16" fill="#071A45"/>
</svg>'''


def steps(active):
    names = ["GÜMRÜK VERGİSİ", "KDV MATRAHI", "KDV", "SONUÇ"]
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


def ledger(lines, write_last=True):
    """Notebook 'çözüm defteri': list of (label, value, cls). The last line is the one written in this scene."""
    rows = []
    for i, (lab, val, cls) in enumerate(lines):
        new = " new" if (write_last and i == len(lines) - 1) else ""
        rows.append(f'<div class="ln {cls}{new}"><span class="lb">{lab}</span><span class="dots"></span><span class="vl">{val}</span></div>')
    empty = "".join('<div class="ln blank"></div>' for _ in range(max(0, 4 - len(lines))))
    return f'<div class="ledger"><div class="lh">{icon("pen", 30)}ÇÖZÜM DEFTERİ</div>{"".join(rows)}{empty}</div>'


LEDGER_CSS = r"""
.ledger { position:absolute; left:1330px; top:250px; width:490px; height:560px; background:#FBF8EE; border-radius:16px; padding:22px 26px 0 64px;
  box-shadow:0 26px 60px rgba(0,0,0,.4); color:#1B2A57; overflow:hidden;
  background-image:linear-gradient(90deg, transparent 46px, #F2A0A0 46px, #F2A0A0 49px, transparent 49px), repeating-linear-gradient(#FBF8EE 0 89px, #C9D6EE 89px 91px); }
.ledger .lh { display:flex; align-items:center; gap:12px; font:900 22px Montserrat; letter-spacing:.1em; color:#2B47A8; height:70px; margin-top:-6px; }
.ledger .ln { display:flex; align-items:baseline; gap:10px; height:91px; padding-top:36px; font:700 26px 'JetBrains Mono'; }
.ledger .ln .lb { font:800 25px Montserrat; white-space:nowrap; }
.ledger .ln .dots { flex:1; border-bottom:3px dotted #8C9BC4; transform:translateY(-6px); }
.ledger .ln .vl { font:700 27px 'JetBrains Mono'; color:#0B6B4F; white-space:nowrap; }
.ledger .ln.tot .lb, .ledger .ln.tot .vl { color:#B4231B; }
.ledger .ln.tot .vl { text-decoration:underline double; }
"""

# ---------------------------------------------------------------- s01 Giriş
S["s01"] = dict(
    sfx=[("pop", 0.15, 0.35), ("whoosh-short", T("s01", "Konumuz") - 0.2, 0.3), ("pop", T("s01", "Kâğıdınızı"), 0.3)],
    keys=dict(hello=T("s01", "Merhaba"), bugun=T("s01", "Bugün"), konu=T("s01", "Konumuz"), cd=T("s01", "CD"),
              yaz=T("s01", "yazılım"), kagit=T("s01", "Kâğıdınızı"), birlikte=T("s01", "birlikte")),
    css=r"""
#s01 .sting { position:absolute; left:1060px; top:420px; width:640px; height:150px; display:flex; align-items:center; justify-content:center;
  background:#F4F7FF; border-radius:26px; box-shadow:0 30px 80px rgba(0,0,0,.45); }
#s01 .sting img { width:520px; }
#s01 .right { position:absolute; left:860px; top:150px; width:960px; }
#s01 .t1 { font-family:'Archivo Black'; font-size:80px; white-space:nowrap; line-height:1; color:var(--fg); margin-top:16px; }
#s01 .t2 { display:flex; align-items:baseline; gap:22px; margin-top:8px; white-space:nowrap; }
#s01 .t2 .w { font-family:'Archivo Black'; font-size:128px; line-height:1; color:var(--gold); text-shadow:0 10px 40px rgba(255,197,61,.35); }
#s01 .t2 .s { font:800 30px Montserrat; color:var(--muted); }
#s01 .topic { position:absolute; left:860px; top:560px; width:960px; height:300px; display:flex; align-items:center; gap:40px; padding:0 40px; }
#s01 .topic .dwrap { position:relative; width:230px; height:230px; flex:none; }
#s01 .topic .code { position:absolute; right:-16px; bottom:-6px; width:96px; height:96px; border-radius:24px; background:var(--teal); color:#03221a;
  display:flex; align-items:center; justify-content:center; box-shadow:0 12px 30px rgba(0,0,0,.35); }
#s01 .topic .tx small { display:block; font:700 22px 'JetBrains Mono'; color:var(--accent2); letter-spacing:.14em; }
#s01 .topic .tx b { display:block; font:900 50px/1.1 Montserrat; color:var(--fg); margin-top:8px; }
#s01 .topic .tx b em { font-style:normal; color:var(--teal); }
#s01 .qs { display:flex; gap:14px; margin-top:20px; }
#s01 .qs span { font:800 26px Montserrat; padding:8px 18px; border-radius:12px; background:rgba(255,197,61,.16); border:2px solid rgba(255,197,61,.6); color:var(--gold); }
#s01 .ready { position:absolute; left:1250px; top:876px; }
""",
    body=f'''
<div class="sting"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div>
<div class="right">
  <div class="kicker k1">GÜMRÜK KOÇU · ÇIKMIŞ SORULAR</div>
  <div class="t1">VERGİ HESAPLAMA</div>
  <div class="t2"><span class="w">SORU #1</span><span class="s">adım adım çözüm</span></div>
</div>
<div class="topic card">
  <div class="dwrap">{disc("s01d", 230)}<div class="code">{icon("code", 58)}</div></div>
  <div class="tx"><small>KONU</small><b>CD içinde gelen <em>yazılım</em></b>
    <div class="qs"><span class="q1">Gümrük vergisi = ?</span><span class="q2">KDV = ?</span></div></div>
</div>
<div class="ready chip">{icon("pen", 32)} Kâğıt + kalem hazır mı? {icon("calc", 32)}</div>
''',
    js=r"""
tl.fromTo(q(".sting"), { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.6, ease: "back.out(1.8)" }, 0.15);
tl.to(q(".sting"), { scale: 0.85, opacity: 0, y: -40, duration: 0.45, ease: "power2.in" }, K.hello - 0.35);
rise(".right .k1", K.hello, 0, 20);
tl.fromTo(q(".t1"), { y: 70, opacity: 0, skewY: 4 }, { y: 0, opacity: 1, skewY: 0, duration: 0.7, ease: "expo.out" }, K.hello + 0.2);
tl.fromTo(q(".t2 .w"), { scale: 2.4, opacity: 0, transformOrigin: "0% 60%" }, { scale: 1, opacity: 1, duration: 0.5, ease: "expo.in" }, K.bugun);
rise(".t2 .s", K.bugun + 0.5, 0, 20);
tl.fromTo(q(".topic"), { y: 220, opacity: 0, rotation: 2 }, { y: 0, opacity: 1, rotation: 0, duration: 0.8, ease: "expo.out" }, K.konu);
tl.fromTo(q(".disc"), { rotation: -120, scale: 0.4 }, { rotation: 0, scale: 1, duration: 0.9, ease: "back.out(1.4)", transformOrigin: "50% 50%" }, K.konu + 0.1);
tl.fromTo(q(".disc .sheen"), { rotation: 0 }, { rotation: 360 * 3, duration: D - K.konu, ease: "none", svgOrigin: "150 150" }, K.konu);
pop(".topic .code", K.yaz, 0, "back.out(3)");
pop(".qs span", K.yaz + 0.5, 0.25);
tl.fromTo(q(".ready"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "back.out(2)" }, K.kagit);
tl.fromTo(q(".ready .ico"), { rotation: 0 }, { rotation: 14, duration: 0.2, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 50%" }, K.kagit + 0.5);
"""
)

# ---------------------------------------------------------------- s02 Soru
S["s02"] = dict(
    sfx=[("click-soft", T("s02", "Taşıyıcı"), 0.4), ("click-soft", T("s02", "yazılımın"), 0.4), ("pop", T("s02", "Gümrük"), 0.3),
         ("pop", T("s02", "KDV"), 0.3), ("ping", T("s02", "Bizden"), 0.35)],
    keys=dict(once=T("s02", "Önce"), ith=T("s02", "İthalatçı"), cd=T("s02", "CD"), bilg=T("s02", "bilgisayarlarda"),
              fat=T("s02", "Faturada"), tas=T("s02", "Taşıyıcı"), on=T("s02", "on"), yaz=T("s02", "yazılımın"), bin=T("s02", "bin"),
              gv=T("s02", "Gümrük"), kdv=T("s02", "KDV"), biz=T("s02", "Bizden")),
    css=r"""
#s02 .hdr { position:absolute; left:600px; top:132px; }
#s02 .who { position:absolute; left:600px; top:318px; width:520px; padding:22px 26px; display:flex; gap:20px; align-items:center; }
#s02 .what { position:absolute; left:600px; top:458px; width:520px; padding:22px 26px; display:flex; gap:20px; align-items:center; }
#s02 .who .ico, #s02 .what .ico { color:var(--accent2); }
#s02 .who b, #s02 .what b { display:block; font:900 28px/1.2 Montserrat; }
#s02 .who span, #s02 .what span { display:block; font:400 21px 'JetBrains Mono'; color:var(--muted); margin-top:4px; }
#s02 .rates { position:absolute; left:600px; top:610px; width:520px; display:flex; gap:20px; }
#s02 .rate { flex:1; height:150px; border-radius:20px; display:flex; flex-direction:column; align-items:center; justify-content:center; }
#s02 .rate small { font:900 19px Montserrat; letter-spacing:.04em; white-space:nowrap; }
#s02 .rate b { font-family:'Archivo Black'; font-size:74px; line-height:1; margin-top:6px; }
#s02 .r-gv { background:rgba(255,197,61,.14); border:3px solid var(--gold); color:var(--gold); }
#s02 .r-kdv { background:rgba(51,217,178,.12); border:3px solid var(--teal); color:var(--teal); }
#s02 .inv { position:absolute; left:1180px; top:250px; width:640px; height:500px; background:#F6F8FF; color:#0B1A44; border-radius:18px;
  padding:28px 34px; box-shadow:0 30px 70px rgba(0,0,0,.45); }
#s02 .inv .ih { display:flex; justify-content:space-between; align-items:center; border-bottom:4px solid #0B1A44; padding-bottom:12px; }
#s02 .inv .ih b { font-family:'Archivo Black'; font-size:40px; letter-spacing:.02em; }
#s02 .inv .ih span { font:700 18px 'JetBrains Mono'; color:#5A6AA0; letter-spacing:.1em; }
#s02 .inv .cols { display:flex; justify-content:space-between; font:700 18px 'JetBrains Mono'; color:#5A6AA0; letter-spacing:.12em; margin:16px 0 4px; }
#s02 .inv .row { position:relative; display:flex; justify-content:space-between; align-items:center; height:108px; border-bottom:2px dashed #B7C3E6; }
#s02 .inv .row .l { display:flex; align-items:center; gap:16px; font:800 28px/1.15 Montserrat; }
#s02 .inv .row .l .ico { color:#2B47A8; }
#s02 .inv .row .l small { display:block; font:600 19px Montserrat; color:#5A6AA0; }
#s02 .inv .row .v { font:700 36px 'JetBrains Mono'; }
#s02 .inv .mk { position:absolute; left:-14px; right:-14px; top:12px; bottom:12px; border-radius:12px; background:rgba(255,197,61,.35); transform-origin:left center; z-index:0; }
#s02 .inv .row > *:not(.mk) { position:relative; z-index:1; }
#s02 .inv .tot { display:flex; justify-content:space-between; margin-top:20px; font:800 26px Montserrat; color:#5A6AA0; }
#s02 .inv .tot b { font:700 30px 'JetBrains Mono'; color:#0B1A44; }
#s02 .two { position:absolute; left:1590px; top:206px; font:900 26px Montserrat; color:#2a1d00; background:var(--gold); padding:8px 18px; border-radius:999px;
  box-shadow:0 8px 0 rgba(0,0,0,.25); transform:rotate(4deg); }
#s02 .ask { position:absolute; left:600px; top:790px; width:1220px; height:110px; display:flex; align-items:center; gap:26px; padding:0 30px;
  background:rgba(63,107,255,.18); border:3px solid var(--accent); border-radius:20px; }
#s02 .ask .t { font:800 34px Montserrat; color:var(--fg); }
#s02 .ask .t b { color:var(--gold); }
#s02 .ask .t em { font-style:normal; color:var(--teal); }
""",
    body=f'''
<div class="hdr"><div class="kicker">SORU 1 · VERİLER</div><div class="h1">Faturada iki kalem var</div></div>
<div class="who card">{icon("building", 56)}<div><b>İthalatçı (A) firması</b><span>yurt dışından ithalat</span></div></div>
<div class="what card">{icon("cd", 56)}<div><b>CD'ye kayıtlı yazılım</b><span>bilgisayarlarda kullanılacak</span></div></div>
<div class="rates"><div class="rate r-gv"><small>GÜMRÜK VERGİSİ</small><b>%10</b></div><div class="rate r-kdv"><small>KDV</small><b>%18</b></div></div>
<div class="inv">
  <div class="ih"><b>FATURA</b><span>INVOICE · USD</span></div>
  <div class="cols"><span>KALEM</span><span>TUTAR</span></div>
  <div class="row r1"><i class="mk"></i><div class="l">{icon("cd", 46)}<div>Taşıyıcı ortam (CD)<small>boş disk değeri</small></div></div><div class="v">10 $</div></div>
  <div class="row r2"><i class="mk"></i><div class="l">{icon("code", 46)}<div>Yazılım<small>veri / komut</small></div></div><div class="v">1.000 $</div></div>
  <div class="tot"><span>Fatura toplamı</span><b>1.010 $</b></div>
</div>
<div class="two">2 AYRI KALEM</div>
<div class="ask">{badge("soru")}<div class="t">İstenen: <b>Gümrük vergisi</b> + <em>KDV</em> toplamı = ? <b>USD</b></div></div>
''',
    js=r"""
rise(".hdr", K.once, 0, 30);
slideX(".who", K.ith, -60);
slideX(".what", K.cd, -60);
pulse(".what .ico", K.bilg, 1.2);
tl.fromTo(q(".inv"), { y: 120, opacity: 0, rotation: -3 }, { y: 0, opacity: 1, rotation: 0, duration: 0.75, ease: "expo.out" }, K.fat);
fadeTo(".inv .row", K.fat, 0.15, 0.01);
fadeTo(".inv .r1", K.tas, 1, 0.3);
strike(".inv .r1 .mk", K.tas + 0.1, 0.5);
pulse(".inv .r1 .v", K.on, 1.25);
fadeTo(".inv .r2", K.yaz, 1, 0.3);
strike(".inv .r2 .mk", K.yaz + 0.1, 0.5);
pulse(".inv .r2 .v", K.bin, 1.2);
pop(".two", K.bin + 0.6, 0, "back.out(3)");
fadeIn(".inv .tot", K.bin + 0.8, 0.4);
pop(".rates .r-gv", K.gv);
pop(".rates .r-kdv", K.kdv);
tl.fromTo(q(".ask"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "back.out(1.6)" }, K.biz);
"""
)

# ---------------------------------------------------------------- s03 Şıklar + geri sayım
_s03 = SCENES["s03"]
_end = round(_s03["audio_local"] + _s03["audio_dur"], 2)
OPTS = [("A", "182,98"), ("B", "181,98"), ("C", "198,98"), ("D", "299,98"), ("E", "282,80")]
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
<div class="opts">{"".join(f'<div class="opt card o{L}"><span class="L">{L}</span><span class="v">{v}</span><span class="u">USD</span></div>' for L, v in OPTS)}</div>
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

# ---------------------------------------------------------------- s04 Anahtar kural (GY md. 54)
S["s04"] = dict(
    sfx=[("impact-bass-1", T("s04", "anahtarı"), 0.35), ("ping", T("s04", "sadece"), 0.35), ("error", T("s04", "girmez"), 0.25),
         ("notification", T("s04", "ayrı"), 0.3), ("chime", T("s04", "Soruda") + 0.6, 0.3)],
    keys=dict(haz=T("s04", "Hazırsanız"), anah=T("s04", "anahtarı"), gy=T("s04", "Gümrük"), elli=T("s04", "elli"), bilg=T("s04", "Bilgisayarda"),
              sadece=T("s04", "sadece"), cd=T("s04", "CD'nin"), yaz=T("s04", "Yazılımın"), ayri=T("s04", "ayrı"), girmez=T("s04", "girmez"),
              soruda=T("s04", "Soruda")),
    css=r"""
#s04 .top { position:absolute; left:600px; top:132px; display:flex; align-items:center; gap:26px; }
#s04 .top .kicker { font-size:26px; }
#s04 .law { position:absolute; left:600px; top:250px; width:1220px; height:180px; background:#F3F6FF; color:#0B1A44; border-radius:20px; padding:24px 34px;
  box-shadow:0 30px 70px rgba(0,0,0,.45); }
#s04 .law .lh { display:flex; align-items:center; gap:16px; font:900 24px Montserrat; letter-spacing:.06em; color:#1E3FBF; }
#s04 .law .lh .no { font:700 22px 'JetBrains Mono'; color:#fff; background:#1E3FBF; padding:4px 12px; border-radius:8px; }
#s04 .law .lt { font:600 34px/1.3 Montserrat; margin-top:14px; }
#s04 .hl { position:relative; display:inline-block; }
#s04 .hl .mk { position:absolute; left:-6px; right:-6px; bottom:4px; height:20px; background:#FFC53D; opacity:.9; transform-origin:left center; border-radius:4px; z-index:0; }
#s04 .hl b { position:relative; z-index:1; font-weight:900; }
#s04 .blk { position:absolute; left:600px; width:380px; height:130px; display:flex; align-items:center; gap:22px; padding:0 26px; }
#s04 .blk .ico { color:var(--accent2); }
#s04 .blk b { display:block; font:900 30px Montserrat; }
#s04 .blk span { display:block; font:700 30px 'JetBrains Mono'; color:var(--gold); margin-top:4px; }
#s04 .b1 { top:470px; } #s04 .b2 { top:640px; }
#s04 svg.ov { position:absolute; left:0; top:0; width:1920px; height:1080px; overflow:visible; }
#s04 .res { position:absolute; left:1270px; width:550px; height:130px; display:flex; align-items:center; gap:20px; padding:0 28px; border-radius:20px; font:900 32px/1.15 Montserrat; }
#s04 .res .ico { flex:none; }
#s04 .ok { top:470px; background:rgba(46,212,122,.14); border:3px solid var(--ok); color:#DFFFEF; }
#s04 .ok .ico { color:var(--ok); }
#s04 .no { top:640px; background:rgba(255,77,94,.14); border:3px solid var(--uyari); color:#FFE3E6; }
#s04 .no .ico { color:var(--uyari); }
#s04 .cond { position:absolute; left:600px; top:800px; width:1220px; height:100px; display:flex; align-items:center; gap:24px; padding:0 26px; }
#s04 .cond .t { font:800 30px Montserrat; color:var(--fg); }
#s04 .cond .t b { color:var(--dikkat); }
#s04 .cond .yes { margin-left:auto; display:flex; align-items:center; gap:10px; font:900 26px Montserrat; color:#03221a; background:var(--ok); padding:10px 18px; border-radius:12px; }
""",
    body=f'''
<div class="top">{badge("onemli", big=True)}<div class="kicker">SORUNUN ANAHTARI</div></div>
<div class="law"><div class="lh">{icon("doc", 34)} GÜMRÜK YÖNETMELİĞİ <span class="no">MADDE 54</span> · özet</div>
  <div class="lt">Bilgisayarda kullanılacak veri / komut yüklü taşıyıcıda gümrük kıymeti:
    <span class="hl"><i class="mk"></i><b>sadece taşıyıcı ortamın kıymeti</b></span></div></div>
<div class="blk card b1">{icon("cd", 64)}<div><b>Taşıyıcı ortam (CD)</b><span>10 $</span></div></div>
<div class="blk card b2">{icon("code", 64)}<div><b>Yazılım</b><span>1.000 $</span></div></div>
<svg class="ov" viewBox="0 0 1920 1080">
  <g fill="none" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">
    <path class="a1" d="M1000 535 H1240" stroke="#2ED47A"/><path class="a1" d="M1222 517 L1246 535 L1222 553" stroke="#2ED47A"/>
    <path class="a2" d="M1000 705 H1240" stroke="#FF4D5E" stroke-dasharray="16 12"/><path class="a2" d="M1222 687 L1246 705 L1222 723" stroke="#FF4D5E"/>
  </g>
  <g class="xx"><circle cx="1120" cy="705" r="26" fill="#FF4D5E"/><path d="M1109 694 l22 22 M1131 694 l-22 22" stroke="#2a0a0e" stroke-width="6" stroke-linecap="round"/></g>
</svg>
<div class="res ok">{icon("check", 54)}<div>GÜMRÜK KIYMETİ<br/>= 10 $</div></div>
<div class="res no">{icon("x", 54)}<div>Gümrük kıymetine<br/>GİRMEZ</div></div>
<div class="cond card">{badge("dikkat")}<div class="t">Şart: yazılım bedeli CD bedelinden <b>ayrı gösterilmiş</b> olmalı</div>
  <div class="yes">{icon("check", 30)} Soruda 2 ayrı kalem</div></div>
''',
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 2.4, opacity: 0, rotation: -8 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.anah);
rise(".top .kicker", K.anah + 0.4, 0, 20);
tl.fromTo(q(".law"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, ease: "expo.out" }, K.gy);
pulse(".law .no", K.elli, 1.25);
strike(".hl .mk", K.sadece, 0.6);
slideX(".b1", K.cd - 0.4, -80);
draw(".a1", K.cd, 0.6);
pop(".res.ok", K.cd + 0.6);
slideX(".b2", K.yaz, -80);
draw(".a2", K.yaz + 0.5, 0.7);
pop(".xx", K.girmez - 0.3, 0, "back.out(3)");
pop(".res.no", K.girmez);
tl.fromTo(q(".res.no"), { x: 0 }, { x: 10, duration: 0.07, yoyo: true, repeat: 5, ease: "none" }, K.girmez + 0.5);
tl.fromTo(q(".cond"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "back.out(1.6)" }, K.ayri - 0.2);
pop(".cond .yes", K.soruda + 0.5, 0, "back.out(3)");
"""
)

# ---------------------------------------------------------------- s05 Adım 1: gümrük vergisi
S["s05"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("error", T("s05", "sadece"), 0.2), ("ping", T("s05", "bir"), 0.35), ("chime", T("s05", "vergimiz"), 0.3)],
    keys=dict(bir=T("s05", "Birinci"), mat=T("s05", "matrahı"), sadece=T("s05", "sadece"), on2=T("s05", "on", 2), yuz=T("s05", "yüzde"),
              res=T("s05", "bir"), gvz=T("s05", "vergimiz")),
    css=STEPS_CSS + LEDGER_CSS + r"""
#s05 .main { position:absolute; left:600px; top:250px; width:690px; height:560px; padding:30px 34px; }
#s05 .main .kicker { color:var(--gold); }
#s05 .base { display:flex; align-items:center; gap:24px; margin-top:20px; }
#s05 .base .v { font-family:'Archivo Black'; font-size:112px; line-height:1; color:var(--fg); }
#s05 .base .v small { font-size:48px; color:var(--muted); }
#s05 .soft { display:flex; align-items:center; gap:14px; margin-top:22px; padding:12px 18px; white-space:nowrap; border-radius:14px; background:rgba(255,77,94,.12);
  border:2px dashed rgba(255,77,94,.7); font:800 26px Montserrat; color:#FFB3BB; width:max-content; position:relative; }
#s05 .soft .st { position:absolute; left:-6px; right:-6px; top:50%; height:5px; background:var(--uyari); transform-origin:left center; border-radius:3px; }
#s05 .soft em { font-style:normal; font:700 18px 'JetBrains Mono'; color:var(--muted); }
#s05 .fx { display:flex; align-items:center; gap:22px; margin-top:44px; font-family:'Archivo Black'; font-size:84px; line-height:1; }
#s05 .fx .op { color:var(--muted); font-size:64px; }
#s05 .fx .r { color:var(--gold); text-shadow:0 0 40px rgba(255,197,61,.45); }
#s05 .fx .u { font:800 40px Montserrat; color:var(--gold); }
""",
    body=f'''
{steps(1)}
<div class="main card"><div class="kicker">ADIM 1 · GÜMRÜK VERGİSİ MATRAHI</div>
  <div class="base">{icon("cd", 110)}<div class="v">10 <small>$</small></div></div>
  <div class="soft">{icon("code", 34)}Yazılım 1.000 $ <em>GV matrahına girmez</em><i class="st"></i></div>
  <div class="fx"><span class="a">10</span><span class="op">×</span><span class="b">%10</span><span class="op">=</span><span class="r">0</span><span class="u">$</span></div>
</div>
{ledger([("Gümrük vergisi", "1,00 $", "")])}
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
pulse(".steps .stp.on .dot", K.bir, 1.25);
tl.fromTo(q(".main"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.bir);
tl.fromTo(q(".ledger"), { x: 80, opacity: 0, rotation: 2 }, { x: 0, opacity: 1, rotation: 0, duration: 0.7, ease: "expo.out" }, K.bir + 0.3);
fadeTo(".ledger .ln.new", 0.01, 0, 0.01);
pop(".base", K.mat, 0, "back.out(2)");
fadeIn(".soft", K.sadece - 0.2, 0.3);
strike(".soft .st", K.sadece + 0.3, 0.4);
fadeTo(".soft", K.sadece + 0.9, 0.45, 0.4);
rise(".fx .a, .fx .op, .fx .b", K.on2, 0.12, 30);
fadeTo(".fx .r, .fx .u", 0.01, 0, 0.01);
fadeIn(".fx .r, .fx .u", K.res - 0.4, 0.2);
count(".fx .r", K.res - 0.4, 0, 1, 0.5, 0);
pulse(".fx .r", K.res + 0.2, 1.3);
tl.fromTo(q(".ledger .ln.new"), { opacity: 1, clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 0.8, ease: "power1.inOut" }, K.gvz);
"""
)

# ---------------------------------------------------------------- s06 Adım 2: KDV matrahı
S["s06"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("notification", T("s06", "dikkat"), 0.3), ("error", T("s06", "girmedi"), 0.2), ("ping", T("s06", "ama"), 0.3),
         ("click-soft", T("s06", "CD"), 0.4), ("click-soft", T("s06", "artı"), 0.4), ("click-soft", T("s06", "artı", 2), 0.4),
         ("chime", T("s06", "Toplam"), 0.35)],
    keys=dict(ik=T("s06", "İkinci"), dik=T("s06", "dikkat"), yaz=T("s06", "Yazılım"), girmedi=T("s06", "girmedi"), ama=T("s06", "ama"),
              mat=T("s06", "KDV", 3), cd=T("s06", "on"), a1=T("s06", "artı"), a2=T("s06", "artı", 2), top=T("s06", "Toplam"), sum=T("s06", "bin", 2)),
    css=STEPS_CSS + LEDGER_CSS + r"""
#s06 .main { position:absolute; left:600px; top:250px; width:690px; height:560px; padding:28px 34px; }
#s06 .main .kicker { color:var(--teal); }
#s06 .dk { position:absolute; left:1060px; top:262px; }
#s06 .two { display:flex; gap:16px; margin-top:18px; }
#s06 .two .c { flex:1; display:flex; align-items:center; gap:12px; padding:14px 16px; border-radius:14px; font:800 25px/1.15 Montserrat; }
#s06 .two .c1 { background:rgba(255,77,94,.12); border:2px solid var(--uyari); color:#FFC9CF; }
#s06 .two .c1 .ico { color:var(--uyari); }
#s06 .two .c2 { background:rgba(46,212,122,.12); border:2px solid var(--ok); color:#CFFFE5; }
#s06 .two .c2 .ico { color:var(--ok); }
#s06 .add { margin-top:26px; font:700 44px 'JetBrains Mono'; }
#s06 .add .r { display:flex; align-items:center; height:70px; }
#s06 .add .op { width:50px; color:var(--muted); }
#s06 .add .n { width:290px; text-align:right; color:var(--fg); white-space:nowrap; }
#s06 .add .n.g { color:var(--gold); } #s06 .add .n.t { color:var(--teal); }
#s06 .add .lb { font:800 22px Montserrat; color:var(--muted); margin-left:22px; white-space:nowrap; }
#s06 .add .ln { height:5px; width:350px; background:var(--fg); border-radius:3px; margin:8px 0 8px 0; transform-origin:left center; }
#s06 .add .sum .n { color:var(--teal); font-size:50px; }
#s06 .add .sum .lb { color:var(--teal); font-size:24px; }
""",
    body=f'''
{steps(2)}
<div class="main card"><div class="kicker">ADIM 2 · KDV MATRAHI</div>
  <div class="two"><div class="c c1">{icon("x", 34)}<span>Yazılım → gümrük kıymeti</span></div><div class="c c2">{icon("check", 34)}<span>Yazılım → KDV matrahı</span></div></div>
  <div class="add">
    <div class="r r1"><span class="op"></span><span class="n">10 $</span><span class="lb">CD (taşıyıcı ortam)</span></div>
    <div class="r r2"><span class="op">+</span><span class="n g">1 $</span><span class="lb">gümrük vergisi</span></div>
    <div class="r r3"><span class="op">+</span><span class="n t">1.000 $</span><span class="lb">yazılım</span></div>
    <div class="ln"></div>
    <div class="r sum"><span class="op">=</span><span class="n"><span class="cnt">0</span> $</span><span class="lb">KDV MATRAHI</span></div>
  </div>
</div>
<div class="dk">{badge("dikkat")}</div>
{ledger([("Gümrük vergisi", "1,00 $", ""), ("KDV matrahı", "1.011,00 $", "")])}
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".main"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.ik);
tl.fromTo(q(".ledger"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.ik + 0.2);
fadeTo(".ledger .ln.new", 0.01, 0, 0.01);
slam(".dk", K.dik);
slideX(".two .c1", K.yaz, -60);
tl.fromTo(q(".two .c1"), { x: 0 }, { x: 8, duration: 0.07, yoyo: true, repeat: 5, ease: "none", immediateRender: false }, K.girmedi);
slideX(".two .c2", K.ama, 60);
pulse(".two .c2", K.ama + 0.7, 1.06);
rise(".add .r1", K.cd, 0, 30);
rise(".add .r2", K.a1, 0, 30);
rise(".add .r3", K.a2, 0, 30);
strike(".add .ln", K.top - 0.3, 0.4);
rise(".add .sum", K.top, 0, 20);
count(".add .sum .cnt", K.top + 0.1, 0, 1011, 0.9, 0);
pulse(".add .sum .n", K.sum + 0.6, 1.12);
tl.fromTo(q(".ledger .ln.new"), { opacity: 1, clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 0.8, ease: "power1.inOut" }, K.sum + 0.3);
"""
)
