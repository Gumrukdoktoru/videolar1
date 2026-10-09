"""Scenes 01-06: giriş, soru, şıklar, anahtar kural, adım 1-2."""
from lib import T, D, SCENES, icon, badge

S = {}


def steps(active):
    names = ["KIYMET & K. FONU", "ÖTV + KDV", "CEZA", "SONUÇ"]
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


def ledger(lines):
    """Notebook 'çözüm defteri': list of (label, value, cls). Rows get classes r0, r1, ... for timed writing.
    cls 'out' = kültür fonu row (struck, outside uzlaşma); 'pen' = penalty row."""
    rows = []
    for i, (lab, val, cls) in enumerate(lines):
        extra = '<i class="sk"></i><em class="tg">UZLAŞMA DIŞI</em>' if "out" in cls else ""
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

# ---------------------------------------------------------------- s01 Giriş
_kf = T("s01", "kültür")
S["s01"] = dict(
    sfx=[("pop", 0.15, 0.35), ("impact-bass-1", T("s01", "tuzak"), 0.3), ("pop", _kf, 0.25), ("pop", T("s01", "eksik"), 0.25),
         ("pop", T("s01", "ceza"), 0.25), ("pop", T("s01", "uzlaşma"), 0.25), ("ping", T("s01", "Hangi"), 0.3), ("pop", T("s01", "Kâğıt"), 0.3)],
    keys=dict(hello=T("s01", "Merhaba"), iki=T("s01", "ikincisine"), bugun=T("s01", "Bugünkü"), tuzak=T("s01", "tuzak"), kf=_kf,
              eks=T("s01", "eksik"), ceza=T("s01", "ceza"), uzl=T("s01", "uzlaşma"), hangi=T("s01", "Hangi"), girmez=T("s01", "girmez"),
              kagit=T("s01", "Kâğıt")),
    css=r"""
#s01 .sting { position:absolute; left:1060px; top:420px; width:640px; height:150px; display:flex; align-items:center; justify-content:center;
  background:#F4F7FF; border-radius:26px; box-shadow:0 30px 80px rgba(0,0,0,.45); }
#s01 .sting img { width:520px; }
#s01 .right { position:absolute; left:860px; top:150px; width:960px; }
#s01 .t1 { font-family:'Archivo Black'; font-size:80px; white-space:nowrap; line-height:1; color:var(--fg); margin-top:16px; }
#s01 .t2 { display:flex; align-items:baseline; gap:22px; margin-top:8px; white-space:nowrap; }
#s01 .t2 .w { font-family:'Archivo Black'; font-size:128px; line-height:1; color:var(--gold); text-shadow:0 10px 40px rgba(255,197,61,.35); }
#s01 .t2 .s { font:800 30px Montserrat; color:var(--muted); }
#s01 .topic { position:absolute; left:860px; top:560px; width:960px; height:300px; display:flex; align-items:center; gap:34px; padding:0 34px; }
#s01 .topic .sc { width:200px; height:200px; flex:none; }
#s01 .topic .tx small { display:block; font:700 22px 'JetBrains Mono'; color:var(--accent2); letter-spacing:.14em; }
#s01 .topic .tx > b { display:block; font:900 46px/1.1 Montserrat; color:var(--fg); margin-top:6px; white-space:nowrap; }
#s01 .topic .tx > b em { font-style:normal; color:var(--teal); }
#s01 .chips { display:flex; gap:12px; margin-top:16px; }
#s01 .chips span { font:800 22px Montserrat; padding:6px 14px; border-radius:12px; white-space:nowrap; }
#s01 .chips .c1 { background:rgba(180,140,255,.18); border:2px solid #B48CFF; color:#E2D3FF; }
#s01 .chips .c2 { background:rgba(51,217,178,.14); border:2px solid var(--teal); color:#C9FFF0; }
#s01 .chips .c3 { background:rgba(255,77,94,.14); border:2px solid var(--uyari); color:#FFC9CF; }
#s01 .chips .c4 { background:rgba(255,197,61,.16); border:2px solid var(--gold); color:var(--gold); }
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
  <div class="t2"><span class="w">DERS #2</span><span class="s">örnek soru · adım adım</span></div>
</div>
<div class="topic card">
  <svg class="sc" viewBox="0 0 200 200" aria-hidden="true">
    <g fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M100 40v128M64 176h72" stroke="#8FB2FF" stroke-width="9"/><circle cx="100" cy="36" r="10" fill="#FFC53D"/>
      <g class="beam">
        <path d="M28 52h144" stroke="#EEF2FF" stroke-width="9"/>
        <path d="M28 52l-22 56M28 52l22 56M172 52l-22 56M172 52l22 56" stroke="#AEBBE3" stroke-width="4"/>
        <path d="M2 108a26 18 0 0 0 52 0z" fill="#B48CFF" stroke="#B48CFF" stroke-width="4"/>
        <path d="M146 108a26 18 0 0 0 52 0z" fill="#33D9B2" stroke="#33D9B2" stroke-width="4"/>
      </g>
    </g>
  </svg>
  <div class="tx"><small>KONU</small><b>Kültür fonu &amp; <em>uzlaşma</em></b>
    <div class="chips"><span class="c1">Kültür fonu</span><span class="c2">Eksik vergi</span><span class="c3">Ceza</span><span class="c4">Uzlaşma</span></div>
    <div class="qq">Hangi tutar <b>uzlaşmaya girer?</b></div></div>
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
const nb = Math.max(1, Math.floor((D - K.bugun - 1.2) / 1.3) - 1);
tl.fromTo(q(".beam"), { rotation: -8 }, { rotation: 8, duration: 1.3, ease: "sine.inOut", yoyo: true, repeat: nb, svgOrigin: "100 52" }, K.bugun + 0.5);
slam(".topic .tz", K.tuzak);
pop(".chips .c1", K.kf, 0, "back.out(2.6)");
pop(".chips .c2", K.eks, 0, "back.out(2.6)");
pop(".chips .c3", K.ceza, 0, "back.out(2.6)");
pop(".chips .c4", K.uzl, 0, "back.out(2.6)");
rise(".topic .qq", K.hangi, 0, 20);
pulse(".topic .qq b", K.girmez, 1.1);
tl.fromTo(q(".ready"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "back.out(2)" }, K.kagit);
tl.fromTo(q(".ready .ico"), { rotation: 0 }, { rotation: 14, duration: 0.2, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 50%" }, K.kagit + 0.5);
"""
)

