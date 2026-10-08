"""Scenes 01-05."""
from lib import T, D, icon, badge, odu, idu, valve

S = {}

# ---------------------------------------------------------------- s01 Giriş
S["s01"] = dict(
    sfx=[("pop", 0.15, 0.35), ("impact-bass-1", T("s01", "dört") + 0.4, 0.4)],
    keys=dict(
        hello=T("s01", "Merhaba"), soru=T("s01", "Bugün"), ms=T("s01", "multi"), vrf=T("s01", "VRF"),
        ggm=T("s01", "Gümrükler"), date=T("s01", "Ekim", off=-0.25), dort=T("s01", "dört"), hadi=T("s01", "Hadi"),
    ),
    css=r"""
#s01 .right { position:absolute; left:860px; top:160px; width:960px; }
#s01 .sting { position:absolute; left:1060px; top:420px; width:640px; height:150px; display:flex; align-items:center; justify-content:center;
  background:#F4F7FF; border-radius:26px; box-shadow:0 30px 80px rgba(0,0,0,.45); }
#s01 .sting img { width:520px; }
#s01 .phaseA { position:absolute; left:0; top:0; width:960px; }
#s01 .t1 { font-family:'Archivo Black'; font-size:128px; line-height:1; color:var(--fg); letter-spacing:-0.01em; margin-top:18px; }
#s01 .t1 em { font-style:normal; color:var(--vrf); }
#s01 .sub { font:400 36px/1.3 Montserrat; color:var(--muted); margin-top:22px; max-width:900px; }
#s01 .phaseB { position:absolute; left:0; top:0; width:960px; }
#s01 .qline { font:700 34px Montserrat; color:var(--muted); margin-bottom:6px; }
#s01 .vs { display:flex; align-items:baseline; gap:22px; }
#s01 .vs .w { font-family:'Archivo Black'; font-size:112px; line-height:1.05; }
#s01 .vs .ms { color:var(--ms); }
#s01 .vs .vr { color:var(--vrf); }
#s01 .vs .mi { font:900 64px Montserrat; color:var(--fg); }
#s01 .doc { position:absolute; left:860px; top:560px; width:950px; height:300px; background:#F3F6FF; color:#0B1A44; border-radius:20px;
  padding:30px 38px; box-shadow:0 30px 70px rgba(0,0,0,.45); }
#s01 .doc .hd { display:flex; align-items:center; gap:18px; border-bottom:3px solid #C9D4F2; padding-bottom:14px; }
#s01 .doc .hd .ico { color:#1E3FBF; }
#s01 .doc .org { font:900 26px Montserrat; letter-spacing:.04em; }
#s01 .doc .org2 { font:700 22px Montserrat; color:#3B4E86; }
#s01 .doc .row { display:flex; gap:20px; margin-top:16px; font:400 26px Montserrat; align-items:baseline; }
#s01 .doc .row b { font:700 20px 'JetBrains Mono'; color:#5A6AA0; width:92px; letter-spacing:.08em; }
#s01 .doc .mono { font-family:'JetBrains Mono'; font-size:24px; }
#s01 .hl { position:relative; display:inline-block; }
#s01 .hl .mk { position:absolute; left:-6px; right:-6px; bottom:2px; height:16px; background:#FFC53D; opacity:.85; transform-origin:left center; z-index:0; border-radius:4px; }
#s01 .hl span { position:relative; z-index:1; font-weight:700; }
#s01 .stamp { position:absolute; left:1470px; top:748px; width:360px; padding:14px 18px; border:6px solid var(--uyari); color:var(--uyari); border-radius:14px;
  font-family:'Archivo Black'; font-size:40px; line-height:1.05; text-align:center; transform:rotate(-9deg); background:rgba(243,246,255,.9); }
#s01 .go { position:absolute; left:1480px; top:430px; display:flex; align-items:center; gap:14px; font:900 30px Montserrat; color:var(--bg);
  background:var(--vrf); padding:14px 28px; border-radius:999px; }
""",
    body=r"""
<div class="sting"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div>
<div class="right">
  <div class="phaseA">
    <div class="kicker k1">GÜMRÜK KOÇU · DERS NOTU</div>
    <div class="t1">VRF <em>KLİMALAR</em></div>
    <div class="sub">Multi-split ile VRF ayrımında yeni teknik kriterler</div>
  </div>
  <div class="phaseB">
    <div class="qline">Bu klima…</div>
    <div class="vs v1"><span class="w ms">MULTI-SPLIT</span><span class="mi">mi?</span></div>
    <div class="vs v2"><span class="w vr">VRF</span><span class="mi">mi?</span></div>
  </div>
</div>
<div class="doc">
  <div class="hd">ICON_BUILDING<div><div class="org">T.C. TİCARET BAKANLIĞI</div><div class="org2">Gümrükler Genel Müdürlüğü</div></div></div>
  <div class="row r1"><b>TARİH</b><span class="hl"><i class="mk"></i><span>01.10.2026</span></span></div>
  <div class="row r2"><b>SAYI</b><span class="mono">E-17474625-162.01-00126963399</span></div>
  <div class="row r3"><b>KONU</b><span><strong>VRF Klimalar</strong></span></div>
</div>
<div class="stamp">4 NET TEKNİK KRİTER</div>
<div class="go">Adım adım inceleyelim ICON_ARROW</div>
""".replace("ICON_BUILDING", icon("building", 52)).replace("ICON_ARROW", icon("arrow", 34)),
    js=r"""
tl.fromTo(q(".sting"), { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.6, ease: "back.out(1.8)" }, 0.15);
tl.to(q(".sting"), { scale: 0.85, opacity: 0, y: -40, duration: 0.45, ease: "power2.in" }, K.hello - 0.35);
rise(".phaseA .k1", K.hello, 0, 20);
tl.fromTo(q(".t1"), { y: 70, opacity: 0, skewY: 4 }, { y: 0, opacity: 1, skewY: 0, duration: 0.7, ease: "expo.out" }, K.hello + 0.15);
rise(".sub", K.hello + 0.6);
tl.to(q(".phaseA"), { opacity: 0, y: -50, duration: 0.45, ease: "power2.in" }, K.ms - 0.75);
rise(".qline", K.ms - 0.45, 0, 20);
slideX(".v1", K.ms, -80);
slideX(".v2", K.vrf, 80);
tl.fromTo(q(".v2 .vr"), { scale: 1 }, { scale: 1.12, duration: 0.18, yoyo: true, repeat: 1, ease: "power2.out", transformOrigin: "left center" }, K.vrf + 0.45);
tl.fromTo(q(".doc"), { y: 260, opacity: 0, rotation: 3 }, { y: 0, opacity: 1, rotation: 0, duration: 0.8, ease: "expo.out" }, K.ggm);
rise(".doc .row", K.ggm + 0.35, 0.12, 20);
strike(".hl .mk", K.date, 0.5);
slam(".stamp", K.dort);
tl.fromTo(q(".go"), { x: -40, opacity: 0 }, { x: 0, opacity: 1, duration: 0.5, ease: "back.out(2)" }, K.hadi);
tl.fromTo(q(".go .ico"), { x: 0 }, { x: 12, duration: 0.35, yoyo: true, repeat: 3, ease: "sine.inOut" }, K.hadi + 0.5);
"""
)

