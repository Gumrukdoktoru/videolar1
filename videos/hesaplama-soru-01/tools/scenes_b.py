"""Scenes 07-12: adım 3, sonuç, tuzaklar, uyarı, koçun notu, kapanış."""
from lib import T, D, icon, badge
from scenes_a import steps, ledger, STEPS_CSS, LEDGER_CSS, disc

S = {}

# ---------------------------------------------------------------- s07 Adım 3: KDV
KEYS = ["7", "8", "9", "÷", "4", "5", "6", "×", "1", "2", "3", "−", "0", ",", "=", "+"]
S["s07"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("click-soft", T("s07", "İki"), 0.4), ("click-soft", T("s07", "yüzde"), 0.4), ("ping", T("s07", "beş", 3) + 0.2, 0.35)],
    keys=dict(uc=T("s07", "Üçüncü"), kdv=T("s07", "KDV"), bin=T("s07", "İki"), yuzde=T("s07", "yüzde"), res=T("s07", "beş", 3), dolar=T("s07", "dolar")),
    css=STEPS_CSS + LEDGER_CSS + r"""
#s07 .calc { position:absolute; left:640px; top:250px; width:610px; height:600px; border-radius:36px; padding:30px;
  background:linear-gradient(160deg,#1B2F6E,#0E1C46); border:4px solid #3B5BB8; box-shadow:0 30px 70px rgba(0,0,0,.5); }
#s07 .scr { height:150px; border-radius:18px; background:#CFE8D6; color:#0B2A1A; padding:14px 22px; display:flex; flex-direction:column; justify-content:space-between;
  box-shadow:inset 0 6px 14px rgba(0,0,0,.25); position:relative; }
#s07 .scr .ex { font:700 34px 'JetBrains Mono'; text-align:right; min-height:42px; }
#s07 .scr .ex span { position:absolute; right:22px; top:14px; }
#s07 .scr .rs { font:700 64px 'JetBrains Mono'; text-align:right; }
#s07 .keys { display:grid; grid-template-columns:repeat(4, 1fr); gap:14px; margin-top:24px; }
#s07 .k { height:78px; border-radius:16px; background:#2A417F; color:#E9EEFF; display:flex; align-items:center; justify-content:center; font:700 34px 'JetBrains Mono';
  box-shadow:0 6px 0 #142555; }
#s07 .k.op { background:#3F6BFF; } #s07 .k.eq { background:var(--gold); color:#2a1d00; }
#s07 .tag { position:absolute; left:600px; top:870px; }
""",
    body=f'''
{steps(3)}
<div class="calc"><div class="scr"><div class="ex"><span class="e1">2.555</span><span class="e2">2.555 × 0,20</span></div><div class="rs"><span class="cnt">0</span></div></div>
  <div class="keys">{"".join(f'<div class="k k{i}{" op" if k in "÷×−+" else " eq" if k == "=" else ""}">{k}</div>' for i, k in enumerate(KEYS))}</div></div>
{ledger([("Gümrük vergisi", "5,00 $", ""), ("KDV matrahı", "2.555,00 $", ""), ("KDV (%20)", "511,00 $", "")])}
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".calc"), { y: 120, opacity: 0, rotation: -4 }, { y: 0, opacity: 1, rotation: 0, duration: 0.7, ease: "expo.out" }, K.uc);
tl.fromTo(q(".ledger"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.uc + 0.2);
fadeTo(".scr .e1, .scr .e2", 0.01, 0, 0.01);
// key presses: 2 5 5 5 → × 0 , 2 → =
const PRESS = [[9, 0], [5, 0.15], [5, 0.3], [5, 0.45], [7, 1.3], [12, 1.45], [13, 1.6], [9, 1.75], [14, 2.2]];
PRESS.forEach(([i, dt]) => {
  tl.fromTo(q(".k" + i), { y: 0, filter: "brightness(1)" }, { y: 5, filter: "brightness(1.6)", duration: 0.07, yoyo: true, repeat: 1, ease: "power1.out", immediateRender: false }, K.bin + dt);
});
fadeIn(".scr .e1", K.bin + 0.1, 0.15);
fadeTo(".scr .e1", K.yuzde - 0.05, 0, 0.1);
fadeIn(".scr .e2", K.yuzde, 0.15);
count(".scr .cnt", K.res - 0.1, 0, 511, 1.0, 2);
pulse(".scr .rs", K.dolar, 1.08);
tl.fromTo(q(".ledger .ln.new"), { opacity: 1, clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 0.7, ease: "power1.inOut" }, K.res + 0.3);
"""
)

# ---------------------------------------------------------------- s08 Sonuç
OPTS = [("A", "16"), ("B", "511"), ("C", "516"), ("D", "765"), ("E", "816")]
S["s08"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("click-soft", T("s08", "Beş"), 0.4), ("click-soft", T("s08", "artı"), 0.4), ("riser", T("s08", "Ödenmesi") - 0.4, 0.3),
         ("impact-bass-1", T("s08", "beş", 3) + 0.9, 0.4), ("chime", T("s08", "C"), 0.45)],
    keys=dict(son=T("s08", "sonuç"), gv=T("s08", "Beş"), arti=T("s08", "artı"), od=T("s08", "Ödenmesi"), tot=T("s08", "beş", 3),
              dogru=T("s08", "Doğru"), A=T("s08", "C")),
    css=STEPS_CSS + r"""
#s08 .rcp { position:absolute; left:600px; top:240px; width:600px; height:580px; background:#FBF8EE; color:#1B2A57; padding:30px 40px;
  box-shadow:0 30px 70px rgba(0,0,0,.45); clip-path:polygon(0 0,100% 0,100% 96%,95% 100%,90% 96%,85% 100%,80% 96%,75% 100%,70% 96%,65% 100%,60% 96%,55% 100%,50% 96%,45% 100%,40% 96%,35% 100%,30% 96%,25% 100%,20% 96%,15% 100%,10% 96%,5% 100%,0 96%); }
#s08 .rcp .rh { text-align:center; font-family:'Archivo Black'; font-size:38px; letter-spacing:.04em; }
#s08 .rcp .rs { text-align:center; font:700 18px 'JetBrains Mono'; color:#5A6AA0; letter-spacing:.14em; margin-top:4px; padding-bottom:16px; border-bottom:3px dashed #9BA8CC; }
#s08 .rcp .ln { display:flex; justify-content:space-between; align-items:baseline; margin-top:26px; font:800 30px Montserrat; }
#s08 .rcp .ln b { font:700 38px 'JetBrains Mono'; }
#s08 .rcp .ln small { display:block; font:600 20px 'JetBrains Mono'; color:#5A6AA0; }
#s08 .rcp .eq { border-top:4px solid #1B2A57; margin-top:30px; padding-top:20px; }
#s08 .rcp .tot { display:flex; justify-content:space-between; align-items:center; font:900 34px Montserrat; color:#B4231B; }
#s08 .rcp .tot b { font:700 60px 'JetBrains Mono'; }
#s08 .rcp .usd { text-align:right; font:800 24px Montserrat; color:#B4231B; }
#s08 .ans { position:absolute; left:1260px; top:250px; width:560px; }
#s08 .ao { display:flex; align-items:center; gap:22px; height:88px; margin-bottom:14px; padding:0 24px 0 14px; position:relative; }
#s08 .ao .L { width:62px; height:62px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:32px;
  color:#071A45; background:var(--accent2); flex:none; }
#s08 .ao .v { font:700 44px 'JetBrains Mono'; color:var(--fg); }
#s08 .ao .ck { margin-left:auto; width:56px; height:56px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center; opacity:0; }
#s08 .ao.win { border-color:var(--ok); background:rgba(46,212,122,.16); }
#s08 .stamp { position:absolute; left:1330px; top:742px; padding:14px 26px; border:7px solid var(--ok); color:var(--ok); border-radius:16px;
  font-family:'Archivo Black'; font-size:52px; line-height:1; background:rgba(7,26,69,.9); transform:rotate(-7deg); }
#s08 .burst { position:absolute; left:1290px; top:454px; width:1px; height:1px; }
#s08 .burst i { position:absolute; left:0; top:0; width:14px; height:14px; border-radius:3px; opacity:0; }
""",
    body=f'''
{steps(4)}
<div class="rcp"><div class="rh">VERGİ MAKBUZU</div><div class="rs">SORU 1 · USD</div>
  <div class="ln l1"><span>Gümrük vergisi<small>50 × %10</small></span><b>5,00</b></div>
  <div class="ln l2"><span>KDV<small>2.555 × %20</small></span><b>511,00</b></div>
  <div class="eq"><div class="tot"><span>TOPLAM</span><b class="cnt">0,00</b></div><div class="usd">ABD Doları</div></div>
