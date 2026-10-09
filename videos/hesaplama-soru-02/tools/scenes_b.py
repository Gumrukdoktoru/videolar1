"""Scenes 07-12: adım 3 (ceza), sonuç, tuzaklar, uyarı, koçun notu, kapanış."""
from lib import T, D, icon, badge
from scenes_a import steps, ledger, STEPS_CSS, LEDGER_CSS

S = {}

# ---------------------------------------------------------------- s07 Adım 3: ceza (GK 234/1)
KEYS = ["7", "8", "9", "÷", "4", "5", "6", "×", "1", "2", "3", "−", "0", ",", "=", "+"]
S["s07"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("impact-bass-1", T("s07", "katı"), 0.35), ("click-soft", T("s07", "On"), 0.4),
         ("click-soft", T("s07", "çarpı"), 0.4), ("ping", T("s07", "otuz") + 0.3, 0.35)],
    keys=dict(uc=T("s07", "Üçüncü"), gk=T("s07", "Gümrük"), iki=T("s07", "iki"), kat=T("s07", "katı"), para=T("s07", "para"),
              on=T("s07", "On"), carpi=T("s07", "çarpı"), otuz=T("s07", "otuz"), lira=T("s07", "lira")),
    css=STEPS_CSS + LEDGER_CSS + r"""
#s07 .law { position:absolute; left:600px; top:196px; width:1220px; height:136px; background:#F3F6FF; color:#0B1A44; border-radius:20px; padding:18px 30px;
  box-shadow:0 30px 70px rgba(0,0,0,.45); }
#s07 .law .lh { display:flex; align-items:center; gap:14px; font:900 22px Montserrat; letter-spacing:.06em; color:#1E3FBF; }
#s07 .law .lh .no { font:700 20px 'JetBrains Mono'; color:#fff; background:#1E3FBF; padding:3px 10px; border-radius:8px; }
#s07 .law .lt { font:600 32px/1.3 Montserrat; margin-top:10px; white-space:nowrap; }
#s07 .law .lt em { font-style:normal; font:700 22px Montserrat; color:#B4231B; margin-left:10px; }
#s07 .hl { position:relative; display:inline-block; }
#s07 .hl .mk { position:absolute; left:-6px; right:-6px; bottom:4px; height:20px; background:#FFC53D; opacity:.9; transform-origin:left center; border-radius:4px; z-index:0; }
#s07 .hl b { position:relative; z-index:1; font-weight:900; }
#s07 .calc { position:absolute; left:640px; top:356px; width:610px; height:520px; border-radius:36px; padding:26px 30px;
  background:linear-gradient(160deg,#1B2F6E,#0E1C46); border:4px solid #3B5BB8; box-shadow:0 30px 70px rgba(0,0,0,.5); }
#s07 .scr { height:124px; border-radius:18px; background:#CFE8D6; color:#0B2A1A; padding:10px 22px; display:flex; flex-direction:column; justify-content:space-between;
  box-shadow:inset 0 6px 14px rgba(0,0,0,.25); position:relative; }
#s07 .scr .ex { font:700 30px 'JetBrains Mono'; text-align:right; min-height:38px; }
#s07 .scr .ex span { position:absolute; right:22px; top:10px; }
#s07 .scr .rs { font:700 58px 'JetBrains Mono'; text-align:right; line-height:1.1; }
#s07 .keys { display:grid; grid-template-columns:repeat(4, 1fr); gap:12px; margin-top:20px; }
#s07 .k { height:70px; border-radius:16px; background:#2A417F; color:#E9EEFF; display:flex; align-items:center; justify-content:center; font:700 32px 'JetBrains Mono';
  box-shadow:0 6px 0 #142555; }
#s07 .k.op { background:#3F6BFF; } #s07 .k.eq { background:var(--gold); color:#2a1d00; }
#s07 .x3 { position:absolute; left:1196px; top:330px; width:110px; height:110px; border-radius:50%; background:var(--uyari); color:#fff; display:flex; align-items:center;
  justify-content:center; font-family:'Archivo Black'; font-size:46px; box-shadow:0 0 0 10px rgba(255,77,94,.2), 0 16px 34px rgba(0,0,0,.45); }
#s07 .ledger { top:356px; height:520px; }
""",
    body=f'''
{steps(3)}
<div class="law"><div class="lh">{icon("gavel", 32)} GÜMRÜK KANUNU <span class="no">MADDE 234/1</span> · özet</div>
  <div class="lt">Eksik alınan vergilerin <span class="hl"><i class="mk"></i><b>3 katı para cezası</b></span><em>· kültür fonuna uygulanmaz</em></div></div>
<div class="calc"><div class="scr"><div class="ex"><span class="e1">11.520</span><span class="e2">11.520 × 3</span></div><div class="rs"><span class="cnt">0</span></div></div>
  <div class="keys">{"".join(f'<div class="k k{i}{" op" if k in "÷×−+" else " eq" if k == "=" else ""}">{k}</div>' for i, k in enumerate(KEYS))}</div></div>
<div class="x3">×3</div>
{ledger([("Kültür fonu", "36.000", "out"), ("Eksik ÖTV", "3.600", ""), ("Eksik KDV", "7.920", ""), ("Ceza (3×)", "34.560", "pen")])}
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".law"), { y: -60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.uc);
pulse(".law .no", K.iki, 1.2);
strike(".hl .mk", K.kat - 0.2, 0.6);
tl.fromTo(q(".calc"), { y: 120, opacity: 0, rotation: -4 }, { y: 0, opacity: 1, rotation: 0, duration: 0.7, ease: "expo.out" }, K.uc + 0.3);
tl.fromTo(q(".ledger"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.uc + 0.5);
slam(".x3", K.kat);
fadeTo(".scr .e1, .scr .e2", 0.01, 0, 0.01);
// key presses: 1 1 5 2 0 → × 3 → =
const PRESS = [[8, K.on], [8, K.on + 0.15], [5, K.on + 0.3], [9, K.on + 0.45], [12, K.on + 0.6], [7, K.carpi], [10, K.carpi + 0.35], [14, K.otuz - 0.25]];
PRESS.forEach(([i, at]) => {
  tl.fromTo(q(".k" + i), { y: 0, filter: "brightness(1)" }, { y: 5, filter: "brightness(1.6)", duration: 0.07, yoyo: true, repeat: 1, ease: "power1.out", immediateRender: false }, at);
});
fadeIn(".scr .e1", K.on + 0.1, 0.15);
fadeTo(".scr .e1", K.carpi - 0.05, 0, 0.1);
fadeIn(".scr .e2", K.carpi, 0.15);
count(".scr .cnt", K.otuz - 0.15, 0, 34560, 1.0, 0);
pulse(".scr .rs", K.lira, 1.08);
write(".ledger .r3", K.otuz + 0.4, 0.7);
"""
)

# ---------------------------------------------------------------- s08 Sonuç
OPTS = [("A", "11.520"), ("B", "36.000"), ("C", "43.200"), ("D", "46.080"), ("E", "82.080")]
S["s08"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("click-soft", T("s08", "on"), 0.4), ("click-soft", T("s08", "artı"), 0.4), ("riser", T("s08", "Uzlaşmaya") - 0.6, 0.3),
         ("impact-bass-1", T("s08", "kırk") + 0.9, 0.4), ("chime", T("s08", "D"), 0.45)],
    keys=dict(son=T("s08", "sonuç"), on=T("s08", "on"), arti=T("s08", "artı"), uzl=T("s08", "Uzlaşmaya"), kirk=T("s08", "kırk"),
              dogru=T("s08", "Doğru"), A=T("s08", "D")),
    css=STEPS_CSS + r"""
#s08 .rcp { position:absolute; left:600px; top:236px; width:620px; height:600px; background:#FBF8EE; color:#1B2A57; padding:26px 38px;
  box-shadow:0 30px 70px rgba(0,0,0,.45); clip-path:polygon(0 0,100% 0,100% 96%,95% 100%,90% 96%,85% 100%,80% 96%,75% 100%,70% 96%,65% 100%,60% 96%,55% 100%,50% 96%,45% 100%,40% 96%,35% 100%,30% 96%,25% 100%,20% 96%,15% 100%,10% 96%,5% 100%,0 96%); }
#s08 .rcp .rh { text-align:center; font-family:'Archivo Black'; font-size:36px; letter-spacing:.04em; }
#s08 .rcp .rs { text-align:center; font:700 18px 'JetBrains Mono'; color:#5A6AA0; letter-spacing:.14em; margin-top:4px; padding-bottom:14px; border-bottom:3px dashed #9BA8CC; }
#s08 .rcp .ln { position:relative; display:flex; justify-content:space-between; align-items:baseline; margin-top:22px; font:800 30px Montserrat; }
#s08 .rcp .ln b { font:700 38px 'JetBrains Mono'; }
#s08 .rcp .ln small { display:block; font:600 19px 'JetBrains Mono'; color:#5A6AA0; }
#s08 .rcp .lx { font-size:24px; color:#7D88A8; }
#s08 .rcp .lx b { font-size:28px; color:#7D88A8; }
#s08 .rcp .lx .sk { position:absolute; right:-6px; top:16px; width:126px; height:4px; background:#B4231B; border-radius:2px; transform-origin:left center; }
#s08 .rcp .lx .tg { position:absolute; left:210px; top:2px; font:900 15px Montserrat; letter-spacing:.08em; color:#B4231B; border:2px solid #B4231B; border-radius:6px; padding:1px 8px; }
#s08 .rcp .eq { border-top:4px solid #1B2A57; margin-top:22px; padding-top:16px; }
#s08 .rcp .tot { display:flex; justify-content:space-between; align-items:center; font:900 28px Montserrat; color:#B4231B; }
#s08 .rcp .tot b { font:700 58px 'JetBrains Mono'; }
#s08 .rcp .usd { text-align:right; font:800 22px Montserrat; color:#B4231B; }
#s08 .ans { position:absolute; left:1270px; top:250px; width:550px; }
#s08 .ao { display:flex; align-items:center; gap:22px; height:88px; margin-bottom:14px; padding:0 24px 0 14px; position:relative; }
#s08 .ao .L { width:62px; height:62px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:32px;
  color:#071A45; background:var(--accent2); flex:none; }
#s08 .ao .v { font:700 44px 'JetBrains Mono'; color:var(--fg); }
#s08 .ao .ck { margin-left:auto; width:56px; height:56px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center; opacity:0; }
#s08 .stamp { position:absolute; left:1340px; top:762px; padding:14px 26px; border:7px solid var(--ok); color:var(--ok); border-radius:16px;
  font-family:'Archivo Black'; font-size:52px; line-height:1; background:rgba(7,26,69,.9); transform:rotate(-7deg); }
#s08 .burst { position:absolute; left:1300px; top:556px; width:1px; height:1px; }
#s08 .burst i { position:absolute; left:0; top:0; width:14px; height:14px; border-radius:3px; opacity:0; }
""",
    body=f'''
{steps(4)}
<div class="rcp"><div class="rh">UZLAŞMA HESABI</div><div class="rs">SORU 2 · TL</div>
  <div class="ln l1"><span>Eksik vergi<small>ÖTV 3.600 + KDV 7.920</small></span><b>11.520</b></div>
  <div class="ln l2"><span>Para cezası<small>11.520 × 3 · GK 234/1</small></span><b>34.560</b></div>
  <div class="ln lx"><span>Kültür fonu<small>kuruma bildirilir</small></span><b>36.000</b><i class="sk"></i><em class="tg">UZLAŞMA DIŞI</em></div>
  <div class="eq"><div class="tot"><span>UZLAŞMAYA KONU</span><b class="cnt">0</b></div><div class="usd">Türk lirası</div></div>
