"""Scenes 11-15."""
from lib import T, D, icon, badge, odu, idu, valve
from scenes_b import crit

S = {}

# ---------------------------------------------------------------- s11 Kriter 4: Haberleşme + adresleme
_k4_x = (40, 320, 600, 880)
_k4 = (
    '<svg viewBox="0 0 1080 440" width="1080" height="440">'
    + '<g transform="translate(0 10)"><g class="ctl"><rect width="220" height="96" rx="16" fill="#0E1C46" stroke="#33D9B2" stroke-width="3"/>'
      '<rect x="16" y="18" width="78" height="44" rx="8" fill="#33D9B2" opacity=".85"/><text x="106" y="44" class="svgs" fill="#BFF5E6">Merkezi</text><text x="106" y="70" class="svgs" fill="#BFF5E6">kumanda</text></g></g>'
    + odu(455, 0, w=170, h=110)
    + '<g transform="translate(430 178)"><g class="bs"><rect width="220" height="70" rx="14" fill="#2A1F55" stroke="#C9A7FF" stroke-width="3"/>'
      '<text x="110" y="30" text-anchor="middle" class="svgs" fill="#E6D8FF">Mod seçim /</text><text x="110" y="54" text-anchor="middle" class="svgs" fill="#E6D8FF">dağıtım kutusu</text></g></g>'
    + '<path class="pp" d="M530 110 V 178" fill="none" stroke="#5E7FD0" stroke-width="8" stroke-linecap="round"/>'
    + "".join(f'<path class="pp" d="M540 248 C 540 290, {x + 90} 280, {x + 90} 336" fill="none" stroke="#5E7FD0" stroke-width="7" stroke-linecap="round"/>' for x in _k4_x)
    + '<path class="dl" d="M220 50 H 455" fill="none" stroke="#4FC3F7" stroke-width="4" stroke-dasharray="6 10"/>'
    + '<path class="dl" d="M560 110 V 178" fill="none" stroke="#4FC3F7" stroke-width="4" stroke-dasharray="6 10"/>'
    + "".join(f'<path class="dl" d="M560 248 C 560 300, {x + 110} 290, {x + 110} 336" fill="none" stroke="#4FC3F7" stroke-width="4" stroke-dasharray="6 10"/>' for x in _k4_x)
    + "".join(idu(x, 340, w=180, h=54) for x in _k4_x)
    + "".join(f'<g transform="translate({x + 90} 416)"><g class="adr"><rect x="-56" y="-20" width="112" height="38" rx="19" fill="#33D9B2"/><text y="7" text-anchor="middle" class="svga">ID: 0{i + 1}</text></g></g>' for i, x in enumerate(_k4_x))
    + "</svg>"
)
sid, d = crit(
    4, "Haberleşme ve adresleme", "Dış ünite, iç üniteler ve mod seçim kutuları arasında veri akışı",
    "İç üniteler sistem tarafından ayrı ayrı tanınabiliyor mu?", "", _k4,
    r"""
fadeIn(".dg .odu", K.dis);
draw(".dg .pp", K.ic, 0.8);
pop(".dg .idu", K.ic + 0.3, 0.1);
pop(".dg .bs", K.mod);
tl.fromTo(q(".dg .ctl"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.5, ease: "expo.out" }, K.veri - 0.5);
fadeIn(".dg .dl", K.veri, 0.4);
flow(".dg .dl", K.veri, D, 90);
tl.fromTo(q(".dg .idu .led"), { opacity: 1 }, { opacity: 0.2, duration: 0.18, yoyo: true, repeat: 9, stagger: 0.07 }, K.veri + 0.2);
pop(".dg .adr", K.ayri, 0.15);
tl.fromTo(q(".dg .adr"), { y: 0 }, { y: -8, duration: 0.2, yoyo: true, repeat: 1, stagger: 0.15 }, K.ayri + 0.9);
spinFans(0, D, 1.1);
""",
    dict(dis=T("s11", "dış"), ic=T("s11", "iç"), mod=T("s11", "mod"), veri=T("s11", "veri"), ayri=T("s11", "ayrı"),
         _q=T("s11", "iç", 2, off=-0.3), _ok=T("s11", "ortak")),
    [("pop", T("s11", "ayrı"), 0.3), ("ping", T("s11", "ortak"), 0.25)],
)
S[sid] = d

