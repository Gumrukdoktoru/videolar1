"""Scenes 07-12: tuzak 2 (DGÖ/DTÖ + 12 haneli kod), soru 3 (ölçü birimleri) + çözüm + tuzak, koçun notu, cevap anahtarı."""
from lib import T, D, SCENES, icon, badge
from scenes_a import S as SA, COMMON_CSS, scoped, answer_bar, char, qscene, CHAR

S = SA  # qscene() registers into the shared dict

# ---------------------------------------------------------------- s07 Tuzak 2
def digits(d):
    return "".join('<span class="dot">.</span>' if ch == "." else f"<span>{ch}</span>" for ch in d)


CODE = [("8501.10", "1–6", "ARMONİZE SİSTEM", "DGÖ · uluslararası ortak", "g0"), ("10", "7–8", "KOMBİNE NOMANKLATÜR", "Avrupa Birliği", "g1"),
        ("00", "9–10", "MİLLİ ALT AÇILIM", "ulusal", "g2"), ("00", "11–12", "İSTATİSTİK", "ulusal", "g3")]
_k7 = dict(tuzak=T("s07", "tuzak"), cano=T("s07", "Cano'ya"), dto=T("s07", "Dünya", 1), dedi=T("s07", "dedi"), hayir=T("s07", "Hayır"),
           dgo=T("s07", "Dünya", 2), eser=T("s07", "eseridir"), baba=T("s07", "Gümrükçü"), form=T("s07", "formülü"), g=T("s07", "gümrük"),
           t=T("s07", "ticaret"), kod=T("s07", "kod"), on2=T("s07", "haneli"),
           grp=[T("s07", "ilk"), T("s07", "yedi"), T("s07", "dokuz"), T("s07", "son")])