</div>
<div class="ans">{"".join(f'<div class="ao card a{L}"><span class="L">{L}</span><span class="v">{v}</span><span class="ck">{icon("check", 34)}</span></div>' for L, v in OPTS)}</div>
<div class="stamp">CEVAP: D</div>
<div class="burst">{"".join(f'<i style="background:{c}"></i>' for c in ["#FFC53D", "#33D9B2", "#8FB2FF", "#FF4D5E", "#2ED47A"] * 4)}</div>
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".rcp"), { y: -200, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, ease: "expo.out" }, K.son);
fadeTo(".rcp .ln, .rcp .eq", 0.01, 0, 0.01);
rise(".rcp .l1", K.on, 0, 20);
rise(".rcp .l2", K.arti, 0, 20);
rise(".rcp .lx", K.uzl - 0.9, 0, 20);
strike(".rcp .lx .sk", K.uzl - 0.5, 0.35);
pop(".rcp .lx .tg", K.uzl - 0.3, 0, "back.out(3)");
rise(".rcp .eq", K.uzl, 0, 20);
count(".rcp .cnt", K.kirk - 0.1, 0, 46080, 1.1, 0);
pulse(".rcp .tot b", K.kirk + 1.1, 1.12);
slideX(".ans .ao", K.uzl + 0.3, 80, 0.08);
fadeTo(".ans .ao:not(.aD)", K.dogru, 0.3, 0.4);
tl.to(q(".ans .aD"), { borderColor: "#2ED47A", backgroundColor: "rgba(46,212,122,.18)", scale: 1.06, duration: 0.35, ease: "back.out(2)", transformOrigin: "0% 50%" }, K.dogru);
tl.fromTo(q(".ans .aD .ck"), { opacity: 0, scale: 0.2 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(3)" }, K.A - 0.2);
slam(".stamp", K.A);
q(".burst i").forEach((p, i) => {
  const a = (i / 20) * Math.PI * 2, r = 160 + (i % 5) * 34;
  tl.fromTo(p, { x: 0, y: 44, opacity: 1, rotation: 0, scale: 1 }, { x: Math.cos(a) * r, y: 44 + Math.sin(a) * r, opacity: 0, rotation: 260 + i * 17, scale: 0.6, duration: 1.1, ease: "power2.out", immediateRender: false }, K.A + 0.05);
});
"""
)

# ---------------------------------------------------------------- s09 Tuzaklar
S["s09"] = dict(
    sfx=[("impact-bass-1", T("s09", "tuzaklara"), 0.4), ("error", T("s09", "A"), 0.25), ("error", T("s09", "B"), 0.25), ("error", T("s09", "C"), 0.25),
         ("error", T("s09", "E"), 0.25), ("pop", T("s09", "E") + 1.6, 0.3)],
    keys=dict(tz=T("s09", "tuzaklara"), cez=T("s09", "Cezayı"), A=T("s09", "A"), sad=T("s09", "Sadece", 2), B=T("s09", "B"),
              otv=T("s09", "ÖTV'yi"), C=T("s09", "C"), kf=T("s09", "Kültür", 2), E=T("s09", "E")),
    css=r"""
#s09 .top { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:24px; }
#s09 .top .kicker { font-size:24px; color:#FFD400; }
#s09 .tc { position:absolute; width:480px; height:312px; padding:14px 22px; }
#s09 .tA { left:600px; top:254px; } #s09 .tB { left:1100px; top:254px; } #s09 .tC { left:600px; top:582px; } #s09 .tE { left:1100px; top:582px; }
#s09 .tc .th { display:flex; align-items:center; gap:14px; }
#s09 .tc .th .L { width:52px; height:52px; border-radius:50%; background:var(--uyari); color:#fff; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:28px; flex:none; }
#s09 .tc .th b { font:700 38px 'JetBrains Mono'; color:#FFB3BB; }
#s09 .tc .why { margin-top:10px; font:800 21px/1.25 Montserrat; color:var(--fg); padding:8px 12px; background:rgba(255,77,94,.12); border-left:5px solid var(--uyari); border-radius:8px; }
#s09 .tc .ln { display:flex; justify-content:space-between; align-items:baseline; margin-top:10px; font:700 21px Montserrat; color:var(--muted); white-space:nowrap; }
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
  <div class="th"><span class="L">A</span><b>11.520 TL</b></div>
  <div class="why">Cezayı unuttu, sadece eksik vergi</div>
  <div class="ln l1"><span>ÖTV + KDV: 3.600 + 7.920</span><b>11.520</b></div>
  <div class="ln miss l2"><span>Ceza (3 kat)</span><b>— ?</b></div>
  <div class="sum"><span>Toplam</span><b>11.520</b></div>
</div>
<div class="tc tB card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">B</span><b>36.000 TL</b></div>
  <div class="why">Sadece kültür fonuna baktı</div>
  <div class="ln l1"><span>KF: 1.200.000 × %3</span><b>36.000</b></div>
  <div class="ln miss l2"><span>Vergi + ceza</span><b>— ?</b></div>
  <div class="sum"><span>Toplam</span><b>36.000</b></div>
</div>
<div class="tc tC card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">C</span><b>43.200 TL</b></div>
  <div class="why">ÖTV'yi KDV matrahına eklemedi</div>
  <div class="ln l1"><span>Vergi: 3.600 + 7.200</span><b>10.800</b></div>
  <div class="ln l2"><span>Ceza: 10.800 × 3</span><b>32.400</b></div>
  <div class="sum"><span>Toplam</span><b>43.200</b></div>
</div>
<div class="tc tE card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">E</span><b>82.080 TL</b></div>
  <div class="why">Kültür fonunu da uzlaşmaya kattı</div>
  <div class="ln l1"><span>Doğru tutar</span><b>46.080</b></div>
  <div class="ln l2"><span>+ kültür fonu</span><b>36.000</b></div>
  <div class="sum"><span>Toplam</span><b>82.080</b></div>
</div>
<img class="baba" src="assets/img/baba-crop.png" alt="Gümrükçü Baba" />
<div class="bub">Doğrusu <em>D: 46.080 TL!</em></div>
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
card("A", K.cez, K.cez + 1.2, K.A);
card("B", K.sad, K.sad + 0.9, K.B);
card("C", K.otv, K.otv + 1.0, K.C);
card("E", K.kf, K.kf + 1.2, K.E);
tl.fromTo(q(".bub"), { scale: 0.3, opacity: 0, transformOrigin: "60% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.E + 1.6);
"""
)

# ---------------------------------------------------------------- s10 Uyarı: uzlaşmaya konu olamayacak alacaklar
S["s10"] = dict(
    sfx=[("notification", T("s10", "uyarı"), 0.35), ("whoosh-short", T("s10", "Her") - 0.1, 0.3), ("pop", T("s10", "matrahına"), 0.3),
         ("impact-bass-1", T("s10", "edilemez"), 0.35), ("pop", T("s10", "Tahsilat"), 0.3), ("pop", T("s10", "kaçakçılık"), 0.3),
         ("error", T("s10", "talep"), 0.25), ("chime", T("s10", "talep") + 0.9, 0.3)],
    keys=dict(uy=T("s10", "uyarı"), her=T("s10", "Her"), yon=T("s10", "Yönetmeliğine"), mat=T("s10", "matrahına"), asli=T("s10", "aslı"),
              edil=T("s10", "edilemez"), tah=T("s10", "Tahsilat"), kac=T("s10", "kaçakçılık"), talep=T("s10", "talep")),
    css=r"""
#s10 .top { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:24px; }
#s10 .top .kicker { font-size:26px; color:#FF8A96; }
#s10 .law { position:absolute; left:600px; top:254px; width:900px; height:424px; padding:20px 26px; }
#s10 .law .lh { display:flex; align-items:center; gap:14px; font:900 22px Montserrat; letter-spacing:.06em; color:var(--accent2); }
#s10 .law .lh .no { font:700 20px 'JetBrains Mono'; color:#071A45; background:var(--accent2); padding:3px 10px; border-radius:8px; }
#s10 .it { position:relative; display:flex; align-items:center; gap:18px; margin-top:16px; padding:14px 18px; border-radius:16px;
  background:rgba(255,77,94,.10); border:2px solid rgba(255,77,94,.5); }
#s10 .it .ico { color:var(--accent2); flex:none; }
#s10 .it .tx { font:800 25px/1.22 Montserrat; color:var(--fg); }
#s10 .it .tx small { display:inline-block; margin-top:6px; font:800 19px Montserrat; color:#E2D3FF; background:rgba(180,140,255,.2); border:2px solid #B48CFF;
  border-radius:8px; padding:1px 10px; }
#s10 .it .no .ico { color:#2a0a0e; }
#s10 .it .no { margin-left:auto; width:54px; height:54px; border-radius:50%; background:var(--uyari); color:#2a0a0e; display:flex; align-items:center; justify-content:center; flex:none; }
#s10 .cano { position:absolute; left:1572px; top:320px; height:440px; filter:drop-shadow(0 18px 30px rgba(0,0,0,.45)); }
#s10 .bub { position:absolute; left:1530px; top:160px; width:290px; padding:14px 18px; background:#F4F7FF; color:#0B1A44; border-radius:20px; font:900 24px/1.25 Montserrat; }
#s10 .bub:after { content:""; position:absolute; left:120px; bottom:-22px; border:12px solid transparent; border-top:14px solid #F4F7FF; }
#s10 .bub em { font-style:normal; color:#6B3FD6; }
#s10 .hayir { position:absolute; left:1560px; top:236px; padding:8px 20px; border:6px solid var(--uyari); border-radius:14px; color:var(--uyari);
  font-family:'Archivo Black'; font-size:48px; line-height:1; background:rgba(7,26,69,.92); transform:rotate(-8deg); }
#s10 .ok { position:absolute; left:600px; top:760px; width:1220px; height:120px; display:flex; align-items:center; gap:24px; padding:0 28px;
  background:rgba(46,212,122,.12); border:3px solid var(--ok); border-radius:22px; }