</div>
<div class="ans">{"".join(f'<div class="ao card a{L}"><span class="L">{L}</span><span class="v">{v}</span><span class="ck">{icon("check", 34)}</span></div>' for L, v in OPTS)}</div>
<div class="stamp">CEVAP: C</div>
<div class="burst">{"".join(f'<i style="background:{c}"></i>' for c in ["#FFC53D", "#33D9B2", "#8FB2FF", "#FF4D5E", "#2ED47A"] * 4)}</div>
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".rcp"), { y: -200, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, ease: "expo.out" }, K.son);
fadeTo(".rcp .ln, .rcp .eq", 0.01, 0, 0.01);
rise(".rcp .l1", K.gv, 0, 20);
rise(".rcp .l2", K.arti, 0, 20);
rise(".rcp .eq", K.od, 0, 20);
count(".rcp .cnt", K.tot, 0, 516, 1.2, 2);
pulse(".rcp .tot b", K.tot + 1.3, 1.12);
slideX(".ans .ao", K.od + 0.3, 80, 0.08);
fadeTo(".ans .ao:not(.aC)", K.dogru, 0.3, 0.4);
tl.to(q(".ans .aC"), { borderColor: "#2ED47A", backgroundColor: "rgba(46,212,122,.18)", scale: 1.06, duration: 0.35, ease: "back.out(2)", transformOrigin: "0% 50%" }, K.dogru);
tl.fromTo(q(".ans .aC .ck"), { opacity: 0, scale: 0.2 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(3)" }, K.A - 0.2);
slam(".stamp", K.A);
q(".burst i").forEach((p, i) => {
  const a = (i / 20) * Math.PI * 2, r = 160 + (i % 5) * 34;
  tl.fromTo(p, { x: 0, y: 44, opacity: 1, rotation: 0, scale: 1 }, { x: Math.cos(a) * r, y: 44 + Math.sin(a) * r, opacity: 0, rotation: 260 + i * 17, scale: 0.6, duration: 1.1, ease: "power2.out", immediateRender: false }, K.A + 0.05);
});
"""
)

# ---------------------------------------------------------------- s09 Tuzaklar
S["s09"] = dict(
    sfx=[("impact-bass-1", T("s09", "tuzaklara"), 0.4), ("error", T("s09", "A"), 0.25), ("error", T("s09", "B"), 0.25), ("error", T("s09", "D"), 0.25),
         ("error", T("s09", "E"), 0.25), ("pop", T("s09", "E") + 1.0, 0.3)],
    keys=dict(tz=T("s09", "tuzaklara"), y1=T("s09", "Yazılımı"), A=T("s09", "A"), gv=T("s09", "Gümrük"), B=T("s09", "B"), y2=T("s09", "Yazılımı", 2),
              iki=T("s09", "iki"), bu=T("s09", "Bu"), Dk=T("s09", "D"), E=T("s09", "E")),
    css=r"""
#s09 .top { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:24px; }
#s09 .top .kicker { font-size:24px; color:#FFD400; }
#s09 .tc { position:absolute; width:480px; height:312px; padding:14px 22px; }
#s09 .tA { left:600px; top:254px; } #s09 .tB { left:1100px; top:254px; } #s09 .tD { left:600px; top:582px; } #s09 .tE { left:1100px; top:582px; }
#s09 .tc .th { display:flex; align-items:center; gap:14px; }
#s09 .tc .th .L { width:52px; height:52px; border-radius:50%; background:var(--uyari); color:#fff; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:28px; flex:none; }
#s09 .tc .th b { font:700 38px 'JetBrains Mono'; color:#FFB3BB; }
#s09 .tc .why { margin-top:10px; font:800 21px/1.25 Montserrat; color:var(--fg); padding:8px 12px; background:rgba(255,77,94,.12); border-left:5px solid var(--uyari); border-radius:8px; }
#s09 .tc .ln { display:flex; justify-content:space-between; align-items:baseline; margin-top:10px; font:700 21px Montserrat; color:var(--muted); }
#s09 .tc .ln b { font:700 25px 'JetBrains Mono'; color:#FF8A96; }
#s09 .tc .ln.miss b { color:var(--gold); }
#s09 .tc .sum { margin-top:10px; padding-top:8px; border-top:3px solid #3B5296; display:flex; justify-content:space-between; align-items:center; font:900 22px Montserrat; color:#FF8A96; }
#s09 .tc .sum b { font:700 30px 'JetBrains Mono'; }
#s09 .tc .x { position:absolute; right:-14px; top:-14px; width:52px; height:52px; border-radius:50%; background:var(--uyari); color:#2a0a0e;
  display:flex; align-items:center; justify-content:center; box-shadow:0 8px 20px rgba(0,0,0,.4); }
#s09 .baba { position:absolute; left:1612px; top:368px; height:520px; filter:drop-shadow(0 18px 30px rgba(0,0,0,.45)); }
#s09 .bub { position:absolute; left:1608px; top:176px; width:270px; padding:14px 18px; background:#F4F7FF; color:#0B1A44; border-radius:20px; font:900 24px/1.25 Montserrat; }
#s09 .bub:after { content:""; position:absolute; right:96px; bottom:-22px; border:12px solid transparent; border-top:14px solid #F4F7FF; }
#s09 .bub em { font-style:normal; color:#0B8A47; }
""",
    body=f"""
<div class="top">{badge("tuzak", big=True)}<div class="kicker">HER YANLIŞ ŞIK = BİR HATA</div></div>
<div class="tc tA card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">A</span><b>16 $</b></div>
  <div class="why">Yazılımı KDV matrahından da çıkardı</div>
  <div class="ln l1"><span>GV: 50 × %10</span><b>5</b></div>
  <div class="ln l2"><span>KDV: (50 + 5) × %20</span><b>11</b></div>
  <div class="sum"><span>Toplam</span><b>16</b></div>
</div>
<div class="tc tB card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">B</span><b>511 $</b></div>
  <div class="why">Gümrük vergisini unuttu</div>
  <div class="ln miss l1"><span>GV</span><b>— ?</b></div>
  <div class="ln l2"><span>KDV: 2.555 × %20</span><b>511</b></div>
  <div class="sum"><span>Toplam</span><b>511</b></div>
</div>
<div class="tc tD card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">D</span><b>765 $</b></div>
  <div class="why">Yazılımı GV'ye kattı, GV'yi KDV'ye eklemedi</div>
  <div class="ln l1"><span>GV: 2.550 × %10</span><b>255</b></div>
  <div class="ln l2"><span>KDV: 2.550 × %20</span><b>510</b></div>
  <div class="sum"><span>Toplam</span><b>765</b></div>
</div>
<div class="tc tE card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">E</span><b>816 $</b></div>
  <div class="why">Yazılımı gümrük vergisi matrahına kattı</div>
  <div class="ln l1"><span>GV: 2.550 × %10</span><b>255</b></div>
  <div class="ln l2"><span>KDV: 2.805 × %20</span><b>561</b></div>
  <div class="sum"><span>Toplam</span><b>816</b></div>
</div>
<img class="baba" src="assets/img/baba-crop.png" alt="Gümrükçü Baba" />
<div class="bub">Doğrusu <em>C: 5 + 511 = 516!</em></div>
""",
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 2.6, opacity: 0, rotation: -10 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.tz);
rise(".top .kicker", K.tz + 0.5, 0, 20);
tl.fromTo(q(".baba"), { x: 260, opacity: 0 }, { x: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }, K.tz + 0.8);
fadeTo(".tc .why, .tc .ln, .tc .sum, .tc .x", 0.01, 0, 0.01);
function card(c, at, lnAt, sumAt) {
  tl.fromTo(q(".t" + c), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "expo.out" }, at);
  fadeIn(".t" + c + " .why", at + 0.3, 0.3);
  fadeIn(".t" + c + " .ln", lnAt, 0.3);
  fadeIn(".t" + c + " .sum", sumAt, 0.3);
  pop(".t" + c + " .x", sumAt, 0, "back.out(3)");
}
card("A", K.y1, K.y1 + 1.0, K.A);
card("B", K.gv, K.gv + 1.2, K.B);
card("D", K.y2, K.iki, K.Dk);
card("E", K.y2 + 0.3, K.iki + 0.3, K.E);
tl.fromTo(q(".bub"), { scale: 0.3, opacity: 0, transformOrigin: "60% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.E + 1.0);
"""
)