# ---------------------------------------------------------------- s02 Soru
S["s02"] = dict(
    sfx=[("whoosh-short", T("s02", "firmasının") - 0.1, 0.3), ("click-soft", T("s02", "kırk"), 0.4), ("error", T("s02", "ödenmediğini"), 0.25),
         ("pop", T("s02", "İdare"), 0.3), ("pop", T("s02", "vergileri"), 0.3), ("pop", T("s02", "gümrük", 3), 0.25), ("pop", T("s02", "ÖTV"), 0.25),
         ("pop", T("s02", "KDV"), 0.25), ("pop", T("s02", "kültür", 3), 0.25), ("pop", T("s02", "Kur"), 0.25), ("ping", T("s02", "Firma"), 0.3),
         ("notification", T("s02", "Soru"), 0.35)],
    keys=dict(once=T("s02", "Önce"), sonra=T("s02", "sonradan"), firma=T("s02", "firmasının"), kirk=T("s02", "kırk"), od=T("s02", "ödenmediğini"),
              idare=T("s02", "İdare"), kurum=T("s02", "kuruma"), gvl=T("s02", "vergileri"), ceza=T("s02", "ceza"), gv=T("s02", "gümrük", 3),
              otv=T("s02", "ÖTV"), kdv=T("s02", "KDV"), kf=T("s02", "kültür", 3), kur=T("s02", "Kur"), firma2=T("s02", "Firma"),
              soru=T("s02", "Soru")),
    css=r"""
#s02 .hdr { position:absolute; left:600px; top:132px; }
#s02 .det { position:absolute; left:600px; top:268px; width:900px; height:140px; display:flex; align-items:center; gap:22px; padding:0 26px; }
#s02 .det .ico { color:var(--accent2); }
#s02 .det > div > b { display:block; font:900 30px Montserrat; }
#s02 .det .kv { font:700 22px 'JetBrains Mono'; }
#s02 .det .sub { display:block; font:400 22px 'JetBrains Mono'; color:var(--muted); margin-top:6px; white-space:nowrap; }
#s02 .det .sub em { font-style:normal; font-weight:700; color:var(--usd); display:inline-block; }
#s02 .det .stp { margin-left:auto; padding:10px 16px; border:5px solid var(--uyari); border-radius:12px; color:#FF8A96; font:900 22px/1.15 Montserrat;
  text-align:center; transform:rotate(-4deg); background:rgba(255,77,94,.08); white-space:nowrap; }
#s02 .rt { position:absolute; top:428px; width:440px; height:150px; padding:18px 22px; }
#s02 .r1 { left:600px; border-color:#B48CFF; } #s02 .r2 { left:1060px; border-color:var(--gold); }
#s02 .rt .fr { display:flex; align-items:center; gap:14px; font:900 28px Montserrat; white-space:nowrap; }
#s02 .r1 .fr .ico { color:#B48CFF; } #s02 .r2 .fr .ico { color:var(--gold); }
#s02 .rt .to { display:flex; align-items:center; gap:12px; margin-top:16px; font:800 25px Montserrat; color:var(--fg); white-space:nowrap; }
#s02 .rt .to .ico { color:var(--muted); }
#s02 .rates { position:absolute; left:600px; top:598px; width:900px; display:flex; gap:14px; }
#s02 .rate { flex:1; height:160px; border-radius:20px; display:flex; flex-direction:column; align-items:center; justify-content:center; }
#s02 .rate small { font:900 14px Montserrat; letter-spacing:.04em; white-space:nowrap; }
#s02 .rate b { font-family:'Archivo Black'; font-size:56px; line-height:1; margin-top:8px; white-space:nowrap; }
#s02 .rate b.sm { font-size:40px; margin-top:14px; }
#s02 .g-gv { background:rgba(255,197,61,.14); border:3px solid var(--gold); color:var(--gold); }
#s02 .g-otv { background:rgba(255,159,67,.14); border:3px solid var(--dikkat); color:var(--dikkat); }
#s02 .g-kdv { background:rgba(51,217,178,.12); border:3px solid var(--teal); color:var(--teal); }
#s02 .g-kf { background:rgba(180,140,255,.14); border:3px solid #B48CFF; color:#CDB4FF; }
#s02 .g-kur { background:rgba(46,212,122,.12); border:3px solid var(--usd); color:var(--usd); }
#s02 .cano { position:absolute; left:1556px; top:300px; height:470px; filter:drop-shadow(0 18px 30px rgba(0,0,0,.45)); }
#s02 .ctag { position:absolute; left:1572px; top:720px; font:900 20px Montserrat; letter-spacing:.08em; color:#071A45; background:var(--accent2);
  padding:6px 14px; border-radius:10px; box-shadow:0 8px 20px rgba(0,0,0,.35); }
#s02 .bub { position:absolute; left:1530px; top:168px; width:290px; padding:14px 18px; background:#F4F7FF; color:#0B1A44; border-radius:20px; font:900 24px/1.25 Montserrat; }
#s02 .bub:after { content:""; position:absolute; left:120px; bottom:-22px; border:12px solid transparent; border-top:14px solid #F4F7FF; }
#s02 .bub em { font-style:normal; color:#1E3FBF; }
#s02 .ask { position:absolute; left:600px; top:790px; width:1220px; height:110px; display:flex; align-items:center; gap:26px; padding:0 30px;
  background:rgba(63,107,255,.18); border:3px solid var(--accent); border-radius:20px; }
#s02 .ask .t { font:800 34px Montserrat; color:var(--fg); }
#s02 .ask .t b { color:var(--gold); display:inline-block; }
#s02 .ask .t em { font-style:normal; color:var(--teal); }
""",
    body=f'''
<div class="hdr"><div class="kicker">ÖRNEK SORU · VERİLER</div><div class="h1">Kültür fonu ödenmemiş</div></div>
<div class="det card">{icon("search", 60)}<div><b>K firması · ithalat</b><span class="sub">kıymet: <em><b class="kv">40.000</b> $</em> · sonradan kontrol</span></div>
  <div class="stp">KÜLTÜR FONU<br/>ÖDENMEMİŞ</div></div>
<div class="rt r1 card"><div class="fr">{icon("mask", 42)}Kültür fonu</div><div class="to">{icon("arrow", 30)}{icon("mail", 30)}İlgili kuruma bildirim</div></div>
<div class="rt r2 card"><div class="fr">{icon("building", 42)}Gümrük vergileri</div><div class="to">{icon("arrow", 30)}{icon("gavel", 30)}Ek tahakkuk + ceza</div></div>
<div class="rates">
  <div class="rate g-gv"><small>GÜMRÜK VERGİSİ</small><b>%0</b></div>
  <div class="rate g-otv"><small>ÖTV</small><b>%10</b></div>
  <div class="rate g-kdv"><small>KDV</small><b>%20</b></div>
  <div class="rate g-kf"><small>KÜLTÜR FONU</small><b>%3</b></div>
  <div class="rate g-kur"><small>KUR · 1 $</small><b class="sm">30 TL</b></div>
</div>
<img class="cano" src="assets/img/cano-cut.png" alt="K firması temsilcisi" />
<div class="ctag">K FİRMASI</div>
<div class="bub">Uzlaşabileceğimiz <em>her tutar</em> için başvuruyoruz!</div>
<div class="ask">{badge("soru")}<div class="t">İstenen: <b>uzlaşmaya konu</b> tutar = ? <em>TL</em></div></div>
''',
    js=r"""
rise(".hdr", K.once, 0, 30);
slideX(".det", K.sonra, -60);
tl.fromTo(q(".cano"), { x: 300, opacity: 0 }, { x: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }, K.firma);
rise(".ctag", K.firma + 0.5, 0, 20);
count(".det .kv", K.kirk, 0, 40000, 0.8, 0);
pulse(".det em", K.kirk + 0.9, 1.15);
slam(".det .stp", K.od);
slideX(".rt.r1", K.idare, -60);
fadeTo(".rt .to", 0.01, 0, 0.01);
rise(".r1 .to", K.kurum, 0, 16);
slideX(".rt.r2", K.gvl, 60);
rise(".r2 .to", K.ceza, 0, 16);
pop(".rates .g-gv", K.gv);
pop(".rates .g-otv", K.otv);
pop(".rates .g-kdv", K.kdv);
pop(".rates .g-kf", K.kf);
pop(".rates .g-kur", K.kur);
tl.fromTo(q(".bub"), { scale: 0.3, opacity: 0, transformOrigin: "40% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.firma2);
tl.fromTo(q(".ask"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "back.out(1.6)" }, K.soru);
pulse(".ask .t b", K.soru + 1.0, 1.1);
"""
)