#s10 .ok .ck { width:64px; height:64px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center; flex:none; }
#s10 .ok .t { font:900 30px/1.2 Montserrat; color:#DFFFEF; }
#s10 .ok .t small { display:block; font:700 22px 'JetBrains Mono'; color:var(--ok); margin-top:4px; }
""",
    body=f'''
<div class="top">{badge("uyari", big=True)}<div class="kicker">HER ALACAK UZLAŞMAYA GİRMEZ</div></div>
<div class="law card"><div class="lh">{icon("doc", 32)} GÜMRÜK UZLAŞMA YÖNETMELİĞİ <span class="no">MADDE 6</span></div>
  <div class="it i1">{icon("mask", 50)}<div class="tx">Matraha giren ama aslı gümrükçe takip ve tahsil edilmeyen mali yükler<br/><small>ör. kültür fonu</small></div><span class="no">{icon("x", 34)}</span></div>
  <div class="it i2">{icon("receipt", 50)}<div class="tx">Tahsilat aşamasına gelmiş alacaklar</div><span class="no">{icon("x", 34)}</span></div>
  <div class="it i3">{icon("shield", 50)}<div class="tx">Kaçakçılık suçlarına ilişkin alacaklar</div><span class="no">{icon("x", 34)}</span></div>
</div>
<img class="cano" src="assets/img/cano-cut.png" alt="K firması temsilcisi" />
<div class="bub">Kültür fonunu da <em>uzlaşalım mı?</em></div>
<div class="hayir">HAYIR!</div>
<div class="ok"><span class="ck">{icon("check", 40)}</span><div class="t">Uzlaşmaya girebilen: eksik ÖTV + KDV ve para cezası<small>11.520 + 34.560 = 46.080 TL</small></div></div>
''',
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 2.4, opacity: 0, rotation: -8 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.uy);
rise(".top .kicker", K.uy + 0.45, 0, 20);
tl.fromTo(q(".cano"), { x: 300, opacity: 0 }, { x: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }, K.her);
tl.fromTo(q(".bub"), { scale: 0.3, opacity: 0, transformOrigin: "40% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.her + 0.7);
tl.fromTo(q(".law"), { x: -80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.yon);
fadeTo(".it .no", 0.01, 0, 0.01);
slideX(".it.i1", K.mat, -50);
pulse(".it.i1 small", K.asli + 0.6, 1.12);
pop(".it.i1 .no", K.edil, 0, "back.out(3)");
slam(".hayir", K.edil + 0.1);
slideX(".it.i2", K.tah, -50);
slideX(".it.i3", K.kac, -50);
pop(".it.i2 .no, .it.i3 .no", K.talep, 0.15, "back.out(3)");
tl.fromTo(q(".ok"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }, K.talep + 0.8);
"""
)

