"""Answer slides (3,5,7,9,11,13), topic mind map (14) and answer key (15)."""
from theme import ICON, CYAN, AMBER, GREEN, RED

CSS2 = r"""
/* ---------- answer slides ---------- */
.ahead { display:flex; gap:26px; align-items:center; }
.ahead .bub { width:112px; height:112px; font-size:52px; border-width:5px; }
.ahead small { display:block; font:700 18px 'JetBrains Mono'; letter-spacing:.22em; color:var(--green); }
.ahead h2 { font:800 39px/1.14 Unbounded; color:#fff; margin-top:8px; letter-spacing:-.01em; }
.ahead h2 em { font-style:normal; color:var(--cyan); text-shadow:0 0 24px rgba(47,230,210,.35); }
.rule { margin-top:22px; display:flex; gap:18px; align-items:center; padding:16px 22px; }
.rule p { font:600 23px/1.38 Montserrat; color:var(--txt); }
.rule p b { color:#fff; font-weight:800; }
.trap { margin-top:20px; display:flex; gap:16px; align-items:center; padding:12px 20px 12px 10px; border:2px dashed var(--amber); border-radius:18px; background:rgba(40,26,4,.78); }
.trap p { font:600 22.5px/1.38 Montserrat; color:#FFE9C2; }
.trap p b { color:#fff; font-weight:800; }
.trap.dikkat { border-color:#FF8A3D; background:rgba(44,18,4,.8); }
.trap .stamp { flex:none; }
.note { margin-top:18px; display:flex; gap:16px; align-items:center; padding:14px 20px; border-radius:16px; background:rgba(60,8,20,.72); border:2px solid var(--red); }
.note .tag { flex:none; font:900 17px Unbounded; color:#fff; background:var(--red); padding:8px 12px; border-radius:6px; letter-spacing:.06em; }
.note p { font:600 22.5px/1.36 Montserrat; color:#FFE1E7; }
.note p b { color:#fff; }
.bub.sm { width:42px; height:42px; font-size:18px; border-width:2.5px; }
.pill { flex:none; font:900 16px Unbounded; padding:8px 12px; border-radius:999px; letter-spacing:.04em; }
.pill.yes { background:#D7F8E6; color:#05622F; border:2px solid #22B566; }
.pill.no { background:var(--red); color:#fff; box-shadow:0 0 0 4px rgba(255,77,109,.25); }

/* A1 matrix + schematic */
.a1 { margin-top:20px; display:flex; gap:20px; }
.mx { flex:1; padding:14px 18px 10px; }
.mxh { display:flex; justify-content:space-between; font:700 14px 'JetBrains Mono'; letter-spacing:.16em; color:var(--muted); padding:0 4px 8px; border-bottom:2px solid #D3E3EA; }
.mr { display:flex; align-items:center; gap:12px; padding:11px 4px; border-bottom:1px dashed #C9DCE4; }
.mr:last-child { border-bottom:0; }
.mr .ic { color:var(--ink2); }
.mr p { flex:1; font:700 20.5px/1.25 Montserrat; color:var(--ink); }
.mr p small { display:block; font:600 15px 'JetBrains Mono'; color:var(--muted); letter-spacing:.04em; margin-top:2px; }
.mr.hit { background:linear-gradient(90deg,#FFE3E9,#FFF5F7); border-radius:14px; border:2px solid var(--red); padding:11px 8px; margin-top:4px; }
.mr.hit .ic { color:#C2183A; }
.mr.tr p small { color:#A15C00; }
.sch { width:372px; flex:none; padding:10px; display:flex; align-items:center; justify-content:center; }

/* A2 law + timeline */
.lawq { margin-top:22px; padding:22px 28px 22px 30px; font:600 29px/1.48 Montserrat; }
.lawq .tab { position:absolute; right:20px; top:-16px; font:800 16px 'JetBrains Mono'; letter-spacing:.12em; background:var(--ink); color:var(--cyan); padding:6px 12px; border-radius:6px; }
mark { background:linear-gradient(180deg, transparent 8%, rgba(47,230,210,.55) 8%, rgba(47,230,210,.55) 92%, transparent 92%); color:var(--ink); font-weight:800; padding:0 6px; border-radius:4px; }
.tl { margin-top:22px; padding:6px 0 0; }
.ns { margin-top:18px; display:flex; gap:12px; align-items:center; flex-wrap:wrap; }
.ns .h { flex-basis:100%; }
.ns .h { font:800 17px 'JetBrains Mono'; letter-spacing:.14em; color:var(--red); margin-right:4px; }
.ns span.x { display:inline-flex; align-items:center; gap:8px; font:700 20px Montserrat; color:#FFE1E7; padding:8px 14px 8px 8px; border-radius:999px; background:rgba(60,8,20,.75); border:1.5px solid rgba(255,77,109,.6); }
.ns span.x i { font:900 15px Unbounded; font-style:normal; background:var(--red); color:#fff; border-radius:50%; width:30px; height:30px; display:flex; align-items:center; justify-content:center; }
.term { display:inline-block; font:900 18px Unbounded; padding:6px 10px; border-radius:6px; margin:0 2px; }
.term.bad { color:#FF9AAD; border:2px solid var(--red); text-decoration:line-through; text-decoration-thickness:3px; }
.term.ok { color:#04210F; background:var(--green); }
.sub2 { margin-top:16px; font:600 21px/1.4 Montserrat; color:rgba(230,244,250,.86); padding-left:18px; border-left:4px solid var(--cyan); }
.sub2 b { color:#fff; }

/* wire diagrams */
.wire { position:relative; }
.wire svg.lines { position:absolute; left:0; top:0; overflow:visible; pointer-events:none; }

/* A3 exits */
.a3w { margin-top:22px; height:470px; }
.zone { position:absolute; left:0; top:10px; width:410px; height:450px; border-radius:50%; border:3px dashed var(--cyan);
  background:radial-gradient(circle at 50% 45%, rgba(47,230,210,.20), rgba(8,24,46,.92) 70%); display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }
.zone small { font:800 17px 'JetBrains Mono'; letter-spacing:.2em; color:var(--cyan); }
.zone .eye { color:var(--cyan); margin:6px 0 10px; }
.zone .wh { width:280px; padding:14px 14px 12px; border-radius:16px; background:#fff; color:var(--ink); position:relative; }
.zone .wh .ic { margin:0 auto; color:var(--ink); }
.zone .wh b { display:block; font:900 20px Unbounded; margin-top:6px; }
.zone .wh span { display:block; font:600 17px/1.3 Montserrat; color:var(--ink2); margin-top:4px; }
.zone .wh .xb { position:absolute; right:-16px; top:-16px; background:var(--red); color:#fff; font:900 16px Unbounded; padding:7px 10px; border-radius:8px; transform:rotate(6deg); }
.zone .lp { font:700 17px Montserrat; color:var(--cyan2); margin-top:12px; }
.door { position:absolute; left:470px; width:498px; display:flex; align-items:center; gap:14px; padding:14px 16px; border-radius:16px; background:var(--paper); color:var(--ink); }
.door .ic { color:#0E7A6E; }
.door p { flex:1; font:800 22px/1.2 Montserrat; }
.door p small { display:block; font:600 15px 'JetBrains Mono'; color:var(--muted); letter-spacing:.06em; margin-top:3px; }
.door .ok { flex:none; width:36px; height:36px; border-radius:50%; background:var(--green); color:#03200F; display:flex; align-items:center; justify-content:center; }
.door.tr { box-shadow:0 0 0 3px var(--amber); }
.door.tr p small { color:#A15C00; }
.gk47 { margin-top:18px; padding:16px 22px; font:600 21.5px/1.4 Montserrat; display:flex; gap:16px; align-items:center; }
.gk47 .ref { color:var(--ink); border-color:#9BC3CF; background:#E3F1F5; }

/* A4 rail + fix table */
.rail { margin-top:22px; padding:4px 0 0; }
.fix { margin-top:20px; padding:10px 18px 6px; }
.fh, .fr { display:grid; grid-template-columns:52px 1fr 1.25fr; gap:14px; align-items:center; }
.fh { font:700 14px 'JetBrains Mono'; letter-spacing:.16em; color:var(--muted); padding:6px 0 8px; border-bottom:2px solid #D3E3EA; }
.fr { padding:13px 0; border-bottom:1px dashed #C9DCE4; }
.fr:last-child { border-bottom:0; }
.fr .was { font:600 21px/1.3 Montserrat; color:#7A2A3A; }
.fr .was b { color:#B0122B; text-decoration:line-through; text-decoration-thickness:2.5px; }
.fr .is { font:700 21px/1.3 Montserrat; color:var(--ink); padding-left:14px; border-left:4px solid #22B566; }
.fr .is b { color:#05622F; }
.fr.good { background:#E2FAEC; border-radius:12px; border-bottom:0; margin:4px 0; padding:11px 6px; }
.fr.good .was { color:#05622F; }

/* A5 flow */
.a5 { margin-top:22px; display:flex; gap:20px; align-items:stretch; }
.flow { flex:1.32; padding:18px 18px 14px; }
.stp { display:flex; gap:14px; align-items:flex-start; position:relative; padding-bottom:26px; }
.stp:last-child { padding-bottom:0; }
.stp:not(:last-child):after { content:""; position:absolute; left:25px; top:54px; bottom:2px; border-left:3px dashed var(--cyan); }
.stp .no { flex:none; width:52px; height:52px; border-radius:50%; background:rgba(47,230,210,.14); border:2.5px solid var(--cyan); color:var(--cyan); display:flex; align-items:center; justify-content:center; }
.stp p { font:600 23px/1.36 Montserrat; color:var(--txt); padding-top:2px; }
.stp p b { color:#fff; }
.stp .t { display:inline-block; font:900 14px Unbounded; padding:4px 8px; border-radius:6px; margin-left:6px; vertical-align:2px; }
.stp .t.g { background:var(--green); color:#03200F; }
.stp .t.r { background:var(--red); color:#fff; }
.stp.key .no { background:var(--green); border-color:var(--green); color:#03200F; box-shadow:0 0 18px rgba(46,224,122,.6); }
.stp.key p { background:rgba(46,224,122,.12); border:2px solid var(--green); border-radius:14px; padding:10px 14px; }
.stp s { color:#FF9AAD; text-decoration-thickness:3px; text-decoration-color:var(--red); }
.prep { flex:1; padding:18px 18px 14px; }
.prep h4 { font:900 21px Unbounded; color:var(--ink); }
.prep .ref { color:var(--ink); border-color:#9BC3CF; background:#E3F1F5; font-size:15px; margin-top:8px; }
.prep ul { list-style:none; margin-top:10px; }
.prep li { display:flex; gap:10px; align-items:flex-start; font:600 21px/1.34 Montserrat; color:var(--ink2); padding:9px 0; border-bottom:1px dashed #C9DCE4; }
.prep li:last-child { border-bottom:0; }
.prep li b { color:var(--ink); }
.prep li .k { flex:none; font:900 14px Unbounded; background:var(--green); color:#03200F; border-radius:6px; padding:4px 7px; margin-top:2px; }

/* A6 change window */
.win { margin-top:24px; padding:24px 20px 22px; display:flex; align-items:center; gap:0; }
.win .key { width:236px; flex:none; padding:16px 14px; border-radius:16px; background:#E2FAEC; color:var(--ink); text-align:center; border:2.5px solid var(--green); }
.win .key .ic { margin:0 auto; color:#0B8A47; }
.win .key b { display:block; font:900 19px Unbounded; margin-top:6px; color:#05622F; }
.win .key span { display:block; font:700 18px/1.3 Montserrat; margin-top:4px; }
.win .key em { display:inline-block; font-style:normal; font:800 15px 'JetBrains Mono'; letter-spacing:.06em; background:var(--green); color:#03200F; padding:4px 8px; border-radius:6px; margin-top:8px; }
.win .band { flex:none; width:250px; height:150px; margin:0 -6px 0 10px; clip-path:polygon(0 0, 84% 0, 100% 50%, 84% 100%, 0 100%, 8% 50%);
  background:linear-gradient(90deg, rgba(46,224,122,.85), rgba(46,224,122,.25)); display:flex; flex-direction:column; justify-content:center; padding:0 46px 0 34px; }
.win .band b { font:900 19px/1.15 Unbounded; color:#03200F; }
.win .band span { font:700 17px/1.25 Montserrat; color:#063A1E; margin-top:6px; }
.win .locks { flex:1; display:flex; flex-direction:column; gap:10px; margin-left:16px; }
.win .lk { display:flex; align-items:center; gap:12px; padding:16px 14px; border-radius:14px; background:rgba(60,8,20,.8); border:2px solid var(--red); }
.win .lk .ic { color:var(--red); }
.win .lk i { flex:none; font:900 16px Unbounded; font-style:normal; color:#fff; background:var(--red); border-radius:6px; padding:5px 8px; min-width:44px; text-align:center; }
.win .lk p { font:700 20px/1.25 Montserrat; color:#FFE1E7; }
.wcap { margin-top:14px; display:flex; justify-content:space-between; gap:14px; }
.wcap div { font:800 19px Montserrat; color:#fff; display:flex; align-items:center; gap:10px; padding:10px 16px; border-radius:999px; background:rgba(4,10,22,.85); border:1.5px solid rgba(46,224,122,.5); }
.wcap div.no { border-color:rgba(255,77,109,.6); }
.wcap .no { color:#FF9AAD; }
.wcap .ic { color:var(--red); }
.exitn { margin-top:22px; padding:20px 22px; display:flex; gap:16px; align-items:center; }
.exitn .tag { flex:none; font:900 15px Unbounded; color:#fff; background:#E46A1C; padding:8px 10px; border-radius:6px; letter-spacing:.04em; text-align:center; line-height:1.2; }
.exitn p { font:600 22.5px/1.42 Montserrat; color:var(--ink2); }
.exitn p b { color:var(--ink); }

/* 14 mind map */
.mmh { display:flex; align-items:center; justify-content:space-between; }
.mmh h2 { font:900 46px/1.05 Unbounded; color:#fff; margin-top:12px; }
.mmh h2 em { font-style:normal; color:var(--cyan); }
.mmw { margin-top:20px; height:880px; }
.mcore { position:absolute; left:354px; top:300px; width:260px; height:260px; border-radius:50%; text-align:center;
  background:radial-gradient(circle at 40% 35%, #1B4E6E, #0B2440 62%, #061428); border:3px solid var(--cyan);
  box-shadow:0 0 0 12px rgba(47,230,210,.12), 0 0 60px rgba(47,230,210,.35); display:flex; flex-direction:column; align-items:center; justify-content:center; }
.mcore .ic { color:var(--cyan); }
.mcore b { font:900 25px/1.1 Unbounded; color:#fff; margin-top:8px; }
.mcore b em { font-style:normal; color:var(--amber); }
.mcore small { font:700 13px 'JetBrains Mono'; letter-spacing:.18em; color:var(--cyan); margin-top:8px; }
.mn { position:absolute; width:322px; padding:14px 16px 12px; }
.mn .h { display:flex; align-items:center; gap:10px; font:900 19px/1.15 Unbounded; color:var(--ink); }
.mn .h .ic { color:#0E7A6E; }
.mn .r { font:700 14px 'JetBrains Mono'; color:#0E7A6E; letter-spacing:.06em; margin-top:4px; }
.mn ul { list-style:none; margin-top:6px; }
.mn li { font:600 17.5px/1.32 Montserrat; color:var(--ink2); padding:5px 0 5px 18px; position:relative; }
.mn li:before { content:""; position:absolute; left:2px; top:13px; width:9px; height:9px; border-radius:50%; background:var(--cyan); box-shadow:0 0 0 2px #0E7A6E; }
.mn li b { color:var(--ink); font-weight:800; }
.mn.l { left:0; } .mn.r2 { left:646px; }
.mn.t1 { top:0; } .mn.t2 { top:300px; } .mn.t3 { top:600px; }

/* 15 answer key */
.kh { display:flex; align-items:flex-end; justify-content:space-between; }
.kh h2 { font:900 52px/1.04 Unbounded; color:#fff; margin-top:14px; }
.kh h2 em { font-style:normal; color:var(--amber); }
.kh .bust { position:relative; width:250px; height:250px; flex:none; overflow:hidden; border-radius:50%; border:3px solid var(--cyan); background:radial-gradient(circle at 50% 40%, #1B4E6E, #081528 70%);
  box-shadow:0 0 0 10px rgba(47,230,210,.12), 0 0 40px rgba(47,230,210,.35); margin-bottom:-6px; }
.kh .bust img { position:absolute; width:500px; left:-125px; top:-6px; }
.form { margin-top:24px; padding:14px 22px 10px; }
.fmh, .fmr { display:grid; grid-template-columns:70px 300px 1fr; align-items:center; gap:14px; }
.fmh { font:700 14px 'JetBrains Mono'; letter-spacing:.16em; color:var(--muted); padding:4px 0 8px; border-bottom:2px solid #D3E3EA; }
.fmh .lt { display:flex; justify-content:space-between; padding:0 12px; }
.fmr { padding:12px 0; border-bottom:1px dashed #C9DCE4; }
.fmr:last-child { border-bottom:0; }
.fmr .qn { font:900 30px Unbounded; color:var(--ink); }
.fmr .bb { display:flex; justify-content:space-between; }
.fmr .bb .bub { width:48px; height:48px; font-size:18px; border-width:2.5px; border-color:#9BB3C2; color:#7D93A3; }
.fmr .bb .bub.ok { border-color:#16A34A; color:#fff; background:#16A34A; box-shadow:0 0 0 4px rgba(46,224,122,.3); }
.fmr p { font:700 20px/1.3 Montserrat; color:var(--ink); }
.fmr p span { color:#0E7A6E; }
.score { margin-top:24px; display:flex; gap:12px; }
.score div { flex:1; padding:12px 14px; border-radius:14px; background:rgba(8,24,46,.85); border:1.5px solid var(--line); }
.score b { display:block; font:900 24px Unbounded; color:var(--cyan); }
.score span { font:700 17px/1.3 Montserrat; color:var(--txt); }
.score .s2 b { color:var(--green); } .score .s3 b { color:var(--amber); }
.ctas { margin-top:20px; display:flex; gap:12px; }
.ctas div { flex:1; display:flex; align-items:center; gap:12px; padding:14px 16px; border-radius:16px; background:var(--cyan); color:#04101F; }
.ctas div:nth-child(2) { background:var(--amber); } .ctas div:nth-child(3) { background:#fff; }
.ctas b { display:block; font:900 20px Unbounded; }
.ctas span { font:700 16px/1.25 Montserrat; }
"""


