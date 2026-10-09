"""Scenes 07-12: adım 3 (ceza + peşin ödeme), sonuç, tuzaklar, uyarı, koçun notu, kapanış."""
from lib import T, D, icon, badge
from scenes_a import steps, STEPS_CSS

S = {}

# ---------------------------------------------------------------- s07 Adım 3: ceza (GK 234/1-b) + peşin ödeme (KK 17/6)
KEYS = ["7", "8", "9", "÷", "4", "5", "6", "×", "1", "2", "3", "−", "0", ",", "=", "+"]
S["s07"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("impact-bass-1", T("s07", "katı"), 0.35), ("click-soft", T("s07", "Yüz", 2), 0.4),
         ("click-soft", T("s07", "çarpı"), 0.4), ("ping", T("s07", "elli") + 0.3, 0.35), ("notification", T("s07", "peşin"), 0.3),
         ("chime", T("s07", "dört") + 0.6, 0.35)],
    keys=dict(uc=T("s07", "Üçüncü"), iki=T("s07", "iki"), kat=T("s07", "katı"), yuz=T("s07", "Yüz", 2), carpi=T("s07", "çarpı"),
              elli=T("s07", "elli"), firma=T("s07", "Firma"), pes=T("s07", "peşin"), dortte=T("s07", "dörtte"), dort=T("s07", "dört")),
    css=STEPS_CSS + r"""
#s07 .law { position:absolute; left:600px; top:196px; width:1220px; height:136px; background:#F3F6FF; color:#0B1A44; border-radius:20px; padding:18px 30px;
  box-shadow:0 30px 70px rgba(0,0,0,.45); }
#s07 .law .lh { display:flex; align-items:center; gap:14px; font:900 22px Montserrat; letter-spacing:.06em; color:#1E3FBF; }
#s07 .law .lh .no { font:700 20px 'JetBrains Mono'; color:#fff; background:#1E3FBF; padding:3px 10px; border-radius:8px; }
#s07 .law .lt { font:600 32px/1.3 Montserrat; margin-top:10px; white-space:nowrap; }
#s07 .hl { position:relative; display:inline-block; }
#s07 .hl .mk { position:absolute; left:-6px; right:-6px; bottom:4px; height:20px; background:#FFC53D; opacity:.9; transform-origin:left center; border-radius:4px; z-index:0; }
#s07 .hl b { position:relative; z-index:1; font-weight:900; }
#s07 .calc { position:absolute; left:620px; top:356px; width:600px; height:520px; border-radius:36px; padding:26px 30px;
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
#s07 .x3 { position:absolute; left:1166px; top:330px; width:104px; height:104px; border-radius:50%; background:var(--uyari); color:#fff; display:flex; align-items:center;
  justify-content:center; font-family:'Archivo Black'; font-size:44px; box-shadow:0 0 0 10px rgba(255,77,94,.2), 0 16px 34px rgba(0,0,0,.45); }
#s07 .pes { position:absolute; left:1290px; top:356px; width:530px; height:520px; padding:22px 26px; }
#s07 .pes .ph { display:flex; align-items:center; gap:12px; font:900 22px Montserrat; letter-spacing:.06em; color:var(--ok); }
#s07 .pes .ref { font:700 17px 'JetBrains Mono'; color:var(--muted); margin-top:6px; }
#s07 .pes .cal { display:flex; align-items:center; gap:16px; margin-top:16px; }
#s07 .pes .cal .d { width:96px; height:96px; border-radius:18px; background:#F3F6FF; color:#0B1A44; display:flex; flex-direction:column; align-items:center; justify-content:center; flex:none; overflow:hidden; }
#s07 .pes .cal .d small { width:100%; text-align:center; background:var(--uyari); color:#fff; font:900 14px Montserrat; letter-spacing:.1em; padding:3px 0; }
#s07 .pes .cal .d b { font-family:'Archivo Black'; font-size:44px; line-height:1.15; }
#s07 .pes .cal p { font:700 22px/1.3 Montserrat; color:var(--fg); }
#s07 .q4 { display:flex; gap:6px; margin-top:20px; height:70px; }
#s07 .q4 i { flex:1; border-radius:10px; background:var(--uyari); display:flex; align-items:center; justify-content:center; font:900 20px 'JetBrains Mono'; color:#fff; font-style:normal; }
#s07 .q4 i.cut { background:repeating-linear-gradient(-45deg, rgba(46,212,122,.85) 0 10px, rgba(46,212,122,.35) 10px 20px); color:#03221a; }
#s07 .q4l { display:flex; justify-content:space-between; font:700 17px 'JetBrains Mono'; color:var(--muted); margin-top:6px; }
#s07 .pr { display:flex; align-items:baseline; gap:12px; margin-top:20px; white-space:nowrap; }
#s07 .pr .o { font:700 30px 'JetBrains Mono'; color:#7D88A8; text-decoration:line-through; text-decoration-color:var(--uyari); text-decoration-thickness:4px; }
#s07 .pr .n { font-family:'Archivo Black'; font-size:54px; color:#DFFFEF; line-height:1; display:inline-block; }
#s07 .pr small { font:800 24px Montserrat; color:var(--ok); }
""",
    body=f'''
{steps(3)}
<div class="law"><div class="lh">{icon("doc", 32)} GÜMRÜK KANUNU <span class="no">MADDE 234/1-(b)</span> · özet</div>
  <div class="lt">Kıymet noksanlığında <span class="hl"><i class="mk"></i><b>vergi farkının 3 katı para cezası</b></span></div></div>
<div class="calc"><div class="scr"><div class="ex"><span class="e1">185.000</span><span class="e2">185.000 × 3</span></div><div class="rs"><span class="cnt">0</span></div></div>
  <div class="keys">{"".join(f'<div class="k k{i}{" op" if k in "÷×−+" else " eq" if k == "=" else ""}">{k}</div>' for i, k in enumerate(KEYS))}</div></div>
<div class="x3">×3</div>
<div class="pes card"><div class="ph">{icon("check", 28)} PEŞİN ÖDEME İNDİRİMİ</div><div class="ref">Kabahatler Kanunu md. 17/6</div>
  <div class="cal"><div class="d"><small>GÜN</small><b>15</b></div><p>Ceza kararının tebliğinden itibaren 15 gün içinde peşin ödeme</p></div>
  <div class="q4"><i>¼</i><i>¼</i><i>¼</i><i class="cut">−¼</i></div><div class="q4l"><span>ödenen: ¾</span><span>indirim: ¼</span></div>
  <div class="pr"><span class="o">555.000</span><span class="n cnt2">0</span><small>TL</small></div></div>
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".law"), { y: -60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.uc);
pulse(".law .no", K.iki, 1.2);
strike(".hl .mk", K.kat - 0.4, 0.6);
tl.fromTo(q(".calc"), { y: 120, opacity: 0, rotation: -4 }, { y: 0, opacity: 1, rotation: 0, duration: 0.7, ease: "expo.out" }, K.uc + 0.3);
slam(".x3", K.kat);
fadeTo(".scr .e1, .scr .e2", 0.01, 0, 0.01);
// key presses: 1 8 5 0 0 0 → × 3 → =
const PRESS = [[8, K.yuz], [1, K.yuz + 0.15], [5, K.yuz + 0.3], [12, K.yuz + 0.45], [12, K.yuz + 0.6], [12, K.yuz + 0.75], [7, K.carpi], [10, K.carpi + 0.35], [14, K.elli - 0.5]];
PRESS.forEach(([i, at]) => {
  tl.fromTo(q(".k" + i), { y: 0, filter: "brightness(1)" }, { y: 5, filter: "brightness(1.6)", duration: 0.07, yoyo: true, repeat: 1, ease: "power1.out", immediateRender: false }, at);
});
fadeIn(".scr .e1", K.yuz + 0.1, 0.15);
fadeTo(".scr .e1", K.carpi - 0.05, 0, 0.1);
fadeIn(".scr .e2", K.carpi, 0.15);
count(".scr .cnt", K.elli - 0.6, 0, 555000, 1.0, 0);
pulse(".scr .rs", K.elli + 0.5, 1.08);
tl.fromTo(q(".pes"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.firma);
pop(".pes .cal .d", K.firma + 0.4, 0, "back.out(2.6)");
fadeTo(".q4, .q4l, .pr", 0.01, 0, 0.01);
fadeIn(".q4", K.pes, 0.3);
tl.fromTo(q(".q4 i.cut"), { scaleY: 1, opacity: 1 }, { scaleY: 0.82, opacity: 0.85, duration: 0.3, ease: "back.out(2)", immediateRender: false }, K.dortte);
fadeIn(".q4l", K.dortte + 0.2, 0.3);
fadeIn(".pr", K.dort - 0.4, 0.3);
count(".pr .cnt2", K.dort - 0.3, 0, 416250, 1.0, 0);
pulse(".pr .n", K.dort + 0.9, 1.12);
"""
)

# ---------------------------------------------------------------- s08 Sonuç
OPTS = [("A", "185.000"), ("B", "568.750"), ("C", "601.250"), ("D", "662.818"), ("E", "740.000")]
S["s08"] = dict(
    sfx=[("whoosh-short", 0.3, 0.25), ("click-soft", T("s08", "yüz"), 0.4), ("click-soft", T("s08", "artı"), 0.4), ("riser", T("s08", "Ödenecek") - 0.6, 0.3),
         ("impact-bass-1", T("s08", "altı") + 0.9, 0.4), ("chime", T("s08", "C"), 0.45)],
    keys=dict(son=T("s08", "sonuç"), yuz=T("s08", "yüz"), arti=T("s08", "artı"), od=T("s08", "Ödenecek"), alti=T("s08", "altı"),
              dogru=T("s08", "Doğru"), A=T("s08", "C")),
    css=STEPS_CSS + r"""
#s08 .rcp { position:absolute; left:600px; top:236px; width:620px; height:600px; background:#FBF8EE; color:#1B2A57; padding:26px 38px;
  box-shadow:0 30px 70px rgba(0,0,0,.45); clip-path:polygon(0 0,100% 0,100% 96%,95% 100%,90% 96%,85% 100%,80% 96%,75% 100%,70% 96%,65% 100%,60% 96%,55% 100%,50% 96%,45% 100%,40% 96%,35% 100%,30% 96%,25% 100%,20% 96%,15% 100%,10% 96%,5% 100%,0 96%); }
#s08 .rcp .rh { text-align:center; font-family:'Archivo Black'; font-size:36px; letter-spacing:.04em; }
#s08 .rcp .rs { text-align:center; font:700 18px 'JetBrains Mono'; color:#5A6AA0; letter-spacing:.14em; margin-top:4px; padding-bottom:14px; border-bottom:3px dashed #9BA8CC; }
#s08 .rcp .ln { position:relative; display:flex; justify-content:space-between; align-items:baseline; margin-top:22px; font:800 30px Montserrat; }
#s08 .rcp .ln b { font:700 38px 'JetBrains Mono'; }
#s08 .rcp .ln small { display:block; font:600 19px 'JetBrains Mono'; color:#5A6AA0; }
#s08 .rcp .ln b s { font-size:24px; color:#7D88A8; text-decoration-color:#B4231B; text-decoration-thickness:3px; margin-right:8px; }
#s08 .rcp .lx { font-size:24px; color:#7D88A8; }
#s08 .rcp .lx b { font-size:28px; color:#7D88A8; }
#s08 .rcp .lx .tg { position:absolute; left:150px; top:2px; font:900 15px Montserrat; letter-spacing:.08em; color:#B4231B; border:2px solid #B4231B; border-radius:6px; padding:1px 8px; }
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
#s08 .burst { position:absolute; left:1300px; top:452px; width:1px; height:1px; }
#s08 .burst i { position:absolute; left:0; top:0; width:14px; height:14px; border-radius:3px; opacity:0; }
""",
    body=f'''
{steps(4)}
<div class="rcp"><div class="rh">ÖDEME HESABI</div><div class="rs">SORU 3 · TL · PEŞİN ÖDEME</div>
  <div class="ln l1"><span>Eksik vergi<small>GV 50.000 + KDV 135.000</small></span><b>185.000</b></div>
  <div class="ln l2"><span>Para cezası<small>3 kat · ¾ peşin ödeme</small></span><b><s>555.000</s>416.250</b></div>
  <div class="ln lx"><span>2021 yılı<small>3 yıl doldu</small></span><b>—</b><em class="tg">ZAMANAŞIMI</em></div>
  <div class="eq"><div class="tot"><span>TOPLAM ÖDEME</span><b class="cnt">0</b></div><div class="usd">Türk lirası</div></div>