# ---------------------------------------------------------------- s02 Sorun
S["s02"] = dict(
    sfx=[("pop", T("s02", "Sonuç"), 0.35), ("pop", T("s02", "Hangi"), 0.3)],
    keys=dict(
        once=T("s02", "Önce"), bolge=T("s02", "Bölge"), farkli=T("s02", "Farklı"), rapor=T("s02", "raporlar"),
        sonuc=T("s02", "Sonuç"), hangi=T("s02", "Hangi"), uyg=T("s02", "uygulama"), tarife=T("s02", "tarife"),
    ),
    css=r"""
#s02 .hdr { position:absolute; left:600px; top:132px; }
#s02 .mail { position:absolute; left:600px; top:292px; }
#s02 .rep { position:absolute; left:600px; width:400px; height:122px; display:flex; align-items:center; gap:20px; padding:0 24px; }
#s02 .rep .ico { color:var(--accent2); flex:none; }
#s02 .rep .n { font:900 30px Montserrat; color:var(--fg); }
#s02 .rep .c { font:400 24px 'JetBrains Mono'; color:var(--muted); margin-top:4px; }
#s02 .rep .c b { color:var(--onemli); font-weight:700; }
#s02 .r1 { top:384px; } #s02 .r2 { top:532px; } #s02 .r3 { top:680px; }
#s02 svg.ov { position:absolute; left:0; top:0; width:1920px; height:1080px; overflow:visible; }
#s02 .qn { position:absolute; left:1150px; top:536px; width:180px; height:180px; border-radius:50%; background:var(--panel); border:5px solid var(--dikkat);
  display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:118px; color:var(--dikkat); box-shadow:0 0 60px rgba(255,159,67,.35); }
#s02 .bd { position:absolute; left:1400px; top:330px; }
#s02 .out { position:absolute; left:1400px; width:420px; padding:22px 26px; font:700 32px/1.2 Montserrat; color:var(--fg); }
#s02 .o1 { top:420px; } #s02 .o2 { top:640px; }
#s02 .out small { display:block; font:400 22px 'JetBrains Mono'; color:var(--dikkat); letter-spacing:.1em; margin-bottom:8px; }
""",
    body=r"""
<div class="hdr"><div class="kicker">BÖLÜM 2 · SORUN</div><div class="h1">Aynı eşya, farklı raporlar</div></div>
<div class="mail chip">ICON_MAIL Bölge Müdürlüklerinden gelen yazılar</div>
<div class="rep card r1">ICON_UNI<div><div class="n">Üniversite A</div><div class="c">Teknik rapor · <b>Kriter X</b></div></div></div>
<div class="rep card r2">ICON_UNI<div><div class="n">Üniversite B</div><div class="c">Teknik rapor · <b>Kriter Y</b></div></div></div>
<div class="rep card r3">ICON_UNI<div><div class="n">Üniversite C</div><div class="c">Teknik rapor · <b>Kriter Z</b></div></div></div>
<svg class="ov" viewBox="0 0 1920 1080">
  <g class="arr in" fill="none" stroke="#8FB2FF" stroke-width="5" stroke-linecap="round">
    <path d="M1010 445 C 1080 445, 1090 600, 1146 620"/>
    <path d="M1010 593 C 1070 593, 1090 618, 1146 624"/>
    <path d="M1010 741 C 1080 741, 1090 650, 1146 632"/>
  </g>
  <g class="arr out" fill="none" stroke="#FF9F43" stroke-width="5" stroke-linecap="round">
    <path d="M1334 600 C 1360 560, 1370 500, 1396 488"/>
    <path d="M1334 650 C 1360 690, 1370 700, 1396 706"/>
  </g>
  <g class="heads" fill="#FF9F43"><path class="h1a" d="M1400 488 l-18 -10 l2 22z"/><path class="h2a" d="M1400 706 l-20 -6 l8 20z"/></g>
</svg>
<div class="qn">?</div>
<div class="bd">BADGE</div>
<div class="out card o1"><small>SONUÇ 1</small>Uygulama farklılıkları</div>
<div class="out card o2"><small>SONUÇ 2</small>Tarife pozisyonunda tereddüt</div>
""".replace("ICON_MAIL", icon("mail", 34)).replace("ICON_UNI", icon("uni", 58)).replace("BADGE", badge("dikkat")),
    js=r"""
rise(".hdr .kicker", K.once - 0.3, 0, 20);
tl.fromTo(q(".hdr .h1"), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.once);
slideX(".mail", K.bolge, -60);
slideX(".rep", K.farkli, -80, 0.22);
tl.fromTo(q(".rep .c b"), { color: "#A9B6DE" }, { color: "#FFC53D", duration: 0.3, stagger: 0.25 }, K.farkli + 1.6);
draw(".arr.in path", K.rapor, 0.8);
pop(".qn", K.sonuc);
tl.fromTo(q(".qn"), { rotation: 0 }, { rotation: 10, duration: 0.14, yoyo: true, repeat: 5, ease: "sine.inOut" }, K.sonuc + 0.5);
breathe(".qn", K.sonuc + 1.4, D - 0.5, 0.05, 1.6);
pop(".bd .badge", K.hangi);
draw(".arr.out path", K.uyg - 0.4, 0.5);
pop(".heads .h1a", K.uyg);
slideX(".o1", K.uyg, 60);
pop(".heads .h2a", K.tarife);
slideX(".o2", K.tarife, 60);
""",
)