# ---------------------------------------------------------------- s10 Uyarı: kapsam
S["s10"] = dict(
    sfx=[("notification", T("s10", "uyarı"), 0.35), ("pop", T("s10", "entegre"), 0.3), ("pop", T("s10", "Veri"), 0.3), ("ping", T("s10", "Yani"), 0.3),
         ("chime", T("s10", "dahil"), 0.35)],
    keys=dict(uy=T("s10", "uyarı"), yon=T("s10", "Yönetmeliğe"), ent=T("s10", "entegre"), yari=T("s10", "yarı"), bun=T("s10", "bunlarla"),
              veri=T("s10", "Veri"), ses=T("s10", "ses"), sin=T("s10", "sinematografik"), vid=T("s10", "video"), yani=T("s10", "Yani"),
              film=T("s10", "film"), dahil=T("s10", "dahil")),
    css=r"""
#s10 .top { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:24px; }
#s10 .top .kicker { font-size:26px; color:#FF8A96; }
#s10 .col { position:absolute; top:256px; width:595px; height:446px; padding:20px 26px; }
#s10 .c1 { left:600px; } #s10 .c2 { left:1225px; }
#s10 .col .ch { font:900 28px/1.15 Montserrat; color:var(--fg); }
#s10 .col .ch small { display:block; font:700 20px 'JetBrains Mono'; color:var(--uyari); letter-spacing:.12em; margin-bottom:6px; }
#s10 .it { display:flex; align-items:center; gap:18px; margin-top:14px; padding:12px 16px; border-radius:14px; background:rgba(255,77,94,.10); border:2px solid rgba(255,77,94,.45); }
#s10 .it .ico { color:var(--accent2); }
#s10 .it span { font:800 25px/1.18 Montserrat; color:var(--fg); }
#s10 .it .no { margin-left:auto; color:var(--uyari); }
#s10 .ex { position:absolute; left:600px; top:716px; width:1220px; height:178px; display:flex; align-items:center; gap:30px; padding:0 30px;
  background:rgba(46,212,122,.10); border:3px solid var(--ok); border-radius:22px; }
#s10 .ex .pair { display:flex; align-items:center; gap:10px; }
#s10 .ex .pair .ico { color:var(--accent2); }
#s10 .ex .plus { font:900 44px Montserrat; color:var(--muted); }
#s10 .ex .t { font:900 34px/1.2 Montserrat; color:#DFFFEF; }
#s10 .ex .t b { color:var(--ok); }
#s10 .ex .t small { display:block; font:700 22px 'JetBrains Mono'; color:var(--muted); margin-top:8px; }
""",
    body=f'''
<div class="top">{badge("uyari", big=True)}<div class="kicker">KURAL HER TAŞIYICIYA UYMAZ</div></div>
<div class="col c1 card"><div class="ch"><small>"TAŞIYICI ORTAM" KAPSAMAZ</small>Bunlar taşıyıcı ortam sayılmaz</div>
  <div class="it i1">{icon("chip", 44)}<span>Entegre devreler</span><span class="no">{icon("x", 34)}</span></div>
  <div class="it i2">{icon("chip", 44)}<span>Yarı iletkenler</span><span class="no">{icon("x", 34)}</span></div>
  <div class="it i3">{icon("calc", 44)}<span>Bunlarla bütünlük oluşturan benzeri araç ve aletler</span><span class="no">{icon("x", 34)}</span></div></div>
<div class="col c2 card"><div class="ch"><small>"VERİ / KOMUT" KAPSAMAZ</small>Bunlar veri/komut sayılmaz</div>
  <div class="it j1">{icon("music", 44)}<span>Ses kayıtları</span><span class="no">{icon("x", 34)}</span></div>
  <div class="it j2">{icon("film", 44)}<span>Sinematografik kayıtlar</span><span class="no">{icon("x", 34)}</span></div>
  <div class="it j3">{icon("film", 44)}<span>Video kayıtları</span><span class="no">{icon("x", 34)}</span></div></div>
<div class="ex"><div class="pair">{icon("cd", 76)}<span class="plus">+</span>{icon("film", 76)}</div>
  <div class="t">DVD içinde film → film bedeli de <b>gümrük kıymetine DAHİL</b>
    <small>Örnek: taşıyıcı 40 $ + film 3.000 $ → gümrük kıymeti 3.040 $</small></div></div>
''',
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 2.4, opacity: 0, rotation: -8 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.uy);
rise(".top .kicker", K.uy + 0.45, 0, 20);
tl.fromTo(q(".c1"), { x: -80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.yon);
slideX(".c1 .i1", K.ent, -50);
slideX(".c1 .i2", K.yari, -50);
slideX(".c1 .i3", K.bun, -50);
tl.fromTo(q(".c2"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.veri);
slideX(".c2 .j1", K.ses, 50);
slideX(".c2 .j2", K.sin, 50);
slideX(".c2 .j3", K.vid, 50);
tl.fromTo(q(".ex"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }, K.yani);
pulse(".ex .pair", K.film, 1.12);
pulse(".ex .t b", K.dahil, 1.08);
"""
)

# ---------------------------------------------------------------- s11 Koçun notu
S["s11"] = dict(
    sfx=[("pop", T("s11", "Koçun"), 0.35), ("click-soft", T("s11", "ihracatta"), 0.4), ("ping", T("s11", "yalnızca"), 0.3), ("whoosh-short", T("s11", "Formülü") - 0.2, 0.3),
         ("chime", T("s11", "hepsinden"), 0.4)],
    keys=dict(koc=T("s11", "Koçun"), ihr=T("s11", "ihracatta"), yaz=T("s11", "Yazılım"), on=T("s11", "yalnızca"), form=T("s11", "Formülü"),
              gv=T("s11", "Gümrük"), kdv=T("s11", "KDV"), hep=T("s11", "hepsinden")),
    css=r"""
#s11 .top { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:24px; }
#s11 .top .kicker { font-size:26px; color:#FFE27A; }
#s11 .exp { position:absolute; left:600px; top:250px; width:1220px; height:220px; display:flex; align-items:center; gap:34px; padding:0 36px; }
#s11 .exp .ic2 { width:140px; height:140px; border-radius:28px; background:rgba(63,107,255,.22); border:3px solid var(--accent2); color:var(--accent2);
  display:flex; align-items:center; justify-content:center; flex:none; position:relative; }
#s11 .exp .ic2 .mini { position:absolute; right:-14px; bottom:-14px; width:62px; height:62px; border-radius:50%; background:#DCE7FF; color:#0B2257;
  display:flex; align-items:center; justify-content:center; }