</div>
<div class="ans">{"".join(f'<div class="ao card a{L}"><span class="L">{L}</span><span class="v">{v}</span><span class="ck">{icon("check", 34)}</span></div>' for L, v in OPTS)}</div>
<div class="stamp">CEVAP: C</div>
<div class="burst">{"".join(f'<i style="background:{c}"></i>' for c in ["#FFC53D", "#33D9B2", "#8FB2FF", "#FF4D5E", "#2ED47A"] * 4)}</div>
''',
    js=r"""
rise(".steps", 0.15, 0, -30);
tl.fromTo(q(".rcp"), { y: -200, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, ease: "expo.out" }, K.son);
fadeTo(".rcp .ln, .rcp .eq", 0.01, 0, 0.01);
rise(".rcp .l1", K.yuz, 0, 20);
rise(".rcp .l2", K.arti, 0, 20);
rise(".rcp .lx", K.od - 0.9, 0, 20);
rise(".rcp .eq", K.od, 0, 20);
count(".rcp .cnt", K.alti - 0.1, 0, 601250, 1.1, 0);
pulse(".rcp .tot b", K.alti + 1.1, 1.12);
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
         ("error", T("s09", "E"), 0.25), ("pop", T("s09", "E") + 1.6, 0.3)],
    keys=dict(tz=T("s09", "tuzaklara"), cez=T("s09", "Cezayı"), A=T("s09", "A"), kdv=T("s09", "KDV"), B=T("s09", "B"),
              zam=T("s09", "Zamanaşımını"), Dk=T("s09", "D"), pes=T("s09", "Peşin"), E=T("s09", "E")),
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
  <div class="th"><span class="L">A</span><b>185.000 TL</b></div>
  <div class="why">Cezayı unuttu, sadece vergi</div>
  <div class="ln l1"><span>GV + KDV: 50.000 + 135.000</span><b>185.000</b></div>
  <div class="ln miss l2"><span>Ceza</span><b>— ?</b></div>
  <div class="sum"><span>Toplam</span><b>185.000</b></div>
</div>
<div class="tc tB card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">B</span><b>568.750 TL</b></div>
  <div class="why">GV'yi KDV matrahına eklemedi</div>
  <div class="ln l1"><span>KDV: 625.000 × %20</span><b>125.000</b></div>
  <div class="ln l2"><span>Vergi 175.000 + ceza ¾</span><b>393.750</b></div>
  <div class="sum"><span>Toplam</span><b>568.750</b></div>
</div>
<div class="tc tD card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">D</span><b>662.818 TL</b></div>
  <div class="why">Zamanaşımını unuttu, 2021'i de kattı</div>
  <div class="ln l1"><span>Kıymet 689.000 → vergi</span><b>203.944</b></div>
  <div class="ln l2"><span>Ceza 3 kat × ¾</span><b>458.874</b></div>
  <div class="sum"><span>Toplam</span><b>662.818</b></div>
</div>
<div class="tc tE card"><div class="x">{icon("x", 32)}</div>
  <div class="th"><span class="L">E</span><b>740.000 TL</b></div>
  <div class="why">Peşin ödeme indirimini unuttu</div>
  <div class="ln l1"><span>Vergi</span><b>185.000</b></div>
  <div class="ln l2"><span>Ceza 3 kat (tam)</span><b>555.000</b></div>
  <div class="sum"><span>Toplam</span><b>740.000</b></div>
</div>
<img class="baba" src="assets/img/baba-crop.png" alt="Gümrükçü Baba" />
<div class="bub">Doğrusu <em>C: 601.250 TL!</em></div>
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
card("B", K.kdv, K.kdv + 1.2, K.B);
card("D", K.zam, K.zam + 1.2, K.Dk);
card("E", K.pes, K.pes + 1.2, K.E);
tl.fromTo(q(".bub"), { scale: 0.3, opacity: 0, transformOrigin: "60% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.E + 1.6);
"""
)

# ---------------------------------------------------------------- s10 Uyarı: lisans ücreti şartları + indirim yalnız cezaya
S["s10"] = dict(
    sfx=[("notification", T("s10", "uyarı"), 0.35), ("pop", T("s10", "ilgiliyse"), 0.3), ("pop", T("s10", "koşulu"), 0.3), ("chime", T("s10", "eklenir"), 0.3),
         ("whoosh-short", T("s10", "Bir", 2) - 0.1, 0.3), ("impact-bass-1", T("s10", "yoktur"), 0.35)],
    keys=dict(uy=T("s10", "uyarı"), her=T("s10", "Her"), gk=T("s10", "Gümrük"), ilg=T("s10", "ilgiliyse"), kos=T("s10", "koşulu"),
              ekl=T("s10", "eklenir"), bir=T("s10", "Bir", 2), cez=T("s10", "cezaya"), verg=T("s10", "vergiye"), yok=T("s10", "yoktur")),
    css=r"""
#s10 .top { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:24px; }
#s10 .top .kicker { font-size:26px; color:#FF8A96; }
#s10 .law { position:absolute; left:600px; top:254px; width:900px; height:330px; padding:20px 26px; }
#s10 .law .lh { display:flex; align-items:center; gap:14px; font:900 22px Montserrat; letter-spacing:.06em; color:var(--accent2); }
#s10 .law .lh .no { font:700 20px 'JetBrains Mono'; color:#071A45; background:var(--accent2); padding:3px 10px; border-radius:8px; }
#s10 .cond { display:flex; align-items:center; gap:16px; margin-top:16px; padding:14px 18px; border-radius:16px; background:rgba(46,212,122,.10); border:2px solid rgba(46,212,122,.55); }
#s10 .cond .n { width:46px; height:46px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center; flex:none; }
#s10 .cond span { font:800 26px/1.2 Montserrat; color:var(--fg); }
#s10 .res { display:flex; align-items:center; gap:14px; margin-top:16px; font:900 26px Montserrat; color:var(--teal); }
#s10 .res b { color:#03221a; background:var(--teal); padding:6px 14px; border-radius:10px; }
#s10 .ind { position:absolute; left:600px; top:604px; width:1220px; height:280px; padding:20px 26px; }
#s10 .ind .lh { font:900 22px Montserrat; letter-spacing:.06em; color:var(--ok); display:flex; align-items:center; gap:12px; }
#s10 .ind .two { display:flex; gap:20px; margin-top:16px; }
#s10 .ind .pl { flex:1; display:flex; align-items:center; gap:18px; padding:18px 22px; border-radius:18px; }
#s10 .ind .pl .k { font:900 28px Montserrat; }
#s10 .ind .pl .v { font:700 34px 'JetBrains Mono'; margin-left:auto; white-space:nowrap; }
#s10 .ind .pv { background:rgba(255,77,94,.12); border:3px solid var(--uyari); color:#FFE3E6; }
#s10 .ind .pv .tg { font:900 18px Montserrat; color:#2a0a0e; background:var(--uyari); padding:4px 10px; border-radius:8px; }
#s10 .ind .pc { background:rgba(46,212,122,.12); border:3px solid var(--ok); color:#DFFFEF; }
#s10 .ind .pc .tg { font:900 18px Montserrat; color:#03221a; background:var(--ok); padding:4px 10px; border-radius:8px; }
#s10 .cano { position:absolute; left:1572px; top:250px; height:340px; filter:drop-shadow(0 18px 30px rgba(0,0,0,.45)); }
#s10 .bub { position:absolute; left:1530px; top:136px; width:290px; padding:12px 16px; background:#F4F7FF; color:#0B1A44; border-radius:20px; font:900 22px/1.25 Montserrat; }
#s10 .bub:after { content:""; position:absolute; left:120px; bottom:-20px; border:11px solid transparent; border-top:13px solid #F4F7FF; }
#s10 .bub em { font-style:normal; color:#6B3FD6; }
#s10 .hayir { position:absolute; left:1556px; top:470px; padding:8px 20px; border:6px solid var(--uyari); border-radius:14px; color:var(--uyari);
  font-family:'Archivo Black'; font-size:46px; line-height:1; background:rgba(7,26,69,.92); transform:rotate(-8deg); }
""",
    body=f'''
