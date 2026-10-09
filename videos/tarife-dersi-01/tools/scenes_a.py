"""Scenes 01-06: giriş, soru 1 (bölüm/fasıl) + çözüm + tuzak, soru 2 (Armonize Sistem) + çözüm."""
from lib import T, D, SCENES, icon, badge

S = {}

CHAR = {  # cutout file, display name
    "stajyer": ("stajyer-cut", "STAJYER"),
    "yardimci": ("yardimci-cut", "YARDIMCI"),
    "baba": ("baba-crop", "GÜMRÜKÇÜ BABA"),
    "cano": ("cano-cut", "CANO"),
}


def aud_end(sid):
    s = SCENES[sid]
    return round(s["audio_local"] + s["audio_dur"], 2)


def scoped(sid, css):
    return css.replace("#S ", f"#{sid} ")


# shared pieces: answer bar, characters, speech bubbles, stamps
COMMON_CSS = r"""
#S .ans { position:absolute; left:600px; top:128px; width:1220px; height:96px; display:flex; align-items:center; gap:20px; padding:0 26px;
  background:rgba(46,212,122,.12); border:3px solid var(--ok); border-radius:20px; }
#S .ans .lab { font:900 24px Montserrat; letter-spacing:.14em; color:var(--ok); }
#S .ans .L { flex:none; width:66px; height:66px; border-radius:50%; background:var(--ok); color:#03221a; font:900 38px Montserrat;
  display:flex; align-items:center; justify-content:center; box-shadow:0 0 0 8px rgba(46,212,122,.18); }
#S .ans .tx { font:800 30px Montserrat; color:var(--fg); white-space:nowrap; }
#S .ans .tx em { font-style:normal; color:var(--ok); }
#S .ans .ck { margin-left:auto; color:var(--ok); }
#S .chr { position:absolute; filter:drop-shadow(0 18px 30px rgba(0,0,0,.45)); }
#S .ctag { position:absolute; font:900 19px Montserrat; letter-spacing:.08em; color:#071A45; background:var(--accent2);
  padding:6px 14px; border-radius:10px; box-shadow:0 8px 20px rgba(0,0,0,.35); white-space:nowrap; }
#S .bub { position:absolute; padding:14px 20px; background:#F4F7FF; color:#0B1A44; border-radius:20px; font:900 25px/1.25 Montserrat;
  box-shadow:0 16px 36px rgba(0,0,0,.35); }
#S .bub:after { content:""; position:absolute; left:var(--tail, 60px); bottom:-22px; border:12px solid transparent; border-top:14px solid #F4F7FF; }
#S .bub em { font-style:normal; color:#B4231B; }
#S .bub i { font-style:normal; color:#0B8A47; }
#S .stamp { position:absolute; display:flex; align-items:center; gap:8px; padding:6px 16px 6px 10px; border:6px solid var(--uyari); border-radius:12px;
  color:#FF8A96; background:rgba(42,10,14,.88); font:900 30px Montserrat; letter-spacing:.06em; transform:rotate(-8deg); white-space:nowrap; }
#S .stamp .ico { color:var(--uyari); }
#S .stamp.ok { border-color:var(--ok); color:#BFFFE0; background:rgba(3,34,26,.88); }
#S .stamp.ok .ico { color:var(--ok); }
"""


def answer_bar(letter, text):
    return (f'<div class="ans"><span class="lab">CEVAP</span><span class="L">{letter}</span>'
            f'<span class="tx">{text}</span><span class="ck">{icon("check", 54)}</span></div>')


def char(kind, cls, h):
    src, name = CHAR[kind]
    return f'<img class="chr {cls}" src="assets/img/{src}.png" alt="{name}" style="height:{h}px" />'