# ---------------------------------------------------------------- s12 BTB uyarı
S["s12"] = dict(
    sfx=[("impact-bass-1", T("s12", "şimdi") + 0.2, 0.4), ("riser", T("s12", "kriterler") - 0.4, 0.15),
         ("impact-bass-1", T("s12", "iptal") + 0.15, 0.45)],
    keys=dict(simdi=T("s12", "şimdi"), yaziya=T("s12", "yazıya"), gecmis=T("s12", "geçmiş"), bag=T("s12", "bağlayıcı"),
              kriterler=T("s12", "kriterler"), degerl=T("s12", "değerlendirilecek"), gerekli=T("s12", "gerekli"),
              btbler=T("s12", "btb'ler"), mevzuat=T("s12", "mevzuat"), iptal=T("s12", "iptal")),
    css=r"""
#s12 .bdg { position:absolute; left:600px; top:128px; }
#s12 .h1 { position:absolute; left:600px; top:246px; margin:0; width:1220px; font-size:50px; white-space:nowrap; }
#s12 .belt { position:absolute; left:600px; top:488px; width:1220px; height:12px; border-radius:6px; background:repeating-linear-gradient(90deg,#2B4C9E 0 30px,#1A3170 30px 60px); }
#s12 .btb { position:absolute; top:342px; width:250px; height:300px; background:#F3F6FF; color:#0B1A44; border-radius:16px; padding:20px 22px; box-shadow:0 22px 50px rgba(0,0,0,.45); }
#s12 .b1 { left:610px; } #s12 .b2 { left:920px; } #s12 .b3 { left:1230px; } #s12 .b4 { left:1540px; }
#s12 .btb .t { font-family:'Archivo Black'; font-size:46px; color:#1E3FBF; }
#s12 .btb .s { font:700 18px Montserrat; color:#3B4E86; margin-top:2px; }
#s12 .btb .y { font:700 18px 'JetBrains Mono'; color:#5A6AA0; margin-top:14px; letter-spacing:.08em; }
#s12 .btb i { display:block; height:10px; border-radius:5px; background:#D2DBF3; margin-top:14px; }
#s12 .btb i:nth-of-type(2) { width:80%; } #s12 .btb i:nth-of-type(3) { width:60%; }
#s12 .ok { position:absolute; left:28px; bottom:22px; display:flex; align-items:center; gap:8px; font:900 22px Montserrat; color:#06221a; background:var(--ok); padding:8px 14px; border-radius:10px; }
#s12 .stamp { position:absolute; left:16px; top:120px; width:218px; text-align:center; font-family:'Archivo Black'; font-size:54px; color:var(--uyari);
  border:6px solid var(--uyari); border-radius:12px; transform:rotate(-14deg); background:rgba(243,246,255,.85); }
#s12 .beam { position:absolute; left:560px; top:322px; width:120px; height:380px; border-radius:20px;
  background:linear-gradient(90deg, rgba(51,217,178,0), rgba(51,217,178,.55), rgba(51,217,178,0)); }
#s12 .beamlab { position:absolute; left:600px; top:702px; font:700 24px 'JetBrains Mono'; letter-spacing:.14em; color:var(--vrf); }
#s12 .note { position:absolute; left:600px; top:774px; width:1220px; display:flex; align-items:center; gap:18px; padding:18px 26px; border-color:var(--uyari) !important; }
#s12 .note .ico { color:var(--uyari); }
#s12 .note .t { font:700 30px/1.25 Montserrat; color:var(--fg); }
#s12 .note .t b { color:var(--uyari); }
""",
    body=r"""
<div class="bdg">BADGE</div>
<div class="h1">Geçmiş BTB'ler yeniden değerlendirilecek</div>
<div class="belt"></div>
<div class="beam"></div>
CARDS
<div class="beamlab">▶ 4 KRİTER KONTROLÜ</div>
<div class="note card">WARN<div class="t">Şartları taşımadığı tespit edilen BTB'ler, mevzuat hükümleri çerçevesinde <b>iptal edilecek.</b></div></div>
""".replace("BADGE", badge("uyari", big=True)).replace("WARN", icon("warn", 56))
    .replace("CARDS", "".join(
        f'<div class="btb b{i}"><div class="t">BTB</div><div class="s">Bağlayıcı Tarife Bilgisi</div><div class="y">GEÇMİŞ YIL · #{i}</div><i></i><i></i><i></i>'
        + (f'<div class="ok">{icon("check", 24)} UYGUN</div>' if i in (1, 3) else '<div class="stamp">İPTAL</div>')
        + "</div>" for i in range(1, 5))),
    js=r"""
slam(".bdg .badge", K.simdi);
tl.fromTo(q(".bdg .badge"), { x: 0 }, { x: 6, duration: 0.06, yoyo: true, repeat: 9, ease: "none" }, K.simdi + 0.5);
tl.fromTo(q(".h1"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.yaziya - 0.2);
strike(".belt", K.gecmis - 0.3, 0.6);
tl.fromTo(q(".btb"), { x: -260, opacity: 0, rotation: -4 }, { x: 0, opacity: 1, rotation: 0, duration: 0.6, ease: "power3.out", stagger: 0.18 }, K.gecmis);
tl.fromTo(q(".beam"), { x: 0, opacity: 0 }, { x: 1180, opacity: 1, duration: K.degerl + 0.8 - K.kriterler, ease: "power1.inOut" }, K.kriterler);
tl.to(q(".beam"), { opacity: 0, duration: 0.3 }, K.degerl + 0.8);
fadeIn(".beamlab", K.kriterler, 0.3);
q(".btb").forEach((b, i) => {
  const at = K.kriterler + (i + 0.6) * (K.degerl + 0.8 - K.kriterler) / 4.4;
  tl.fromTo(b, { y: 0 }, { y: -18, duration: 0.22, yoyo: true, repeat: 1, ease: "sine.inOut" }, at);
});
tl.to(q(".beamlab"), { opacity: 0, duration: 0.3 }, K.gerekli);
pop(".b1 .ok, .b3 .ok", K.gerekli, 0.2);
tl.to(q(".b2, .b4"), { y: 14, duration: 0.3, ease: "power2.out" }, K.btbler);
slam(".b2 .stamp", K.iptal - 0.3);
slam(".b4 .stamp", K.iptal - 0.05);
tl.to(q(".b2, .b4"), { opacity: 0.8, duration: 0.3 }, K.iptal + 0.4);
rise(".note", K.mevzuat - 0.2, 0, 30);
""",
)