<div class="top">{badge("uyari", big=True)}<div class="kicker">KIYMETE GİRİŞİN ŞARTLARI</div></div>
<div class="law card"><div class="lh">{icon("doc", 32)} GÜMRÜK KANUNU <span class="no">MADDE 27/1-(c)</span> · iki şart birlikte</div>
  <div class="cond c1"><span class="n">{icon("check", 28)}</span><span>Lisans ücreti <b>ithal eşyasıyla ilgili</b></span></div>
  <div class="cond c2"><span class="n">{icon("check", 28)}</span><span>Alıcı tarafından <b>satış koşulu olarak</b> ödeniyor</span></div>
  <div class="res">{icon("arrow", 30)} <b>GÜMRÜK KIYMETİNE EKLE</b></div></div>
<div class="ind card"><div class="lh">{icon("check", 26)} PEŞİN ÖDEME İNDİRİMİ NEYE UYGULANIR?</div>
  <div class="two"><div class="pl pv"><span class="k">Vergi</span><span class="tg">İNDİRİM YOK</span><span class="v">185.000</span></div>
    <div class="pl pc"><span class="k">Ceza</span><span class="tg">¾ ÖDENİR</span><span class="v">555.000 → 416.250</span></div></div></div>
<img class="cano" src="assets/img/cano-cut.png" alt="M firması temsilcisi" />
<div class="bub">Vergiye de <em>indirim var mı?</em></div>
<div class="hayir">HAYIR!</div>
''',
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 2.4, opacity: 0, rotation: -8 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, K.uy);
rise(".top .kicker", K.uy + 0.45, 0, 20);
tl.fromTo(q(".law"), { x: -80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.gk);
slideX(".cond.c1", K.ilg - 0.3, -50);
slideX(".cond.c2", K.kos - 0.3, -50);
fadeTo(".law .res", 0.01, 0, 0.01);
pop(".law .res", K.ekl, 0, "back.out(2.4)");
tl.fromTo(q(".cano"), { x: 300, opacity: 0 }, { x: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }, K.her);
tl.fromTo(q(".bub"), { scale: 0.3, opacity: 0, transformOrigin: "40% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.bir);
tl.fromTo(q(".ind"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }, K.bir + 0.2);
fadeTo(".ind .pl", 0.01, 0, 0.01);
pop(".ind .pc", K.cez - 0.2);
pop(".ind .pv", K.verg - 0.2);
tl.fromTo(q(".ind .pv"), { x: 0 }, { x: 10, duration: 0.07, yoyo: true, repeat: 5, ease: "none", immediateRender: false }, K.yok);
slam(".hayir", K.yok);
"""
)

# ---------------------------------------------------------------- s11 Koçun notu
CHAIN = [("Süreyi kontrol et", "clock"), ("Kıymete ekle", "doc"), ("Vergiyi hesapla", "calc"), ("Cezayı üçle", "x"), ("¾'ünü öde", "check")]
S["s11"] = dict(
    sfx=[("pop", T("s11", "Koçun"), 0.35), ("ping", T("s11", "tescil"), 0.3), ("error", T("s11", "değil"), 0.2), ("pop", T("s11", "itiraz"), 0.3),
         ("whoosh-short", T("s11", "Formülü") - 0.2, 0.3), ("pop", T("s11", "Süreyi"), 0.25), ("pop", T("s11", "kıymete"), 0.25),
         ("pop", T("s11", "vergiyi"), 0.25), ("pop", T("s11", "cezayı"), 0.25), ("chime", T("s11", "dörtte"), 0.3)],
    keys=dict(koc=T("s11", "Koçun"), zam=T("s11", "Zamanaşımı"), tes=T("s11", "tescil"), od=T("s11", "Ödeme"), deg=T("s11", "değil"),
              bir=T("s11", "Bir"), itr=T("s11", "itiraz"), form=T("s11", "Formülü"), c1=T("s11", "Süreyi"), c2=T("s11", "kıymete"),
              c3=T("s11", "vergiyi"), c4=T("s11", "cezayı"), c5=T("s11", "dörtte")),
    css=r"""
#s11 .top { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:24px; }
#s11 .top .kicker { font-size:26px; color:#FFE27A; }
#s11 .st { position:absolute; left:600px; top:250px; width:780px; height:330px; padding:20px 26px; }
#s11 .st .lh { font:900 22px Montserrat; letter-spacing:.06em; color:var(--gold); display:flex; align-items:center; gap:12px; }
#s11 .opt { display:flex; align-items:center; gap:16px; margin-top:14px; padding:14px 18px; border-radius:16px; }
#s11 .opt .m { width:46px; height:46px; border-radius:50%; display:flex; align-items:center; justify-content:center; flex:none; }
#s11 .opt b { font:900 27px Montserrat; }
#s11 .opt small { margin-left:auto; font:700 18px 'JetBrains Mono'; letter-spacing:.06em; }
#s11 .opt.ok { background:rgba(46,212,122,.14); border:3px solid var(--ok); color:#DFFFEF; } #s11 .opt.ok .m { background:var(--ok); color:#03221a; } #s11 .opt.ok small { color:var(--ok); }
#s11 .opt.no { background:rgba(255,77,94,.10); border:2px solid rgba(255,77,94,.5); color:#C9D3F2; } #s11 .opt.no .m { background:var(--uyari); color:#2a0a0e; } #s11 .opt.no small { color:#FF8A96; }
#s11 .it { position:absolute; left:1400px; top:250px; width:420px; height:330px; padding:22px 24px; display:flex; flex-direction:column; }
#s11 .it .lh { font:900 22px Montserrat; letter-spacing:.06em; color:var(--accent2); }
#s11 .it .big { font-family:'Archivo Black'; font-size:44px; line-height:1.1; color:var(--fg); margin-top:16px; }
#s11 .it .big em { font-style:normal; color:var(--teal); }
#s11 .it p { font:700 21px/1.3 Montserrat; color:#C9D3F2; margin-top:12px; }
#s11 .it .ref { margin-top:auto; font:700 17px 'JetBrains Mono'; color:var(--muted); }
#s11 .fm { position:absolute; left:600px; top:604px; width:1220px; height:270px; padding:24px 30px; border-radius:24px;
  background:linear-gradient(180deg, rgba(255,197,61,.14), rgba(255,197,61,.04)); border:4px solid var(--gold); }
#s11 .fm .kicker { color:var(--gold); }
#s11 .chain { display:flex; align-items:center; gap:10px; margin-top:26px; }
#s11 .ch { flex:1; height:132px; border-radius:18px; background:rgba(255,255,255,.07); border:2px solid rgba(255,255,255,.25); display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:10px; text-align:center; }
#s11 .ch .n { width:44px; height:44px; border-radius:50%; background:var(--gold); color:#2a1d00; display:flex; align-items:center; justify-content:center; }
#s11 .ch b { font:900 22px/1.15 Montserrat; color:var(--fg); }
#s11 .ar { color:var(--gold); flex:none; }
""",
    body=f'''