S["s07"] = dict(
    sfx=[("whoosh-short", _k7["cano"] - 0.1, 0.25), ("pop", _k7["dto"], 0.3), ("error", _k7["hayir"], 0.3), ("chime", _k7["dgo"], 0.3),
         ("whoosh-short", _k7["baba"] - 0.1, 0.25), ("pop", _k7["g"], 0.25), ("pop", _k7["t"], 0.25), ("whoosh-short", _k7["kod"] - 0.2, 0.3)]
        + [("pop", t, 0.3) for t in _k7["grp"]],
    keys=_k7,
    css=scoped("s07", COMMON_CSS + r"""
#S .p1 { position:absolute; inset:0; }
#S .hdr { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:22px; }
#S .hdr .h1 { font-size:46px; margin:0; white-space:nowrap; }
#S .org { position:absolute; left:600px; width:580px; height:170px; padding:20px 24px; border-radius:22px; display:flex; align-items:center; gap:20px; }
#S .org.dto { top:250px; background:rgba(255,77,94,.08); border:3px solid rgba(255,77,94,.7); }
#S .org.dgo { top:446px; background:rgba(46,212,122,.10); border:3px solid var(--ok); }
#S .org .ab { flex:none; width:100px; height:100px; border-radius:20px; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:34px; line-height:1; }
#S .org.dto .ab { background:rgba(255,77,94,.2); color:#FF8A96; } #S .org.dgo .ab { background:rgba(46,212,122,.2); color:var(--ok); }
#S .org b { display:block; font:900 24px Montserrat; color:var(--fg); white-space:nowrap; }
#S .org small { display:block; font:400 20px 'JetBrains Mono'; color:var(--muted); margin-top:6px; white-space:nowrap; }
#S .org .mk { margin-left:auto; }
#S .org.dto .mk { color:var(--uyari); } #S .org.dgo .mk { color:var(--ok); }
#S .formula { position:absolute; left:600px; top:650px; width:580px; height:150px; padding:18px 24px; border-radius:22px; background:#F4F7FF; color:#0B1A44; }
#S .formula .tt { font:900 19px Montserrat; letter-spacing:.12em; color:#5A6AA0; }
#S .formula .ln { display:flex; align-items:baseline; gap:12px; margin-top:8px; font:900 30px Montserrat; white-space:nowrap; }
#S .formula .ln b { font-family:'Archivo Black'; font-weight:400; }
#S .formula .ln u { text-decoration:none; color:#0B8A47; border-bottom:4px solid #0B8A47; }
#S .formula .ln.l2 u { color:#B4231B; border-color:#B4231B; }
#S .cano { left:1214px; top:420px; }
#S .canotag { left:1262px; top:850px; }
#S .bub.bc { left:1206px; top:252px; width:270px; --tail:80px; }
#S .stamp.sc { left:1224px; top:600px; }
#S .baba { left:1560px; top:380px; }
#S .babatag { left:1556px; top:850px; }
#S .bub.bb { left:1496px; top:188px; width:324px; --tail:150px; }
#S .p2 { position:absolute; inset:0; opacity:0; }
#S .p2 .tt { position:absolute; left:600px; top:250px; font:900 24px Montserrat; letter-spacing:.12em; color:var(--accent2); white-space:nowrap; }
#S .p2 .ex { position:absolute; left:600px; top:290px; font:400 21px 'JetBrains Mono'; color:var(--muted); white-space:nowrap; }
#S .p2 .ex b { color:var(--fg); }
#S .code { position:absolute; left:600px; top:360px; width:1220px; display:flex; gap:40px; }
#S .grp { flex:none; width:150px; display:flex; flex-direction:column; align-items:stretch; }
#S .grp.g0 { width:490px; }
#S .grp .dg { display:flex; gap:6px; justify-content:center; }
#S .grp .dg span { width:72px; height:104px; border-radius:12px; display:flex; align-items:center; justify-content:center; font:700 54px 'JetBrains Mono';
  background:rgba(13,36,92,.94); border:3px solid currentColor; color:var(--fg); }
#S .grp .dg span.dot { width:32px; border:none; background:none; color:var(--muted); }
#S .grp .br { height:20px; margin:12px 6px 0; border:4px solid currentColor; border-top:none; border-radius:0 0 12px 12px; }
#S .grp .lb { margin-top:12px; text-align:center; }
#S .grp .lb .hn { font:700 22px 'JetBrains Mono'; }
#S .grp .lb b { display:block; font:900 18px/1.2 Montserrat; color:var(--fg); margin-top:4px; }
#S .grp .lb small { display:block; font:700 17px Montserrat; color:var(--muted); margin-top:2px; white-space:nowrap; }
#S .g0 { color:var(--ok); } #S .g1 { color:var(--accent2); } #S .g2 { color:var(--gold); } #S .g3 { color:var(--dikkat); }
#S .p2 .on { position:absolute; left:600px; top:690px; width:1220px; height:100px; display:flex; align-items:center; gap:22px; padding:0 26px; }
#S .p2 .on .tx { font:800 27px Montserrat; color:var(--fg); white-space:nowrap; }
#S .p2 .on .tx em { font-style:normal; color:var(--ok); }
"""),
    body=f'''
<div class="p1">
  <div class="hdr">{badge("tuzak")}<div class="h1">AS'yi kim hazırladı?</div></div>
  <div class="org dto"><span class="ab">DTÖ</span><div><b>Dünya Ticaret Örgütü</b><small>Cenevre · ticaret kuralları</small></div><span class="mk">{icon("x", 46)}</span></div>
  <div class="org dgo"><span class="ab">DGÖ</span><div><b>Dünya Gümrük Örgütü</b><small>Brüksel · Armonize Sistem</small></div><span class="mk">{icon("check", 46)}</span></div>
  <div class="formula"><div class="tt">GÜMRÜKÇÜ BABA'NIN FORMÜLÜ</div>
    <div class="ln l1"><b>D<u>G</u>Ö</b><span>→ <u>G</u>ümrük · AS burada</span></div><div class="ln l2"><b>D<u>T</u>Ö</b><span>→ <u>T</u>icaret</span></div></div>
  <div class="bub bc">Dünya <em>Ticaret</em> Örgütü!</div>
  {char("cano", "cano", 430)}
  <span class="ctag canotag">CANO</span>
  <div class="stamp sc">{icon("x", 34)}HAYIR</div>
  <div class="bub bb"><i>DGÖ</i> gümrük,<br/><em>DTÖ</em> ticaret!</div>
  {char("baba", "baba", 470)}
  <span class="ctag babatag">GÜMRÜKÇÜ BABA</span>
</div>
<div class="p2">
  <div class="tt">12 HANELİ TARİFE KODU (GTİP) · NASIL OKUNUR?</div>
  <div class="ex">Örnek: <b>8501.10.10.00.00</b> · çıkış gücü 18 W'ı geçmeyen senkron motorlar</div>
  <div class="code">{"".join(f'<div class="grp {g}"><div class="dg">{digits(d)}</div><div class="br"></div><div class="lb"><span class="hn">{h}. hane</span><b>{n}</b><small>{sub}</small></div></div>' for d, h, n, sub, g in CODE)}</div>
  <div class="on card">{icon("globe", 54)}<div class="tx">İlk <em>6 hane</em> = Armonize Sistem → AS’ye taraf her ülkede aynı</div></div>
</div>
''',
    js=r"""
slam(".hdr .badge", K.tuzak - 0.1);
rise(".hdr .h1", K.tuzak + 0.3, 0, 30);
tl.fromTo(q(".cano"), { x: 200, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.cano - 0.2);
pop(".canotag", K.cano + 0.2, 0, "back.out(2.4)");
tl.fromTo(q(".bub.bc"), { scale: 0.3, opacity: 0, transformOrigin: "30% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.dto);
slideX(".org.dto", K.dto, -60);
slam(".stamp.sc", K.hayir);
pop(".org.dto .mk", K.hayir + 0.1, 0, "back.out(3)");
slideX(".org.dgo", K.dgo - 0.1, -60);
pop(".org.dgo .mk", K.eser, 0, "back.out(3)");
tl.fromTo(q(".baba"), { x: 220, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.baba - 0.3);
pop(".babatag", K.baba + 0.1, 0, "back.out(2.4)");
tl.fromTo(q(".bub.bb"), { scale: 0.3, opacity: 0, transformOrigin: "50% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.form);
tl.fromTo(q(".formula"), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }, K.form - 0.1);
pulse(".formula .l1", K.g, 1.06);
pulse(".formula .l2", K.t, 1.06);
tl.to(q(".p1"), { opacity: 0, y: -30, duration: 0.45, ease: "power2.in" }, K.kod - 0.5);
tl.fromTo(q(".p2"), { opacity: 0 }, { opacity: 1, duration: 0.4, ease: "power1.out" }, K.kod - 0.05);
rise(".p2 .tt", K.kod, 0, 16);
rise(".p2 .ex", K.on2, 0, 12);
tl.fromTo(q(".grp .dg span"), { y: -40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)", stagger: 0.04 }, K.on2 - 0.2);
K.grp.forEach((t, i) => {
  tl.fromTo(q(".grp.g" + i + " .br"), { scaleX: 0, opacity: 0 }, { scaleX: 1, opacity: 1, duration: 0.4, ease: "power2.out" }, t);
  rise(".grp.g" + i + " .lb", t + 0.1, 0, 16);
  tl.fromTo(q(".grp.g" + i + " .dg span:not(.dot)"), { backgroundColor: "rgba(13,36,92,.94)" }, { backgroundColor: "rgba(255,255,255,.14)", duration: 0.3, immediateRender: false }, t);
});
tl.fromTo(q(".p2 .on"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }, K.grp[1] - 0.4);
"""
)