# ------------------------------------------------------------------ question scene builder
def qscene(sid, num, stem, opts, *, neg=None, small=False, stem_word, extra_sfx=()):
    """Question card: header + stem + five options read one by one, then a 3-second think countdown."""
    end = aud_end(sid)
    k = dict(soru=T(sid, "soru"), stem=T(sid, stem_word), ops=[round(T(sid, "şıkkı", i) - 0.3, 2) for i in range(1, 6)],
             san=T(sid, "saniye"), end=end)
    if neg:
        k["neg"] = T(sid, neg)
    sfx = [("notification", k["soru"], 0.3), ("whoosh-short", k["stem"] - 0.1, 0.25)]
    sfx += [("pop", t + 0.1, 0.25) for t in k["ops"]]
    sfx += [("click-soft", end + i, 0.55) for i in range(3)] + [("ping", end + 3.0, 0.3)]
    if neg:
        sfx.append(("impact-bass-1", k["neg"], 0.3))
    sfx += list(extra_sfx)
    rows = "".join(f'<div class="op o{i}"><span class="lt">{"ABCDE"[i]}</span><span class="ot">{t}</span></div>' for i, t in enumerate(opts))
    fs = 24 if small else 27
    css = scoped(sid, COMMON_CSS + r"""
#S .qh { position:absolute; left:600px; top:124px; display:flex; align-items:center; gap:22px; }
#S .qh .qn { font-family:'Archivo Black'; font-size:56px; line-height:1; color:var(--fg); white-space:nowrap; }
#S .qh .qn small { font:700 26px 'JetBrains Mono'; color:var(--accent2); margin-left:8px; }
#S .qh .tp { display:inline-flex; align-items:center; gap:10px; font:800 22px Montserrat; color:var(--accent2); border:2px solid rgba(143,178,255,.55);
  border-radius:999px; padding:6px 16px; white-space:nowrap; }
#S .qcol { position:absolute; left:600px; top:216px; width:1220px; display:flex; flex-direction:column; gap:18px; }
#S .stem { position:relative; padding:20px 30px; font:800 32px/1.32 Montserrat; color:var(--fg); }
#S .stem mark { background:none; color:var(--gold); }
#S .stem .neg { position:relative; display:inline-block; color:#FF8A96; }
#S .stem .neg i { position:absolute; left:0; right:0; bottom:-2px; height:5px; border-radius:3px; background:var(--uyari); transform-origin:left center; }
#S .wb { position:absolute; left:1124px; top:124px; display:flex; align-items:center; gap:12px; }
#S .wb > span { font:900 22px Montserrat; color:#FF8A96; white-space:nowrap; }
#S .ops { display:flex; flex-direction:column; gap:11px; }
#S .op { display:flex; align-items:center; gap:22px; padding:10px 24px 10px 12px; background:rgba(13,36,92,.86); border:2px solid #2B4C9E; border-radius:16px; }
#S .op .lt { flex:none; width:52px; height:52px; border-radius:50%; background:var(--accent); color:#fff; display:flex; align-items:center;
  justify-content:center; font:900 28px Montserrat; }
#S .op .ot { font:700 __FS__px/1.28 Montserrat; color:var(--fg); }
#S .op .ot b { font:700 __FS2__px 'JetBrains Mono'; color:var(--gold); }
#S .ring { position:absolute; left:1712px; top:110px; width:108px; height:108px; }
#S .ring svg { position:absolute; inset:0; }
#S .ring .n { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:52px; color:var(--gold); opacity:0; }
#S .think { position:absolute; left:1582px; top:146px; font:900 22px Montserrat; letter-spacing:.12em; color:var(--gold); white-space:nowrap; }
""").replace("__FS__", str(fs)).replace("__FS2__", str(fs + 2))
    body = f'''
<div class="qh"><div class="qn">SORU {num}<small>/ 3</small></div>{badge("soru")}<span class="tp">{icon("layers", 26)}Tarife cetvelinin sistematiği</span></div>
<div class="qcol">
  <div class="stem card">{stem}</div>
  <div class="ops">{rows}</div>
</div>
{'<div class="wb">' + badge("dikkat") + '<span>yanlışı bul!</span></div>' if neg else ''}
<div class="think">DÜŞÜN!</div>
<div class="ring"><svg viewBox="0 0 108 108"><circle cx="54" cy="54" r="46" fill="rgba(4,14,40,.85)" stroke="#2B4C9E" stroke-width="8"/>
  <circle class="arc" cx="54" cy="54" r="46" fill="none" stroke="#FFC53D" stroke-width="8" stroke-linecap="round" transform="rotate(-90 54 54)"/></svg>
  <span class="n n3">3</span><span class="n n2">2</span><span class="n n1">1</span></div>
'''
    js = r"""
tl.fromTo(q(".qh .qn"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "expo.out" }, Math.max(0.05, K.soru - 0.35));
pop(".qh .badge", K.soru + 0.15, 0, "back.out(2.6)");
rise(".qh .tp", K.soru + 0.35, 0, 18);
tl.fromTo(q(".stem"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }, K.stem - 0.25);
tl.fromTo(q(".stem mark"), { color: "#EEF2FF" }, { color: "#FFC53D", duration: 0.4, ease: "power1.out" }, K.stem + 0.2);
K.ops.forEach((t, i) => {
  tl.fromTo(q(".op.o" + i), { x: 70, opacity: 0 }, { x: 0, opacity: 1, duration: 0.5, ease: "expo.out" }, t);
  tl.fromTo(q(".op.o" + i + " .lt"), { scale: 0.3 }, { scale: 1, duration: 0.45, ease: "back.out(3)" }, t + 0.05);
  tl.fromTo(q(".op.o" + i), { borderColor: "#8FB2FF" }, { borderColor: "#2B4C9E", duration: 0.9, ease: "power1.out", immediateRender: false }, t + 0.4);
});
if (K.neg != null) {
  tl.fromTo(q(".stem .neg i"), { scaleX: 0 }, { scaleX: 1, duration: 0.35, ease: "power2.out" }, K.neg);
  tl.to(q(".qh .tp"), { opacity: 0, y: -20, duration: 0.25, ease: "power2.in" }, K.neg - 0.2);
  slam(".wb .badge", K.neg + 0.05);
  rise(".wb > span", K.neg + 0.4, 0, 12);
}
rise(".think", K.san - 0.2, 0, 14);
pop(".ring", K.san - 0.1, 0, "back.out(2.2)");
draw(".ring .arc", K.end, 3.0, "none");
["n3", "n2", "n1"].forEach((n, i) => {
  tl.fromTo(q(".ring ." + n), { opacity: 0, scale: 1.7 }, { opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2)" }, K.end + i);
  tl.to(q(".ring ." + n), { opacity: 0, duration: 0.15 }, K.end + i + 0.85);
});
tl.fromTo(q(".ops"), { opacity: 1 }, { opacity: 0.9, duration: 0.5, yoyo: true, repeat: 3, ease: "sine.inOut" }, K.end);
"""
    S[sid] = dict(sfx=sfx, keys=k, css=css, body=body, js=js)


