"""Diplomatik İşlemler Genelgesi carousel — passport / visa-page theme. Writes carousel.html."""
import pathlib, sys
from theme import visa_bg, cover_bg, stamp, seal, perf_number, mrz, ic, pouch, emblem, W, H

D = pathlib.Path(__file__).resolve().parent
TOTAL = 15

CSS = r"""
:root { --navy:#10224F; --ink:#1B1F2E; --ink2:#454B63; --muted:#6E6A5E; --burg:#7A1428; --gold:#B8893B; --gold2:#E9C77E;
  --teal:#0F7C7C; --rose:#C9637A; --card:rgba(255,255,255,.93); --line:rgba(16,34,79,.18); --green:#0B7A55; --red:#B0122B; --amber:#B45309; }
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#555; font-family:Montserrat, sans-serif; color:var(--ink); }
.slide { position:relative; width:1080px; height:1350px; overflow:hidden; margin:0 auto 40px; background:#F4EFE3; }
.bgsvg { position:absolute; inset:0; }
.top { position:absolute; left:64px; right:64px; top:52px; height:70px; display:flex; justify-content:space-between; align-items:center; }
.top .lab { font:700 19px 'JetBrains Mono'; letter-spacing:.16em; color:var(--burg); }
.top .lab b { color:var(--navy); }
.top .perf { margin-top:4px; }
.c { position:absolute; left:64px; right:64px; top:140px; height:1010px; }
.kick { display:inline-flex; align-items:center; gap:10px; font:700 19px 'JetBrains Mono'; letter-spacing:.16em; color:#fff; background:var(--burg); padding:8px 14px; border-radius:4px; }
.t { font-family:Marcellus, serif; font-size:64px; line-height:1.06; color:var(--navy); margin-top:16px; letter-spacing:.005em; }
.t em { font-style:normal; color:var(--burg); }
.sub { font:500 26px/1.4 Montserrat; color:var(--ink2); margin-top:12px; }
.card { background:var(--card); border:2px solid var(--navy); border-radius:18px; box-shadow:0 14px 34px rgba(16,34,79,.16); }
.mrz { position:absolute; left:0; right:0; bottom:0; height:132px; background:rgba(255,255,255,.75); border-top:2px dashed rgba(16,34,79,.35);
  padding:24px 64px 0; font:700 28px/1.35 'JetBrains Mono'; letter-spacing:.14em; color:#2A2F40; white-space:nowrap; overflow:hidden; }
.foot { position:absolute; right:64px; bottom:150px; display:flex; align-items:center; gap:14px; }
.foot img { height:34px; }
.stamp { display:block; }
.row { display:flex; gap:18px; }
.mini { font:700 16px 'JetBrains Mono'; letter-spacing:.12em; color:var(--muted); }
.big { font-family:'Archivo Black'; color:var(--navy); line-height:1; }
.ic { display:block; flex:none; }
.pill { display:inline-flex; align-items:center; gap:8px; font:800 20px Montserrat; padding:7px 14px; border-radius:999px; border:2px solid var(--navy); background:#fff; }

/* ---- cover ---- */
.cov { background:#5E0F1F; }
.cov .emb { position:absolute; left:340px; top:230px; }
.cov .ctop { position:absolute; left:0; right:0; top:110px; text-align:center; font-family:Marcellus; font-size:30px; letter-spacing:.42em; color:var(--gold2); }
.cov .ttl { position:absolute; left:80px; right:80px; top:690px; text-align:center; font-family:Marcellus; font-size:76px; line-height:1.05; letter-spacing:.06em;
  background:linear-gradient(180deg,#FBE7B5 0%,#E2B865 45%,#B07E2E 100%); -webkit-background-clip:text; background-clip:text; color:transparent; }
.cov .num { position:absolute; left:0; right:0; top:880px; text-align:center; font:700 26px 'JetBrains Mono'; letter-spacing:.3em; color:var(--gold2); }
.cov .tags { position:absolute; left:80px; right:80px; top:950px; display:flex; justify-content:center; gap:14px; flex-wrap:wrap; }
.cov .tags span { font:800 22px Montserrat; color:#2E0710; background:linear-gradient(180deg,#F8DFA3,#D6A754); padding:10px 18px; border-radius:999px; }
.cov .src { position:absolute; left:0; right:0; top:1040px; text-align:center; font:600 21px Montserrat; color:#F1D9DD; opacity:.9; }
.cov .swipe { position:absolute; left:0; right:0; top:1150px; text-align:center; font:800 24px Montserrat; color:var(--gold2); letter-spacing:.08em; }
.cov .chip { position:absolute; left:80px; top:1206px; }
.cov .lg { position:absolute; right:80px; top:1188px; background:#F4EFE3; border-radius:12px; padding:8px 14px; }
.cov .lg img { height:38px; display:block; }
.cov .st1 { position:absolute; left:742px; top:520px; }

/* ---- mindmap ---- */
.mm svg.lines { position:absolute; left:-64px; top:-140px; }
.mm .core { position:absolute; left:322px; top:430px; width:308px; height:308px; border-radius:50%; background:radial-gradient(circle at 38% 32%,#9C2A3E,#6E1123 60%,#3E0812);
  display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; color:#F6E2C0; box-shadow:0 0 0 10px rgba(184,137,59,.35), 0 24px 50px rgba(78,10,24,.35); }
.mm .core small { font:700 16px 'JetBrains Mono'; letter-spacing:.18em; color:var(--gold2); }
.mm .core b { font-family:Marcellus; font-size:46px; line-height:1.05; margin-top:6px; color:#FFF3DA; }
.mm .core span { font:600 18px Montserrat; margin-top:8px; color:#F1D9DD; }
.mm .nd { position:absolute; width:440px; padding:18px 20px; }
.mm .nd .h { display:flex; align-items:center; gap:12px; font:900 25px Montserrat; color:var(--navy); }
.mm .nd .h .ic { color:var(--burg); }
.mm .nd ul { list-style:none; margin-top:8px; }
.mm .nd li { font:500 21px/1.35 Montserrat; color:var(--ink2); padding-left:22px; position:relative; margin-top:5px; }
.mm .nd li:before { content:""; position:absolute; left:2px; top:10px; width:10px; height:10px; border-radius:50%; background:var(--gold); }
.mm .nd li b { color:var(--ink); font-weight:800; }
.mm .n1 { left:0; top:170px; } .mm .n2 { left:512px; top:170px; } .mm .n3 { left:0; top:790px; } .mm .n4 { left:512px; top:790px; }

/* ---- courier containers ---- */
.kc .left { position:absolute; left:0; top:190px; width:430px; }
.kc .letter { padding:22px 22px 18px; background:#FFFDF6; border:2px solid var(--navy); border-radius:6px; box-shadow:0 18px 30px rgba(16,34,79,.18); position:relative; }
.kc .letter .hd { font:700 15px 'JetBrains Mono'; letter-spacing:.14em; color:var(--burg); }
.kc .letter .tt { font-family:Marcellus; font-size:32px; color:var(--navy); margin-top:4px; }
.kc .fld { margin-top:12px; padding:10px 12px; border:1.5px dashed rgba(16,34,79,.35); border-radius:6px; background:#fff; }
.kc .fld small { display:block; font:700 13px 'JetBrains Mono'; letter-spacing:.1em; color:var(--muted); }
.kc .fld b { display:block; font:800 21px Montserrat; color:var(--ink); margin-top:2px; }
.kc .letter .sealx { position:absolute; right:-24px; bottom:-30px; }
.kc .forms { display:flex; gap:12px; margin-top:44px; }
.kc .forms .f { flex:1; text-align:center; padding:12px 8px; border-radius:12px; border:2px solid var(--navy); background:var(--card); }
.kc .forms .f b { display:block; font-family:'Archivo Black'; font-size:30px; color:var(--navy); }
.kc .forms .f span { font:700 17px Montserrat; color:var(--ink2); }
.kc .right { position:absolute; left:470px; top:190px; width:482px; }
.kc .bags { padding:20px 20px 16px; }
.kc .bagrow { display:flex; gap:6px; justify-content:space-between; margin-top:8px; }
.kc .bg { width:84px; text-align:center; }
.kc .bg .ic { color:var(--navy); margin:0 auto; }
.kc .bg b { display:block; font:900 20px Montserrat; color:var(--burg); margin-top:2px; }
.kc .lim { display:flex; align-items:baseline; gap:10px; margin-top:12px; }
.kc .lim .big { font-size:62px; }
.kc .lim span { font:700 21px Montserrat; color:var(--ink2); }
.kc .tol { margin-top:16px; padding:14px 16px; border-radius:14px; background:#FFF4E0; border:2px solid var(--amber); font:600 20px/1.35 Montserrat; color:#5A3A0A; }
.kc .tol b { color:#3A2404; }
.kc .over { margin-top:14px; padding:14px 16px; border-radius:14px; background:#F9E4E8; border:2px solid var(--red); font:600 20px/1.35 Montserrat; color:#5E0B1A; }
.kc .over b { color:#3E0712; }
.kc .unacc { position:absolute; left:0; top:830px; width:952px; display:flex; gap:16px; align-items:center; padding:16px 20px; }
.kc .unacc .ic { color:var(--teal); }
.kc .unacc p { font:600 20px/1.35 Montserrat; color:var(--ink2); } .kc .unacc p b { color:var(--ink); }
.kc .st { position:absolute; right:-6px; top:16px; }
"""