<div class="top">{badge("ipucu", big=True)}<div class="kicker">KOÇUN NOTU</div></div>
<div class="st card"><div class="lh">{icon("clock", 28)} ZAMANAŞIMI NEREDEN BAŞLAR?</div>
  <div class="opt ok o1"><span class="m">{icon("check", 26)}</span><b>Beyannamenin tescil tarihi</b><small>YÜKÜMLÜLÜK DOĞAR</small></div>
  <div class="opt no o2"><span class="m">{icon("x", 26)}</span><b>Lisans ücretinin ödeme tarihi</b><small>DEĞİL</small></div>
  <div class="opt no o3"><span class="m">{icon("x", 26)}</span><b>Sonradan kontrol tarihi</b><small>DEĞİL</small></div></div>
<div class="it card"><div class="lh">PEŞİN ÖDEME</div><div class="big">İtiraz hakkı <em>saklı</em></div>
  <p>Cezayı 15 gün içinde peşin ödemek, karara karşı kanun yoluna başvurma hakkını ortadan kaldırmaz.</p><div class="ref">Kabahatler K. md. 17/6</div></div>
<div class="fm"><div class="kicker">AKILDA TUT · 5 ADIMLI FORMÜL</div>
  <div class="chain">{f'<span class="ar">{icon("arrow", 34)}</span>'.join(f'<div class="ch c{k + 1}"><span class="n">{icon(ic, 24)}</span><b>{t}</b></div>' for k, (t, ic) in enumerate(CHAIN))}</div></div>