# ---------------------------------------------------------------- s01 Giriş
TEAM = [("stajyer", 300), ("yardimci", 330), ("baba", 330), ("cano", 318)]
_k1 = dict(hello=T("s01", "Merhaba"), ilk=T("s01", "ilkine"), bugun=T("s01", "Bugün"), bolum=T("s01", "bölüm"), arm=T("s01", "Armonize"),
           olcu=T("s01", "ölçü"), ekip=T("s01", "Ekip"), team=[T("s01", "Stajyer"), T("s01", "Yardımcı"), T("s01", "Gümrükçü"), T("s01", "Cano")],
           kagit=T("s01", "Kâğıt"))
S["s01"] = dict(
    sfx=[("pop", 0.15, 0.35), ("whoosh-short", _k1["hello"] - 0.1, 0.3), ("impact-bass-1", _k1["ilk"], 0.25),
         ("pop", _k1["bolum"], 0.3), ("pop", _k1["arm"], 0.3), ("pop", _k1["olcu"], 0.3), ("whoosh-short", _k1["ekip"] - 0.1, 0.25)]
        + [("pop", t, 0.25) for t in _k1["team"]] + [("ping", _k1["kagit"], 0.3)],
    keys=_k1,
    css=scoped("s01", COMMON_CSS + r"""
#S .sting { position:absolute; left:1000px; top:420px; width:640px; height:150px; display:flex; align-items:center; justify-content:center;
  background:#F4F7FF; border-radius:26px; box-shadow:0 30px 80px rgba(0,0,0,.45); }
#S .sting img { width:520px; }
#S .ttl { position:absolute; left:640px; top:140px; width:1180px; }
#S .ttl .t1 { display:flex; align-items:baseline; gap:24px; margin-top:12px; white-space:nowrap; }
#S .ttl .t1 b { font-family:'Archivo Black'; font-size:84px; line-height:1; color:var(--fg); font-weight:400; }
#S .ttl .t1 span { font-family:'Archivo Black'; font-size:84px; line-height:1; color:var(--gold); text-shadow:0 10px 40px rgba(255,197,61,.35); }
#S .ttl .t2 { margin-top:12px; font:800 30px Montserrat; color:var(--muted); white-space:nowrap; }
#S .ttl .t2 em { font-style:normal; color:var(--teal); }
#S .topics { position:absolute; left:640px; top:352px; width:1180px; display:flex; gap:20px; }
#S .tc { flex:1; height:112px; display:flex; align-items:center; gap:18px; padding:0 22px; }
#S .tc .ico { color:var(--gold); }
#S .tc b { display:block; font:900 24px Montserrat; color:var(--fg); white-space:nowrap; }
#S .tc small { display:block; font:400 19px 'JetBrains Mono'; color:var(--accent2); margin-top:4px; white-space:nowrap; }
#S .tc .nb { margin-left:auto; font-family:'Archivo Black'; font-size:44px; color:rgba(143,178,255,.35); }
#S .team { position:absolute; left:640px; top:498px; width:1180px; height:390px; display:flex; gap:20px; }
#S .slot { position:relative; flex:1; height:390px; }
#S .slot .ped { position:absolute; left:0; right:0; bottom:0; height:150px; border-radius:22px; background:linear-gradient(rgba(63,107,255,.22), rgba(13,36,92,.9));
  border:2px solid rgba(143,178,255,.4); }
#S .slot .chr { position:absolute; left:50%; bottom:46px; transform:translateX(-50%); }
#S .slot .ctag { left:50%; bottom:10px; transform:translateX(-50%); }
#S .ready { position:absolute; left:1480px; top:150px; }
"""),
    body=f'''
<div class="sting"><img src="assets/img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div>
<div class="ttl">
  <div class="kicker">GÜMRÜK KOÇU · TARİFE DERSLERİ</div>
  <div class="t1"><b>TARİFE DERSİ</b><span>#1</span></div>
  <div class="t2">Tarife cetvelinin sistematiği · <em>3 soru</em> · adım adım çözüm</div>
</div>
<div class="topics">
  <div class="tc card c1">{icon("layers", 46)}<div><b>Bölüm &amp; fasıl</b><small>hangi eşya nerede?</small></div></div>
  <div class="tc card c2">{icon("globe", 46)}<div><b>Armonize Sistem</b><small>sınıflandırma mantığı</small></div></div>
  <div class="tc card c3">{icon("ruler", 46)}<div><b>Ölçü birimleri</b><small>kısaltmalar</small></div></div>
</div>
<div class="team">{"".join(f'<div class="slot s{i}"><div class="ped"></div><img class="chr" src="assets/img/{CHAR[c][0]}.png" alt="{CHAR[c][1]}" style="height:{h}px" /><span class="ctag">{CHAR[c][1]}</span></div>' for i, (c, h) in enumerate(TEAM))}</div>
<div class="ready chip">{icon("pen", 30)} Kâğıt + kalem hazır</div>
''',
    js=r"""
tl.fromTo(q(".sting"), { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.6, ease: "back.out(1.8)" }, 0.15);
tl.to(q(".sting"), { scale: 0.85, opacity: 0, y: -40, duration: 0.45, ease: "power2.in" }, K.hello - 0.35);
rise(".ttl .kicker", K.hello, 0, 20);
tl.fromTo(q(".ttl .t1 b"), { y: 70, opacity: 0, skewY: 4 }, { y: 0, opacity: 1, skewY: 0, duration: 0.7, ease: "expo.out" }, K.hello + 0.2);
tl.fromTo(q(".ttl .t1 span"), { scale: 2.4, opacity: 0, transformOrigin: "0% 60%" }, { scale: 1, opacity: 1, duration: 0.5, ease: "expo.in" }, K.ilk - 0.2);
rise(".ttl .t2", K.bugun, 0, 20);
tl.fromTo(q(".tc.c1"), { y: 60, opacity: 0, rotation: -2 }, { y: 0, opacity: 1, rotation: 0, duration: 0.55, ease: "back.out(1.8)" }, K.bolum);
tl.fromTo(q(".tc.c2"), { y: 60, opacity: 0, rotation: 2 }, { y: 0, opacity: 1, rotation: 0, duration: 0.55, ease: "back.out(1.8)" }, K.arm);
tl.fromTo(q(".tc.c3"), { y: 60, opacity: 0, rotation: -2 }, { y: 0, opacity: 1, rotation: 0, duration: 0.55, ease: "back.out(1.8)" }, K.olcu);
rise(".slot .ped", K.ekip - 0.2, 0.08, 40);
K.team.forEach((t, i) => {
  tl.fromTo(q(".slot.s" + i + " .chr"), { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }, t - 0.15);
  pop(".slot.s" + i + " .ctag", t + 0.15, 0, "back.out(2.4)");
});
tl.fromTo(q(".ready"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "back.out(2)" }, K.kagit);
pulse(".ttl .t1 span", K.kagit + 0.6, 1.12);
"""
)