# ---------------------------------------------------------------- s13 Koçun tavsiyesi
DOCS = [("Teknik katalog", "teknik"), ("Borulama şeması", "borulama"), ("Kontrol sistemi dokümanları", "kontrol")]
MAP = [("valve", "EEV"), ("pipes", "Ortak hat"), ("gauge", "Kapasite"), ("net", "Haberleşme")]
S["s13"] = dict(
    sfx=[("chime", T("s13", "koçun"), 0.2)] + [("click-soft", T("s13", w) + 0.5, 0.35) for _, w in DOCS] + [("ping", T("s13", "elinizi"), 0.25)],
    keys=dict(kocun=T("s13", "koçun"), elinizde=T("s13", "elinizde"), yeni=T("s13", "yeni"), teknik=T("s13", "teknik"),
              borulama=T("s13", "borulama"), kontrol=T("s13", "kontrol"), simdiden=T("s13", "şimdiden"), dort=T("s13", "dört"),
              belge=T("s13", "belgeyle"), elinizi=T("s13", "elinizi")),
    css=r"""
#s13 .hd { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:22px; }
#s13 .hd .bulb { width:96px; height:96px; border-radius:50%; background:#FFE27A; color:#5a4300; display:flex; align-items:center; justify-content:center; box-shadow:0 0 60px rgba(255,226,122,.55); }
#s13 .hd .tt { font-family:'Archivo Black'; font-size:70px; color:var(--fg); }
#s13 .sit { position:absolute; left:600px; top:268px; display:flex; gap:18px; }
#s13 .sit .chip { font-size:26px; }
#s13 .list { position:absolute; left:600px; top:370px; width:660px; padding:24px 30px; }
#s13 .list .lt { display:flex; align-items:center; gap:16px; }
#s13 .list .lt .ttl { font:700 22px 'JetBrains Mono'; letter-spacing:.14em; color:var(--muted); }
#s13 .dr { display:flex; align-items:center; gap:18px; margin-top:22px; font:900 32px Montserrat; color:var(--fg); }
#s13 .dr .bx { width:52px; height:52px; border-radius:12px; border:4px solid var(--accent2); display:flex; align-items:center; justify-content:center; color:#06221a; flex:none; }
#s13 .dr .bx .ico { opacity:0; }
#s13 .map { position:absolute; left:1300px; top:370px; width:520px; padding:22px 26px; }
#s13 .map .ttl { font:700 22px 'JetBrains Mono'; letter-spacing:.14em; color:var(--muted); }
#s13 .mr { display:flex; align-items:center; gap:14px; margin-top:16px; font:700 26px Montserrat; color:var(--fg); }
#s13 .mr .a { color:var(--vrf); } #s13 .mr .d { color:var(--onemli); }
#s13 .mr .ok { margin-left:auto; color:var(--ok); }
#s13 .shield { position:absolute; left:1300px; top:770px; width:520px; display:flex; align-items:center; gap:16px; padding:16px 22px; background:var(--ok); color:#06221a; border-radius:18px;
  font:900 30px Montserrat; box-shadow:0 0 50px rgba(46,212,122,.45); }
""",
    body=r"""
<div class="hd"><div class="bulb">BULB</div><div class="tt">KOÇUN TAVSİYESİ</div></div>
<div class="sit"><div class="chip s1">DOCI Elinizde VRF olarak alınmış BTB mi var?</div><div class="chip s2">BOXI Yeni ithalat mı planlıyorsunuz?</div></div>
<div class="list card"><div class="lt">DIKKAT<span class="ttl">ŞİMDİDEN HAZIRLAYIN</span></div>__DOCROWS__</div>
<div class="map card"><div class="ttl">4 KRİTER ↔ BELGE</div>__MAPROWS__</div>
<div class="shield">SHIELD Olası bir incelemede eliniz güçlenir</div>
""".replace("BULB", icon("bulb", 58)).replace("DOCI", icon("doc", 30)).replace("BOXI", icon("arrow", 30))
    .replace("DIKKAT", badge("dikkat")).replace("SHIELD", icon("shield", 48))
    .replace("__DOCROWS__", "".join(f'<div class="dr r{i}"><div class="bx">{icon("check", 34)}</div>{n}</div>' for i, (n, _) in enumerate(DOCS)))
    .replace("__MAPROWS__", "".join(f'<div class="mr">{icon(ic, 34, "a")}<span>{n}</span>{icon("arrow", 28)}{icon("doc", 30, "d")}{icon("check", 30, "ok")}</div>' for ic, n in MAP)),
    js=r"""
tl.fromTo(q(".hd .bulb"), { scale: 0, rotation: -40 }, { scale: 1, rotation: 0, duration: 0.6, ease: "back.out(2.4)" }, K.kocun - 0.3);
tl.fromTo(q(".hd .bulb"), { boxShadow: "0 0 20px rgba(255,226,122,.3)" }, { boxShadow: "0 0 80px rgba(255,226,122,.9)", duration: 0.5, yoyo: true, repeat: 3 }, K.kocun + 0.3);
slideX(".hd .tt", K.kocun, -50);
slideX(".sit .s1", K.elinizde, -50);
slideX(".sit .s2", K.yeni, -50);
rise(".list", K.teknik - 0.6, 0, 30);
["teknik", "borulama", "kontrol"].forEach((w, i) => {
  rise(`.dr.r${i}`, K[w] - 0.1, 0, 20);
  tl.fromTo(q(`.dr.r${i} .bx`), { backgroundColor: "rgba(46,212,122,0)", borderColor: "#8FB2FF" }, { backgroundColor: "#2ED47A", borderColor: "#2ED47A", duration: 0.25 }, K[w] + 0.5);
  tl.fromTo(q(`.dr.r${i} .bx .ico`), { opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(3)" }, K[w] + 0.5);
});
pop(".list .badge", K.simdiden - 0.2);
tl.fromTo(q(".map"), { x: 60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.dort - 0.3);
tl.fromTo(q(".mr"), { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: "power3.out", stagger: 0.18 }, K.dort);
pop(".mr .ok", K.belge, 0.12);
tl.fromTo(q(".shield"), { y: 60, opacity: 0, scale: 0.9 }, { y: 0, opacity: 1, scale: 1, duration: 0.6, ease: "back.out(1.8)" }, K.elinizi - 0.2);
""",
)