#s11 .exp .tx small { display:block; font:700 22px 'JetBrains Mono'; color:var(--accent2); letter-spacing:.12em; }
#s11 .exp .tx b { display:block; font:900 38px/1.2 Montserrat; color:var(--fg); margin-top:8px; }
#s11 .exp .val { margin-left:auto; text-align:center; flex:none; }
#s11 .exp .val small { display:block; font:800 22px Montserrat; color:var(--muted); }
#s11 .exp .val b { display:block; font-family:'Archivo Black'; font-size:46px; line-height:1.05; color:var(--gold); margin-top:6px; }
#s11 .fm { position:absolute; left:600px; top:506px; width:1220px; height:390px; padding:30px 40px; border-radius:24px;
  background:linear-gradient(180deg, rgba(255,197,61,.14), rgba(255,197,61,.04)); border:4px solid var(--gold); }
#s11 .fm .kicker { color:var(--gold); }
#s11 .fr { display:flex; align-items:center; gap:24px; margin-top:26px; }
#s11 .fr .lh { width:330px; height:110px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:33px; flex:none; white-space:nowrap; }
#s11 .fr .gv { background:var(--gold); color:#2a1d00; }
#s11 .fr .kd { background:var(--teal); color:#03221a; }
#s11 .fr .arr { color:var(--fg); }
#s11 .fr .rh { display:flex; align-items:center; gap:10px; flex-wrap:nowrap; }
#s11 .fr .rh span { font:900 30px Montserrat; padding:12px 16px; border-radius:14px; background:rgba(255,255,255,.08); border:2px solid rgba(255,255,255,.25); color:var(--fg); white-space:nowrap; }
#s11 .fr .rh i { font:900 34px Montserrat; font-style:normal; color:var(--muted); }
""",
    body=f'''
<div class="top">{badge("ipucu", big=True)}<div class="kicker">KOÇUN NOTU</div></div>
<div class="exp card"><div class="ic2">{icon("export", 80)}<div class="mini">{icon("cd", 44)}</div></div>
  <div class="tx"><small>AYNI MANTIK · İHRACAT</small><b>Yazılım ihracatında beyannamede<br/>gümrük kıymeti = taşıyıcı ortam</b></div>
  <div class="val"><small>gümrük kıymeti</small><b>SADECE<br/>TAŞIYICI</b></div></div>
<div class="fm"><div class="kicker">AKILDA TUT · FORMÜL</div>
  <div class="fr r1"><div class="lh gv">GÜMRÜK VERGİSİ</div><div class="arr">{icon("arrow", 60)}</div><div class="rh"><span>TAŞIYICI (DVD)</span></div></div>
  <div class="fr r2"><div class="lh kd">KDV</div><div class="arr">{icon("arrow", 60)}</div><div class="rh"><span>TAŞIYICI</span><i>+</i><span>GV</span><i>+</i><span>YAZILIM</span></div></div>
</div>
''',
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 0.3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.5, ease: "back.out(2.4)" }, K.koc);
rise(".top .kicker", K.koc + 0.3, 0, 20);
tl.fromTo(q(".exp"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.65, ease: "expo.out" }, K.ihr);
tl.fromTo(q(".exp .ic2"), { y: 0 }, { y: -16, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }, K.yaz);
fadeTo(".exp .val", 0.01, 0, 0.01);
pop(".exp .val", K.on, 0, "back.out(2.6)");
tl.fromTo(q(".fm"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }, K.form);
slideX(".fm .r1 > *", K.gv, -40, 0.12);
slideX(".fm .r2 > *", K.kdv, -40, 0.12);
pop(".fm .r2 .rh span", K.kdv + 0.4, 0.15);
pulse(".fm .r2 .rh", K.hep, 1.06);
"""
)