# ---------------------------------------------------------------- s02 Soru 1
qscene("s02", 1,
       'Türk Gümrük Tarife Cetvelinde <mark>adi metaller ve adi metallerden eşya</mark> hangi bölüm ve fasıllarda yer almaktadır?',
       ["On dördüncü bölüm, 71. fasıl", "On altıncı bölüm, 84-85. fasıllar", "On beşinci bölüm, 72-83. fasıllar",
        "On üçüncü bölüm, 68-70. fasıllar", "On yedinci bölüm, 86-89. fasıllar"],
       stem_word="Adi")

# ---------------------------------------------------------------- s03 Çözüm 1
ROMAN = "I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI".split()
NEAR = {12: "68–70", 13: "71", 14: "72–83", 15: "84–85", 16: "86–89"}
FASIL = [("72", "Demir ve çelik", "demir"), ("73", "Demir/çelikten eşya", "çelikle"), ("74", "Bakır", "bakır"), ("75", "Nikel", "nikel"),
         ("76", "Alüminyum", "alüminyum"), ("77", "SAKLI", None), ("78", "Kurşun", "kurşun"), ("79", "Çinko", "çinko"), ("80", "Kalay", "kalay"),
         ("81", "Diğer adi metaller", "diğer"), ("82", "Aletler, bıçakçı eşyası", "aletler"), ("83", "Çeşitli eşya", "çeşitli")]
_k3 = dict(cevap=T("s03", "Cevap"), C=T("s03", "C"), adi=T("s03", "Adi"), xv=T("s03", "beşinci"), yet=T("s03", "yetmiş", 1),
           bolum=T("s03", "Bölüm"), hl=[T("s03", w) if w else None for _, _, w in FASIL], dikkat=T("s03", "Dikkat"),
           y77=T("s03", "yetmiş", 2), bos=T("s03", "boştur"), sakli=T("s03", "saklı"))