def page(n, body, cls="", lab="GENELGE <b>2026/11</b> · DİPLOMATİK İŞLEMLER", seed=None):
    return f'''<section class="slide {cls}" id="p{n}">
  {visa_bg(seed if seed is not None else n)}
  <div class="top"><div class="lab">{lab}</div>{perf_number(n)}</div>
  <div class="c">{body}</div>
  <div class="foot"><img src="img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div>
  {mrz(n, TOTAL)}
</section>'''


S = {}

S[1] = f'''<section class="slide cov" id="p1">
  {cover_bg()}
  <div class="ctop">GÜMRÜK KOÇU · DERS NOTU</div>
  <div class="emb">{emblem(400)}</div>
  <div class="st1">{stamp("gold", "05.10.2026", rot=12, scale=0.85)}</div>
  <div class="ttl">DİPLOMATİK<br/>İŞLEMLER GENELGESİ</div>
  <div class="num">TİCARET BAKANLIĞI GGM · 05.10.2026</div>
  <div class="tags"><span>Araçlar</span><span>Kişisel &amp; ev eşyası</span><span>Kurye kapları</span><span>Karşılıklılık</span></div>
  <div class="src">2000/21 ve 2015/10 sayılı genelgeler yürürlükten kalktı</div>
  <div class="swipe">KAYDIRARAK İNCELEYİN →</div>
  <div class="lg"><img src="img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div>
</section>'''