# ---------------------------------------------------------------- s08 Soru 3
qscene("s08", 3,
       'Türk Gümrük Tarife Cetvelinde kullanılan <mark>ölçü birimi kısaltmaları</mark> ile anlamlarına ilişkin aşağıdaki eşleştirmelerden hangisi <span class="neg">yanlıştır<i></i></span>?',
       ["<b>ct/l</b> – Karat", "<b>p/st</b> – Adet", "<b>ce/el</b> – Hücre adedi", "<b>p/a</b> – Çift", "<b>TJ</b> – Terajul (brüt kalori değeri)"],
       neg="yanlıştır", stem_word="Türk")

# ---------------------------------------------------------------- s09 Çözüm 3
UNITS = [("c/k", "Karat", "kıymetli taşlar", "gem", "u0"), ("ct/l", "Ton başına taşıma kapasitesi", "", "ship", "u1"),
         ("p/st", "Adet", "parça sayısı", "box", "u2"), ("ce/el", "Hücre adedi", "", "battery", "u3"),
         ("p/a", "Çift", "ayakkabı, eldiven…", "shoe", "u4"), ("TJ", "Terajul", "brüt kalori değeri", "flame", "u5")]
_k9 = dict(cevap=T("s09", "Cevap"), A=T("s09", "A"), kar=T("s09", "Karatın"),
           u=[T("s09", "ke"), T("s09", "taşıma"), T("s09", "adet"), T("s09", "hücre"), T("s09", "çift"), T("s09", "terajul")],
           diger=T("s09", "Diğer"), not_=T("s09", "not"), karat=T("s09", "karat"), gram=T("s09", "gramdır"))