# ---------------------------------------------------------------- s03 Şıklar + geri sayım
_s03 = SCENES["s03"]
_end = round(_s03["audio_local"] + _s03["audio_dur"], 2)
OPTS = [("A", "11.520"), ("B", "36.000"), ("C", "43.200"), ("D", "46.080"), ("E", "82.080")]
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

# ---------------------------------------------------------------- s04 Anahtar kural: kültür fonunun iki özelliği
_dst_y = [262, 400, 538, 676]
_paths = []
for i, y in enumerate(_dst_y, 1):
    cy = y + 59
    col = "#2ED47A" if i == 2 else "#FF4D5E"
    _paths.append(f'<path class="p{i}" d="M934 540 C1086 540 1080 {cy} 1226 {cy}" stroke="{col}"/>'
                  f'<path class="p{i}" d="M1206 {cy - 16} L1230 {cy} L1206 {cy + 16}" stroke="{col}"/>')
S["s04"] = dict(
    sfx=[("impact-bass-1", T("s04", "anahtarı"), 0.35), ("whoosh-short", T("s04", "iki") - 0.2, 0.3), ("error", T("s04", "girmez"), 0.25),
         ("ping", T("s04", "girer"), 0.35), ("error", T("s04", "edilemez"), 0.25), ("error", T("s04", "uygulanmaz"), 0.25)],
    keys=dict(anah=T("s04", "anahtarı"), iki=T("s04", "iki"), bir=T("s04", "Bir"), kiy=T("s04", "kıymetine"), girmez=T("s04", "girmez"),
              otv=T("s04", "ÖTV"), girer=T("s04", "girer"), iki2=T("s04", "İki", 2), asli=T("s04", "aslı"), uzl=T("s04", "uzlaşmaya"),
              edil=T("s04", "edilemez"), uc=T("s04", "üç"), uyg=T("s04", "uygulanmaz")),
    css=r"""
#s04 .top { position:absolute; left:600px; top:132px; display:flex; align-items:center; gap:26px; }
#s04 .top .kicker { font-size:26px; }
#s04 .tok { position:absolute; left:630px; top:390px; width:300px; height:300px; }
#s04 .tok .ring { position:absolute; inset:0; border-radius:50%; border:8px dashed #B48CFF; }
#s04 .tok .in { position:absolute; inset:26px; border-radius:50%; background:radial-gradient(circle at 35% 30%, #5B3FA8, #2A1A5E); display:flex; flex-direction:column;
  align-items:center; justify-content:center; box-shadow:0 20px 50px rgba(0,0,0,.45), inset 0 0 0 4px rgba(205,180,255,.6); color:#E2D3FF; }
#s04 .tok .in b { font:900 30px/1.05 Montserrat; text-align:center; color:#fff; margin-top:6px; letter-spacing:.04em; }
#s04 .tok .in span { font-family:'Archivo Black'; font-size:40px; color:#CDB4FF; line-height:1; margin-top:6px; }
#s04 .tag { position:absolute; left:600px; display:flex; align-items:center; gap:14px; font:800 25px Montserrat; color:var(--fg); white-space:nowrap; }
#s04 .tag b { width:44px; height:44px; border-radius:50%; background:#B48CFF; color:#1A0E3A; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:24px; }
#s04 .tg1 { top:722px; } #s04 .tg2 { top:790px; }
#s04 svg.ov { position:absolute; left:0; top:0; width:1920px; height:1080px; overflow:visible; }
#s04 .dst { position:absolute; left:1240px; width:580px; height:118px; display:flex; align-items:center; gap:18px; padding:0 22px; border-radius:18px; }
#s04 .dst .n { width:40px; height:40px; border-radius:50%; background:#B48CFF; color:#1A0E3A; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:22px; flex:none; }
#s04 .dst .ico { flex:none; }
#s04 .dst b { display:block; font:900 30px Montserrat; white-space:nowrap; }
#s04 .dst small { display:block; font:700 22px 'JetBrains Mono'; margin-top:2px; letter-spacing:.06em; }
#s04 .dst.no { background:rgba(255,77,94,.13); border:3px solid var(--uyari); color:#FFE3E6; }
#s04 .dst.no .ico, #s04 .dst.no small { color:#FF8A96; }
#s04 .dst.ok { background:rgba(46,212,122,.14); border:3px solid var(--ok); color:#DFFFEF; }
#s04 .dst.ok .ico, #s04 .dst.ok small { color:var(--ok); }
#s04 .d1 { top:262px; } #s04 .d2 { top:400px; } #s04 .d3 { top:538px; } #s04 .d4 { top:676px; }
""",
    body=f'''
<div class="top">{badge("onemli", big=True)}<div class="kicker">SORUNUN ANAHTARI · KÜLTÜR FONU</div></div>
<svg class="ov" viewBox="0 0 1920 1080"><g fill="none" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">{"".join(_paths)}</g></svg>
<div class="tok"><div class="ring"></div><div class="in">{icon("mask", 74)}<b>KÜLTÜR<br/>FONU</b><span>%3</span></div></div>
<div class="tag tg1"><b>1</b>Yurt içinde doğan bir yük</div>
<div class="tag tg2"><b>2</b>Aslı gümrükçe tahsil edilmez</div>
<div class="dst d1 no"><span class="n">1</span>{icon("x", 44)}<div><b>Gümrük kıymeti</b><small>GİRMEZ</small></div></div>
<div class="dst d2 ok"><span class="n">1</span>{icon("check", 44)}<div><b>ÖTV + KDV matrahı</b><small>GİRER</small></div></div>
<div class="dst d3 no"><span class="n">2</span>{icon("x", 44)}<div><b>Uzlaşma</b><small>KONU EDİLEMEZ</small></div></div>
<div class="dst d4 no"><span class="n">2</span>{icon("x", 44)}<div><b>3 kat ceza</b><small>UYGULANMAZ</small></div></div>
''',
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 2.4, opacity: 0, rotation: -8 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.anah);
rise(".top .kicker", K.anah + 0.4, 0, 20);
tl.fromTo(q(".tok"), { scale: 0.3, opacity: 0, rotation: -90 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.8, ease: "back.out(1.6)" }, K.iki - 0.2);
tl.fromTo(q(".tok .ring"), { rotation: 0 }, { rotation: 240, duration: D - K.iki, ease: "none" }, K.iki);
rise(".tag.tg1", K.bir, 0, 20);
draw(".p1", K.kiy - 0.5, 0.6);
pop(".d1", K.girmez - 0.3);
tl.fromTo(q(".d1"), { x: 0 }, { x: 10, duration: 0.07, yoyo: true, repeat: 5, ease: "none", immediateRender: false }, K.girmez + 0.3);
draw(".p2", K.otv - 0.2, 0.6);
pop(".d2", K.girer - 0.3);
pulse(".d2", K.girer + 0.3, 1.06);
rise(".tag.tg2", K.iki2, 0, 20);
draw(".p3", K.uzl - 0.5, 0.6);
pop(".d3", K.edil - 0.3);
draw(".p4", K.uc - 0.5, 0.6);
pop(".d4", K.uyg - 0.3);
pulse(".tok .in", K.uyg + 0.5, 1.06);
"""
)

# ---------------------------------------------------------------- s05 Adım 1: TL kıymet + kültür fonu
S["s05"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("click-soft", T("s05", "çarpı"), 0.4), ("ping", T("s05", "milyon") + 0.6, 0.3), ("pop", T("s05", "yok"), 0.3),
         ("ping", T("s05", "otuz", 2) + 0.4, 0.35), ("error", T("s05", "girmez"), 0.25)],
    keys=dict(bir=T("s05", "Birinci"), kirk=T("s05", "Kırk"), mil=T("s05", "milyon"), gv=T("s05", "Gümrük"), yok=T("s05", "yok"),
              eks=T("s05", "Eksik"), mil2=T("s05", "milyon", 2), otuz2=T("s05", "otuz", 2), bu=T("s05", "Bu"), uzl=T("s05", "uzlaşmaya"),
              girmez=T("s05", "girmez")),
    css=STEPS_CSS + LEDGER_CSS + r"""