def svg_icon(name, x, y, s, color):
    return f'<svg x="{x}" y="{y}" width="{s}" height="{s}" viewBox="0 0 24 24" style="color:{color}">{ICON[name]}</svg>'


def build(page, ic, stamp):
    S = {}

    def ahead(L, k, title, label="DOĞRU CEVAP"):
        return f'<div class="ahead"><span class="bub ok">{L}</span><div><small>{label} · SORU 0{k}</small><h2>{title}</h2></div></div>'

    def rule(ref, text):
        return f'<div class="brk rule"><span class="ref">{ic("scale", 20)}{ref}</span><p>{text}</p></div>'

    def trap(text, kind="tuzak", sub="ÇELDİRİCİ", label=None):
        return f'<div class="trap {kind}">{stamp(kind, sub, rot=-5, scale=.64, label=label)}<p>{text}</p></div>'

    # ------------------------------------------------------------ A1
    rows = [("A", "gate", "Serbest bölgeye doğrudan, TGB dışından", "GK 152 · açıkça sayılmış", "yes", "tr"),
            ("B", "bulk", "Dökme hâlde denizyoluyla limana", "taşıma şekli = süre farkı", "yes", ""),
            ("C", "train", "Demiryoluyla TGB'ye", "taşıma şekli = süre farkı", "yes", ""),
            ("D", "plane", "Uzun mesafeli uçuşla havalimanına", "taşıma şekli = süre farkı", "yes", ""),
            ("E", "route", "Kara sularından durmaksızın geçen gemi", "GK 35/A istisnası", "no", "hit")]
    mrows = "".join(
        f'<div class="mr {cls}"><span class="bub sm {"ok" if v == "no" else "ink"}">{L}</span>{ic(icn, 34)}'
        f'<p>{t}<small>{sm}</small></p><span class="pill {v}">{"YOK" if v == "no" else "VAR"}</span></div>'
        for L, icn, t, sm, v, cls in rows)
    sch = f'''<svg width="352" height="452" viewBox="0 0 352 452" aria-hidden="true">
  <defs><pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><rect width="10" height="10" fill="#0F3A57"/><line x1="0" y1="0" x2="0" y2="10" stroke="{CYAN}" stroke-width="2.5" opacity=".45"/></pattern>
    <marker id="ah1" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{AMBER}"/></marker>
    <marker id="ah2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{GREEN}"/></marker></defs>
  <rect width="352" height="452" rx="12" fill="#06213A"/>
  <path d="M176 0 C156 92,214 166,188 246 C166 326,224 386,204 452 L276 452 C296 386,238 326,260 246 C286 166,228 92,248 0 Z" fill="url(#hatch)"/>
  <path d="M248 0 C228 92,286 166,260 246 C238 326,296 386,276 452 L352 452 L352 0 Z" fill="#163A5A" stroke="{CYAN}" stroke-width="2"/>
  <text transform="translate(318 300) rotate(-90)" text-anchor="middle" font-family="Unbounded" font-weight="900" font-size="20" fill="#9FF8EE" letter-spacing="3">TÜRKİYE</text>
  <text transform="translate(222 120) rotate(-74)" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="13" fill="#fff" letter-spacing="2">KARA SULARI</text>
  <path d="M238 440 C206 372,252 326,226 250 C204 176,236 98,212 14" fill="none" stroke="{AMBER}" stroke-width="4" stroke-dasharray="9 7" marker-end="url(#ah1)"/>
  <path d="M10 318 C90 318,150 300,246 300" fill="none" stroke="{GREEN}" stroke-width="4" marker-end="url(#ah2)"/>
  <rect x="252" y="290" width="22" height="20" rx="3" fill="{GREEN}"/>
  <circle cx="263" cy="300" r="16" fill="none" stroke="{GREEN}" stroke-width="2" opacity=".6"/>
  {svg_icon("ship", 220, 404, 34, AMBER)}
  {svg_icon("ship", 8, 326, 34, GREEN)}
  <text x="14" y="34" font-family="Montserrat" font-weight="800" font-size="16" fill="#fff">① DURMAKSIZIN</text>
  <text x="14" y="54" font-family="Montserrat" font-weight="800" font-size="16" fill="#fff">GEÇİŞ (E)</text>
  <rect x="14" y="64" width="176" height="32" rx="16" fill="{RED}"/>
  <text x="102" y="86" text-anchor="middle" font-family="Unbounded" font-weight="900" font-size="13" fill="#fff">ÖZET BEYAN YOK</text>
  <text x="14" y="392" font-family="Montserrat" font-weight="800" font-size="16" fill="#fff">② LİMANA GELİŞ</text>
  <rect x="14" y="402" width="176" height="32" rx="16" fill="#D7F8E6"/>
  <text x="102" y="424" text-anchor="middle" font-family="Unbounded" font-weight="900" font-size="13" fill="#05622F">ÖZET BEYAN VAR</text>
</svg>'''
    S[3] = page(3, f'''
  {ahead("E", 1, "Kara sularından <em>durmaksızın geçen</em> gemideki eşya")}
  {rule("GK 35/A", "TGB'ye getirilen eşya için özet beyan verilir; <b>kara suları veya hava sahasından durmaksızın geçen</b> taşıtlarla taşınan eşya <b>hariç</b>.")}
  <div class="a1"><div class="paper mx"><div class="mxh"><span>ŞIK · GELİŞ ŞEKLİ</span><span>ÖZET BEYAN</span></div>{mrows}</div>
    <div class="brk sch">{sch}</div></div>
  <div class="note"><span class="tag">ÖNEMLİ</span><p>Taşıma şekli özet beyanı kaldırmaz; yalnızca <b>verilme süresini</b> değiştirir.</p></div>
  {trap("<b>A · Serbest bölge:</b> Kanunun serbest bölgelere ilişkin hükmü (md. 152), serbest bölgeye <b>doğrudan TGB dışından</b> gelen eşya için de özet beyan verileceğini açıkça belirtir.")}
''', cls="a", hud_r="ÇÖZÜM <b>01</b>/06", active=1, bg=dict(cx=980, cy=1060, R=520, sweep=-130))

    # ------------------------------------------------------------ A2
    tl = f'''<svg width="968" height="300" viewBox="0 0 968 300" aria-hidden="true">
  <defs><filter id="tg" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8"/></filter>
    <marker id="ax" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#9FB8C8"/></marker></defs>
  <rect x="0" y="0" width="300" height="300" rx="14" fill="#fff" opacity=".035"/>
  <text x="22" y="36" font-family="JetBrains Mono" font-weight="700" font-size="15" letter-spacing="2" fill="#9FB8C8">TGB DIŞI</text>
  <text x="322" y="36" font-family="JetBrains Mono" font-weight="700" font-size="15" letter-spacing="2" fill="{CYAN}">TÜRKİYE GÜMRÜK BÖLGESİ</text>
  <rect x="300" y="54" width="668" height="44" fill="{CYAN}" opacity=".2"/>
  <rect x="300" y="54" width="668" height="4" fill="{CYAN}"/>
  <text x="324" y="84" font-family="Unbounded" font-weight="900" font-size="19" fill="{CYAN}" letter-spacing="1">GÜMRÜK GÖZETİMİ</text>
  {"".join(f'<path d="M{x} 64 l12 12 -12 12" fill="none" stroke="{CYAN}" stroke-width="3" opacity=".7"/>' for x in range(640, 930, 34))}
  <line x1="300" y1="18" x2="300" y2="112" stroke="{AMBER}" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="40" y1="170" x2="950" y2="170" stroke="#9FB8C8" stroke-width="3" marker-end="url(#ax)"/>
  <circle cx="118" cy="170" r="30" fill="#0B2440" stroke="#9FB8C8" stroke-width="3"/>{svg_icon("doc", 101, 153, 34, "#E6F4FA")}
  <circle cx="300" cy="170" r="52" fill="{CYAN}" opacity=".35" filter="url(#tg)"/>
  <circle cx="300" cy="170" r="38" fill="{CYAN}"/><circle cx="300" cy="170" r="50" fill="none" stroke="{CYAN}" stroke-width="2" opacity=".6"/>
  {svg_icon("eye", 280, 150, 40, "#04101F")}
  <circle cx="575" cy="170" r="30" fill="#0B2440" stroke="#9FB8C8" stroke-width="3"/>{svg_icon("search", 558, 153, 34, "#E6F4FA")}
  <circle cx="830" cy="170" r="30" fill="#0B2440" stroke="#9FB8C8" stroke-width="3"/>{svg_icon("unload", 813, 153, 34, "#E6F4FA")}
  <g font-family="Montserrat" text-anchor="middle">
    <text x="118" y="238" font-weight="800" font-size="21" fill="#fff">Özet beyan</text>
    <text x="118" y="264" font-weight="700" font-size="17" fill="#9FB8C8">girişten ÖNCE verilir</text>
    <text x="300" y="250" font-weight="900" font-size="24" fill="{CYAN}">GİRİŞ</text>
    <text x="300" y="276" font-weight="800" font-size="17" fill="{CYAN}">gözetim BAŞLAR</text>
    <text x="575" y="238" font-weight="800" font-size="21" fill="#fff">Gümrüğe sunma</text>
    <text x="575" y="264" font-weight="700" font-size="17" fill="#9FB8C8">başlangıcı ertelemez</text>
    <text x="830" y="238" font-weight="800" font-size="21" fill="#fff">Taşıttan boşaltma</text>
    <text x="830" y="264" font-weight="700" font-size="17" fill="#9FB8C8">gözetim altında (GY 74)</text>
  </g>
</svg>'''
    S[5] = page(5, f'''
  {ahead("A", 2, "girişinden – <em>gümrük gözetimine</em>")}
  <div class="paper lawq"><span class="tab">GK md. 36</span>“Türkiye Gümrük Bölgesine getirilen eşya, <mark>girişinden</mark> itibaren <mark>gümrük gözetimine</mark> tabidir. Bunlar, yürürlükteki hükümlere uygun olarak gümrük idareleri tarafından denetlenir.”</div>
  <div class="brk tl">{tl}</div>
  <div class="ns"><span class="h">BAŞLANGIÇ ANI DEĞİL:</span><span class="x"><i>C</i>gümrüğe sunma</span><span class="x"><i>D</i>özet beyanın tescili</span><span class="x"><i>E</i>taşıttan boşaltma</span></div>
  <div class="sub2">Yönetmelik: eşya taşıttan <b>gümrük gözetimi altında</b> boşaltılır; yani boşaltma anında eşya <b>zaten</b> gözetimdedir.</div>
  {trap('<b>B · “girişinden – gümrük kontrolüne”:</b> başlangıç anı doğru; ama Kanun bu cümlede <span class="term bad">KONTROL</span> değil <span class="term ok">GÖZETİM</span> der.')}
''', cls="a", hud_r="ÇÖZÜM <b>02</b>/06", active=2, bg=dict(cx=100, cy=1100, R=560, sweep=-70))

    # ------------------------------------------------------------ A3
    doors = [("swap", "Gümrük statüsü değişir", "A · çıkış kapısı", ""),
             ("gate", "Serbest bölgeye girer", "C · Kanun açıkça sayar", "tr"),
             ("export", "Yeniden ihraç edilir", "D · çıkış kapısı", ""),
             ("fire", "İmha edilir", "E · çıkış kapısı", "")]
    dhtml = "".join(
        f'<div class="spoke door {cls}" style="top:{12 + i * 116}px">{ic(icn, 40)}<p>{t}<small>{sm}</small></p><span class="ok">{ic("check", 22)}</span></div>'
        for i, (icn, t, sm, cls) in enumerate(doors))
    S[7] = page(7, f'''
  {ahead("B", 3, "Geçici depolama <em>gözetimi bitirmez</em>")}
  {rule("GK 36", "Serbest dolaşımda olmayan eşya; <b>gümrük statüsü değişinceye</b>, <b>serbest bölgeye girinceye</b> yahut <b>yeniden ihraç</b> veya <b>imha</b> edilinceye kadar gümrüğün gözetimi altında kalır.")}
  <div class="wire a3w" data-round="1" data-color="#2FE6D2"><svg class="lines" width="968" height="470" aria-hidden="true"></svg>
    <div class="hub zone"><small>GÜMRÜK GÖZETİMİ</small>{ic("eye", 44, "eye")}
      <div class="wh"><span class="xb">B ✗</span>{ic("warehouse", 40)}<b>GEÇİCİ DEPOLAMA</b><span>ara durum: işlem tayini beklenir</span></div>
      <div class="lp">eşya hâlâ gözetim altında</div></div>
    {dhtml}
  </div>
  <div class="paper gk47"><span class="ref">GK 47</span><p>Gümrüğe sunulan eşya, gümrükçe onaylanmış bir işlem veya kullanıma tabi tutuluncaya kadar <b>geçici depolanan eşya</b> statüsündedir: gözetimi bitiren bir işlem değil, <b>ara durum</b>.</p></div>
  {trap("<b>C · Serbest bölgeye girmesi:</b> eşya hâlâ gümrük denetimine tabi bir alana girdiği için listede yok sanılabilir; oysa Kanun bunu <b>açıkça sayar</b>.")}
''', cls="a", hud_r="ÇÖZÜM <b>03</b>/06", active=3, bg=dict(cx=1000, cy=180, R=520, sweep=120))

    # ------------------------------------------------------------ A4
    rail = f'''<svg width="968" height="210" viewBox="0 0 968 210" aria-hidden="true">
  <defs><marker id="br" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{AMBER}"/></marker></defs>
  {"".join(f'<rect x="{x}" y="160" width="10" height="22" rx="2" fill="#2A4A66"/>' for x in range(14, 960, 30))}
  <line x1="0" y1="164" x2="968" y2="164" stroke="#9FB8C8" stroke-width="4"/>
  <line x1="0" y1="178" x2="968" y2="178" stroke="#9FB8C8" stroke-width="4"/>
  <g transform="translate(40 92)">
    <rect x="0" y="0" width="190" height="62" rx="14" fill="#E6F4FA"/><rect x="150" y="10" width="34" height="24" rx="5" fill="{CYAN}"/>
    {"".join(f'<rect x="{12 + j * 34}" y="12" width="26" height="20" rx="4" fill="#0B2440"/>' for j in range(4))}
    <rect x="0" y="40" width="190" height="8" fill="{AMBER}"/>
    <circle cx="36" cy="66" r="9" fill="#0B2440" stroke="#E6F4FA" stroke-width="3"/><circle cx="150" cy="66" r="9" fill="#0B2440" stroke="#E6F4FA" stroke-width="3"/>
  </g>
  {"".join(f'<line x1="{-10 - j * 8}" y1="{106 + j * 14}" x2="{24 - j * 8}" y2="{106 + j * 14}" stroke="{CYAN}" stroke-width="3" opacity="{.7 - j * .15:.2f}" stroke-linecap="round"/>' for j in range(4))}
  <g transform="translate(818 46)">
    <rect x="0" y="40" width="130" height="78" rx="6" fill="#163A5A" stroke="{CYAN}" stroke-width="2.5"/>
    <path d="M-10 44 L65 6 L140 44" fill="none" stroke="{CYAN}" stroke-width="3"/>
    <rect x="50" y="78" width="30" height="40" fill="#0B2440" stroke="{CYAN}" stroke-width="2"/>
    <line x1="65" y1="6" x2="65" y2="-30" stroke="#E6F4FA" stroke-width="2.5"/><path d="M65 -30 h26 l-6 8 6 8 h-26z" fill="{RED}"/>
  </g>
  <text x="883" y="200" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="13" fill="{CYAN}" letter-spacing="1">GİRİŞ GÜMRÜK İD.</text>
  <line x1="448" y1="40" x2="448" y2="160" stroke="{GREEN}" stroke-width="3" stroke-dasharray="6 5"/>
  <circle cx="448" cy="40" r="22" fill="{GREEN}"/>{svg_icon("doc", 434, 26, 28, "#03200F")}
  <text x="448" y="88" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="16" fill="#fff">ÖZET BEYAN</text>
  <line x1="486" y1="40" x2="800" y2="40" stroke="{AMBER}" stroke-width="3.5" marker-start="url(#br)" marker-end="url(#br)"/>
  <rect x="540" y="14" width="200" height="52" rx="26" fill="#2A1A02" stroke="{AMBER}" stroke-width="2.5"/>
  {svg_icon("clock", 552, 24, 32, AMBER)}
  <text x="660" y="50" text-anchor="middle" font-family="Unbounded" font-weight="900" font-size="20" fill="{AMBER}">≥ 2 SAAT</text>
  <text x="536" y="100" font-family="Montserrat" font-weight="700" font-size="17" fill="#9FB8C8">en az iki saat önce · GY 67</text>
</svg>'''
    fixes = [("A", "Kural: <b>boşaltma idaresi</b>; giriş idaresi istisna", "Kural <b>giriş gümrük idaresi</b>. Başka idare ancak bilgi derhal iletilebiliyor ya da elektronik erişim varsa.", ""),
             ("B", "TGB'ye getirildikten <b>sonra</b> verilir", "TGB'ye getirilmeden <b>önce</b> verilir.", ""),
             ("C", "Karayolu transit beyanı: en az <b>dört saat</b> önce", "Saat yok: varıştan önce <b>elektronik ortamda</b> verilmesi yeterli.", ""),
             ("D", "Demiryolu: varıştan en az iki saat önce", "Hükümle birebir aynı <b>(GY 67)</b>", "good"),
             ("E", "Bildirimi <b>giriş gümrük idaresi</b> kabul eder", "Bu yetki <b>Müsteşarlık</b>'a aittir.", "")]
    frows = "".join(
        f'<div class="fr {cls}"><span class="bub sm {"ok" if cls else "ink"}">{L}</span><div class="was">{w}</div><div class="is">{i}</div></div>'
        for L, w, i, cls in fixes)
    S[9] = page(9, f'''
  {ahead("D", 4, "Demiryolu: varıştan <em>en az 2 saat önce</em>")}
  <div class="brk rail">{rail}</div>
  <div class="paper fix"><div class="fh"><span>ŞIK</span><span>ŞIKTA YAZAN</span><span>HÜKÜMDE OLAN · GK 35/A · GY 67</span></div>{frows}</div>
  {trap("<b>E · Bildirim:</b> hüküm doğru aktarılmış, yalnızca <b>yetkili makam</b> değiştirilmiş (giriş gümrük idaresi değil, Müsteşarlık).")}
''', cls="a", hud_r="ÇÖZÜM <b>04</b>/06", active=4, bg=dict(cx=160, cy=220, R=520, sweep=40))

    # ------------------------------------------------------------ A5
    S[11] = page(11, f'''
  {ahead("A", 5, "“Sunuluncaya” değil, <em>“tescil edilinceye”</em> kadar", label="YANLIŞ İFADE = DOĞRU CEVAP")}
  <div class="a5">
    <div class="brk flow">
      <div class="stp"><span class="no">{ic("clock", 28)}</span><p>Özet beyanın verilme <b>süresi dolmadan</b> gümrük beyannamesi verilir.</p></div>
      <div class="stp"><span class="no">{ic("door", 28)}</span><p>Giriş gümrük idaresi özet beyan verilmesinden <b>vazgeçebilir</b>.<span class="t g">D ✓</span></p></div>
      <div class="stp"><span class="no">{ic("doc", 28)}</span><p>Beyanname, özet beyanda bulunması gerekli <b>asgari bilgileri</b> içerir.<span class="t g">E ✓</span></p></div>
      <div class="stp key"><span class="no">{ic("check", 28)}</span><p>Beyanname <b>tescil edilinceye kadar</b> özet beyan statüsündedir.<br/><s>eşya gümrüğe sunuluncaya kadar</s><span class="t r">A ✗</span></p></div>
    </div>
    <div class="paper prep"><h4>HAZIRLAMA</h4><span class="ref">{ic("scale", 18)}GK 35/B</span>
      <ul><li><span class="k">B ✓</span><span><b>Veri işleme tekniği</b> kullanılarak hazırlanır.</span></li>
        <li><span class="k">B ✓</span><span>Gerekli ayrıntıları içeriyorsa <b>ticari, liman veya taşıma</b> bilgileri kullanılabilir.</span></li>
        <li><span class="k">C ✓</span><span>İstisnai durumda <b>yazılı</b> özet beyanı <b>Müsteşarlık</b> kabul edebilir…</span></li>
        <li><span class="k">C ✓</span><span>…şartı: <b>aynı düzeyde risk yönetimi</b> uygulanabilmesi.</span></li></ul></div>
  </div>
  {rule("GK 35/C", "Vazgeçme hâlinde beyanname asgari bilgileri içerir ve <b>tescil edilinceye kadar</b> özet beyan statüsüne sahiptir.")}
  {trap("Soru kökü <b>yanlış</b> olanı soruyor. A şıkkında değiştirilen tek unsur: statünün <b>sona erdiği an</b>.", kind="dikkat", sub="SORU KÖKÜ")}
''', cls="a", hud_r="ÇÖZÜM <b>05</b>/06", active=5, bg=dict(cx=1000, cy=640, R=560, sweep=170))

    # ------------------------------------------------------------ A6
    S[13] = page(13, f'''
  {ahead("D", 6, "I, III ve IV: <em>değişiklik kapısı kapanır</em>")}
  {rule("GK 35/B", "Özet beyanı verebilecek kişilerin talebi hâlinde, özet beyanın <b>verilmesinden sonra</b> bir veya daha fazla bilginin değiştirilmesine gümrük idarelerince izin verilir.")}
  <div class="brk win">
    <div class="key">{ic("key", 44)}<b>II · VERİLDİ</b><span>Özet beyanın gümrük idaresine verilmesi</span><em>ÖN KOŞUL, ENGEL DEĞİL</em></div>
    <div class="band"><b>DEĞİŞİKLİK AÇIK</b><span>talep üzerine, idare izin verir</span></div>
    <div class="locks">
      <div class="lk"><i>I</i>{ic("search", 30)}<p>Eşyanın <b>muayene edileceği</b> bildirildi</p></div>
      <div class="lk"><i>III</i>{ic("alert", 30)}<p>Bilgilerin <b>yanlış olduğu</b> tespit edildi</p></div>
      <div class="lk"><i>IV</i>{ic("unload", 30)}<p>Eşyanın <b>boşaltılmasına izin</b> verildi</p></div>
    </div>
  </div>
  <div class="wcap"><div>{ic("key", 28)}<span>II değişikliğin <b style="color:var(--green)">ön koşulu</b></span></div><div class="no">{ic("lock", 28)}I · III · IV'ten herhangi biri → DEĞİŞİKLİK YOK</div></div>
  <div class="paper exitn"><span class="tag">ÇIKIŞ<br/>FARKI</span><p>Çıkış özet beyanında üçüncü an <b>boşaltma izni değil</b>; eşyanın TGB dışına çıkarılmak üzere <b>ilgilisine teslimi</b>dir (GK 165/D). İki hüküm karıştırılmamalı.</p></div>
  {trap("<b>A · “I ve III”:</b> boşaltma izninin (IV) de değişikliği engelleyen anlardan biri olduğunu atlayan aday bu şıkka gider.")}
''', cls="a", hud_r="ÇÖZÜM <b>06</b>/06", active=6, bg=dict(cx=80, cy=420, R=560, sweep=10))

    # ------------------------------------------------------------ 14 mind map
    nodes = [("l t1", "ship", "KAPSAM", "GK 35/A · 152",
              ["TGB'ye getirilen eşya → <b>özet beyan</b>", "İstisna: kara suları / hava sahasından <b>durmaksızın geçen</b> taşıt", "Serbest bölgeye doğrudan gelen eşya <b>dahil</b>"]),
             ("l t2", "clock", "YER &amp; ZAMAN", "GK 35/A · GY 67",
              ["<b>Giriş</b> gümrük idaresine, getirilmeden <b>önce</b>", "Demiryolu: varıştan <b>≥ 2 saat</b> önce", "Bildirim kabulü: <b>Müsteşarlık</b>"]),
             ("l t3", "chip", "HAZIRLAMA", "GK 35/B",
              ["<b>Veri işleme tekniği</b>", "Ticari, liman, taşıma bilgileri kullanılabilir", "Yazılı: istisnai + <b>aynı düzeyde risk yönetimi</b>"]),
             ("r2 t1", "pen", "DEĞİŞİKLİK", "GK 35/B · 165/D",
              ["Talep üzerine, <b>verildikten sonra</b>", "Kapanır: <b>muayene bildirimi · yanlışlık tespiti · boşaltma izni</b>", "Çıkışta 3. an: <b>teslim</b>"]),
             ("r2 t2", "door", "VAZGEÇME", "GK 35/C",
              ["Süre dolmadan <b>beyanname</b> verilirse", "Beyanname <b>asgari bilgileri</b> içerir", "<b>Tescil edilinceye kadar</b> özet beyan statüsü"]),
             ("r2 t3", "eye", "GÖZETİM", "GK 36 · 47",
              ["<b>Girişten</b> itibaren başlar", "Biter: statü değişimi · serbest bölge · yeniden ihraç · imha", "Geçici depolama = <b>ara durum</b>"])]
    nh = "".join(
        f'<div class="spoke paper mn {pos}"><div class="h">{ic(icn, 30)}{h}</div><div class="r">{r}</div><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul></div>'
        for pos, icn, h, r, li in nodes)
    S[14] = page(14, f'''
  <div class="mmh"><div><span class="chip">{ic("radar", 20)} KONU HARİTASI</span><h2>6 soruda <em>tek harita</em></h2></div>{stamp("onemli", "KAYDET", rot=6, scale=.62)}</div>
  <div class="wire mmw" data-round="1" data-color="#2FE6D2"><svg class="lines" width="968" height="880" aria-hidden="true"></svg>
    <div class="hub mcore">{ic("radar", 48)}<b>ÖZET BEYAN<br/><em>&amp;</em> GÖZETİM</b><small>4458 S. GK</small></div>
    {nh}
  </div>
''', cls="mm", hud_r="HARİTA <b>06</b>/06", active=7, bg=dict(cx=540, cy=640, R=600, sweep=-60))

    # ------------------------------------------------------------ 15 answer key
    key = [("01", "E", "Durmaksızın geçiş → <span>özet beyan yok</span>"),
           ("02", "A", "Gözetim <span>girişte</span> başlar (kontrol değil)"),
           ("03", "B", "Geçici depolama <span>ara durum</span>, çıkış değil"),
           ("04", "D", "Demiryolu: <span>en az 2 saat</span> önce"),
           ("05", "A", "<span>Tescil edilinceye</span> kadar, sunuluncaya değil"),
           ("06", "D", "I, III, IV kapatır; <span>II ön koşul</span>")]
    krows = "".join(
        f'<div class="fmr"><span class="qn">{n}</span><div class="bb">{"".join(f"<span class=\"bub{" ok" if L == a else ""}\">{L}</span>" for L in "ABCDE")}</div><p>{t}</p></div>'
        for n, a, t in key)
    S[15] = page(15, f'''
  <div class="kh"><div><span class="chip">{ic("check", 20)} CEVAP ANAHTARI</span><h2>Kaç doğru<br/><em>yaptın?</em></h2></div>
    <div class="bust"><img src="img/koc-cutout.png" alt="Gümrük Koçu"/></div></div>
  <div class="paper form"><div class="fmh"><span>SORU</span><span class="lt"><span>A</span><span>B</span><span>C</span><span>D</span><span>E</span></span><span>AKILDA KALSIN</span></div>{krows}</div>
  <div class="score"><div class="s1"><b>6/6</b><span>Radar ustası, tuzak yakalandı</span></div><div class="s2"><b>4–5</b><span>Sağlam; çeldiricilere dikkat</span></div><div class="s3"><b>0–3</b><span>Başa kaydır, tekrar çöz</span></div></div>
  <div class="ctas"><div>{ic("bookmark", 34)}<p><b>KAYDET</b><span>Sınav öncesi tekrar</span></p></div><div>{ic("share", 34)}<p><b>PAYLAŞ</b><span>Çalışma arkadaşına</span></p></div><div>{ic("comment", 34)}<p><b>YORUMLA</b><span>Puanını yaz</span></p></div></div>
''', cls="key", hud_r="SONUÇ <b>06</b>/06", active=7, bg=dict(cx=900, cy=300, R=520, sweep=-100), swipe=False)
    return S