# ---------------------------------------------------------------- s11 Koçun notu: kendiliğinden bildirim + formül
S["s11"] = dict(
    sfx=[("pop", T("s11", "Koçun"), 0.35), ("click-soft", T("s11", "önce"), 0.4), ("ping", T("s11", "yüzde"), 0.3), ("error", T("s11", "yerine"), 0.2),
         ("chime", T("s11", "üç") + 0.6, 0.35), ("whoosh-short", T("s11", "Formülü") - 0.2, 0.3), ("pop", T("s11", "kıymete"), 0.25),
         ("pop", T("s11", "vergiye"), 0.25), ("pop", T("s11", "cezaya"), 0.25), ("pop", T("s11", "uzlaşmaya"), 0.25)],
    keys=dict(koc=T("s11", "Koçun"), ayni=T("s11", "Aynı"), once=T("s11", "önce"), yuzde=T("s11", "yüzde"), yani=T("s11", "Yani"),
              yerine=T("s11", "yerine"), uc=T("s11", "üç"), form=T("s11", "Formülü"), kiy=T("s11", "kıymete"), verg=T("s11", "vergiye"),
              cez=T("s11", "cezaya"), uzl=T("s11", "uzlaşmaya")),
    css=r"""
#s11 .top { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:24px; }
#s11 .top .kicker { font-size:26px; color:#FFE27A; }
#s11 .cmp { position:absolute; left:600px; top:250px; width:1220px; height:214px; display:flex; align-items:stretch; gap:22px; }
#s11 .cmp .side { flex:1; padding:18px 26px; position:relative; }
#s11 .cmp .side small { display:block; font:700 20px 'JetBrains Mono'; letter-spacing:.1em; }
#s11 .cmp .side b { display:block; font:900 28px/1.2 Montserrat; color:var(--fg); margin-top:6px; }
#s11 .cmp .side .v { display:flex; align-items:baseline; gap:12px; margin-top:12px; white-space:nowrap; }
#s11 .cmp .side .v span { font:700 30px 'JetBrains Mono'; color:var(--muted); }
#s11 .cmp .side .v strong { font-family:'Archivo Black'; font-size:62px; line-height:1; display:inline-block; }
#s11 .cmp .s1 small { color:#FF8A96; } #s11 .cmp .s1 .v strong { color:#FFB3BB; }
#s11 .cmp .s1 .sk { position:absolute; left:20px; bottom:58px; width:330px; height:6px; background:var(--uyari); border-radius:3px; transform-origin:left center; transform:rotate(-4deg); }
#s11 .cmp .s2 { border-color:var(--ok); background:rgba(46,212,122,.10); }
#s11 .cmp .s2 small { color:var(--ok); } #s11 .cmp .s2 .v strong { color:#DFFFEF; }
#s11 .cmp .arr { align-self:center; color:var(--fg); flex:none; }
#s11 .fm { position:absolute; left:600px; top:500px; width:1220px; height:350px; padding:26px 34px; border-radius:24px;
  background:linear-gradient(180deg, rgba(255,197,61,.14), rgba(255,197,61,.04)); border:4px solid var(--gold); }
#s11 .fm .kicker { color:var(--gold); }
#s11 .fm .row { display:flex; align-items:center; gap:18px; margin-top:22px; }
#s11 .fm .kf { width:220px; height:220px; border-radius:50%; flex:none; display:flex; flex-direction:column; align-items:center; justify-content:center;
  background:radial-gradient(circle at 35% 30%, #5B3FA8, #2A1A5E); box-shadow:inset 0 0 0 4px rgba(205,180,255,.6); color:#E2D3FF; }
#s11 .fm .kf b { font:900 26px/1.05 Montserrat; color:#fff; text-align:center; margin-top:4px; }
#s11 .fm .tiles { display:grid; grid-template-columns:repeat(2, 1fr); gap:16px; flex:1; }
#s11 .fm .tl { display:flex; align-items:center; gap:16px; height:102px; padding:0 22px; border-radius:18px; font:900 30px Montserrat; white-space:nowrap; }
#s11 .fm .tl .m { width:58px; height:58px; border-radius:50%; display:flex; align-items:center; justify-content:center; flex:none; }
#s11 .fm .tl small { font:700 20px 'JetBrains Mono'; margin-left:auto; letter-spacing:.06em; }
#s11 .fm .no { background:rgba(255,77,94,.13); border:3px solid var(--uyari); color:#FFE3E6; }
#s11 .fm .no .m { background:var(--uyari); color:#2a0a0e; } #s11 .fm .no small { color:#FF8A96; }
#s11 .fm .ok { background:rgba(46,212,122,.14); border:3px solid var(--ok); color:#DFFFEF; }
#s11 .fm .ok .m { background:var(--ok); color:#03221a; } #s11 .fm .ok small { color:var(--ok); }
""",
    body=f'''
<div class="top">{badge("ipucu", big=True)}<div class="kicker">KOÇUN NOTU · ÖNCE SEN BİLDİR</div></div>
<div class="cmp">
  <div class="side s1 card"><small>İDARE TESPİT EDERSE</small><b>Ceza: eksik vergi × 3</b><div class="v"><strong>34.560</strong><span>TL</span></div><i class="sk"></i></div>
  <div class="arr">{icon("arrow", 70)}</div>
  <div class="side s2 card"><small>FİRMA ÖNCE BİLDİRİRSE · GK 234/3</small><b>Ceza %10 nispetinde</b><div class="v"><strong class="cnt">0</strong><span>TL</span></div></div>
</div>
<div class="fm"><div class="kicker">AKILDA TUT · KÜLTÜR FONU FORMÜLÜ</div>
  <div class="row"><div class="kf">{icon("mask", 70)}<b>KÜLTÜR<br/>FONU</b></div>
    <div class="tiles">
      <div class="tl no t1"><span class="m">{icon("x", 32)}</span>Kıymete<small>GİRMEZ</small></div>
      <div class="tl ok t2"><span class="m">{icon("check", 32)}</span>Vergiye<small>ÖTV · KDV</small></div>
      <div class="tl no t3"><span class="m">{icon("x", 32)}</span>Cezaya<small>GİRMEZ</small></div>
      <div class="tl no t4"><span class="m">{icon("x", 32)}</span>Uzlaşmaya<small>GİRMEZ</small></div>
    </div></div>
</div>
''',
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 0.3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.5, ease: "back.out(2.4)" }, K.koc);
rise(".top .kicker", K.koc + 0.3, 0, 20);
slideX(".cmp .s1", K.ayni, -60);
tl.fromTo(q(".cmp .arr"), { x: -30, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: "power2.out" }, K.once);
slideX(".cmp .s2", K.once + 0.2, 60);
fadeTo(".cmp .s2 .v", 0.01, 0, 0.01);
pulse(".cmp .s2 b", K.yuzde, 1.08);
strike(".cmp .s1 .sk", K.yerine, 0.4);
fadeTo(".cmp .s1", K.yerine + 0.3, 0.55, 0.4);
fadeIn(".cmp .s2 .v", K.uc - 0.3, 0.2);
count(".cmp .s2 .cnt", K.uc - 0.3, 0, 3456, 0.9, 0);
pulse(".cmp .s2 .v strong", K.uc + 0.8, 1.15);
tl.fromTo(q(".fm"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }, K.form);
tl.fromTo(q(".fm .kf"), { rotation: -40, scale: 0.6 }, { rotation: 0, scale: 1, duration: 0.7, ease: "back.out(1.8)" }, K.form + 0.1);
pop(".fm .t1", K.kiy - 0.1);
pop(".fm .t2", K.verg - 0.1);
pop(".fm .t3", K.cez - 0.1);
pop(".fm .t4", K.uzl - 0.1);
"""
)

# ---------------------------------------------------------------- s12 Kapanış
S["s12"] = dict(
    exit=False,
    sfx=[("whoosh-short", 0.3, 0.25), ("impact-bass-1", T("s12", "D"), 0.4), ("pop", T("s12", "abone"), 0.35), ("pop", T("s12", "paylaşmayı"), 0.35),
         ("chime", T("s12", "sonraki"), 0.35)],
    keys=dict(oz=T("s12", "Özetle"), eks=T("s12", "Eksik"), ceza=T("s12", "ceza"), uzl=T("s12", "uzlaşmaya"), Dk=T("s12", "D"), kirk=T("s12", "kırk"),
              abone=T("s12", "abone"), pay=T("s12", "paylaşmayı"), bir=T("s12", "sonraki")),
    css=r"""