''',
    js=r"""
tl.fromTo(q(".top .badge"), { scale: 0.3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.5, ease: "back.out(2.4)" }, K.koc);
rise(".top .kicker", K.koc + 0.3, 0, 20);
tl.fromTo(q(".st"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.zam);
fadeTo(".st .opt", 0.01, 0, 0.01);
pop(".st .o1", K.tes - 0.2);
pop(".st .o2, .st .o3", K.od, 0.25);
tl.fromTo(q(".st .opt.no"), { x: 0 }, { x: 8, duration: 0.07, yoyo: true, repeat: 5, ease: "none", immediateRender: false }, K.deg);
tl.fromTo(q(".it"), { x: 60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.bir);
pulse(".it .big em", K.itr + 0.3, 1.15);
tl.fromTo(q(".fm"), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }, K.form);
fadeTo(".chain .ch, .chain .ar", 0.01, 0, 0.01);
["c1", "c2", "c3", "c4", "c5"].forEach((c, i) => {
  pop(".chain ." + c, K[c] - 0.1);
  if (i) fadeIn(".chain .ar:nth-of-type(" + i + ")", K[c] - 0.2, 0.2);
});
"""
)

# ---------------------------------------------------------------- s12 Kapanış
S["s12"] = dict(
    exit=False,
    sfx=[("whoosh-short", 0.3, 0.25), ("impact-bass-1", T("s12", "C"), 0.4), ("pop", T("s12", "abone"), 0.35), ("pop", T("s12", "paylaşmayı"), 0.35),
         ("chime", T("s12", "sonraki"), 0.35)],
    keys=dict(oz=T("s12", "Özetle"), zam=T("s12", "Zamanaşımı"), eks=T("s12", "eksik"), ind=T("s12", "indirimli"), C=T("s12", "C"),
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
#s12 .note { display:flex; align-items:center; gap:14px; padding:14px 18px; border-radius:16px; background:rgba(255,197,61,.12); border:2px dashed var(--gold);
  font:800 22px/1.25 Montserrat; color:#FFE9B0; }
#s12 .note .ico { color:var(--gold); flex:none; }
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
  <div class="kicker">ÖZET · SORU 3</div>
  <div class="sum">
    <div class="row card r1"><span class="n n1">1</span><div><b>Eksik vergi (2022 + 2023)</b><span>50.000 + 135.000 = 185.000 TL</span></div></div>
    <div class="row card r2"><span class="n n2">2</span><div><b>Ceza: 3 kat, ¾ peşin ödeme</b><span>555.000 × ¾ = 416.250 TL</span></div></div>
  </div>
  <div class="arow"><div class="ans"><span class="L">C</span><b>601.250</b><small>TL</small></div>
    <div class="note">{icon("clock", 40)}<div>2021: 3 yıl doldu<br/><em>zamanaşımı</em></div></div></div>
  <div class="cta"><div class="btn sub">{icon("bell", 34)} ABONE OL</div><div class="btn shr">{icon("share", 34)} PAYLAŞ</div></div>
</div>
<div class="bye"><div class="lg"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div><span>Bir sonraki hesaplama dersinde görüşmek üzere!</span></div>
''',
    js=r"""
rise(".right .kicker", K.oz, 0, 20);
slideX(".arow .note", K.zam, 60);
slideX(".sum .r1", K.eks, 80);
slideX(".sum .r2", K.ind, 80);
tl.fromTo(q(".ans"), { scale: 2.2, opacity: 0, transformOrigin: "0% 50%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "expo.in" }, K.C - 0.3);
tl.fromTo(q(".ans"), { boxShadow: "0 0 20px rgba(46,212,122,.15)" }, { boxShadow: "0 0 80px rgba(46,212,122,.55)", duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 3 }, K.C + 0.5);
pop(".cta .sub", K.abone, 0, "back.out(2.6)");
pop(".cta .shr", K.pay, 0, "back.out(2.6)");
tl.fromTo(q(".cta .sub .ico"), { rotation: 0 }, { rotation: 18, duration: 0.12, yoyo: true, repeat: 7, ease: "sine.inOut", transformOrigin: "50% 10%" }, K.abone + 0.4);
tl.fromTo(q(".bye"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }, K.bir);
"""
)