S["s09"] = dict(
    sfx=[("chime", _k9["A"], 0.35)] + [("pop", t, 0.28) for t in _k9["u"]] + [("notification", _k9["not_"], 0.25), ("ping", _k9["gram"], 0.3)],
    keys=_k9,
    css=scoped("s09", COMMON_CSS + r"""
#S .ans .tx b { font:700 30px 'JetBrains Mono'; }
#S .ans .tx s { color:#FF8A96; text-decoration-color:var(--uyari); text-decoration-thickness:4px; }
#S .units { position:absolute; left:600px; top:250px; width:1220px; display:grid; grid-template-columns:repeat(3, 1fr); gap:16px; }
#S .un { position:relative; height:196px; padding:18px 22px; border-radius:20px; background:rgba(13,36,92,.94); border:3px solid #2B4C9E; overflow:hidden; }
#S .un .ab { font:700 52px 'JetBrains Mono'; line-height:1; color:var(--gold); }
#S .un .ico { position:absolute; right:20px; top:18px; color:var(--accent2); opacity:.9; }
#S .un b { display:block; font:900 25px/1.2 Montserrat; color:var(--fg); margin-top:14px; }
#S .un small { display:block; font:400 18px 'JetBrains Mono'; color:var(--muted); margin-top:6px; white-space:nowrap; }
#S .un.u0, #S .un.u1 { border-color:var(--ok); }
#S .un .tg { position:absolute; right:16px; bottom:14px; font:900 15px Montserrat; letter-spacing:.08em; padding:3px 10px; border-radius:8px; }
#S .un.u0 .tg { background:var(--ok); color:#03221a; } #S .un.u1 .tg { background:var(--accent2); color:#071A45; }
#S .note { position:absolute; left:600px; top:690px; width:1220px; height:170px; display:flex; align-items:center; gap:30px; padding:0 30px;
  border-color:var(--dikkat); background:rgba(255,159,67,.10); }
#S .note .eq { display:flex; align-items:center; gap:18px; font-family:'Archivo Black'; font-size:54px; line-height:1; color:var(--fg); white-space:nowrap; }
#S .note .eq em { font-style:normal; color:var(--gold); }
#S .note .eq .ico { color:var(--gold); }
#S .note small { font:700 22px Montserrat; color:var(--muted); white-space:nowrap; }
"""),
    body=f'''
{answer_bar("A", "<s><b>ct/l</b> – Karat</s> → karat = <b>c/k</b>")}
<div class="units">{"".join(f'<div class="un {u}"><div class="ab">{ab}</div>{icon(ic, 48)}<b>{m}</b>{f"<small>{sm}</small>" if sm else ""}{"<span class=tg>KARAT ✓</span>" if u == "u0" else "<span class=tg>KARAT DEĞİL</span>" if u == "u1" else ""}</div>' for ab, m, sm, ic, u in UNITS)}</div>
<div class="note card">{badge("dikkat")}<div class="eq">{icon("gem", 60)}1 karat = <em>0,2 g</em></div><small>200 miligram</small></div>
''',
    js=r"""
tl.fromTo(q(".ans"), { y: -40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }, K.cevap - 0.15);
slam(".ans .L", K.A);
pop(".ans .ck", K.A + 0.35, 0, "back.out(3)");
K.u.forEach((t, i) => {
  tl.fromTo(q(".un.u" + i), { y: 50, opacity: 0, rotationX: -40 }, { y: 0, opacity: 1, rotationX: 0, duration: 0.5, ease: "back.out(1.7)" }, t - 0.35);
  pop(".un.u" + i + " .ico", t - 0.1, 0, "back.out(2.6)");
});
pop(".un .tg", K.u[1] + 0.4, 0.2, "back.out(2.6)");
tl.fromTo(q(".note"), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }, K.not_ - 0.2);
slam(".note .badge", K.not_);
pop(".note .eq", K.karat, 0, "back.out(2)");
fadeIn(".note small", K.gram, 0.4);
"""
)