S["s03"] = dict(
    sfx=[("chime", _k3["C"], 0.35), ("whoosh-short", _k3["adi"], 0.25), ("impact-bass-1", _k3["xv"], 0.3), ("whoosh-short", _k3["yet"], 0.2)]
        + [("click-soft", t, 0.4) for t in _k3["hl"] if t] + [("error", _k3["dikkat"], 0.25), ("impact-bass-1", _k3["sakli"], 0.25)],
    keys=_k3,
    css=scoped("s03", COMMON_CSS + r"""
#S .strip { position:absolute; left:600px; top:268px; width:1220px; height:64px; }
#S .sec { position:absolute; top:0; width:54px; height:64px; border-radius:10px; display:flex; align-items:center; justify-content:center;
  background:rgba(13,36,92,.9); border:2px solid #2B4C9E; font:700 15px 'JetBrains Mono'; color:#AEBBE3; }
#S .sec.xv { background:var(--gold); border-color:var(--gold); color:#2a1d00; font-size:17px; }
#S .near { position:absolute; top:72px; width:96px; margin-left:-21px; text-align:center; font:700 16px 'JetBrains Mono'; color:#7E8DBA; white-space:nowrap; }
#S .near.xv { color:var(--gold); font-size:18px; }
#S .slab { position:absolute; left:600px; top:238px; font:700 18px 'JetBrains Mono'; letter-spacing:.14em; color:var(--accent2); white-space:nowrap; }
#S svg.ov { position:absolute; left:0; top:0; width:1920px; height:1080px; overflow:visible; }
#S .grid { position:absolute; left:600px; top:420px; width:1220px; display:grid; grid-template-columns:repeat(6, 1fr); gap:12px; }
#S .ft { position:relative; height:132px; border-radius:16px; background:rgba(13,36,92,.92); border:2px solid #2B4C9E; padding:14px 16px; overflow:hidden; }
#S .ft .hl { position:absolute; inset:0; background:linear-gradient(160deg, rgba(51,217,178,.38), rgba(51,217,178,.08)); opacity:0; }
#S .ft .no { position:relative; font-family:'Archivo Black'; font-size:44px; line-height:1; color:var(--fg); }
#S .ft .nm { position:relative; font:800 18px/1.2 Montserrat; color:var(--muted); margin-top:10px; }
#S .ft.f77 { background:repeating-linear-gradient(-45deg, rgba(255,159,67,.10) 0 12px, rgba(13,36,92,.92) 12px 24px); border:2px dashed var(--dikkat); }
#S .ft.f77 .nm { color:var(--dikkat); letter-spacing:.12em; }
#S .gl { position:absolute; left:600px; top:378px; font:900 22px Montserrat; letter-spacing:.1em; color:var(--teal); white-space:nowrap; }
#S .note { position:absolute; left:600px; top:722px; width:1220px; height:150px; display:flex; align-items:center; gap:26px; padding:0 28px;
  border-color:var(--dikkat); background:rgba(255,159,67,.10); }
#S .note .tx { font:800 28px/1.3 Montserrat; color:var(--fg); }
#S .note .tx b { color:var(--dikkat); }
#S .note .tx small { display:block; font:400 20px 'JetBrains Mono'; color:var(--muted); margin-top:6px; }
#S .note .lock { margin-left:auto; color:var(--dikkat); }
#S .sk { position:absolute; left:1660px; top:470px; }
"""),
    body=f'''
{answer_bar("C", "On beşinci bölüm · <em>72–83.</em> fasıllar")}
<div class="slab">21 BÖLÜM · TARİFE CETVELİ</div>
<div class="strip">{"".join(f'<div class="sec{" xv" if i == 14 else ""} r{i}" style="left:{i * 58}px">{r}</div>' for i, r in enumerate(ROMAN))}
  {"".join(f'<div class="near{" xv" if i == 14 else ""} nr{i}" style="left:{i * 58}px">{v}</div>' for i, v in NEAR.items())}</div>
<svg class="ov" aria-hidden="true"><g fill="none" stroke="#FFC53D" stroke-width="3" stroke-dasharray="8 8" stroke-linecap="round" opacity=".8">
  <path class="cn" d="M1412 362 L1000 412"/><path class="cn" d="M1466 362 L1818 412"/></g></svg>
<div class="gl">BÖLÜM XV · ADİ METALLER</div>
<div class="grid">{"".join(f'<div class="ft f{n} t{i}"><span class="hl"></span><div class="no">{n}</div><div class="nm">{nm}</div></div>' for i, (n, nm, _) in enumerate(FASIL))}</div>
<div class="note card">{badge("dikkat")}<div class="tx"><b>Fasıl 77 boş!</b> Armonize Sistemde ileride kullanılmak üzere saklı tutulur.<small>72 … 76 · [77] · 78 … 83</small></div><span class="lock">{icon("shield", 64)}</span></div>
''',
    js=r"""
tl.fromTo(q(".ans"), { y: -40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }, K.cevap - 0.15);
slam(".ans .L", K.C);
pop(".ans .ck", K.C + 0.35, 0, "back.out(3)");
rise(".slab", K.adi - 0.2, 0, 14);
tl.fromTo(q(".sec"), { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.35, ease: "power2.out", stagger: 0.03 }, K.adi - 0.1);
tl.fromTo(q(".sec:not(.xv)"), { opacity: 1 }, { opacity: 0.35, duration: 0.4, immediateRender: false }, K.xv);
tl.fromTo(q(".sec.xv"), { scale: 1 }, { scale: 1.35, duration: 0.3, yoyo: true, repeat: 1, ease: "power2.out", transformOrigin: "50% 50%" }, K.xv);
rise(".near", K.xv + 0.15, 0.06, 12);
fadeIn(".ov .cn", K.yet - 0.1, 0.5);
rise(".gl", K.yet, 0, 16);
tl.fromTo(q(".ft"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.45, ease: "power3.out", stagger: 0.05 }, K.yet + 0.1);
K.hl.forEach((t, i) => {
  if (t == null) return;
  fadeIn(".ft.t" + i + " .hl", t, 0.3);
  pulse(".ft.t" + i + " .no", t, 1.18);
});
tl.fromTo(q(".ft.f77"), { scale: 1 }, { scale: 1.08, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut", transformOrigin: "50% 50%" }, K.dikkat);
tl.fromTo(q(".note"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "back.out(1.6)" }, K.dikkat - 0.1);
slam(".note .badge", K.dikkat);
pop(".note .lock", K.sakli, 0, "back.out(2.6)");
"""
)