# ---------------------------------------------------------------- s03 Süreç
S["s03"] = dict(
    keys=dict(
        bunun=T("s03", "Bunun"), ggm=T("s03", "Gümrükler"), konuyu=T("s03", "konuyu"), igm=T("s03", "İthalat"),
        igm2=T("s03", "İthalat", 2), teknik=T("s03", "teknik"), payl=T("s03", "paylaştı"), bu=T("s03", "Bu"),
        mevcut=T("s03", "mevcut"), birlikte=T("s03", "birlikte"),
    ),
    css=r"""
#s03 .hdr { position:absolute; left:600px; top:132px; }
#s03 .node { position:absolute; top:330px; width:440px; height:150px; display:flex; align-items:center; gap:22px; padding:0 28px; }
#s03 .node .ico { color:var(--accent2); flex:none; }
#s03 .node .n { font:900 32px/1.15 Montserrat; color:var(--fg); }
#s03 .node .r { font:400 22px 'JetBrains Mono'; color:var(--muted); margin-top:6px; letter-spacing:.06em; }
#s03 .na { left:600px; } #s03 .nb { left:1380px; }
#s03 svg.ov { position:absolute; left:0; top:0; width:1920px; height:1080px; }
#s03 .lab { position:absolute; font:700 26px Montserrat; color:var(--fg); background:var(--bg); padding:6px 16px; border-radius:10px; }
#s03 .l1 { left:1100px; top:358px; }
#s03 .info { position:absolute; left:960px; top:560px; width:560px; display:flex; align-items:center; gap:18px; padding:18px 22px; }
#s03 .info svg.mini { flex:none; }
#s03 .info .t { font:700 28px/1.2 Montserrat; color:var(--fg); }
#s03 .docs { position:absolute; left:600px; top:760px; width:420px; display:flex; align-items:center; gap:18px; padding:20px 24px; }
#s03 .docs .ico { color:var(--onemli); }
#s03 .docs .t { font:700 28px Montserrat; color:var(--fg); }
#s03 .eval { position:absolute; left:1240px; top:750px; width:580px; display:flex; align-items:center; gap:22px; padding:22px 28px; border-color:var(--vrf) !important; }
#s03 .eval .ico { color:var(--vrf); }
#s03 .eval .t { font:900 32px Montserrat; color:var(--fg); }
#s03 .eval .s { font:400 22px 'JetBrains Mono'; color:var(--muted); margin-top:4px; }
""",
    body=r"""
<div class="hdr"><div class="kicker">BÖLÜM 2 · SÜREÇ</div><div class="h1">Tereddüt nasıl giderildi?</div></div>
<div class="node card na">ICON_B<div><div class="n">Gümrükler Genel Müdürlüğü</div><div class="r">TİCARET BAKANLIĞI</div></div></div>
<div class="node card nb">ICON_B<div><div class="n">İthalat Genel Müdürlüğü</div><div class="r">TİCARET BAKANLIĞI</div></div></div>
<svg class="ov" viewBox="0 0 1920 1080">
  <path class="a1" d="M1046 405 H 1366" fill="none" stroke="#8FB2FF" stroke-width="6" stroke-linecap="round"/>
  <path class="h1a" d="M1374 405 l-22 -13 v26z" fill="#8FB2FF"/>
  <path class="a2" d="M1600 486 C 1600 600, 1560 618, 1530 618 M 950 618 C 820 618, 820 560, 820 492" fill="none" stroke="#33D9B2" stroke-width="6" stroke-linecap="round"/>
  <path class="h2a" d="M820 486 l-13 22 h26z" fill="#33D9B2"/>
  <path class="a3" d="M1024 830 H 1232" fill="none" stroke="#FFC53D" stroke-width="6" stroke-linecap="round" stroke-dasharray="2 14"/>
  <path class="h3a" d="M1238 830 l-22 -13 v26z" fill="#FFC53D"/>
</svg>
<div class="lab l1">konuyu iletti</div>
<div class="info card">MINI<div class="t">İç ve dış ünitelere ilişkin teknik bilgiler paylaşıldı</div></div>
<div class="docs card">ICON_DOC<div class="t">Mevcut teknik raporlar</div></div>
<div class="eval card">ICON_S<div><div class="t">Birlikte incelendi</div><div class="s">GGM DEĞERLENDİRMESİ</div></div></div>
""".replace("ICON_B", icon("building", 64)).replace("ICON_DOC", icon("doc", 52)).replace("ICON_S", icon("search", 56))
    .replace("MINI", '<svg class="mini" width="150" height="80" viewBox="0 0 340 180">' + odu(0, 20, w=150, h=110) + idu(175, 50, w=160, h=54) + "</svg>"),
    js=r"""
rise(".hdr .kicker", K.bunun - 0.3, 0, 20);
tl.fromTo(q(".hdr .h1"), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.bunun);
slideX(".na", K.ggm, -70);
draw(".a1", K.konuyu, 0.7);
pop(".h1a", K.konuyu + 0.65);
fadeIn(".l1", K.konuyu + 0.2);
slideX(".nb", K.igm, 70);
tl.fromTo(q(".nb"), { boxShadow: "0 0 0 rgba(51,217,178,0)" }, { boxShadow: "0 0 50px rgba(51,217,178,.45)", duration: 0.4, yoyo: true, repeat: 1 }, K.igm2);
draw(".a2", K.igm2 + 0.2, 1.4);
pop(".h2a", K.igm2 + 1.55);
rise(".info", K.teknik - 0.2);
spinFans(K.teknik - 0.2, D, 0.9);
slideX(".docs", K.mevcut - 0.2, -60);
draw(".a3", K.birlikte - 0.5, 0.45);
pop(".h3a", K.birlikte - 0.05);
pop(".eval", K.birlikte);
tl.fromTo(q(".eval .ico"), { rotation: -15 }, { rotation: 15, duration: 0.5, yoyo: true, repeat: 1, ease: "sine.inOut" }, K.birlikte + 0.4);
""",
)