# ---------------------------------------------------------------- s14 Mini quiz
S["s14"] = dict(
    sfx=[("pop", T("s14", "soru"), 0.3), ("click-soft", T("s14", "mi") + 0.6, 0.3), ("click-soft", T("s14", "mi") + 1.6, 0.3),
         ("click-soft", T("s14", "mi") + 2.6, 0.3), ("chime", T("s14", "hayır"), 0.35)],
    keys=dict(simdi=T("s14", "şimdi"), soru=T("s14", "soru"), bir=T("s14", "bir", 2), bes=T("s14", "beş"), bu=T("s14", "bu"),
              yeterli=T("s14", "yeterli"), mi=T("s14", "mi"), cevap=T("s14", "cevap", off=0.35), hayir=T("s14", "hayır"),
              baglan=T("s14", "bağlanabilen"), dort=T("s14", "dört")),
    css=r"""
#s14 .hd { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:20px; }
#s14 .hd .tt { font-family:'Archivo Black'; font-size:70px; color:var(--fg); }
#s14 .qc { position:absolute; left:600px; top:262px; width:1220px; height:250px; padding:28px 34px; display:flex; gap:30px; align-items:center; }
#s14 .qc .tx { flex:1; }
#s14 .qc .l1 { font:700 34px/1.25 Montserrat; color:var(--fg); }
#s14 .qc .l1 b { color:var(--onemli); }
#s14 .qc .l2 { font-family:'Archivo Black'; font-size:44px; line-height:1.15; color:var(--fg); margin-top:16px; }
#s14 .qc .l2 span { color:var(--vrf); }
#s14 .opt { position:absolute; top:552px; width:420px; height:130px; border-radius:24px; display:flex; align-items:center; justify-content:center; gap:16px;
  font-family:'Archivo Black'; font-size:64px; border:5px solid rgba(143,178,255,.6); background:var(--panel); color:var(--fg); }
#s14 .yes { left:640px; } #s14 .no { left:1120px; }
#s14 .opt .mk { position:absolute; right:-22px; top:-22px; width:64px; height:64px; border-radius:50%; display:flex; align-items:center; justify-content:center; }
#s14 .yes .mk { background:var(--uyari); color:#2a0a0e; } #s14 .no .mk { background:var(--ok); color:#06221a; }
#s14 .ring { position:absolute; left:1620px; top:552px; width:130px; height:130px; }
#s14 .ring .n { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:62px; color:var(--onemli); }
#s14 .exp { position:absolute; left:600px; top:722px; width:1220px; display:flex; align-items:center; gap:22px; padding:18px 26px; border-color:var(--ok) !important; }
#s14 .exp .t { font:700 30px/1.25 Montserrat; color:var(--fg); flex:1; }
#s14 .exp .ics { display:flex; gap:10px; color:var(--vrf); }
#s14 .burst i { position:absolute; width:14px; height:14px; border-radius:3px; opacity:0; }
""",
    body=r"""
<div class="hd">SORUB<div class="tt">MİNİ QUIZ</div></div>
<div class="qc card">MINI<div class="tx"><div class="l1">Bir dış üniteye <b>5 iç ünite</b> bağlanabiliyor.</div><div class="l2">Bu, tek başına <span>VRF</span> demek için yeterli mi?</div></div></div>
<div class="opt yes">EVET<span class="mk">XI</span></div>
<div class="opt no">HAYIR<span class="mk">CK</span></div>
<svg class="ring" viewBox="0 0 130 130"><circle cx="65" cy="65" r="56" fill="none" stroke="rgba(255,197,61,.25)" stroke-width="10"/>
  <circle class="rg" cx="65" cy="65" r="56" fill="none" stroke="#FFC53D" stroke-width="10" stroke-linecap="round" transform="rotate(-90 65 65)"/></svg>
<div class="ring"><div class="n n3">3</div><div class="n n2">2</div><div class="n n1">1</div></div>
<div class="burst" style="position:absolute;left:1330px;top:617px;width:0;height:0;">BURST</div>
<div class="exp card"><div class="t">İç ünite sayısı tek başına belirleyici değil → <b>4 kritere</b> tek tek bakılmalı.</div><div class="ics">ICS</div></div>
""".replace("SORUB", badge("soru", big=True)).replace("XI", icon("x", 38)).replace("CK", icon("check", 38))
    .replace("ICS", "".join(icon(i, 46) for i in ("valve", "pipes", "gauge", "net")))
    .replace("BURST", "".join(f'<i style="background:{["#33D9B2", "#FFC53D", "#8FB2FF", "#2ED47A", "#FF9F43"][k % 5]}"></i>' for k in range(24)))
    .replace("MINI", '<svg width="230" height="150" viewBox="0 0 700 420">' + odu(265, 0, w=170, h=120)
             + "".join(idu(x, 340, w=120, h=46) for x in (0, 145, 290, 435, 580))
             + '<path d="M350 122 V 240 M60 240 H 640 M60 240 V 335 M205 240 V 335 M350 240 V 335 M495 240 V 335 M640 240 V 335" fill="none" stroke="#8FB2FF" stroke-width="12" stroke-linecap="round"/></svg>'),
    js=r"""
tl.fromTo(q(".hd .badge"), { scale: 0, rotation: -20 }, { scale: 1, rotation: 0, duration: 0.5, ease: "back.out(2.5)" }, K.simdi);
slideX(".hd .tt", K.soru - 0.4, -60);
tl.fromTo(q(".qc"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.bir - 0.2);
rise(".qc .l1", K.bir, 0, 20);
tl.fromTo(q(".qc .l1 b"), { scale: 1 }, { scale: 1.15, duration: 0.2, yoyo: true, repeat: 1, transformOrigin: "50% 50%" }, K.bes);
rise(".qc .l2", K.bu, 0, 20);
tl.fromTo(q(".opt"), { y: 60, opacity: 0, scale: 0.9 }, { y: 0, opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)", stagger: 0.15 }, K.yeterli - 0.2);
// countdown 3-2-1 during the thinking pause
const c0 = K.mi + 0.5, c1 = K.cevap - 0.1;
q(".rg").forEach((r) => { r.setAttribute("pathLength", "1"); r.style.strokeDasharray = "1 1"; });
tl.fromTo(q(".rg"), { strokeDashoffset: 0 }, { strokeDashoffset: 1, duration: c1 - c0, ease: "none" }, c0);
tl.fromTo(q("svg.ring"), { opacity: 0 }, { opacity: 1, duration: 0.2 }, c0 - 0.1);
const step = (c1 - c0) / 3;
["n3", "n2", "n1"].forEach((n, i) => {
  tl.fromTo(q(`.ring .${n}`), { opacity: 0, scale: 1.8 }, { opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2)" }, c0 + i * step);
  tl.to(q(`.ring .${n}`), { opacity: 0, duration: 0.15 }, c0 + (i + 1) * step - 0.12);
});
tl.to(q("svg.ring"), { opacity: 0, duration: 0.2 }, c1);
tl.fromTo(q(".opt"), { rotation: 0 }, { rotation: 1.5, duration: 0.12, yoyo: true, repeat: 7, ease: "sine.inOut", stagger: 0.06 }, c0 + 0.4);
// answer
tl.to(q(".no"), { scale: 0.9, duration: 0.1, ease: "power2.in" }, K.hayir - 0.15);
tl.to(q(".no"), { scale: 1.08, backgroundColor: "#2ED47A", borderColor: "#2ED47A", color: "#06221a", duration: 0.4, ease: "back.out(3)" }, K.hayir - 0.05);
tl.to(q(".yes"), { opacity: 0.4, scale: 0.94, duration: 0.4 }, K.hayir);
pop(".no .mk", K.hayir + 0.1);
pop(".yes .mk", K.hayir + 0.3);
q(".burst i").forEach((p, i) => {
  const a = (i / 24) * Math.PI * 2 + (i % 3) * 0.2, sp = 260 + (i * 37) % 140;
  const st = { k: 0 };
  tl.fromTo(st, { k: 0 }, { k: 1, duration: 1.2, ease: "none", onUpdate: () => {
    const k = st.k;
    p.style.transform = `translate(${(Math.cos(a) * sp * k).toFixed(1)}px, ${(Math.sin(a) * sp * k + 420 * k * k).toFixed(1)}px) rotate(${(k * 540 + i * 30).toFixed(0)}deg)`;
    p.style.opacity = (k < 0.02 || k > 0.98) ? "0" : String((1 - k).toFixed(2));
  } }, K.hayir);
});
rise(".exp", K.baglan, 0, 30);
pop(".exp .ics .ico", K.dort, 0.1);
""",
)