# ---------------------------------------------------------------- s10 Tuzak 3
_k10 = dict(tuzak=T("s10", "Tuzak"), staj=T("s10", "Stajyerimiz"), sandi=T("s10", "sandı"), hayir=T("s10", "Hayır"), cift=T("s10", "çift"),
            ayak=T("s10", "ayakkabı"), adet=T("s10", "Adet"), ayni=T("s10", "Aynı"), karat=T("s10", "karat"), tasima=T("s10", "taşıma"),
            harf=T("s10", "Harfler"), farkli=T("s10", "farklı"))
S["s10"] = dict(
    sfx=[("whoosh-short", _k10["staj"] - 0.1, 0.25), ("pop", _k10["sandi"] - 0.4, 0.3), ("error", _k10["hayir"], 0.3), ("pop", _k10["cift"], 0.25),
         ("pop", _k10["adet"], 0.25), ("whoosh-short", _k10["ayni"], 0.2), ("pop", _k10["karat"], 0.25), ("pop", _k10["tasima"], 0.25),
         ("impact-bass-1", _k10["harf"], 0.3)],
    keys=_k10,
    css=scoped("s10", COMMON_CSS + r"""
#S .hdr { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:22px; }
#S .hdr .h1 { font-size:46px; margin:0; white-space:nowrap; }
#S .staj { left:1600px; top:360px; }
#S .stajtag { left:1594px; top:850px; }
#S .bub.bs { left:1530px; top:200px; width:290px; --tail:120px; }
#S .stamp.ss { left:1580px; top:580px; }
#S .pair { position:absolute; left:600px; width:900px; height:200px; display:flex; align-items:center; gap:18px; }
#S .pair.p0 { top:250px; } #S .pair.p1 { top:480px; }
#S .uc { flex:1; height:200px; padding:18px 22px; border-radius:20px; background:rgba(13,36,92,.94); border:3px solid #2B4C9E; position:relative; }
#S .uc .ab { font:700 56px 'JetBrains Mono'; line-height:1; color:var(--gold); }
#S .uc b { display:block; font:900 27px/1.2 Montserrat; color:var(--fg); margin-top:16px; }
#S .uc small { display:block; font:400 18px 'JetBrains Mono'; color:var(--muted); margin-top:6px; white-space:nowrap; }
#S .uc .ico { position:absolute; right:20px; top:20px; color:var(--accent2); }
#S .uc.hot { border-color:var(--dikkat); }
#S .ne { flex:none; width:76px; height:76px; border-radius:50%; background:var(--uyari); color:#2a0a0e; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:50px; line-height:1; }
#S .tag { position:absolute; left:600px; top:730px; width:900px; height:120px; display:flex; align-items:center; justify-content:center; gap:22px;
  border-radius:20px; background:#14141A; border:4px solid #FFD400; }
#S .tag b { font-family:'Archivo Black'; font-weight:400; font-size:38px; color:#FFD400; white-space:nowrap; }
"""),
    body=f'''
<div class="hdr">{badge("tuzak")}<div class="h1">Benzer harf, farklı birim</div></div>
<div class="bub bs"><b>p/a</b>… bu <em>adet</em> olmalı!</div>
{char("stajyer", "staj", 480)}
<span class="ctag stajtag">STAJYER</span>
<div class="stamp ss">{icon("x", 34)}HAYIR</div>
<div class="pair p0"><div class="uc hot u0"><div class="ab">p/a</div>{icon("shoe", 48)}<b>Çift</b><small>ayakkabı, eldiven…</small></div><div class="ne">≠</div>
  <div class="uc u1"><div class="ab">p/st</div>{icon("box", 48)}<b>Adet</b><small>parça sayısı</small></div></div>
<div class="pair p1"><div class="uc hot u2"><div class="ab">c/k</div>{icon("gem", 48)}<b>Karat</b><small>kıymetli taşlar</small></div><div class="ne">≠</div>
  <div class="uc u3"><div class="ab">ct/l</div>{icon("ship", 48)}<b>Taşıma kapasitesi</b><small>ton başına</small></div></div>
<div class="tag">{icon("trap", 44)}<b>Harfler benzer, anlamlar farklı!</b></div>
''',
    js=r"""
slam(".hdr .badge", K.tuzak - 0.1);
rise(".hdr .h1", K.tuzak + 0.3, 0, 30);
tl.fromTo(q(".staj"), { x: 200, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.staj - 0.2);
pop(".stajtag", K.staj + 0.2, 0, "back.out(2.4)");
tl.fromTo(q(".bub.bs"), { scale: 0.3, opacity: 0, transformOrigin: "40% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.sandi - 0.6);
slam(".stamp.ss", K.hayir);
slideX(".pair.p0 .u0", K.cift - 0.2, -60);
pop(".pair.p0 .u0 .ico", K.ayak, 0, "back.out(2.6)");
pop(".pair.p0 .ne", K.adet - 0.2, 0, "back.out(2.6)");
slideX(".pair.p0 .u1", K.adet, 60);
slideX(".pair.p1 .u2", K.karat - 0.3, -60);
pop(".pair.p1 .ne", K.tasima - 0.4, 0, "back.out(2.6)");
slideX(".pair.p1 .u3", K.tasima - 0.2, 60);
tl.fromTo(q(".tag"), { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }, K.harf - 0.1);
pulse(".tag b", K.farkli, 1.06);
"""
)