# ---------------------------------------------------------------- s04 Tuzak 1
_k4 = dict(tuzak=T("s04", "tuzak"), yard=T("s04", "Yardımcımız"), mak=T("s04", "makineleri"), B=T("s04", "B"), ama=T("s04", "Ama"),
           bir=T("s04", "Bir"), madde=T("s04", "maddeye"), s84=T("s04", "seksen", 4), islev=T("s04", "işlevine"), A=T("s04", "A"),
           kiy=T("s04", "kıymetli", 1), altin=T("s04", "altın"), platin=T("s04", "platin"), ayri=T("s04", "Kıymetli"), adi=T("s04", "adi"))
S["s04"] = dict(
    sfx=[("whoosh-short", _k4["yard"] - 0.1, 0.25), ("pop", _k4["mak"], 0.3), ("error", _k4["ama"], 0.3), ("whoosh-short", _k4["bir"], 0.2),
         ("pop", _k4["madde"], 0.25), ("pop", _k4["islev"], 0.25), ("whoosh-short", _k4["A"], 0.2), ("pop", _k4["kiy"], 0.25),
         ("impact-bass-1", _k4["ayri"], 0.3)],
    keys=_k4,
    css=scoped("s04", COMMON_CSS + r"""
#S .hdr { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:22px; }
#S .hdr .h1 { font-size:46px; margin:0; white-space:nowrap; }
#S .yard { left:1572px; top:330px; }
#S .yardtag { left:1600px; top:850px; }
#S .bub.b1 { left:1520px; top:200px; width:300px; --tail:140px; }
#S .stamp.s1 { left:1574px; top:560px; }
#S .spec { position:absolute; left:600px; top:236px; width:900px; height:268px; padding:22px 28px; }
#S .spec .tt { font:900 22px Montserrat; letter-spacing:.1em; color:var(--accent2); }
#S .bar { position:relative; margin-top:22px; height:96px; display:flex; gap:8px; }
#S .seg { position:relative; height:96px; border-radius:14px; display:flex; align-items:center; gap:14px; padding:0 18px; transform-origin:left center; overflow:hidden; }
#S .seg.m { flex:83; background:rgba(51,217,178,.16); border:3px solid var(--teal); color:var(--teal); }
#S .seg.i { flex:13; min-width:290px; background:rgba(255,197,61,.16); border:3px solid var(--gold); color:var(--gold); }
#S .seg b { font:900 25px Montserrat; white-space:nowrap; }
#S .seg small { display:block; font:700 18px 'JetBrains Mono'; color:var(--fg); opacity:.8; white-space:nowrap; }
#S .ex { display:flex; gap:16px; margin-top:22px; }
#S .ex span { display:inline-flex; align-items:center; gap:10px; font:800 22px Montserrat; padding:8px 16px; border-radius:12px; white-space:nowrap; }
#S .ex .e1 { background:rgba(51,217,178,.12); border:2px solid var(--teal); color:#C9FFF0; }
#S .ex .e2 { background:rgba(255,197,61,.12); border:2px solid var(--gold); color:#FFE7A6; }
#S .ex b { font:700 22px 'JetBrains Mono'; }
#S .vs { position:absolute; left:600px; top:532px; width:900px; height:290px; display:flex; align-items:center; gap:18px; }
#S .mc { flex:1; height:290px; padding:22px 24px; border-radius:22px; }
#S .mc.k { background:rgba(255,197,61,.12); border:3px solid var(--gold); }
#S .mc.a { background:rgba(51,217,178,.10); border:3px solid var(--teal); }
#S .mc .hd { display:flex; align-items:center; gap:14px; }
#S .mc .hd .no { font-family:'Archivo Black'; font-size:46px; line-height:1; }
#S .mc.k .hd { color:var(--gold); } #S .mc.a .hd { color:var(--teal); }
#S .mc > b { display:block; margin-top:8px; font:900 24px Montserrat; letter-spacing:.06em; white-space:nowrap; }
#S .mc.k > b { color:var(--gold); } #S .mc.a > b { color:var(--teal); }
#S .mc ul { list-style:none; margin-top:8px; }
#S .mc li { font:700 23px Montserrat; color:var(--fg); margin-top:6px; white-space:nowrap; }
#S .mc li:before { content:"• "; color:var(--muted); }
#S .neq { flex:none; width:84px; height:84px; border-radius:50%; background:var(--uyari); color:#2a0a0e; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:56px; line-height:1; box-shadow:0 12px 30px rgba(0,0,0,.4); }
"""),
    body=f'''
<div class="hdr">{badge("tuzak")}<div class="h1">Metalden yapılmış ≠ metal faslı</div></div>
<div class="bub b1">Metalden yapılmış… o zaman <em>B şıkkı!</em></div>
{char("yardimci", "yard", 520)}
<span class="ctag yardtag">YARDIMCI</span>
<div class="stamp s1">{icon("x", 34)}YANLIŞ</div>
<div class="spec card"><div class="tt">SINIFLANDIRMA MANTIĞI · GENEL OLARAK</div>
  <div class="bar"><div class="seg m">{icon("box", 44)}<div><b>Fasıl 1–83</b><small>yapıldığı MADDEYE göre</small></div></div>
    <div class="seg i">{icon("gear", 44)}<div><b>Fasıl 84–96</b><small>İŞLEVİNE göre</small></div></div></div>
  <div class="ex"><span class="e1">Çelik vida → <b>73.18</b></span><span class="e2">Torna tezgâhı → <b>84.58</b></span></div></div>
<div class="vs"><div class="mc k"><div class="hd">{icon("gem", 46)}<span class="no">71</span></div><b>KIYMETLİ METALLER</b><ul><li>altın</li><li>gümüş</li><li>platin</li></ul></div>
  <div class="neq">≠</div>
  <div class="mc a"><div class="hd">{icon("box", 46)}<span class="no">72–83</span></div><b>ADİ METALLER</b><ul><li>demir, çelik</li><li>bakır, alüminyum</li><li>çinko, kalay…</li></ul></div></div>
''',
    js=r"""
slam(".hdr .badge", K.tuzak - 0.1);
rise(".hdr .h1", K.tuzak + 0.3, 0, 30);
tl.fromTo(q(".yard"), { x: 260, opacity: 0 }, { x: 0, opacity: 1, duration: 0.7, ease: "expo.out" }, K.yard - 0.2);
pop(".yardtag", K.yard + 0.3, 0, "back.out(2.4)");
tl.fromTo(q(".bub.b1"), { scale: 0.3, opacity: 0, transformOrigin: "50% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.mak - 0.1);
slam(".stamp.s1", K.ama);
tl.fromTo(q(".spec"), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "power3.out" }, K.bir - 0.4);
tl.fromTo(q(".seg.m"), { scaleX: 0, opacity: 0 }, { scaleX: 1, opacity: 1, duration: 0.6, ease: "expo.out" }, K.bir);
tl.fromTo(q(".seg.i"), { scaleX: 0, opacity: 0 }, { scaleX: 1, opacity: 1, duration: 0.6, ease: "expo.out" }, K.s84);
pop(".ex .e1", K.madde, 0, "back.out(2.4)");
pop(".ex .e2", K.islev, 0, "back.out(2.4)");
slideX(".mc.k", K.kiy - 0.2, -60);
rise(".mc.k li", K.altin - 0.1, 0.25, 16);
slideX(".mc.a", K.ayri - 0.3, 60);
rise(".mc.a li", K.ayri, 0.12, 16);
slam(".neq", K.adi - 0.1);
"""
)