#s12 .right { position:absolute; left:860px; top:140px; width:960px; }
#s12 .sum { margin-top:18px; }
#s12 .row { display:flex; align-items:center; gap:22px; height:118px; padding:0 26px; margin-bottom:16px; }
#s12 .row .n { width:58px; height:58px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:28px; flex:none; }
#s12 .row .n1 { background:var(--teal); color:#03221a; } #s12 .row .n2 { background:var(--uyari); color:#2a0a0e; }
#s12 .row b { display:block; font:900 30px Montserrat; color:var(--fg); }
#s12 .row span { display:block; font:700 26px 'JetBrains Mono'; color:var(--muted); margin-top:4px; }
#s12 .arow { display:flex; align-items:center; gap:24px; margin-top:12px; }
#s12 .ans { display:flex; align-items:center; gap:26px; padding:22px 30px; border-radius:24px; background:rgba(46,212,122,.14); border:4px solid var(--ok);
  box-shadow:0 0 60px rgba(46,212,122,.25); width:max-content; }
#s12 .ans .L { width:96px; height:96px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:56px; }
#s12 .ans b { font-family:'Archivo Black'; font-size:76px; line-height:1; color:#DFFFEF; }
#s12 .ans small { font:800 30px Montserrat; color:var(--ok); margin-left:6px; }
#s12 .note { display:flex; align-items:center; gap:14px; padding:14px 18px; border-radius:16px; background:rgba(180,140,255,.12); border:2px dashed #B48CFF;
  font:800 22px/1.25 Montserrat; color:#E2D3FF; }