# ---------------------------------------------------------------- s04 Tuzak
S["s04"] = dict(
    sfx=[("impact-bass-1", T("s04", "tuzak") + 0.15, 0.45), ("error", T("s04", "yapmaz") - 0.1, 0.25)],
    keys=dict(
        inc=T("s04", "İnceleme"), ms=T("s04", "Multi"), vrf=T("s04", "VRF"), ortak=T("s04", "ortak"), ama=T("s04", "ama"),
        mimari=T("s04", "mimari"), calisma=T("s04", "çalışma"), ve=T("s04", "işte", off=-0.3), tuzak=T("s04", "tuzak"),
        her=T("s04", "Her"), ama2=T("s04", "ama", 2), vrf2=T("s04", "VRF", 2), yapmaz=T("s04", "yapmaz"),
    ),
    css=r"""
#s04 .hdr { position:absolute; left:600px; top:132px; }
#s04 .venn { position:absolute; left:0; top:0; width:1920px; height:1080px; }
#s04 .vl { font-family:'Archivo Black'; font-size:44px; }
#s04 .vo { font:700 26px Montserrat; fill:#EEF2FF; }
#s04 .neq { position:absolute; left:1176px; top:760px; font-family:'Archivo Black'; font-size:96px; color:var(--uyari); }
#s04 .diff { position:absolute; top:830px; font:700 28px Montserrat; color:var(--fg); }
#s04 .d1 { left:770px; } #s04 .d2 { left:1370px; }
#s04 .tz { position:absolute; left:0; top:318px; width:1920px; padding-left:580px; display:flex; justify-content:center; }
#s04 .eq { position:absolute; left:600px; top:462px; width:1220px; display:flex; align-items:center; justify-content:space-between; }
#s04 .eq .c1 { width:560px; padding:22px 26px; display:flex; align-items:center; gap:18px; }
#s04 .eq .c1 .t { font:700 30px/1.2 Montserrat; color:var(--fg); }
#s04 .eq .ne { font-family:'Archivo Black'; font-size:130px; color:var(--uyari); width:140px; text-align:center; }
#s04 .eq .c2 { width:440px; height:180px; position:relative; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:96px; color:var(--vrf); }
#s04 .eq .c2 .xx { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; color:var(--uyari); }
#s04 .verdict { position:absolute; left:600px; top:664px; width:1220px; text-align:center; font-family:'Archivo Black'; font-size:54px; color:var(--fg); }
#s04 .verdict span { color:var(--uyari); }
#s04 .hz { position:absolute; left:580px; width:1240px; height:22px; background:repeating-linear-gradient(-45deg,#FFD400 0 22px,#14141A 22px 44px); opacity:.9; transform-origin:left center; }
#s04 .hz1 { top:300px; } #s04 .hz2 { top:740px; }
""",
    body=r"""
<div class="hdr"><div class="kicker">BÖLÜM 3 · ORTAK NOKTA</div><div class="h1">Benzer görünür, farklı çalışır</div></div>
<svg class="venn" viewBox="0 0 1920 1080">
  <g class="vg">
    <g class="cl"><circle cx="1010" cy="560" r="210" fill="rgba(143,178,255,.14)" stroke="#8FB2FF" stroke-width="6"/><text x="930" y="575" class="vl" fill="#8FB2FF" text-anchor="middle">MULTI-SPLIT</text></g>
    <g class="cr"><circle cx="1390" cy="560" r="210" fill="rgba(51,217,178,.14)" stroke="#33D9B2" stroke-width="6"/><text x="1490" y="575" class="vl" fill="#33D9B2" text-anchor="middle">VRF</text></g>
    <g class="ov"><text x="1200" y="548" class="vo" text-anchor="middle">Ortak</text><text x="1200" y="582" class="vo" text-anchor="middle">özellikler</text></g>
  </g>
</svg>
<div class="neq">≠</div>
<div class="diff d1">Teknik mimari</div>
<div class="diff d2">Çalışma prensibi</div>
<div class="hz hz1"></div><div class="hz hz2"></div>
<div class="tz">BADGE</div>
<div class="eq">
  <div class="card c1">MINI<div class="t">Bir dış üniteye birden fazla iç ünite bağlanabilir</div></div>
  <div class="ne">≠</div>
  <div class="card c2">VRF<div class="xx">XICON</div></div>
</div>
<div class="verdict">Bu, <span>tek başına</span> VRF yapmaz!</div>
""".replace("BADGE", badge("tuzak", big=True)).replace("XICON", icon("x", 200))
    .replace("MINI", '<svg width="170" height="120" viewBox="0 0 560 400">' + odu(195, 0, w=170, h=120)
             + "".join(idu(x, 320, w=150, h=50) for x in (0, 205, 410))
             + '<path d="M280 130 V 230 M75 230 H 485 M75 230 V 312 M280 230 V 312 M485 230 V 312" fill="none" stroke="#8FB2FF" stroke-width="10" stroke-linecap="round"/></svg>'),
    js=r"""
rise(".hdr .kicker", K.inc - 0.3, 0, 20);
tl.fromTo(q(".hdr .h1"), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.inc);
tl.fromTo(q(".cl"), { x: -260, opacity: 0 }, { x: 0, opacity: 1, duration: 0.8, ease: "expo.out" }, K.ms);
tl.fromTo(q(".cr"), { x: 260, opacity: 0 }, { x: 0, opacity: 1, duration: 0.8, ease: "expo.out" }, K.vrf);
pop(".ov", K.ortak);
tl.to(q(".cl"), { x: -70, duration: 0.7, ease: "power3.inOut" }, K.ama);
tl.to(q(".cr"), { x: 70, duration: 0.7, ease: "power3.inOut" }, K.ama);
tl.to(q(".ov"), { opacity: 0, duration: 0.3 }, K.ama);
pop(".neq", K.ama + 0.4);
rise(".d1", K.mimari, 0, 24);
rise(".d2", K.calisma, 0, 24);
tl.to(q(".venn, .neq, .diff"), { opacity: 0, scale: 0.92, duration: 0.45, ease: "power2.in", transformOrigin: "1200px 560px" }, K.ve - 0.1);
strike(".hz1", K.ve + 0.1, 0.5);
tl.fromTo(q(".hz2"), { scaleX: 0, transformOrigin: "right center" }, { scaleX: 1, duration: 0.5, ease: "power2.out" }, K.ve + 0.1);
slam(".tz .badge", K.tuzak - 0.25);
tl.fromTo(q(".tz .badge"), { rotation: 0 }, { rotation: -3, duration: 0.09, yoyo: true, repeat: 7, ease: "none" }, K.tuzak + 0.5);
tl.to(q(".tz .badge"), { scale: 0.86, duration: 0.5, ease: "power3.inOut" }, K.her - 0.3);
tl.to(q(".hz"), { opacity: 0.35, duration: 0.5 }, K.her - 0.3);
slideX(".eq .c1", K.her, -80);
pop(".eq .ne", K.ama2);
pop(".eq .c2", K.vrf2 - 0.3);
tl.fromTo(q(".eq .xx"), { scale: 3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "expo.in" }, K.yapmaz - 0.25);
rise(".verdict", K.yapmaz - 0.1, 0, 30);
""",
)