# ---------------------------------------------------------------- s05 Soru 2
qscene("s05", 2,
       '<mark>Armonize Sistem</mark> ve tarife cetvelinin sınıflandırma mantığı ile ilgili aşağıdaki ifadelerden hangisi <span class="neg">yanlıştır<i></i></span>?',
       ["Armonize Sistem, merkezi Brüksel’de bulunan Dünya Gümrük Örgütü bünyesinde hazırlanmıştır.",
        "Kodun ilk altı hanesi, sisteme taraf tüm ülkelerde aynı şekilde uygulanır.",
        "Sınıflandırma genel olarak canlıdan cansıza, ham maddeden mamul eşyaya doğru bir sıra izler.",
        "84-96. fasıllardaki eşya, genel olarak işlevine göre sınıflandırılır.",
        "İlk bakışta iki pozisyona girebilen eşya, vergi oranı yüksek olan pozisyonda sınıflandırılır."],
       neg="yanlıştır", small=True, stem_word="Armonize")

# ---------------------------------------------------------------- s06 Çözüm 2
GYK3 = [("a", "En özel tanım", "Eşyayı en özel şekilde tanımlayan pozisyon", "search"),
        ("b", "Esas nitelik", "Eşyaya esas niteliğini veren madde veya parça", "star"),
        ("c", "Numara sırası", "Numara sırasına göre en son gelen pozisyon", "sort")]
_k6 = dict(cevap=T("s06", "Cevap"), E=T("s06", "E"), vergi=T("s06", "vergi"), yok=T("s06", "yoktur"), esya=T("s06", "Eşya"),
           kural=T("s06", "kural"), sira=T("s06", "sırayla"), st=[T("s06", "Önce"), T("s06", "yetmezse"), T("s06", "vermezse")],
           son=T("s06", "son"), diger=T("s06", "Diğer"), dogru=T("s06", "doğrudur"))