# ---------------------------------------------------------------- s15 Kapanış
S["s15"] = dict(
    sfx=[("impact-bass-1", T("s15", "tekniğe") + 0.2, 0.3), ("click-soft", T("s15", "abone") + 0.3, 0.45),
         ("notification", T("s15", "abone") + 0.5, 0.2)],
    keys=dict(ozet=T("s15", "özetle"), isme=T("s15", "isme"), teknige=T("s15", "tekniğe"), dort=T("s15", "dört"),
              tek=T("s15", "tek"), abone=T("s15", "abone"), payl=T("s15", "paylaşmayı"), bir=T("s15", "bir"),
              gorusmek=T("s15", "görüşmek")),
    css=r"""
#s15 .r { position:absolute; left:880px; top:150px; width:940px; }
#s15 .big { font-family:'Archivo Black'; font-size:104px; line-height:1.02; color:var(--fg); margin-top:12px; }
#s15 .big .l2 { position:relative; display:inline-block; color:var(--vrf); }
#s15 .big .l2 i { position:absolute; left:-8px; right:-8px; bottom:6px; height:22px; background:rgba(51,217,178,.28); border-radius:6px; transform-origin:left center; }
#s15 .eqr { display:flex; align-items:center; gap:16px; margin-top:34px; }
#s15 .eqr .c { width:84px; height:84px; border-radius:18px; background:var(--panel); border:3px solid var(--vrf); display:flex; align-items:center; justify-content:center; color:var(--vrf); }
#s15 .eqr .eqs { font-family:'Archivo Black'; font-size:60px; color:var(--onemli); margin-left:10px; }
#s15 .cta { display:flex; gap:20px; margin-top:44px; }
#s15 .sub { display:flex; align-items:center; gap:14px; font:900 34px Montserrat; color:#fff; background:#E5243B; padding:18px 30px; border-radius:16px; box-shadow:0 10px 0 #8E1424; }
#s15 .shr { display:flex; align-items:center; gap:14px; font:900 34px Montserrat; color:var(--fg); background:rgba(63,107,255,.25); border:3px solid var(--accent2); padding:16px 28px; border-radius:16px; }
#s15 .end { position:absolute; left:880px; top:800px; width:940px; display:flex; align-items:center; gap:24px; }
#s15 .end .lg { background:#F4F7FF; border-radius:16px; padding:12px 20px; display:flex; }
#s15 .end .lg img { height:46px; }
#s15 .end .t { font:700 30px Montserrat; color:var(--fg); }
#s15 .src { position:absolute; left:880px; top:888px; width:940px; font:400 18px 'JetBrains Mono'; color:var(--muted); letter-spacing:.04em; }
""",
    body=r"""
<div class="r">
  <div class="kicker">ÖZET</div>
  <div class="big"><span class="l1">İSME DEĞİL,</span><br/><span class="l2"><i></i>TEKNİĞE BAKIN.</span></div>
  <div class="eqr">ICONS<span class="eqs">= 1 KARAR</span></div>
  <div class="cta"><div class="sub">BELL ABONE OL</div><div class="shr">SHARE PAYLAŞ</div></div>
</div>
<div class="end"><div class="lg"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div><div class="t">Bir sonraki derste görüşmek üzere!</div></div>
""".replace("ICONS", "".join(f'<div class="c">{icon(i, 50)}</div>' for i in ("valve", "pipes", "gauge", "net")))
    .replace("BELL", icon("bell", 40)).replace("SHARE", icon("share", 38)),
    js=r"""
rise(".r .kicker", K.ozet, 0, 16);
tl.fromTo(q(".big .l1"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.isme - 0.15);
tl.fromTo(q(".big .l2"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.teknige - 0.15);
strike(".big .l2 i", K.teknige + 0.35, 0.5);
pop(".eqr .c", K.dort - 0.1, 0.1);
tl.fromTo(q(".eqr .eqs"), { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 0.5, ease: "back.out(2)" }, K.tek);
tl.fromTo(q(".sub"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "back.out(2)" }, K.abone - 0.5);
tl.to(q(".sub"), { y: 8, boxShadow: "0 2px 0 #8E1424", duration: 0.1, ease: "power2.in" }, K.abone + 0.25);
tl.to(q(".sub"), { y: 0, boxShadow: "0 10px 0 #8E1424", duration: 0.4, ease: "elastic.out(1,0.4)" }, K.abone + 0.38);
tl.fromTo(q(".sub .ico"), { rotation: 0, transformOrigin: "50% 10%" }, { rotation: 18, duration: 0.1, yoyo: true, repeat: 7, ease: "sine.inOut" }, K.abone + 0.5);
tl.fromTo(q(".shr"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "back.out(2)" }, K.payl - 0.2);
tl.fromTo(q(".end"), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.bir - 0.2);
fadeIn(".src", K.gorusmek, 0.6);
""",
)
S["s15"]["exit"] = False
S["s15"]["body"] += '<div class="src">Kaynak: T.C. Ticaret Bakanlığı Gümrükler Genel Müdürlüğü · 01.10.2026 tarihli, E-17474625-162.01-00126963399 sayılı “VRF Klimalar” yazısı</div>\n'