#s05 .main { position:absolute; left:600px; top:250px; width:690px; height:560px; padding:26px 32px; }
#s05 .main .kicker { color:var(--gold); }
#s05 .conv .eq { display:flex; align-items:center; gap:14px; margin-top:16px; font:700 40px 'JetBrains Mono'; color:var(--fg); white-space:nowrap; }
#s05 .conv .eq .u { color:var(--usd); }
#s05 .conv .eq .op { color:var(--muted); }
#s05 .conv .res { display:flex; align-items:baseline; gap:12px; margin-top:6px; white-space:nowrap; }
#s05 .conv .res .op { font:700 44px 'JetBrains Mono'; color:var(--muted); }
#s05 .conv .res b { font-family:'Archivo Black'; font-size:72px; line-height:1; color:var(--fg); }
#s05 .conv .res small { font:800 32px Montserrat; color:var(--muted); }
#s05 .gv0 { position:relative; display:flex; align-items:center; gap:12px; margin-top:16px; padding:10px 16px; border-radius:14px; width:max-content;
  background:rgba(255,197,61,.10); border:2px dashed rgba(255,197,61,.6); font:800 24px Montserrat; color:var(--gold); white-space:nowrap; }
#s05 .gv0 .z { font:700 26px 'JetBrains Mono'; color:#2a1d00; background:var(--gold); border-radius:8px; padding:2px 10px; }
#s05 .kf { margin-top:18px; padding:16px 20px; border-radius:18px; background:rgba(180,140,255,.12); border:3px solid #B48CFF; }
#s05 .kf .lb { display:flex; align-items:center; gap:12px; font:900 22px Montserrat; letter-spacing:.08em; color:#CDB4FF; }
#s05 .kf .row { display:flex; align-items:baseline; gap:14px; margin-top:6px; white-space:nowrap; }
#s05 .kf .eq2 { font:700 30px 'JetBrains Mono'; color:var(--fg); }
#s05 .kf .r { font-family:'Archivo Black'; font-size:50px; line-height:1; color:#E2D3FF; text-shadow:0 0 36px rgba(180,140,255,.5); display:inline-block; }
#s05 .kf .r small { font:800 24px Montserrat; color:#CDB4FF; }
#s05 .dest { display:flex; align-items:center; gap:14px; margin-top:16px; font:800 25px Montserrat; color:var(--fg); white-space:nowrap; }
#s05 .dest .ico { color:#B48CFF; }
#s05 .dest .stamp { margin-left:auto; padding:6px 12px; border:4px solid var(--uyari); border-radius:10px; color:#FF8A96; font:900 22px Montserrat; transform:rotate(-5deg); }
""",
    body=f'''
{steps(1)}
<div class="main card"><div class="kicker">ADIM 1 · KIYMET &amp; KÜLTÜR FONU</div>
  <div class="conv"><div class="eq"><span>40.000</span><span class="u">$</span><span class="op">×</span><span>30</span></div>
    <div class="res"><span class="op">=</span><b class="cnt">0</b><small>TL</small></div></div>
  <div class="gv0">{icon("building", 30)}Gümrük vergisi %0 → ek GV <span class="z">0 TL</span></div>
  <div class="kf"><div class="lb">{icon("mask", 30)}EKSİK KÜLTÜR FONU</div>
    <div class="row"><span class="eq2">1.200.000 × %3 =</span><span class="r"><span class="cnt2">0</span> <small>TL</small></span></div></div>
  <div class="dest">{icon("mail", 34)}İlgili kuruma bildirilir<span class="stamp">UZLAŞMA DIŞI</span></div>
</div>
{ledger([("Kültür fonu", "36.000", "out")])}
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
pulse(".steps .stp.on .dot", K.bir, 1.25);
tl.fromTo(q(".main"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.bir);
tl.fromTo(q(".ledger"), { x: 80, opacity: 0, rotation: 2 }, { x: 0, opacity: 1, rotation: 0, duration: 0.7, ease: "expo.out" }, K.bir + 0.3);
rise(".conv .eq > *", K.kirk, 0.12, 30);
fadeTo(".conv .res", 0.01, 0, 0.01);
fadeIn(".conv .res", K.mil - 0.4, 0.2);
count(".conv .res .cnt", K.mil - 0.4, 0, 1200000, 1.0, 0);
pulse(".conv .res b", K.mil + 0.8, 1.08);
slideX(".gv0", K.gv, -40);
pop(".gv0 .z", K.yok - 0.2, 0, "back.out(3)");
rise(".kf", K.eks, 0, 30);
fadeTo(".kf .row", 0.01, 0, 0.01);
fadeIn(".kf .row", K.mil2 - 0.2, 0.3);
count(".kf .cnt2", K.otuz2 - 0.3, 0, 36000, 0.8, 0);
pulse(".kf .r", K.otuz2 + 0.7, 1.15);
write(".ledger .r0", K.otuz2 + 0.5, 0.8);
fadeTo(".ledger .r0 .tg", 0.01, 0, 0.01);
slideX(".dest", K.bu, -40);
fadeTo(".dest .stamp", 0.01, 0, 0.01);
slam(".dest .stamp", K.girmez - 0.2);
strike(".ledger .r0 .sk", K.girmez, 0.4);
pop(".ledger .r0 .tg", K.girmez + 0.2, 0, "back.out(3)");
"""
)