S["s06"] = dict(
    sfx=[("chime", _k6["E"], 0.35), ("error", _k6["yok"], 0.3), ("whoosh-short", _k6["esya"], 0.2)]
        + [("pop", t, 0.3) for t in _k6["st"]] + [("ping", _k6["diger"], 0.3)],
    keys=_k6,
    css=scoped("s06", COMMON_CSS + r"""
#S .wrong { position:absolute; left:600px; top:244px; width:1220px; height:86px; display:flex; align-items:center; gap:18px; padding:0 24px;
  border-radius:16px; background:rgba(255,77,94,.10); border:2px solid rgba(255,77,94,.6); }
#S .wrong .lt { flex:none; width:50px; height:50px; border-radius:50%; background:var(--uyari); color:#2a0a0e; display:flex; align-items:center; justify-content:center; font:900 26px Montserrat; }
#S .wrong .ot { position:relative; font:700 25px Montserrat; color:#FFC9CF; white-space:nowrap; }
#S .wrong .ot i { position:absolute; left:0; right:0; top:52%; height:4px; background:var(--uyari); transform-origin:left center; }
#S .no-tax { position:absolute; left:600px; top:350px; width:1220px; height:96px; display:flex; align-items:center; justify-content:center; gap:22px;
  border-radius:18px; background:#14141A; border:4px solid var(--uyari); }
#S .no-tax .pc { position:relative; color:var(--gold); }
#S .no-tax .pc:after { content:""; position:absolute; left:-6px; right:-6px; top:50%; height:7px; background:var(--uyari); transform:rotate(-38deg); border-radius:4px; }
#S .no-tax b { font:900 34px Montserrat; color:var(--fg); letter-spacing:.02em; white-space:nowrap; }
#S .no-tax b em { font-style:normal; color:var(--uyari); }
#S .gk { position:absolute; left:600px; top:470px; display:flex; align-items:center; gap:16px; }
#S .gk .tt { font:900 24px Montserrat; letter-spacing:.1em; color:var(--accent2); white-space:nowrap; }
#S .stairs { position:absolute; left:600px; top:520px; width:1220px; height:300px; }
#S .st { position:absolute; width:350px; height:160px; padding:18px 20px; border-radius:20px; background:rgba(13,36,92,.94); border:3px solid var(--accent); }
#S .st .hd { display:flex; align-items:center; gap:12px; color:var(--accent2); }
#S .st .hd .k { font-family:'Archivo Black'; font-size:32px; line-height:1; color:var(--gold); }
#S .st .hd b { font:900 22px Montserrat; color:var(--fg); white-space:nowrap; }
#S .st p { font:700 21px/1.3 Montserrat; color:var(--muted); margin-top:12px; }
#S .st.s0 { left:0; top:0; } #S .st.s1 { left:435px; top:50px; } #S .st.s2 { left:870px; top:100px; }
#S .ar { position:absolute; width:85px; display:flex; flex-direction:column; align-items:center; font:900 14px Montserrat; letter-spacing:.08em; color:var(--dikkat); white-space:nowrap; }
#S .ar.a0 { left:350px; top:70px; } #S .ar.a1 { left:785px; top:120px; }
#S .ar .ico { color:var(--dikkat); }
#S .okl { position:absolute; left:600px; top:840px; display:flex; align-items:center; gap:12px; }
#S .okl span { display:inline-flex; align-items:center; gap:6px; font:900 22px Montserrat; color:var(--ok); padding:4px 14px 4px 10px; border-radius:10px;
  background:rgba(46,212,122,.12); border:2px solid var(--ok); }
#S .okl small { font:800 22px Montserrat; color:var(--muted); margin-left:6px; white-space:nowrap; }
"""),
    body=f'''
{answer_bar("E", "Vergi oranı, sınıflandırma ölçütü <em>değildir</em>")}
<div class="wrong"><span class="lt">E</span><span class="ot">İki pozisyona girebilen eşya → vergi oranı yüksek olan pozisyon<i></i></span></div>
<div class="no-tax"><span class="pc">{icon("percent", 58)}</span><b>Vergi oranına göre sınıflandırma <em>YOK!</em></b>{badge("uyari")}</div>
<div class="gk"><span class="tt">İKİ POZİSYONA GİREBİLEN EŞYA · GENEL KURAL 3 · SIRAYLA</span></div>
<div class="stairs">
  {"".join(f'<div class="st s{i}"><div class="hd"><span class="k">3({k})</span><b>{t}</b></div><p>{p}</p></div>' for i, (k, t, p, ic) in enumerate(GYK3))}
  <div class="ar a0">{icon("arrow", 54)}OLMAZSA</div><div class="ar a1">{icon("arrow", 54)}OLMAZSA</div>
</div>
<div class="okl">{"".join(f'<span class="c{i}">{icon("check", 22)}{L}</span>' for i, L in enumerate("ABCD"))}<small>diğer dört ifade doğru</small></div>
''',
    js=r"""
tl.fromTo(q(".ans"), { y: -40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }, K.cevap - 0.15);
slam(".ans .L", K.E);
pop(".ans .ck", K.E + 0.35, 0, "back.out(3)");
slideX(".wrong", K.E + 0.4, 60);
tl.fromTo(q(".wrong .ot i"), { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: "power2.inOut" }, K.vergi);
tl.fromTo(q(".no-tax"), { scaleY: 0, opacity: 0, transformOrigin: "50% 0%" }, { scaleY: 1, opacity: 1, duration: 0.45, ease: "back.out(1.6)" }, K.vergi + 0.2);
slam(".no-tax .badge", K.yok);
pulse(".no-tax .pc", K.yok + 0.3, 1.2);
rise(".gk", K.esya - 0.1, 0, 18);
K.st.forEach((t, i) => {
  tl.fromTo(q(".st.s" + i), { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.55, ease: "back.out(1.6)" }, t - 0.2);
  if (i > 0) tl.fromTo(q(".ar.a" + (i - 1)), { x: -30, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: "power2.out" }, t - 0.45);
});
tl.fromTo(q(".st.s2"), { borderColor: "#3F6BFF" }, { borderColor: "#FFC53D", duration: 0.4, immediateRender: false }, K.son);
rise(".okl small", K.diger + 0.2, 0, 14);
tl.fromTo(q(".okl span"), { scale: 0.2, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(2.6)", stagger: 0.12 }, K.diger);
"""
)