# ---------------------------------------------------------------- s05 Karşılaştırma
_ms_svg = (
    '<svg class="msd" viewBox="0 0 540 420" width="520" height="404">'
    + odu(185, 20, w=170, h=120, label="Dış ünite")
    + "".join(
        f'<path class="mp" d="M{270 + dx} 140 V 200 Q {270 + dx} 220 {250 + dx} 220 H {x + 75 + o} V 320" fill="none" stroke="#5E7FD0" stroke-width="7" stroke-linecap="round"/>'
        for x, dx, o in ((20, -30, -8), (195, -6, 0), (370, 20, 8))
    )
    + "".join(
        f'<path class="mf" d="M{270 + dx} 140 V 200 Q {270 + dx} 220 {250 + dx} 220 H {x + 75 + o} V 320" fill="none" stroke="#CFE2FF" stroke-width="3" stroke-dasharray="6 14" stroke-linecap="round"/>'
        for x, dx, o in ((20, -30, -8), (195, -6, 0), (370, 20, 8))
    )
    + "".join(idu(x, 324, w=150, h=50, label="İç ünite") for x in (20, 195, 370))
    + "</svg>"
)
_vrf_idus = (60, 220, 380, 540)
_vrf_svg = (
    '<svg class="vrd" viewBox="0 0 690 420" width="650" height="396">'
    + odu(30, 10, w=170, h=120, label="Dış ünite")
    + '<g transform="translate(470 18)"><g class="ctl"><rect width="190" height="86" rx="14" fill="#0E1C46" stroke="#33D9B2" stroke-width="3"/>'
      '<rect x="16" y="16" width="70" height="40" rx="6" fill="#33D9B2" opacity=".85"/><text x="100" y="40" class="svgs" fill="#BFF5E6">Merkezi</text><text x="100" y="66" class="svgs" fill="#BFF5E6">kontrol</text></g></g>'
    + '<path class="dl" d="M470 62 H 210" fill="none" stroke="#33D9B2" stroke-width="3" stroke-dasharray="4 10"/>'
    + '<path class="main" d="M115 132 V 190 H 640" fill="none" stroke="#7FA6FF" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
    + '<path class="mainf" d="M115 132 V 190 H 640" fill="none" stroke="#E0ECFF" stroke-width="4" stroke-dasharray="8 16" stroke-linecap="round"/>'
    + "".join(f'<path class="br" d="M{x + 70} 190 V 300" fill="none" stroke="#7FA6FF" stroke-width="8" stroke-linecap="round"/>' for x in _vrf_idus)
    + "".join(f'<path class="brf" d="M{x + 70} 190 V 300" fill="none" stroke="#E0ECFF" stroke-width="3" stroke-dasharray="6 12"/>' for x in _vrf_idus)
    + "".join(f'<rect class="joint" x="{x + 62}" y="182" width="16" height="16" rx="3" transform="rotate(45 {x + 70} 190)" fill="#FFC53D"/>' for x in _vrf_idus)
    + "".join(valve(x + 70, 252, cls="vv", s=0.8) for x in _vrf_idus)
    + "".join(idu(x, 304, w=140, h=48) for x in _vrf_idus)
    + "".join(f'<g transform="translate({x + 70} 384)"><g class="adr"><rect x="-38" y="-18" width="76" height="34" rx="17" fill="#33D9B2"/><text y="8" text-anchor="middle" class="svga">#0{i + 1}</text></g></g>' for i, x in enumerate(_vrf_idus))
    + "".join(f'<g transform="translate({x + 128} 296)"><g class="lvl"><rect x="0" y="-40" width="10" height="40" rx="3" fill="#24386F"/><rect class="lf" x="0" y="-40" width="10" height="40" rx="3" fill="#33D9B2"/></g></g>' for x in _vrf_idus)
    + "</svg>"
)
S["s05"] = dict(
    keys=dict(
        ms=T("s05", "Multi"), bir=T("s05", "Bir"), vrf=T("s05", "VRF'yi"), f1=T("s05", "Soğutucu"), f1b=T("s05", "değişken"),
        f2=T("s05", "akışkan", 2), f2b=T("s05", "branşmanlar"), f3=T("s05", "Her"), f3b=T("s05", "bağımsız"), f4=T("s05", "ve", 2),
        f4b=T("s05", "adresleme"), hr=T("s05", "Isı"), hr2=T("s05", "bir", 2), es=T("s05", "eş"),
    ),
    css=r"""
#s05 .hdr { position:absolute; left:600px; top:132px; }
#s05 .pl { position:absolute; top:268px; height:640px; padding:20px 24px; }
#s05 .L { left:600px; width:550px; }
#s05 .R { left:1170px; width:650px; padding:20px 0 20px 0; }
#s05 .pill { display:inline-block; font-family:'Archivo Black'; font-size:36px; padding:4px 22px; border-radius:12px; color:var(--bg); }
#s05 .L .pill { background:var(--ms); } #s05 .R .pill { background:var(--vrf); margin-left:24px; }
#s05 .msd { position:absolute; left:10px; top:84px; }
#s05 .vrd { position:absolute; left:0; top:76px; }
#s05 .cap1 { position:absolute; left:24px; top:540px; width:510px; font:700 28px/1.25 Montserrat; color:var(--fg); }
#s05 .feat { position:absolute; left:24px; top:452px; width:610px; }
#s05 .fr { display:flex; align-items:center; gap:14px; height:42px; font:700 25px Montserrat; color:var(--fg); }
#s05 .fr .ico { color:var(--vrf); flex:none; }
#s05 .fr i { font-style:normal; color:var(--muted); font-weight:400; }
#s05 .hr { position:absolute; left:600px; top:268px; width:550px; height:640px; padding:20px 24px; border-color:var(--onemli) !important; }
#s05 .hr .pill { background:var(--onemli); font-size:30px; }
#s05 .rooms { position:absolute; left:24px; top:300px; width:512px; display:flex; gap:22px; }
#s05 .room { flex:1; height:200px; border-radius:18px; border:4px solid; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px; font:900 28px Montserrat; }
#s05 .hot { border-color:var(--hot); color:var(--hot); background:rgba(255,122,69,.12); }
#s05 .cold { border-color:var(--cold); color:var(--cold); background:rgba(79,195,247,.12); }
#s05 .room small { font:400 22px 'JetBrains Mono'; color:var(--muted); }
#s05 .hrsvg { position:absolute; left:24px; top:92px; }
#s05 .same { position:absolute; left:24px; top:536px; width:512px; text-align:center; font-family:'Archivo Black'; font-size:44px; color:var(--onemli); }
#s05 .hrnote { position:absolute; left:24px; top:76px; font:700 24px Montserrat; color:var(--muted); }
""",
    body=r"""
<div class="hdr"><div class="kicker">BÖLÜM 4 · KARŞILAŞTIRMA</div><div class="h1">Multi-split ve VRF nasıl ayrılır?</div></div>
<div class="pl card L"><span class="pill">MULTI-SPLIT</span>MSSVG<div class="cap1">Temel mantık: bir dış ünite, birden fazla iç üniteyi çalıştırır.</div></div>
<div class="pl card R"><span class="pill">VRF</span>VRFSVG
  <div class="feat">
    <div class="fr r1">CHK Değişken akışkan debisi <i>· anlık yüke göre</i></div>
    <div class="fr r2">CHK Ortak ana hat + branşmanlar</div>
    <div class="fr r3">CHK Her iç ünitede bağımsız akışkan ayarı</div>
    <div class="fr r4">CHK Gelişmiş adresleme + merkezi kontrol</div>
  </div>
</div>
<div class="hr card"><span class="pill">ISI GERİ KAZANIMLI VRF</span>
  <svg class="hrsvg" viewBox="0 0 512 190" width="512" height="190">HRSVG</svg>
  <div class="rooms"><div class="room hot">FLAME ISITMA<small>Mahal 1</small></div><div class="room cold">SNOW SOĞUTMA<small>Mahal 2</small></div></div>
  <div class="same">AYNI ANDA!</div>
</div>
""".replace("MSSVG", _ms_svg).replace("VRFSVG", _vrf_svg).replace("CHK", icon("check", 30))
    .replace("FLAME", icon("flame", 52)).replace("SNOW", icon("snow", 52))
    .replace("HRSVG", odu(171, 0, w=170, h=110, label="")
             + '<path class="hp" d="M200 110 V 150 H 128 V 190" fill="none" stroke="#FF7A45" stroke-width="9" stroke-linecap="round"/>'
             + '<path class="cp" d="M312 110 V 150 H 384 V 190" fill="none" stroke="#4FC3F7" stroke-width="9" stroke-linecap="round"/>'
             + '<path class="hpf" d="M200 110 V 150 H 128 V 190" fill="none" stroke="#FFE1D3" stroke-width="3" stroke-dasharray="6 12"/>'
             + '<path class="cpf" d="M312 110 V 150 H 384 V 190" fill="none" stroke="#DDF4FF" stroke-width="3" stroke-dasharray="6 12"/>'),
    js=r"""
rise(".hdr .kicker", 0.05, 0, 20);
tl.fromTo(q(".hdr .h1"), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, 0.15);
tl.fromTo(q(".L"), { x: -40, opacity: 0, rotationY: 12, transformPerspective: 1400 }, { x: 0, opacity: 1, rotationY: 0, duration: 0.7, ease: "expo.out" }, K.ms - 0.2);
fadeIn(".msd .odu", K.ms);
draw(".msd .mp", K.bir, 0.9);
pop(".msd .idu", K.bir + 0.4, 0.12);
fadeIn(".msd .mf", K.bir + 1.1, 0.3);
flow(".msd .mf", K.bir + 1.1, D, 40);
rise(".cap1", K.bir + 0.6, 0, 24);
tl.fromTo(q(".R"), { x: 40, opacity: 0, rotationY: -12, transformPerspective: 1400 }, { x: 0, opacity: 1, rotationY: 0, duration: 0.7, ease: "expo.out" }, K.vrf - 0.3);
tl.to(q(".L"), { opacity: 0.45, scale: 0.97, duration: 0.5 }, K.vrf - 0.2);
fadeIn(".vrd .odu, .vrd .ctl", K.vrf);
draw(".vrd .main", K.vrf + 0.3, 0.8);
draw(".vrd .br", K.vrf + 0.9, 0.5);
pop(".vrd .joint", K.vrf + 1.0, 0.08);
pop(".vrd .idu", K.vrf + 1.2, 0.08);
spinFans(0, D, 1.1);
// 1 — değişken debi: flow overlays with varying speeds + level bars
rise(".fr.r1", K.f1, 0, 18);
fadeIn(".vrd .mainf, .vrd .brf", K.f1, 0.3);
flow(".vrd .mainf", K.f1, D, 70);
flow(".vrd .brf", K.f1, D, [25, 70, 45, 10]);
fadeIn(".vrd .lvl", K.f1, 0.3);
q(".vrd .lf").forEach((el, i) => {
  const a = [0.35, 0.9, 0.6, 0.15][i], b = [0.8, 0.3, 0.55, 0.95][i];
  tl.fromTo(el, { scaleY: 0, transformOrigin: "50% 100%" }, { scaleY: a, duration: 0.8, ease: "power2.out" }, K.f1b);
  tl.to(el, { scaleY: b, duration: 0.9, ease: "power2.inOut" }, K.f3b);
});
// 2 — ortak ana hat + branşman
rise(".fr.r2", K.f2, 0, 18);
tl.fromTo(q(".vrd .main"), { stroke: "#7FA6FF" }, { stroke: "#FFC53D", duration: 0.35, yoyo: true, repeat: 3 }, K.f2 + 0.3);
tl.fromTo(q(".vrd .joint"), { scale: 1 }, { scale: 1.7, duration: 0.2, yoyo: true, repeat: 1, stagger: 0.1, transformOrigin: "50% 50%" }, K.f2b);
// 3 — bağımsız ayar: EEV valves
rise(".fr.r3", K.f3, 0, 18);
pop(".vrd .vv", K.f3 + 0.2, 0.1);
// 4 — adresleme + merkezi kontrol
rise(".fr.r4", K.f4, 0, 18);
pop(".vrd .adr", K.f4b, 0.1);
draw(".vrd .dl", K.f4b + 0.4, 0.5);
tl.fromTo(q(".vrd .ctl"), { scale: 1 }, { scale: 1.08, duration: 0.25, yoyo: true, repeat: 1, transformOrigin: "50% 50%" }, K.f4b + 0.8);
// heat recovery card replaces multi-split panel
tl.to(q(".L"), { opacity: 0, x: -40, duration: 0.4, ease: "power2.in" }, K.hr - 0.3);
tl.fromTo(q(".hr"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.hr);
draw(".hr .hp, .hr .cp", K.hr + 0.5, 0.6);
fadeIn(".hr .hpf, .hr .cpf", K.hr + 1.1, 0.3);
flow(".hr .hpf, .hr .cpf", K.hr + 1.1, D, 40);
slideX(".room.hot", K.hr2, -40);
slideX(".room.cold", K.hr2 + 0.9, 40);
pop(".same", K.es);
breathe(".same", K.es + 0.6, D - 0.4, 0.05, 1.2);
""",
)