# ---------------------------------------------------------------- s11 Koçun notu (mindmap)
NODES = [("n0", "SIRALAMA", ["ham madde → mamul", "1–83: maddeye göre", "84–96: işlevine göre"], "layers"),
         ("n1", "GENEL KURAL 3", ["a → b → c sırayla", "vergi oranı ölçüt DEĞİL"], "sort"),
         ("n2", "KISALTMA ÇİFTLERİ", ["c/k karat ≠ ct/l taşıma", "p/a çift ≠ p/st adet"], "ruler")]
_k11 = dict(koc=T("s11", "Koçun"), ezb=T("s11", "ezberle"), mant=T("s11", "mantıkla"),
            br=[T("s11", "Bir"), T("s11", "İki"), T("s11", "Üç")], vergi=T("s11", "vergi"), cift=T("s11", "çift", 1))
S["s11"] = dict(
    sfx=[("whoosh-short", _k11["koc"], 0.25), ("impact-bass-1", _k11["mant"], 0.25)] + [("pop", t, 0.3) for t in _k11["br"]] + [("ping", _k11["cift"], 0.25)],
    keys=_k11,
    css=scoped("s11", COMMON_CSS + r"""
#S .hdr { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:22px; }
#S .hdr .h1 { font-size:50px; margin:0; white-space:nowrap; }
#S .motto { position:absolute; left:1330px; top:140px; display:flex; align-items:center; gap:12px; font:900 26px Montserrat; color:var(--fg); white-space:nowrap; }
#S .motto s { color:#FF8A96; text-decoration-color:var(--uyari); text-decoration-thickness:4px; }
#S .motto em { font-style:normal; color:var(--teal); }
#S svg.mm { position:absolute; left:0; top:0; width:1920px; height:1080px; overflow:visible; }
#S .core { position:absolute; left:1080px; top:420px; width:260px; height:260px; border-radius:50%; display:flex; flex-direction:column; align-items:center;
  justify-content:center; text-align:center; background:radial-gradient(circle at 40% 35%, #3F6BFF, #16307A); border:5px solid #8FB2FF;
  box-shadow:0 0 0 14px rgba(63,107,255,.18), 0 26px 60px rgba(0,0,0,.45); }
#S .core b { font-family:'Archivo Black'; font-weight:400; font-size:30px; line-height:1.1; color:#fff; }
#S .core small { font:700 17px 'JetBrains Mono'; color:#CFE0FF; margin-top:8px; letter-spacing:.1em; }
#S .nd { position:absolute; width:420px; padding:18px 22px; border-radius:20px; background:rgba(13,36,92,.95); border:3px solid var(--teal); }
#S .nd .hd { display:flex; align-items:center; gap:12px; font:900 20px Montserrat; letter-spacing:.08em; color:var(--teal); white-space:nowrap; }
#S .nd .hd .num { width:40px; height:40px; border-radius:50%; background:var(--teal); color:#03221a; display:flex; align-items:center; justify-content:center; font:900 22px Montserrat; }
#S .nd ul { list-style:none; margin-top:10px; }
#S .nd li { font:700 22px/1.3 Montserrat; color:var(--fg); margin-top:4px; white-space:nowrap; }
#S .nd li:before { content:"▸ "; color:var(--teal); }
#S .nd.n0 { left:600px; top:270px; }
#S .nd.n1 { left:1400px; top:270px; border-color:var(--gold); } #S .nd.n1 .hd { color:var(--gold); } #S .nd.n1 .hd .num { background:var(--gold); color:#2a1d00; } #S .nd.n1 li:before { color:var(--gold); }
#S .nd.n2 { left:1000px; top:730px; border-color:var(--dikkat); } #S .nd.n2 .hd { color:var(--dikkat); } #S .nd.n2 .hd .num { background:var(--dikkat); color:#2b1300; } #S .nd.n2 li:before { color:var(--dikkat); }
"""),
    body=f'''
<div class="hdr">{badge("ipucu")}<div class="h1">Koçun notu</div></div>
<div class="motto"><s>ezber</s>{icon("arrow", 30)}<em>mantık</em></div>
<svg class="mm" aria-hidden="true"><g fill="none" stroke-width="5" stroke-linecap="round">
  <path class="l0" d="M1100 500 C1020 470 1000 400 1020 390" stroke="#33D9B2"/>
  <path class="l1" d="M1320 500 C1400 470 1420 400 1400 390" stroke="#FFC53D"/>
  <path class="l2" d="M1210 680 C1210 700 1210 712 1210 728" stroke="#FF9F43"/></g></svg>
<div class="core"><b>TARİFE<br/>SİSTEMATİĞİ</b><small>3 KURAL</small></div>
{"".join(f'<div class="nd {n}"><div class="hd"><span class="num">{i + 1}</span>{icon(ic, 30)}{t}</div><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul></div>' for i, (n, t, li, ic) in enumerate(NODES))}
''',
    js=r"""
slam(".hdr .badge", K.koc - 0.1);
rise(".hdr .h1", K.koc + 0.2, 0, 30);
rise(".motto", K.ezb - 0.2, 0, 16);
pulse(".motto em", K.mant, 1.2);
pop(".core", K.mant - 0.2, 0, "back.out(1.8)");
breathe(".core", K.mant + 0.4, D - 0.5, 0.03, 2.4);
K.br.forEach((t, i) => {
  draw(".mm .l" + i, t - 0.2, 0.5);
  tl.fromTo(q(".nd.n" + i), { scale: 0.5, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.5, ease: "back.out(1.8)" }, t + 0.1);
  rise(".nd.n" + i + " li", t + 0.5, 0.35, 12);
});
pulse(".nd.n1 li:last-child", K.vergi, 1.06);
"""
)