S[2] = page(2, f'''
  <span class="kick">ZİHİN HARİTASI</span>
  <div class="t" style="font-size:56px">Genelge <em>bir bakışta</em></div>
  <svg class="lines" width="1080" height="1350" viewBox="0 0 1080 1350" aria-hidden="true"></svg>
  <div class="core"><small>GENELGE</small><b>2026/11</b><span>Diplomatik İşlemler</span></div>
  <div class="card nd n1"><div class="h">{ic("scale", 34)}Dayanak · 4458 s. GK</div>
    <ul><li><b>m.167/1-2:</b> mütekabiliyetle ithal diplomatik eşya vergiden muaf</li><li><b>m.60/5-(b):</b> misyon şefi yazısı ve kurye mektubu = beyanname</li></ul></div>
  <div class="card nd n2"><div class="h">{ic("car", 34)}A · Gümrük ayrıcalıkları</div>
    <ul><li><b>Araçlar:</b> ithal, satış, devir, ihraç, terk</li><li><b>Eşya:</b> kişisel, ev eşyası, diplomatik paket</li><li>Makine · sergi · bağış · kültür varlığı</li></ul></div>
  <div class="card nd n3"><div class="h">{ic("bag", 34)}B · Kurye</div>
    <ul><li><b>Kurye mektubu:</b> Form C giriş, Form D çıkış</li><li><b>Kaplar:</b> günde 5 kap × 30 kg</li></ul></div>
  <div class="card nd n4"><div class="h">{ic("globe", 34)}Karşılıklılık</div>
    <ul><li>Tespit: <b>Dışişleri Bakanlığı</b></li><li>Kaldırılan: <b>2000/21</b> ve <b>2015/10</b> genelgeler</li></ul></div>
''', cls="mm")