# ---------------------------------------------------------------- s06 Adım 2: eksik ÖTV + KDV
S["s06"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("notification", T("s06", "dikkat"), 0.3), ("click-soft", T("s06", "üç") - 0.1, 0.4),
         ("click-soft", T("s06", "dokuz") - 0.2, 0.4), ("click-soft", T("s06", "yedi"), 0.4), ("chime", T("s06", "on") + 0.4, 0.35)],
    keys=dict(ik=T("s06", "İkinci"), dik=T("s06", "dikkat"), kf=T("s06", "Kültür"), ode=T("s06", "ödenmemesi"), eotv=T("s06", "eksik", 3),
              uc=T("s06", "üç"), ekdv=T("s06", "eksik", 4), art=T("s06", "artı"), dokuz=T("s06", "dokuz"), bunun=T("s06", "Bunun"),
              yedi=T("s06", "yedi"), top=T("s06", "Toplam"), on=T("s06", "on")),
    css=STEPS_CSS + LEDGER_CSS + r"""
#s06 .main { position:absolute; left:600px; top:250px; width:690px; height:560px; padding:26px 32px; }
#s06 .main .kicker { color:var(--teal); }
#s06 .dk { position:absolute; left:1080px; top:226px; }
#s06 .info { display:flex; align-items:center; gap:12px; margin-top:14px; padding:10px 16px; border-radius:14px; width:max-content;
  background:rgba(46,212,122,.12); border:2px solid var(--ok); font:800 24px Montserrat; color:#CFFFE5; white-space:nowrap; }
#s06 .info .ico { color:var(--ok); }
#s06 .rw { margin-top:16px; }
#s06 .rw small { display:block; font:800 20px Montserrat; letter-spacing:.06em; color:var(--muted); }
#s06 .rw .e { display:flex; align-items:baseline; gap:14px; font:700 38px 'JetBrains Mono'; color:var(--fg); white-space:nowrap; margin-top:2px; }
#s06 .rw .e .op { color:var(--muted); }
#s06 .rw .e .v { display:inline-block; }
#s06 .rw1 .e .v { color:var(--dikkat); } #s06 .rw2 .e .v { color:var(--accent2); } #s06 .rw3 .e .v { color:var(--teal); }
#s06 .ln2 { height:5px; width:626px; background:var(--fg); border-radius:3px; margin:16px 0 10px; transform-origin:left center; }
#s06 .sum { display:flex; align-items:baseline; gap:16px; white-space:nowrap; }
#s06 .sum small { font:900 24px Montserrat; letter-spacing:.06em; color:var(--teal); }
#s06 .sum b { font-family:'Archivo Black'; font-size:60px; line-height:1; color:#DFFFF6; display:inline-block; }
#s06 .sum em { font-style:normal; font:800 28px Montserrat; color:var(--teal); }
""",
    body=f'''
{steps(2)}
<div class="main card"><div class="kicker">ADIM 2 · EKSİK ÖTV + KDV</div>
  <div class="info">{icon("check", 30)}Kültür fonu → ÖTV &amp; KDV matrahına girer</div>
  <div class="rw rw1"><small>EKSİK ÖTV</small><div class="e"><span>36.000 × %10</span><span class="op">=</span><span class="v c1">0</span></div></div>
  <div class="rw rw2"><small>EKSİK KDV MATRAHI</small><div class="e"><span>36.000 + 3.600</span><span class="op">=</span><span class="v c2">0</span></div></div>
  <div class="rw rw3"><small>EKSİK KDV</small><div class="e"><span>39.600 × %20</span><span class="op">=</span><span class="v c3">0</span></div></div>
  <div class="ln2"></div>
  <div class="sum"><small>EKSİK VERGİ</small><b class="c4">0</b><em>TL</em></div>
</div>
<div class="dk">{badge("dikkat")}</div>
{ledger([("Kültür fonu", "36.000", "out"), ("Eksik ÖTV", "3.600", ""), ("Eksik KDV", "7.920", "")])}
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".main"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.ik);
tl.fromTo(q(".ledger"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.ik + 0.2);
slam(".dk", K.dik);
slideX(".info", K.kf, -40);
pulse(".info", K.ode + 0.3, 1.05);
rise(".rw1", K.eotv, 0, 24);
count(".rw1 .c1", K.uc - 0.2, 0, 3600, 0.6, 0);
pulse(".rw1 .v", K.uc + 0.5, 1.2);
write(".ledger .r1", K.uc + 0.6, 0.7);
rise(".rw2", K.ekdv, 0, 24);
count(".rw2 .c2", K.dokuz - 0.4, 0, 39600, 0.8, 0);
pulse(".rw2 .v", K.dokuz + 0.5, 1.15);
rise(".rw3", K.bunun, 0, 24);
count(".rw3 .c3", K.yedi - 0.2, 0, 7920, 0.7, 0);
pulse(".rw3 .v", K.yedi + 0.6, 1.2);
write(".ledger .r2", K.yedi + 0.7, 0.7);
strike(".ln2", K.top - 0.3, 0.4);
rise(".sum", K.top, 0, 20);
count(".sum .c4", K.on - 0.1, 0, 11520, 0.8, 0);
pulse(".sum b", K.on + 0.9, 1.12);
"""
)