# ---------------------------------------------------------------- s12 Cevap anahtarı
KEYS = [("1", "C", "Adi metaller", "XV. bölüm · 72–83"), ("2", "E", "Sınıflandırma", "vergi oranı ölçüt değil"), ("3", "A", "Ölçü birimi", "karat = c/k, ct/l değil")]
_k12 = dict(bug=T("s12", "Bugünün"), qs=[T("s12", "C"), T("s12", "E"), T("s12", "A")], kac=T("s12", "Kaç"), yor=T("s12", "Yorumlara"),
            abone=T("s12", "abone"), pay=T("s12", "paylaşmayı"), sonraki=T("s12", "sonraki"), hosca=T("s12", "Hoşça"))
S["s12"] = dict(
    sfx=[("whoosh-short", _k12["bug"], 0.25)] + [("chime", t, 0.3) for t in _k12["qs"]]
        + [("pop", _k12["kac"], 0.3), ("pop", _k12["abone"], 0.3), ("pop", _k12["pay"], 0.3), ("ping", _k12["hosca"], 0.3)],
    keys=_k12,
    exit=False,
    css=scoped("s12", COMMON_CSS + r"""
#S .hdr { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:22px; }
#S .hdr .h1 { font-size:54px; margin:0; white-space:nowrap; }
#S .keys { position:absolute; left:600px; top:236px; width:1220px; display:flex; gap:22px; }
#S .kc { flex:1; height:280px; padding:22px 24px; border-radius:22px; background:rgba(13,36,92,.95); border:3px solid var(--ok); position:relative; }
#S .kc .qn { font:700 20px 'JetBrains Mono'; letter-spacing:.14em; color:var(--accent2); }
#S .kc .L { width:96px; height:96px; border-radius:50%; background:var(--ok); color:#03221a; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:56px; line-height:1; margin-top:14px; box-shadow:0 0 0 10px rgba(46,212,122,.18); }
#S .kc b { display:block; font:900 26px Montserrat; color:var(--fg); margin-top:20px; white-space:nowrap; }
#S .kc small { display:block; font:400 19px 'JetBrains Mono'; color:var(--muted); margin-top:6px; white-space:nowrap; }
#S .score { position:absolute; left:600px; top:546px; width:560px; height:110px; display:flex; align-items:center; gap:18px; padding:0 24px; }
#S .score .tx { font:900 30px Montserrat; color:var(--fg); white-space:nowrap; }
#S .score .tx em { font-style:normal; color:var(--gold); }
#S .score .bx { display:flex; gap:10px; margin-left:auto; }
#S .score .bx i { width:34px; height:34px; border-radius:8px; border:3px solid var(--gold); }
#S .cta { position:absolute; left:600px; top:684px; display:flex; gap:16px; }
#S .cta .chip { font-size:22px; padding:8px 18px; gap:10px; }
#S .nxt { position:absolute; left:600px; top:784px; font:800 26px Montserrat; color:var(--muted); white-space:nowrap; }
#S .nxt b { color:var(--teal); }
#S .crew { position:absolute; left:1470px; top:590px; width:350px; height:296px; }
#S .crew .chr { bottom:0; }
#S .crew .c0 { left:0; } #S .crew .c1 { left:72px; } #S .crew .c2 { left:152px; } #S .crew .c3 { left:228px; }
"""),
    body=f'''
<div class="hdr">{badge("onemli")}<div class="h1">Cevap anahtarı</div></div>
<div class="keys">{"".join(f'<div class="kc k{i}"><div class="qn">SORU {n}</div><div class="L">{L}</div><b>{t}</b><small>{s}</small></div>' for i, (n, L, t, s) in enumerate(KEYS))}</div>
<div class="score card">{icon("pen", 40)}<div class="tx">Kaç tanesini <em>bildin?</em></div><div class="bx"><i></i><i></i><i></i></div></div>
<div class="cta"><span class="chip c1">{icon("mail", 30)} Yorumlara yaz</span><span class="chip c2">{icon("bell", 30)} Abone ol</span><span class="chip c3">{icon("share", 30)} Paylaş</span></div>
<div class="nxt">Sıradaki: <b>Tarife Dersi #2</b> · yeni 3 soru</div>
<div class="crew">{"".join(f'<img class="chr c{i}" src="assets/img/{CHAR[c][0]}.png" alt="{CHAR[c][1]}" style="height:{h}px" />' for i, (c, h) in enumerate([("stajyer", 262), ("yardimci", 280), ("baba", 290), ("cano", 272)]))}</div>
''',
    js=r"""
slam(".hdr .badge", K.bug - 0.1);
rise(".hdr .h1", K.bug + 0.2, 0, 30);
tl.fromTo(q(".kc"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "power3.out", stagger: 0.12 }, K.bug + 0.3);
K.qs.forEach((t, i) => {
  tl.fromTo(q(".kc.k" + i + " .L"), { scale: 0, opacity: 0, rotation: -90 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.5, ease: "back.out(2.2)" }, t);
});
rise(".score", K.kac - 0.1, 0, 30);
pop(".score .bx i", K.kac + 0.4, 0.15, "back.out(2.6)");
pop(".cta .c1", K.yor, 0, "back.out(2.2)");
pop(".cta .c2", K.abone, 0, "back.out(2.2)");
pop(".cta .c3", K.pay, 0, "back.out(2.2)");
rise(".nxt", K.sonraki - 0.2, 0, 16);
tl.fromTo(q(".crew .chr"), { y: 160, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.5)", stagger: 0.12 }, K.kac);
"""
)