# ---------------------------------------------------------------- s12 Kapanış
S["s12"] = dict(
    exit=False,
    sfx=[("whoosh-short", 0.3, 0.25), ("impact-bass-1", T("s12", "Cevap"), 0.4), ("pop", T("s12", "abone"), 0.35), ("pop", T("s12", "paylaşmayı"), 0.35),
         ("chime", T("s12", "Bir"), 0.35)],
    keys=dict(oz=T("s12", "Özetle"), tas=T("s12", "Taşıyıcı"), yaz=T("s12", "yazılım"), cev=T("s12", "Cevap"), bu=T("s12", "Bu"),
              abone=T("s12", "abone"), pay=T("s12", "paylaşmayı"), bir=T("s12", "Bir")),
    css=r"""
#s12 .right { position:absolute; left:860px; top:140px; width:960px; }
#s12 .sum { margin-top:18px; }
#s12 .row { display:flex; align-items:center; gap:22px; height:118px; padding:0 26px; margin-bottom:16px; }
#s12 .row .n { width:58px; height:58px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:28px; flex:none; }
#s12 .row .n1 { background:var(--gold); color:#2a1d00; } #s12 .row .n2 { background:var(--teal); color:#03221a; }
#s12 .row b { display:block; font:900 30px Montserrat; color:var(--fg); }
#s12 .row span { display:block; font:700 26px 'JetBrains Mono'; color:var(--muted); margin-top:4px; }
#s12 .ans { display:flex; align-items:center; gap:26px; margin-top:12px; padding:22px 30px; border-radius:24px; background:rgba(46,212,122,.14); border:4px solid var(--ok);
  box-shadow:0 0 60px rgba(46,212,122,.25); width:max-content; }
#s12 .ans .L { width:96px; height:96px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:56px; }
#s12 .ans b { font-family:'Archivo Black'; font-size:84px; line-height:1; color:#DFFFEF; }
#s12 .ans small { font:800 30px Montserrat; color:var(--ok); margin-left:6px; }
#s12 .cta { display:flex; gap:20px; margin-top:34px; }
#s12 .btn { display:flex; align-items:center; gap:14px; padding:18px 30px; border-radius:16px; font:900 30px Montserrat; }
#s12 .sub { background:#FF0033; color:#fff; box-shadow:0 10px 0 #9c0020; }
#s12 .shr { background:#F4F7FF; color:#0B1A44; box-shadow:0 10px 0 #9aa8d0; }
#s12 .bye { position:absolute; left:860px; top:790px; display:flex; align-items:center; gap:20px; }
#s12 .bye .lg { background:#F4F7FF; border-radius:14px; padding:10px 18px; }
#s12 .bye .lg img { height:46px; display:block; }
#s12 .bye span { font:800 28px/1.25 Montserrat; color:var(--fg); max-width:520px; }
""",
    body=f'''
<div class="right">
  <div class="kicker">ÖZET · SORU 1</div>
  <div class="sum">
    <div class="row card r1"><span class="n n1">1</span><div><b>Gümrük vergisi: sadece taşıyıcı ortam</b><span>50 × %10 = 5,00 $</span></div></div>
    <div class="row card r2"><span class="n n2">2</span><div><b>KDV: yazılım dahil toplam matrah</b><span>(50 + 5 + 2.500) × %20 = 511,00 $</span></div></div>
  </div>
  <div class="ans"><span class="L">C</span><b>516</b><small>USD</small></div>
  <div class="cta"><div class="btn sub">{icon("bell", 34)} ABONE OL</div><div class="btn shr">{icon("share", 34)} PAYLAŞ</div></div>
</div>
<div class="bye"><div class="lg"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div><span>Bir sonraki hesaplama dersinde görüşmek üzere!</span></div>
''',
    js=r"""
rise(".right .kicker", K.oz, 0, 20);
slideX(".sum .r1", K.tas, 80);
slideX(".sum .r2", K.yaz, 80);
tl.fromTo(q(".ans"), { scale: 2.2, opacity: 0, transformOrigin: "0% 50%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "expo.in" }, K.cev);
tl.fromTo(q(".ans"), { boxShadow: "0 0 20px rgba(46,212,122,.15)" }, { boxShadow: "0 0 80px rgba(46,212,122,.55)", duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 3 }, K.cev + 0.5);
pop(".cta .sub", K.abone, 0, "back.out(2.6)");
pop(".cta .shr", K.pay, 0, "back.out(2.6)");
tl.fromTo(q(".cta .sub .ico"), { rotation: 0 }, { rotation: 18, duration: 0.12, yoyo: true, repeat: 7, ease: "sine.inOut", transformOrigin: "50% 10%" }, K.abone + 0.4);
tl.fromTo(q(".bye"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }, K.bir);
"""
)
