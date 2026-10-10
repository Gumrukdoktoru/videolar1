"""Reusable scene templates for the 3-question tariff lessons (Gümrük Koçu).

Every template takes scene id + content + word anchors; an anchor is a script word ("Cevap"), a (word, n) tuple
for the n-th occurrence, or a number (scene-local seconds). Templates register into S[sid].
"""
from lib import T, D, SCENES, icon, badge

S = {}

CHAR = {  # cutout file, display name, natural aspect (w/h)
    "stajyer": ("stajyer-cut", "STAJYER", 403 / 1150),
    "yardimci": ("yardimci-cut", "YARDIMCI", 565 / 1150),
    "baba": ("baba-crop", "GÜMRÜKÇÜ BABA", 759 / 1882),
    "cano": ("cano-cut", "CANO", 523 / 1143),
}


def A(sid, a, off=0.0):
    if a is None:
        return None
    if isinstance(a, (int, float)):
        return round(a + off, 2)
    if isinstance(a, tuple):
        return T(sid, a[0], a[1], off)
    return T(sid, a, 1, off)


def aud_end(sid):
    s = SCENES[sid]
    return round(s["audio_local"] + s["audio_dur"], 2)


def scoped(sid, css):
    return css.replace("#S ", f"#{sid} ")


COMMON_CSS = r"""
#S .ans { position:absolute; left:600px; top:128px; width:1220px; height:96px; display:flex; align-items:center; gap:20px; padding:0 26px;
  background:rgba(46,212,122,.12); border:3px solid var(--ok); border-radius:20px; }
#S .ans .lab { font:900 24px Montserrat; letter-spacing:.14em; color:var(--ok); }
#S .ans .L { flex:none; width:66px; height:66px; border-radius:50%; background:var(--ok); color:#03221a; font:900 38px Montserrat;
  display:flex; align-items:center; justify-content:center; box-shadow:0 0 0 8px rgba(46,212,122,.18); }
#S .ans .tx { font:800 30px Montserrat; color:var(--fg); white-space:nowrap; }
#S .ans .tx em { font-style:normal; color:var(--ok); }
#S .ans .tx b { font:700 30px 'JetBrains Mono'; color:var(--gold); }
#S .ans .ck { margin-left:auto; color:var(--ok); }
#S .hdr { position:absolute; left:600px; top:128px; display:flex; align-items:center; gap:22px; }
#S .hdr .h1 { font-size:46px; margin:0; white-space:nowrap; }
#S .chr { position:absolute; filter:drop-shadow(0 18px 30px rgba(0,0,0,.45)); }
#S .ctag { position:absolute; font:900 19px Montserrat; letter-spacing:.08em; color:#071A45; background:var(--accent2);
  padding:6px 14px; border-radius:10px; box-shadow:0 8px 20px rgba(0,0,0,.35); white-space:nowrap; }
#S .bub { position:absolute; padding:14px 20px; background:#F4F7FF; color:#0B1A44; border-radius:20px; font:900 24px/1.25 Montserrat;
  box-shadow:0 16px 36px rgba(0,0,0,.35); }
#S .bub:after { content:""; position:absolute; left:var(--tail, 60px); bottom:-22px; border:12px solid transparent; border-top:14px solid #F4F7FF; }
#S .bub em { font-style:normal; color:#B4231B; }
#S .bub i { font-style:normal; color:#0B8A47; }
#S .bub b { font-family:'JetBrains Mono'; }
#S .stamp { position:absolute; display:flex; align-items:center; gap:8px; padding:6px 16px 6px 10px; border:6px solid var(--uyari); border-radius:12px;
  color:#FF8A96; background:rgba(42,10,14,.88); font:900 30px Montserrat; letter-spacing:.06em; transform:rotate(-8deg); white-space:nowrap; }
#S .stamp .ico { color:var(--uyari); }
"""


def answer_bar(letter, text):
    return (f'<div class="ans"><span class="lab">CEVAP</span><span class="L">{letter}</span>'
            f'<span class="tx">{text}</span><span class="ck">{icon("check", 54)}</span></div>')


ANS_JS = r"""
tl.fromTo(q(".ans"), { y: -40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }, K.cevap - 0.15);
slam(".ans .L", K.L);
pop(".ans .ck", K.L + 0.35, 0, "back.out(3)");
"""