#s12 .note .ico { color:#B48CFF; flex:none; }
#s12 .note em { font-style:normal; color:#FF8A96; }
#s12 .cta { display:flex; gap:20px; margin-top:30px; }
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
  <div class="kicker">ÖZET · SORU 2</div>
  <div class="sum">
    <div class="row card r1"><span class="n n1">1</span><div><b>Eksik vergi (ÖTV + KDV)</b><span>3.600 + 7.920 = 11.520 TL</span></div></div>
    <div class="row card r2"><span class="n n2">2</span><div><b>Para cezası (3 kat)</b><span>11.520 × 3 = 34.560 TL</span></div></div>
  </div>
  <div class="arow"><div class="ans"><span class="L">D</span><b>46.080</b><small>TL</small></div>
    <div class="note">{icon("mask", 40)}<div>Kültür fonu 36.000 TL<br/><em>uzlaşma dışı</em></div></div></div>
  <div class="cta"><div class="btn sub">{icon("bell", 34)} ABONE OL</div><div class="btn shr">{icon("share", 34)} PAYLAŞ</div></div>
</div>
<div class="bye"><div class="lg"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div><span>Bir sonraki hesaplama dersinde görüşmek üzere!</span></div>
''',
    js=r"""
rise(".right .kicker", K.oz, 0, 20);
slideX(".sum .r1", K.eks, 80);
slideX(".sum .r2", K.ceza, 80);
tl.fromTo(q(".ans"), { scale: 2.2, opacity: 0, transformOrigin: "0% 50%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "expo.in" }, K.Dk - 0.3);
tl.fromTo(q(".ans"), { boxShadow: "0 0 20px rgba(46,212,122,.15)" }, { boxShadow: "0 0 80px rgba(46,212,122,.55)", duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 3 }, K.Dk + 0.5);
slideX(".arow .note", K.kirk + 0.8, 60);
pop(".cta .sub", K.abone, 0, "back.out(2.6)");
pop(".cta .shr", K.pay, 0, "back.out(2.6)");
tl.fromTo(q(".cta .sub .ico"), { rotation: 0 }, { rotation: 18, duration: 0.12, yoyo: true, repeat: 7, ease: "sine.inOut", transformOrigin: "50% 10%" }, K.abone + 0.4);
tl.fromTo(q(".bye"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }, K.bir);
"""
)