bag_cells = "".join(f'<div class="bg">{ic("bag", 62)}<b>30 kg</b></div>' for _ in range(5))
S[13] = page(13, f'''
  <span class="kick">B · KURYE</span>
  <div class="t" style="font-size:50px">Kurye mektubu &amp; <em>kurye kapları</em></div>
  <div class="st">{stamp("dikkat", "GÜNLÜK LİMİT", rot=8, scale=0.8)}</div>
  <div class="left">
    <div class="letter"><div class="hd">KURYE MEKTUBU · ZORUNLU BİLGİLER</div><div class="tt">Beyanname yerine geçer</div>
      <div class="fld"><small>01</small><b>Kuryenin adı soyadı</b></div>
      <div class="fld"><small>02</small><b>Pasaport numarası</b></div>
      <div class="fld"><small>03</small><b>Düzenleyen makamın açık adı + mührü</b></div>
      <div class="fld"><small>04</small><b>Kurye kabı parça sayısı</b></div>
      <div class="sealx">{seal(110, "CD", "KURYE")}</div></div>
    <div class="forms"><div class="f"><b>FORM C</b><span>Giriş beyanı</span></div><div class="f"><b>FORM D</b><span>Çıkış beyanı</span></div></div>
  </div>
  <div class="right">
    <div class="card bags"><div class="mini">1 KURYE · 1 GÜN · 1 MEKTUP / KONŞİMENTO</div>
      <div class="bagrow">{bag_cells}</div>
      <div class="lim"><span class="big">5 × 30</span><span>kg'a kadar kap</span></div></div>
    <div class="tol"><b>+5 kg tolerans:</b> 30 kg aşılırsa olay bazında, parça başına en çok 5 kg; gümrük müdürü veya müdür yardımcısının takdiriyle.</div>
    <div class="over"><b>Daha ağır ya da daha fazla kap:</b> Dışişleri onaylı Takrir (Form A) gerekir.</div>
  </div>
  <div class="card unacc">{ic("plane", 48)}<p><b>Refakatsiz / pilota emanet kaplar:</b> aynı limit (günde 5 kap, 30 kg), tek konşimento. Teslim: gümrüksüz saha (Transit Hall), Kurye Karşılama Kartı hamili görevli, Form C / D ile.</p></div>
''', cls="kc")

import slides_more
S.update(slides_more.build(page, TOTAL))
CSS += slides_more.CSS2

JS = r"""<script>
(() => {
  const S = document.querySelector(".mm"); if (!S) return;
  const svg = S.querySelector("svg.lines"), base = svg.getBoundingClientRect();
  const r = (el) => { const b = el.getBoundingClientRect(); return { l: b.left - base.left, t: b.top - base.top, r: b.right - base.left, b: b.bottom - base.top, cx: (b.left + b.right) / 2 - base.left, cy: (b.top + b.bottom) / 2 - base.top }; };
  const c = r(S.querySelector(".core")); let d = "", dots = "";
  S.querySelectorAll(".nd").forEach((n) => {
    const nb = r(n), top = nb.b < c.t;
    const ang = Math.atan2(nb.cy - c.cy, nb.cx - c.cx), rad = (c.r - c.l) / 2 + 8;
    const sx = c.cx + rad * Math.cos(ang), sy = c.cy + rad * Math.sin(ang);
    const ex = nb.cx, ey = top ? nb.b : nb.t, my = (sy + ey) / 2;
    d += `M${sx} ${sy} C ${sx} ${my}, ${ex} ${my}, ${ex} ${ey} `;
    dots += `<circle cx="${ex}" cy="${ey}" r="10" fill="#7A1428"/><circle cx="${sx}" cy="${sy}" r="8" fill="#E9C77E" stroke="#7A1428" stroke-width="3"/>`;
  });
  svg.innerHTML = `<path d="${d}" fill="none" stroke="#B8893B" stroke-width="6" stroke-linecap="round" stroke-dasharray="2 12"/><path d="${d}" fill="none" stroke="#7A1428" stroke-width="2.5"/>` + dots;
})();
</script>"""

only = [int(x) for x in sys.argv[1:]] or sorted(S)
html = f'''<!doctype html><html lang="tr"><head><meta charset="UTF-8"/><title>Diplomatik İşlemler Genelgesi — Carousel</title>
<link rel="stylesheet" href="fonts/fonts.css"/><style>{CSS}</style></head><body>
{"".join(S[i] for i in only if i in S)}
{JS}
</body></html>'''
(D / "carousel.html").write_text(html)
print("slides:", [i for i in only if i in S])