# ------------------------------------------------------------------ intro
TEAM = [("stajyer", 300), ("yardimci", 330), ("baba", 330), ("cano", 318)]


def intro(sid, num, subtitle, topics, ordinal):
    """topics: [(icon, title, small, anchor)] x3; ordinal: the word announcing the lesson number (e.g. 'ikincisine')."""
    k = dict(hello=A(sid, "Merhaba"), ilk=A(sid, ordinal), bugun=A(sid, "Bugün"), tp=[A(sid, t[3]) for t in topics],
             ekip=A(sid, "Ekip"), team=[A(sid, "Stajyer"), A(sid, "Yardımcı"), A(sid, "Gümrükçü"), A(sid, "Cano")], kagit=A(sid, "Kâğıt"))
    cards = "".join(f'<div class="tc card c{i}">{icon(ic, 46)}<div><b>{t}</b><small>{sm}</small></div></div>' for i, (ic, t, sm, _) in enumerate(topics))
    team = "".join(f'<div class="slot s{i}"><div class="ped"></div><img class="chr" src="assets/img/{CHAR[c][0]}.png" alt="{CHAR[c][1]}" style="height:{h}px" /><span class="ctag">{CHAR[c][1]}</span></div>' for i, (c, h) in enumerate(TEAM))
    S[sid] = dict(
        sfx=[("pop", 0.15, 0.35), ("whoosh-short", k["hello"] - 0.1, 0.3), ("impact-bass-1", k["ilk"], 0.25)]
            + [("pop", t, 0.3) for t in k["tp"]] + [("whoosh-short", k["ekip"] - 0.1, 0.25)]
            + [("pop", t, 0.25) for t in k["team"]] + [("ping", k["kagit"], 0.3)],
        keys=k,
        css=scoped(sid, COMMON_CSS + r"""
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
  <div class="t1"><b>TARİFE DERSİ</b><span>#{num}</span></div>
  <div class="t2">{subtitle} · <em>3 soru</em> · adım adım çözüm</div>
</div>
<div class="topics">{cards}</div>
<div class="team">{team}</div>
<div class="ready chip">{icon("pen", 30)} Kâğıt + kalem hazır</div>
''',
        js=r"""
tl.fromTo(q(".sting"), { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.6, ease: "back.out(1.8)" }, 0.15);
tl.to(q(".sting"), { scale: 0.85, opacity: 0, y: -40, duration: 0.45, ease: "power2.in" }, K.hello - 0.35);
rise(".ttl .kicker", K.hello, 0, 20);
tl.fromTo(q(".ttl .t1 b"), { y: 70, opacity: 0, skewY: 4 }, { y: 0, opacity: 1, skewY: 0, duration: 0.7, ease: "expo.out" }, K.hello + 0.2);
tl.fromTo(q(".ttl .t1 span"), { scale: 2.4, opacity: 0, transformOrigin: "0% 60%" }, { scale: 1, opacity: 1, duration: 0.5, ease: "expo.in" }, K.ilk - 0.2);
rise(".ttl .t2", K.bugun, 0, 20);
K.tp.forEach((t, i) => {
  tl.fromTo(q(".tc.c" + i), { y: 60, opacity: 0, rotation: i % 2 ? 2 : -2 }, { y: 0, opacity: 1, rotation: 0, duration: 0.55, ease: "back.out(1.8)" }, t);
});
rise(".slot .ped", K.ekip - 0.2, 0.08, 40);
K.team.forEach((t, i) => {
  tl.fromTo(q(".slot.s" + i + " .chr"), { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }, t - 0.15);
  pop(".slot.s" + i + " .ctag", t + 0.15, 0, "back.out(2.4)");
});
tl.fromTo(q(".ready"), { x: 80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "back.out(2)" }, K.kagit);
pulse(".ttl .t1 span", K.kagit + 0.6, 1.12);
""")


# ------------------------------------------------------------------ question
def qscene(sid, num, stem, opts, *, stem_word, topic, neg=None, small=False, mono=False):
    """Question card: header + stem + five options read one by one, then a 3-second think countdown."""
    end = aud_end(sid)
    k = dict(soru=A(sid, "soru"), stem=A(sid, stem_word), ops=[round(T(sid, "şıkkı", i) - 0.3, 2) for i in range(1, 6)],
             san=A(sid, "saniye"), end=end, neg=A(sid, neg))
    sfx = [("notification", k["soru"], 0.3), ("whoosh-short", k["stem"] - 0.1, 0.25)]
    sfx += [("pop", t + 0.1, 0.25) for t in k["ops"]]
    sfx += [("click-soft", end + i, 0.55) for i in range(3)] + [("ping", end + 3.0, 0.3)]
    if neg:
        sfx.append(("impact-bass-1", k["neg"], 0.3))
    rows = "".join(f'<div class="op o{i}"><span class="lt">{"ABCDE"[i]}</span><span class="ot">{t}</span></div>' for i, t in enumerate(opts))
    fs = 24 if small else (30 if mono else 27)
    css = scoped(sid, COMMON_CSS + r"""
#S .qh { position:absolute; left:600px; top:124px; display:flex; align-items:center; gap:22px; }
#S .qh .qn { font-family:'Archivo Black'; font-size:56px; line-height:1; color:var(--fg); white-space:nowrap; }
#S .qh .qn small { font:700 26px 'JetBrains Mono'; color:var(--accent2); margin-left:8px; }
#S .qh .tp { display:inline-flex; align-items:center; gap:10px; font:800 22px Montserrat; color:var(--accent2); border:2px solid rgba(143,178,255,.55);
  border-radius:999px; padding:6px 16px; white-space:nowrap; }
#S .wb { position:absolute; left:1124px; top:124px; display:flex; align-items:center; gap:12px; }
#S .wb > span { font:900 22px Montserrat; color:#FF8A96; white-space:nowrap; }
#S .qcol { position:absolute; left:600px; top:216px; width:1220px; display:flex; flex-direction:column; gap:18px; }
#S .stem { position:relative; padding:20px 30px; font:800 32px/1.32 Montserrat; color:var(--fg); }
#S .stem mark { background:none; color:var(--gold); }
#S .stem .neg { position:relative; display:inline-block; color:#FF8A96; }
#S .stem .neg i { position:absolute; left:0; right:0; bottom:-2px; height:5px; border-radius:3px; background:var(--uyari); transform-origin:left center; }
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
<div class="qh"><div class="qn">SORU {num}<small>/ 3</small></div>{badge("soru")}<span class="tp">{icon("layers", 26)}{topic}</span></div>
{'<div class="wb">' + badge("dikkat") + '<span>yanlışı bul!</span></div>' if neg == "yanlıştır" else ('<div class="wb">' + badge("dikkat") + '<span>dikkatli oku!</span></div>' if neg else '')}
<div class="qcol">
  <div class="stem card">{stem}</div>
  <div class="ops">{rows}</div>
</div>
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


# ------------------------------------------------------------------ solution: which statement is wrong/right
def sol_statements(sid, letter, ans_text, wrong_text, fix_html, fix_tag, others, *, cevap="Cevap", L=None, strike, fix, oth):
    """others: [(letter, text, tag)] x4; oth: anchors for each other card."""
    k = dict(cevap=A(sid, cevap), L=A(sid, L or letter), strike=A(sid, strike), fix=A(sid, fix), oth=[A(sid, a) for a in oth])
    cards = "".join(f'<div class="oc c{i}"><span class="ok">{icon("check", 30)}</span><span class="lt">{l}</span><div class="tx">{t}<small>{tg}</small></div></div>'
                    for i, (l, t, tg) in enumerate(others))
    S[sid] = dict(
        sfx=[("chime", k["L"], 0.35), ("error", k["strike"], 0.25), ("pop", k["fix"], 0.3)] + [("pop", t, 0.25) for t in k["oth"]],
        keys=k,
        css=scoped(sid, COMMON_CSS + r"""
#S .wrong { position:absolute; left:600px; top:244px; width:1220px; height:76px; display:flex; align-items:center; gap:18px; padding:0 24px;
  border-radius:16px; background:rgba(255,77,94,.10); border:2px solid rgba(255,77,94,.6); }
#S .wrong .lt { flex:none; width:48px; height:48px; border-radius:50%; background:var(--uyari); color:#2a0a0e; display:flex; align-items:center; justify-content:center; font:900 25px Montserrat; }
#S .wrong .ot { position:relative; font:700 24px Montserrat; color:#FFC9CF; white-space:nowrap; }
#S .wrong .ot i { position:absolute; left:0; right:0; top:52%; height:4px; background:var(--uyari); transform-origin:left center; }
#S .fix { position:absolute; left:600px; top:338px; width:1220px; height:132px; display:flex; align-items:center; gap:24px; padding:0 28px;
  border-radius:20px; background:rgba(46,212,122,.10); border:3px solid var(--ok); }
#S .fix .lab { flex:none; font:900 22px Montserrat; letter-spacing:.12em; color:var(--ok); }
#S .fix .tx { font:800 28px/1.3 Montserrat; color:var(--fg); }
#S .fix .tx em { font-style:normal; color:var(--ok); }
#S .fix .tg { flex:none; margin-left:auto; font:700 22px 'JetBrains Mono'; color:#03221a; background:var(--ok); border-radius:10px; padding:6px 14px; white-space:nowrap; }
#S .others { position:absolute; left:600px; top:494px; width:1220px; display:grid; grid-template-columns:1fr 1fr; gap:16px; }
#S .oc { height:176px; display:flex; align-items:flex-start; gap:14px; padding:18px 20px; border-radius:18px; background:rgba(13,36,92,.94); border:2px solid #2B4C9E; }
#S .oc .ok { flex:none; width:44px; height:44px; border-radius:50%; background:rgba(46,212,122,.18); color:var(--ok); display:flex; align-items:center; justify-content:center; }
#S .oc .lt { flex:none; font-family:'Archivo Black'; font-size:34px; line-height:44px; color:var(--accent2); }
#S .oc .tx { font:700 21px/1.3 Montserrat; color:var(--fg); }
#S .oc .tx small { display:inline-block; margin-top:8px; font:700 18px 'JetBrains Mono'; color:var(--teal); border:2px solid rgba(51,217,178,.5); border-radius:8px; padding:2px 10px; }
"""),
        body=f'''
{answer_bar(letter, ans_text)}
<div class="wrong"><span class="lt">{letter}</span><span class="ot">{wrong_text}<i></i></span></div>
<div class="fix"><span class="lab">DOĞRUSU</span><div class="tx">{fix_html}</div><span class="tg">{fix_tag}</span></div>
<div class="others">{cards}</div>
''',
        js=ANS_JS + r"""
slideX(".wrong", K.L + 0.3, 60);
tl.fromTo(q(".wrong .ot i"), { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: "power2.inOut" }, K.strike);
tl.fromTo(q(".fix"), { scaleY: 0, opacity: 0, transformOrigin: "50% 0%" }, { scaleY: 1, opacity: 1, duration: 0.45, ease: "back.out(1.6)" }, K.fix - 0.2);
pop(".fix .tg", K.fix + 0.5, 0, "back.out(2.6)");
K.oth.forEach((t, i) => {
  tl.fromTo(q(".oc.c" + i), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.45, ease: "back.out(1.6)" }, t - 0.2);
  pop(".oc.c" + i + " .ok", t + 0.1, 0, "back.out(3)");
});
""")


# ------------------------------------------------------------------ solution: classification path
def sol_classify(sid, letter, ans_text, product, steps, result, cands, *, cevap="Cevap", L=None, cand_at):
    """product: dict(icon, name, chips=[(text, anchor)], at); steps: [(icon, title, text, anchor)] x3;
    result: dict(code, title, at); cands: [(code, label, ok)] x5; cand_at: anchor for the candidate strip."""
    k = dict(cevap=A(sid, cevap), L=A(sid, L or letter), prod=A(sid, product["at"]), chips=[A(sid, a) for _, a in product["chips"]],
             st=[A(sid, s[3]) for s in steps], res=A(sid, result["at"]), cand=A(sid, cand_at))
    chips = "".join(f'<span class="cp p{i}">{t}</span>' for i, (t, _) in enumerate(product["chips"]))
    stp = "".join(f'<div class="st s{i}"><span class="nb">{i + 1}</span>{icon(ic, 34)}<div><b>{t}</b><small>{x}</small></div></div>' for i, (ic, t, x, _) in enumerate(steps))
    cnd = "".join(f'<div class="cd {"ok" if ok else "no"}"><b>{c}</b><small>{lb}</small><span class="mk">{icon("check" if ok else "x", 26)}</span></div>' for c, lb, ok in cands)
    S[sid] = dict(
        sfx=[("chime", k["L"], 0.35), ("whoosh-short", k["prod"], 0.25)] + [("pop", t, 0.25) for t in k["chips"]]
            + [("pop", t, 0.3) for t in k["st"]] + [("impact-bass-1", k["res"], 0.3), ("whoosh-short", k["cand"], 0.2)],
        keys=k,
        css=scoped(sid, COMMON_CSS + r"""
#S .prod { position:absolute; left:600px; top:250px; width:350px; height:370px; padding:22px; border-radius:22px; background:rgba(13,36,92,.95); border:3px solid var(--accent2); }
#S .prod .ic { color:var(--gold); }
#S .prod .nm { font:900 25px/1.25 Montserrat; color:var(--fg); margin-top:12px; }
#S .prod .chips { display:flex; flex-direction:column; align-items:flex-start; gap:8px; margin-top:14px; }
#S .prod .cp { font:800 19px Montserrat; color:#C9FFF0; background:rgba(51,217,178,.14); border:2px solid var(--teal); border-radius:10px; padding:4px 12px; white-space:nowrap; }
#S .steps { position:absolute; left:1000px; top:250px; width:440px; display:flex; flex-direction:column; gap:12px; }
#S .st { height:115px; display:flex; align-items:center; gap:14px; padding:0 18px; border-radius:18px; background:rgba(13,36,92,.95); border:2px solid #2B4C9E; }
#S .st .nb { flex:none; width:38px; height:38px; border-radius:50%; background:var(--accent); color:#fff; display:flex; align-items:center; justify-content:center; font:900 20px Montserrat; }
#S .st .ico { color:var(--accent2); }
#S .st b { display:block; font:900 21px Montserrat; color:var(--fg); }
#S .st small { display:block; font:700 18px/1.25 Montserrat; color:var(--muted); margin-top:4px; }
#S .res { position:absolute; left:1480px; top:250px; width:340px; height:370px; padding:24px; border-radius:22px; background:rgba(46,212,122,.12); border:3px solid var(--ok);
  display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }
#S .res .lab { font:900 20px Montserrat; letter-spacing:.14em; color:var(--ok); }
#S .res .cd0 { font-family:'Archivo Black'; font-size:84px; line-height:1; color:var(--fg); margin-top:12px; }
#S .res .tt { font:800 20px/1.3 Montserrat; color:var(--muted); margin-top:14px; }
#S .res .ico { color:var(--ok); margin-top:10px; }
#S .ar { position:absolute; top:410px; color:var(--gold); }
#S .ar.a0 { left:954px; } #S .ar.a1 { left:1442px; }
#S .cands { position:absolute; left:600px; top:650px; width:1220px; display:flex; gap:14px; }
#S .cd { position:relative; flex:1; height:150px; padding:16px; border-radius:18px; background:rgba(13,36,92,.9); border:2px solid #2B4C9E; }
#S .cd b { display:block; font:700 34px 'JetBrains Mono'; color:var(--fg); }
#S .cd small { display:block; font:700 18px/1.25 Montserrat; color:var(--muted); margin-top:8px; }
#S .cd .mk { position:absolute; right:12px; top:12px; width:38px; height:38px; border-radius:50%; display:flex; align-items:center; justify-content:center; }
#S .cd.no .mk { background:rgba(255,77,94,.2); color:var(--uyari); }
#S .cd.ok { border:3px solid var(--ok); background:rgba(46,212,122,.12); }
#S .cd.ok b { color:var(--ok); }
#S .cd.ok .mk { background:var(--ok); color:#03221a; }
"""),
        body=f'''
{answer_bar(letter, ans_text)}
<div class="prod"><span class="ic">{icon(product["icon"], 84)}</span><div class="nm">{product["name"]}</div><div class="chips">{chips}</div></div>
<span class="ar a0">{icon("arrow", 44)}</span>
<div class="steps">{stp}</div>
<span class="ar a1">{icon("arrow", 36)}</span>
<div class="res"><span class="lab">POZİSYON</span><div class="cd0">{result["code"]}</div><div class="tt">{result["title"]}</div>{icon("check", 54)}</div>
<div class="cands">{cnd}</div>
''',
        js=ANS_JS + r"""
tl.fromTo(q(".prod"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "expo.out" }, K.prod - 0.2);
pop(".prod .ic", K.prod, 0, "back.out(2.2)");
K.chips.forEach((t, i) => pop(".prod .cp.p" + i, t, 0, "back.out(2.6)"));
pop(".ar.a0", K.st[0] - 0.4, 0, "back.out(2)");
K.st.forEach((t, i) => tl.fromTo(q(".st.s" + i), { x: 60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.5, ease: "expo.out" }, t - 0.2));
pop(".ar.a1", K.res - 0.4, 0, "back.out(2)");
tl.fromTo(q(".res"), { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.5, ease: "back.out(1.8)" }, K.res - 0.2);
pulse(".res .cd0", K.res + 0.5, 1.1);
tl.fromTo(q(".cd"), { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.45, ease: "power3.out", stagger: 0.1 }, K.cand);
pop(".cd .mk", K.cand + 0.6, 0.1, "back.out(3)");
""")


# ------------------------------------------------------------------ trap
def trap(sid, title, who, bubble, wrong, right, tagline, *, note=None, who2=None, at):
    """who: (char, height); who2: optional (char, height, bubble_html) that replaces the first character;
    wrong/right: dict(code, title, sub, icon); note: optional (badge_kind, html);
    at: dict(tuzak, who, bub, hayir, wrong, right, note, who2, tag) anchors."""
    k = {n: A(sid, a) for n, a in at.items()}
    ch, h = who
    w = round(CHAR[ch][2] * h)
    left = 1690 - w // 2
    def card(c, cls):
        return f'<div class="uc {cls}"><div class="ab">{c["code"]}</div>{icon(c["icon"], 46)}<b>{c["title"]}</b><small>{c["sub"]}</small></div>'
    second = ""
    if who2:
        c2, h2, b2 = who2
        w2 = round(CHAR[c2][2] * h2)
        second = (f'<div class="bub b2">{b2}</div><img class="chr ch2" src="assets/img/{CHAR[c2][0]}.png" alt="{CHAR[c2][1]}" '
                  f'style="height:{h2}px; left:{1690 - w2 // 2}px; top:{860 - h2}px" /><span class="ctag t2">{CHAR[c2][1]}</span>')
    note_html = f'<div class="note card">{badge(note[0])}<div class="tx">{note[1]}</div></div>' if note else ""
    sfx = [("whoosh-short", k["who"] - 0.1, 0.25), ("pop", k["bub"], 0.3), ("error", k["hayir"], 0.3), ("pop", k["wrong"], 0.25),
           ("pop", k["right"], 0.25), ("impact-bass-1", k["tag"], 0.3)]
    if note:
        sfx.append(("notification", k["note"], 0.25))
    if who2:
        sfx.append(("whoosh-short", k["who2"] - 0.1, 0.25))
    S[sid] = dict(
        sfx=sfx, keys=k,
        css=scoped(sid, COMMON_CSS + r"""
#S .ch1 { left:__L__px; top:__T__px; }
#S .ctag.t1, #S .ctag.t2 { left:1690px; top:866px; transform:translateX(-50%); }
#S .bub { left:1520px; top:200px; width:300px; --tail:150px; }
#S .stamp { left:1576px; top:560px; }
#S .pair { position:absolute; left:600px; top:250px; width:900px; height:210px; display:flex; align-items:center; gap:18px; }
#S .uc { position:relative; flex:1; height:210px; padding:18px 22px; border-radius:20px; background:rgba(13,36,92,.94); border:3px solid #2B4C9E; }
#S .uc .ab { font:700 46px 'JetBrains Mono'; line-height:1; color:var(--gold); }
#S .uc b { display:block; font:900 24px/1.2 Montserrat; color:var(--fg); margin-top:14px; }
#S .uc small { display:block; font:700 18px/1.3 Montserrat; color:var(--muted); margin-top:6px; }
#S .uc .ico { position:absolute; right:20px; top:20px; color:var(--accent2); }
#S .uc.w { border-color:rgba(255,77,94,.75); background:rgba(255,77,94,.08); } #S .uc.w .ab { color:#FF8A96; }
#S .uc.r { border-color:var(--ok); background:rgba(46,212,122,.10); } #S .uc.r .ab { color:var(--ok); }
#S .ne { flex:none; width:76px; height:76px; border-radius:50%; background:var(--uyari); color:#2a0a0e; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:50px; line-height:1; }
#S .note { position:absolute; left:600px; top:486px; width:900px; height:220px; display:flex; align-items:center; gap:22px; padding:0 26px;
  border-color:var(--dikkat); background:rgba(255,159,67,.10); }
#S .note .tx { font:800 25px/1.35 Montserrat; color:var(--fg); }
#S .note .tx em { font-style:normal; color:var(--dikkat); }
#S .note .tx b { font:700 25px 'JetBrains Mono'; color:var(--gold); }
#S .tag { position:absolute; left:600px; top:734px; width:900px; height:116px; display:flex; align-items:center; justify-content:center; gap:20px;
  border-radius:20px; background:#14141A; border:4px solid #FFD400; padding:0 24px; }
#S .tag b { font-family:'Archivo Black'; font-weight:400; font-size:34px; line-height:1.15; color:#FFD400; text-align:center; }
#S .tag .ico { color:#FFD400; }
""").replace("__L__", str(left)).replace("__T__", str(860 - h)),
        body=f'''
<div class="hdr">{badge("tuzak")}<div class="h1">{title}</div></div>
<div class="bub b1">{bubble}</div>
<img class="chr ch1" src="assets/img/{CHAR[ch][0]}.png" alt="{CHAR[ch][1]}" style="height:{h}px" />
<span class="ctag t1">{CHAR[ch][1]}</span>
<div class="stamp">{icon("x", 34)}HAYIR</div>
{second}
<div class="pair">{card(wrong, "w")}<div class="ne">≠</div>{card(right, "r")}</div>
{note_html}
<div class="tag">{icon("trap", 44)}<b>{tagline}</b></div>
''',
        js=r"""
slam(".hdr .badge", K.tuzak - 0.1);
rise(".hdr .h1", K.tuzak + 0.3, 0, 30);
tl.fromTo(q(".ch1"), { x: 220, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.who - 0.2);
pop(".ctag.t1", K.who + 0.2, 0, "back.out(2.4)");
tl.fromTo(q(".bub.b1"), { scale: 0.3, opacity: 0, transformOrigin: "50% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.bub);
slam(".stamp", K.hayir);
slideX(".uc.w", K.wrong - 0.2, -60);
pop(".ne", K.right - 0.4, 0, "back.out(2.6)");
slideX(".uc.r", K.right - 0.2, 60);
if (K.note != null) tl.fromTo(q(".note"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }, K.note - 0.2);
if (K.note != null) slam(".note .badge", K.note);
if (K.who2 != null) {
  tl.to(q(".ch1, .ctag.t1, .bub.b1, .stamp"), { opacity: 0, x: 60, duration: 0.35, ease: "power2.in" }, K.who2 - 0.4);
  tl.fromTo(q(".ch2"), { x: 220, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.who2 - 0.1);
  pop(".ctag.t2", K.who2 + 0.3, 0, "back.out(2.4)");
  tl.fromTo(q(".bub.b2"), { scale: 0.3, opacity: 0, transformOrigin: "50% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, K.who2 + 0.5);
}
tl.fromTo(q(".tag"), { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }, K.tag - 0.1);
""")


# ------------------------------------------------------------------ coach note (mindmap)
def coach(sid, nodes, *, core="TARİFE<br/>MANTIĞI", motto=("ezber", "mantık"), at_koc="Koçun", at_motto=None, br):
    """nodes: [(title, [lines], icon)] x3; br: anchors for each branch."""
    k = dict(koc=A(sid, at_koc), motto=A(sid, at_motto) if at_motto else A(sid, at_koc, 1.0), br=[A(sid, a) for a in br])
    nd = "".join(f'<div class="nd n{i}"><div class="hd"><span class="num">{i + 1}</span>{icon(ic, 30)}{t}</div><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul></div>' for i, (t, li, ic) in enumerate(nodes))
    S[sid] = dict(
        sfx=[("whoosh-short", k["koc"], 0.25), ("impact-bass-1", k["motto"], 0.25)] + [("pop", t, 0.3) for t in k["br"]],
        keys=k,
        css=scoped(sid, COMMON_CSS + r"""
#S .hdr .h1 { font-size:50px; }
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
#S .nd li { font:700 21px/1.3 Montserrat; color:var(--fg); margin-top:4px; }
#S .nd li:before { content:"▸ "; color:var(--teal); }
#S .nd.n0 { left:600px; top:250px; }
#S .nd.n1 { left:1400px; top:250px; border-color:var(--gold); } #S .nd.n1 .hd { color:var(--gold); } #S .nd.n1 .hd .num { background:var(--gold); color:#2a1d00; } #S .nd.n1 li:before { color:var(--gold); }
#S .nd.n2 { left:1000px; top:724px; border-color:var(--dikkat); } #S .nd.n2 .hd { color:var(--dikkat); } #S .nd.n2 .hd .num { background:var(--dikkat); color:#2b1300; } #S .nd.n2 li:before { color:var(--dikkat); }
"""),
        body=f'''
<div class="hdr">{badge("ipucu")}<div class="h1">Koçun notu</div></div>
<div class="motto"><s>{motto[0]}</s>{icon("arrow", 30)}<em>{motto[1]}</em></div>
<svg class="mm" aria-hidden="true"><g fill="none" stroke-width="5" stroke-linecap="round">
  <path class="l0" d="M1100 500 C1040 470 1030 430 1020 410" stroke="#33D9B2"/>
  <path class="l1" d="M1320 500 C1380 470 1390 430 1400 410" stroke="#FFC53D"/>
  <path class="l2" d="M1210 680 C1210 700 1210 708 1210 722" stroke="#FF9F43"/></g></svg>
<div class="core"><b>{core}</b><small>3 KURAL</small></div>
{nd}
''',
        js=r"""
slam(".hdr .badge", K.koc - 0.1);
rise(".hdr .h1", K.koc + 0.2, 0, 30);
rise(".motto", K.motto - 0.2, 0, 16);
pulse(".motto em", K.motto + 0.4, 1.2);
pop(".core", K.koc + 0.6, 0, "back.out(1.8)");
breathe(".core", K.koc + 1.2, D - 0.5, 0.03, 2.4);
K.br.forEach((t, i) => {
  draw(".mm .l" + i, t - 0.2, 0.5);
  tl.fromTo(q(".nd.n" + i), { scale: 0.5, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.5, ease: "back.out(1.8)" }, t + 0.1);
  rise(".nd.n" + i + " li", t + 0.5, 0.35, 12);
});
""")


# ------------------------------------------------------------------ answer key
def answer_key(sid, keys, next_num):
    """keys: [(letter, title, sub)] x3."""
    k = dict(bug=A(sid, "Bugünün"), qs=[A(sid, L) for L, _, _ in keys], kac=A(sid, "Kaç"), yor=A(sid, "Yorumlara"),
             abone=A(sid, "abone"), pay=A(sid, "paylaşmayı"), sonraki=A(sid, "sonraki"), hosca=A(sid, "Hoşça"))
    crew = "".join(f'<img class="chr c{i}" src="assets/img/{CHAR[c][0]}.png" alt="{CHAR[c][1]}" style="height:{h}px" />'
                   for i, (c, h) in enumerate([("stajyer", 262), ("yardimci", 280), ("baba", 290), ("cano", 272)]))
    S[sid] = dict(
        sfx=[("whoosh-short", k["bug"], 0.25)] + [("chime", t, 0.3) for t in k["qs"]]
            + [("pop", k["kac"], 0.3), ("pop", k["abone"], 0.3), ("pop", k["pay"], 0.3), ("ping", k["hosca"], 0.3)],
        keys=k, exit=False,
        css=scoped(sid, COMMON_CSS + r"""
#S .hdr .h1 { font-size:54px; }
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
<div class="keys">{"".join(f'<div class="kc k{i}"><div class="qn">SORU {i + 1}</div><div class="L">{L}</div><b>{t}</b><small>{s}</small></div>' for i, (L, t, s) in enumerate(keys))}</div>
<div class="score card">{icon("pen", 40)}<div class="tx">Kaç tanesini <em>bildin?</em></div><div class="bx"><i></i><i></i><i></i></div></div>
<div class="cta"><span class="chip c1">{icon("mail", 30)} Yorumlara yaz</span><span class="chip c2">{icon("bell", 30)} Abone ol</span><span class="chip c3">{icon("share", 30)} Paylaş</span></div>
<div class="nxt">Sıradaki: <b>Tarife Dersi #{next_num}</b> · yeni 3 soru</div>
<div class="crew">{crew}</div>
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
""")
