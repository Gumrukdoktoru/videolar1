"""TIR İşlemleri Seri No: 9 carousel — "Otoyol tabelası + clean sheet" theme. Writes carousel.html (11 slides, 1080×1350)."""
import pathlib

D = pathlib.Path(__file__).resolve().parent
N = 11

# ---------------------------------------------------------------- icons (24x24, stroke=currentColor)
P = {
    "doc": '<path d="M6 2.5h8.5L19 7v14.5H6z M14 2.5V7h5 M9 12h7 M9 15.5h7 M9 19h4" />',
    "cert": '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M7 8.5h10 M7 12h6"/><circle cx="16.5" cy="17.5" r="3"/><path d="M15 20l-.8 3 2.3-1.2 2.3 1.2-.8-3"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2.5"/>',
    "eye": '<path d="M2 12s3.8-7 10-7 10 7 10 7-3.8 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "route": '<circle cx="5" cy="18" r="2.5"/><circle cx="19" cy="6" r="2.5"/><path d="M7.5 18H15a3.5 3.5 0 0 0 0-7H9a3.5 3.5 0 0 1 0-7h7.5"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5z M3 12.5l9 5 9-5 M3 17l9 5 9-5"/>',
    "box": '<path d="M3 7.5L12 3l9 4.5v9L12 21l-9-4.5z M3 7.5l9 4.5 9-4.5 M12 12v9"/>',
    "building": '<path d="M3 21h18 M5 21V9l7-5 7 5v12 M9 21v-6h6v6 M8 11h2 M14 11h2"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18 M8 3v4 M16 3v4"/>',
    "gavel": '<path d="M14 3l7 7-3 3-7-7z M12.5 9.5L4 18 M3 21h9"/>',
    "check": '<path d="M4 12.5l5 5L20 6.5"/>',
    "x": '<path d="M6 6l12 12 M18 6L6 18"/>',
    "warn": '<path d="M12 3L22 20H2z M12 9.5v5 M12 17.2v.3"/>',
    "star": '<path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9z"/>',
    "flag": '<path d="M5 21V4 M5 4h11l-2 4 2 4H5"/>',
    "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1 M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    "scan": '<path d="M4 8V5a1 1 0 0 1 1-1h3 M16 4h3a1 1 0 0 1 1 1v3 M20 16v3a1 1 0 0 1-1 1h-3 M8 20H5a1 1 0 0 1-1-1v-3 M4 12h16"/>',
    "pen": '<path d="M4 20l1.2-4.8L16 4.4a2 2 0 0 1 2.8 0l.8.8a2 2 0 0 1 0 2.8L8.8 18.8z M14 6.5l3.5 3.5"/>',
    "save": '<path d="M6 3h12v18l-6-4-6 4z"/>',
    "share": '<circle cx="18" cy="5" r="2.6"/><circle cx="6" cy="12" r="2.6"/><circle cx="18" cy="19" r="2.6"/><path d="M8.4 10.7l7.2-4.2 M8.4 13.3l7.2 4.2"/>',
    "arrow": '<path d="M4 12h15 M13 6l6 6-6 6"/>',
    "border": '<path d="M12 2v20" stroke-dasharray="2.5 2.5"/><path d="M3 9h6 M6 6l3 3-3 3 M15 15h6 M18 12l3 3-3 3"/>',
    "unload": '<path d="M3 15h18 M5 15V8h9v7 M14 10h4l3 3v2 M8 4v6 M5.5 7.5L8 10l2.5-2.5"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
}


def ic(name, size=32, cls="", sw=2.2):
    return (f'<svg class="ic {cls}" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>')


def plate(w=300, cls="plate"):
    """TIR plate: blue field, white inner border, white TIR letters."""
    h = round(w * 0.45)
    return (f'<svg class="{cls}" viewBox="0 0 400 180" width="{w}" height="{h}" aria-hidden="true">'
            '<rect x="2" y="2" width="396" height="176" rx="18" fill="#0F3E96"/>'
            '<rect x="14" y="14" width="372" height="152" rx="10" fill="none" stroke="#fff" stroke-width="7"/>'
            '<text x="200" y="133" text-anchor="middle" font-family="Archivo Black" font-size="118" fill="#fff" letter-spacing="10">TIR</text>'
            '<circle cx="34" cy="34" r="5" fill="#9DB4E0"/><circle cx="366" cy="34" r="5" fill="#9DB4E0"/>'
            '<circle cx="34" cy="146" r="5" fill="#9DB4E0"/><circle cx="366" cy="146" r="5" fill="#9DB4E0"/></svg>')


def truck(w=170, cls="truck"):
    return (f'<svg class="{cls}" viewBox="0 0 220 96" width="{w}" height="{round(w * 96 / 220)}" aria-hidden="true">'
            '<rect x="4" y="10" width="140" height="62" rx="5" fill="#F4F7FC" stroke="#0E1B33" stroke-width="3"/>'
            '<rect x="4" y="52" width="140" height="8" fill="#0F3E96"/>'
            '<rect x="54" y="20" width="44" height="22" rx="3" fill="#0F3E96"/><rect x="58" y="24" width="36" height="14" rx="2" fill="none" stroke="#fff" stroke-width="1.6"/>'
            '<text x="76" y="35.5" text-anchor="middle" font-family="Archivo Black" font-size="10.5" fill="#fff">TIR</text>'
            '<path d="M150 72V30h34l22 22v20z" fill="#0F3E96" stroke="#0E1B33" stroke-width="3" stroke-linejoin="round"/>'
            '<path d="M158 36h22l15 15h-37z" fill="#BFD3F5"/><rect x="144" y="62" width="8" height="10" fill="#0E1B33"/>'
            '<rect x="200" y="58" width="9" height="6" rx="2" fill="#FFC21A"/>'
            + "".join(f'<circle cx="{x}" cy="78" r="12" fill="#1A1F29"/><circle cx="{x}" cy="78" r="5" fill="#B8C2D3"/>' for x in (30, 58, 118, 180))
            + '</svg>')


CSS = r"""
:root { --blue:#0F3E96; --blue2:#2E6BD6; --sky:#E7EFFC; --ink:#0E1B33; --ink2:#33415C; --muted:#5E6E89; --line:#D5DDEA;
  --paper:#F6F8FC; --yellow:#FFC21A; --yel2:#FFF3C7; --green:#14935A; --grn2:#E2F5EB; --red:#D63A3A; --red2:#FCE6E6; --asph:#2A2F38; }
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#cfd5df; font-family:Montserrat, sans-serif; color:var(--ink); }
.slide { position:relative; width:1080px; height:1350px; overflow:hidden; margin:0 auto 40px; background:var(--paper); }
.slide:before { content:""; position:absolute; inset:0;
  background-image:linear-gradient(rgba(15,62,150,.055) 1.5px, transparent 1.5px), linear-gradient(90deg, rgba(15,62,150,.055) 1.5px, transparent 1.5px);
  background-size:40px 40px; background-position:20px 20px; }
.ic { display:block; flex:none; }
.mono { font-family:'JetBrains Mono', monospace; }

/* header: motorway sign */
.hdr { position:absolute; left:60px; right:60px; top:44px; height:64px; display:flex; align-items:center; justify-content:space-between; z-index:3; }
.sign { display:flex; align-items:center; gap:14px; height:64px; padding:0 22px 0 14px; background:var(--blue); color:#fff; border-radius:12px;
  box-shadow:inset 0 0 0 4px var(--blue), inset 0 0 0 7px #fff, 0 8px 18px rgba(15,62,150,.22); font:900 21px Montserrat; letter-spacing:.07em; }
.sign .sh { width:40px; height:36px; border-radius:6px; background:#fff; color:var(--blue); display:flex; align-items:center; justify-content:center;
  font:900 13px 'Archivo Black'; letter-spacing:.02em; }
.pg { display:flex; align-items:center; gap:12px; font:700 18px 'JetBrains Mono'; color:var(--muted); letter-spacing:.12em; }
.pg b { display:inline-flex; align-items:center; height:46px; padding:0 14px; border-radius:10px; background:#fff; border:2px solid var(--line); color:var(--ink); }

/* road footer with moving truck */
.road { position:absolute; left:0; right:0; bottom:0; height:96px; background:var(--asph); z-index:2; }
.road:before { content:""; position:absolute; left:0; right:0; top:0; height:6px; background:repeating-linear-gradient(90deg,#fff 0 36px,#D63A3A 36px 72px); opacity:.9; }
.road .lane { position:absolute; left:0; right:0; top:56px; height:5px; background:repeating-linear-gradient(90deg,var(--yellow) 0 44px,transparent 44px 80px); }
.road .logo { position:absolute; left:60px; top:24px; background:#fff; border-radius:10px; padding:7px 12px; z-index:3; }
.road .logo img { height:30px; display:block; }
.road .swipe { position:absolute; right:60px; top:30px; font:900 19px Montserrat; letter-spacing:.14em; color:#fff; display:flex; align-items:center; gap:8px; z-index:3; }
.road .km { position:absolute; top:22px; font:700 14px 'JetBrains Mono'; color:#9AA6BA; letter-spacing:.1em; }
.road .truck { position:absolute; top:-30px; z-index:4; filter:drop-shadow(0 6px 8px rgba(0,0,0,.35)); }

/* content */
.c { position:absolute; left:60px; right:60px; top:136px; bottom:118px; z-index:1; }
.kick { font:700 19px 'JetBrains Mono'; letter-spacing:.18em; color:var(--blue2); text-transform:uppercase; display:flex; align-items:center; gap:12px; }
.kick .md { font:800 16px Montserrat; letter-spacing:.06em; color:#fff; background:var(--blue); padding:5px 10px; border-radius:7px; }
.h2 { font-family:'Archivo Black'; font-size:52px; line-height:1.05; color:var(--ink); margin-top:10px; letter-spacing:-.005em; }
.h2 em { font-style:normal; color:var(--blue); }
.card { background:#fff; border:2px solid var(--line); border-radius:18px; box-shadow:0 10px 26px rgba(14,27,51,.07); }
.tag { display:inline-flex; align-items:center; gap:8px; font:900 15px Montserrat; letter-spacing:.1em; padding:6px 12px; border-radius:8px; }
.t-new { background:var(--green); color:#fff; } .t-old { background:var(--red); color:#fff; } .t-same { background:#E4E9F2; color:var(--ink2); }
.t-onemli { background:var(--yellow); color:#2a1d00; } .t-dikkat { background:#FF8A1F; color:#2b1300; } .t-uyari { background:var(--red); color:#fff; }
.t-tuzak { background:#14141A; color:#FFD400; }
.note { display:flex; gap:14px; align-items:flex-start; padding:16px 20px; border-radius:16px; font:600 22px/1.35 Montserrat; color:var(--ink2); }
.note b { color:var(--ink); }
.note .tag { flex:none; margin-top:1px; }
.n-y { background:var(--yel2); border:2px solid #F3D26A; } .n-r { background:var(--red2); border:2px solid #F2B4B4; } .n-g { background:var(--grn2); border:2px solid #9ED9BA; }
.n-b { background:var(--sky); border:2px solid #B9CCF0; }
.hl { background:linear-gradient(transparent 58%, rgba(255,194,26,.65) 58%); padding:0 3px; }
.strike { text-decoration:line-through; text-decoration-color:var(--red); text-decoration-thickness:5px; color:#8A96AA; }

/* ---- s01 cover */
#s01 .ttl { position:absolute; left:0; top:244px; width:960px; }
#s01 .ttl small { display:block; font:800 25px Montserrat; color:var(--ink2); letter-spacing:.02em; }
#s01 .ttl .big { font-family:'Archivo Black'; font-size:128px; line-height:.95; color:var(--ink); margin-top:8px; white-space:nowrap; }
#s01 .ttl .big em { font-style:normal; color:var(--blue); }
#s01 .ttl .sub { font:800 36px/1.2 Montserrat; color:var(--ink); margin-top:14px; }
#s01 .ttl .sub span { background:var(--yellow); padding:0 10px; border-radius:6px; }
#s01 .plate { position:absolute; left:0; top:4px; transform:rotate(-4deg); filter:drop-shadow(0 16px 22px rgba(15,62,150,.3)); }
#s01 .rg { position:absolute; left:372px; top:42px; width:560px; padding:16px 20px; }
#s01 .rg .r1 { font:700 17px 'JetBrains Mono'; color:var(--muted); letter-spacing:.12em; }
#s01 .rg .r2 { font:900 26px Montserrat; color:var(--ink); margin-top:6px; }
#s01 .rg .r2 b { color:var(--blue); }
#s01 .nums { position:absolute; left:0; top:590px; width:600px; display:grid; grid-template-columns:1fr 1fr; gap:16px; }
#s01 .num { padding:20px 22px; height:190px; position:relative; }
#s01 .num .v { font-family:'Archivo Black'; font-size:46px; line-height:1; color:var(--blue); white-space:nowrap; }
#s01 .num .v s { color:#9AA6BA; text-decoration-color:var(--red); text-decoration-thickness:4px; font-size:34px; }
#s01 .num .l { font:700 19px/1.25 Montserrat; color:var(--ink2); margin-top:10px; }
#s01 .num .md { position:absolute; right:12px; top:12px; font:700 13px 'JetBrains Mono'; color:var(--muted); }
#s01 .koc { position:absolute; right:-60px; bottom:-24px; height:600px; z-index:1; filter:drop-shadow(0 18px 24px rgba(14,27,51,.25)); }
#s01 .bub { position:absolute; right:10px; top:388px; width:300px; padding:16px 18px; font:900 23px/1.25 Montserrat; color:var(--ink); z-index:2; }
#s01 .bub:after { content:""; position:absolute; left:150px; bottom:-24px; border:12px solid transparent; border-top:16px solid #fff; }
#s01 .bub em { font-style:normal; color:var(--blue); }

/* ---- s02 mind map */
#s02 .map { position:absolute; left:0; top:160px; width:960px; height:980px; }
#s02 svg.wires { position:absolute; inset:0; }
#s02 .hub { position:absolute; left:330px; top:390px; width:300px; height:190px; display:flex; flex-direction:column; align-items:center; justify-content:center; }
#s02 .hub .plate { filter:drop-shadow(0 14px 20px rgba(15,62,150,.3)); }
#s02 .hub b { font:900 22px Montserrat; letter-spacing:.12em; color:var(--ink); margin-top:10px; }
#s02 .node { position:absolute; width:300px; padding:16px 18px 16px; }
#s02 .node .nh { display:flex; align-items:center; gap:12px; }
#s02 .node .nh .ib { width:46px; height:46px; border-radius:12px; display:flex; align-items:center; justify-content:center; color:#fff; flex:none; }
#s02 .node .nh b { font:900 22px/1.15 Montserrat; color:var(--ink); }
#s02 .node .md { font:700 15px 'JetBrains Mono'; color:var(--muted); letter-spacing:.06em; margin-top:10px; }
#s02 .node .tx { font:700 20px/1.3 Montserrat; color:var(--ink2); margin-top:6px; }
#s02 .node .tx em { font-style:normal; color:var(--blue); font-weight:900; }

/* ---- generic two-column before/after */
.ba { display:flex; align-items:stretch; gap:18px; }
.ba .side { flex:1; padding:20px 22px; position:relative; }
.ba .side .lb { display:flex; align-items:center; gap:10px; }
.ba .arr { align-self:center; color:var(--blue); flex:none; }
.big { font-family:'Archivo Black'; line-height:1; }

/* ---- s03 taşıt onay belgesi */
#s03 .hero { margin-top:26px; display:flex; gap:20px; align-items:stretch; }
#s03 .doc { width:330px; height:404px; position:relative; padding:20px 22px; background:#fff; border:2px solid var(--line); border-radius:16px;
  box-shadow:0 14px 30px rgba(14,27,51,.1); }
#s03 .doc:before { content:""; position:absolute; left:12px; right:12px; top:12px; bottom:12px; border:2px dashed #B9CCF0; border-radius:10px; }
#s03 .doc .dh { position:relative; font:900 20px/1.15 Montserrat; color:var(--blue); letter-spacing:.04em; }
#s03 .doc .dh small { display:block; font:700 14px 'JetBrains Mono'; color:var(--muted); letter-spacing:.1em; margin-top:6px; }
#s03 .doc .ln { position:relative; height:10px; border-radius:5px; background:#E4EAF4; margin-top:14px; }
#s03 .doc .ek { position:absolute; right:18px; top:18px; font:900 15px Montserrat; color:#fff; background:var(--ink); border-radius:7px; padding:4px 9px; }
#s03 .doc .seal { position:absolute; right:22px; bottom:22px; width:118px; height:118px; border-radius:50%; border:6px solid var(--green); color:var(--green);
  display:flex; flex-direction:column; align-items:center; justify-content:center; transform:rotate(-12deg); background:rgba(255,255,255,.9); }
#s03 .doc .seal b { font-family:'Archivo Black'; font-size:44px; line-height:1; }
#s03 .doc .seal span { font:900 15px Montserrat; letter-spacing:.12em; }
#s03 .yrs { flex:1; display:flex; flex-direction:column; gap:16px; }
#s03 .yr { flex:1; display:flex; align-items:center; gap:20px; padding:0 24px; }
#s03 .yr .big { font-size:96px; }
#s03 .yr.o .big { color:#A9B3C4; text-decoration:line-through; text-decoration-color:var(--red); text-decoration-thickness:8px; }
#s03 .yr.n { border-color:var(--green); background:var(--grn2); }
#s03 .yr.n .big { color:var(--green); }
#s03 .yr .d b { display:block; font:900 24px Montserrat; color:var(--ink); }
#s03 .yr .d span { display:block; font:700 18px 'JetBrains Mono'; color:var(--muted); margin-top:6px; letter-spacing:.04em; }
#s03 .flow { margin-top:22px; display:flex; align-items:stretch; gap:10px; }
#s03 .st { flex:1; padding:14px 14px; text-align:center; position:relative; }
#s03 .st .ib { width:48px; height:48px; border-radius:50%; margin:0 auto; background:var(--sky); color:var(--blue); display:flex; align-items:center; justify-content:center; }
#s03 .st b { display:block; font:900 18px/1.2 Montserrat; color:var(--ink); margin-top:8px; }
#s03 .st span { display:block; font:600 15px/1.25 Montserrat; color:var(--muted); margin-top:4px; }
#s03 .st + .st:before { content:"›"; position:absolute; left:-14px; top:34%; font:900 30px Montserrat; color:var(--blue2); }
#s03 .notes { margin-top:20px; display:flex; flex-direction:column; gap:12px; }

/* ---- s04 süre aşımı */
#s04 .sea { margin-top:24px; display:flex; gap:16px; }
#s04 .sea .sc { flex:1; padding:18px 22px; display:flex; align-items:center; gap:18px; }
#s04 .sea .sc .big { font-size:62px; color:var(--blue); }
#s04 .sea .sc .big small { font:900 22px Montserrat; color:var(--muted); margin-left:6px; }
#s04 .sea .sc .m { font:800 19px/1.3 Montserrat; color:var(--ink2); }
#s04 .sea .sc .m b { display:block; font:900 15px 'JetBrains Mono'; color:var(--muted); letter-spacing:.1em; margin-bottom:4px; }
#s04 .chain { margin-top:22px; display:flex; flex-direction:column; align-items:center; }
#s04 .step { width:100%; display:flex; align-items:center; gap:18px; padding:16px 22px; }
#s04 .step .ib { width:54px; height:54px; border-radius:14px; display:flex; align-items:center; justify-content:center; color:#fff; flex:none; }
#s04 .step b { display:block; font:900 24px Montserrat; color:var(--ink); }
#s04 .step span { display:block; font:600 19px/1.3 Montserrat; color:var(--ink2); margin-top:3px; }
#s04 .step .tag { margin-left:auto; }
#s04 .dn { height:36px; color:var(--blue2); display:flex; align-items:center; }
#s04 .fk { width:100%; display:flex; gap:16px; }
#s04 .fk .side { flex:1; padding:18px 20px; }
#s04 .fk .side p { font:700 22px/1.32 Montserrat; color:var(--ink); margin-top:10px; }
#s04 .fk .o { background:#FBF3F3; border-color:#F2B4B4; } #s04 .fk .o p { color:#8A96AA; }
#s04 .fk .n { background:var(--grn2); border-color:#9ED9BA; }
#s04 .fk .n p em { font-style:normal; background:linear-gradient(transparent 55%, rgba(255,194,26,.7) 55%); }

/* ---- s05 8 idare */
#s05 .lane { position:relative; margin-top:30px; height:250px; border-radius:20px; background:var(--asph); overflow:hidden; }
#s05 .lane .dash { position:absolute; left:0; right:0; top:123px; height:5px; background:repeating-linear-gradient(90deg,var(--yellow) 0 34px,transparent 34px 64px); }
#s05 .lane .post { position:absolute; top:34px; width:92px; height:184px; display:flex; flex-direction:column; align-items:center; }
#s05 .lane .post .bx { width:80px; height:80px; border-radius:14px; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:30px;
  color:#fff; box-shadow:inset 0 0 0 4px rgba(255,255,255,.85); }
#s05 .lane .post .bx.h { background:var(--blue2); } #s05 .lane .post .bx.v { background:var(--green); }
#s05 .lane .post .pole { width:6px; flex:1; background:#C9D2E1; }
#s05 .lane .post i { font:700 14px 'JetBrains Mono'; color:#C9D2E1; font-style:normal; margin-top:6px; }
#s05 .lane .lim { position:absolute; right:18px; top:18px; width:92px; height:92px; border-radius:50%; background:#fff; border:10px solid var(--red);
  display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:44px; color:var(--ink); }
#s05 .leg { display:flex; gap:22px; margin-top:14px; font:800 19px Montserrat; color:var(--ink2); }
#s05 .leg span { display:flex; align-items:center; gap:8px; }
#s05 .leg i { width:22px; height:22px; border-radius:6px; display:block; }
#s05 .rules { margin-top:20px; display:flex; flex-direction:column; gap:14px; }
#s05 .rule { display:flex; align-items:center; gap:20px; padding:18px 22px; }
#s05 .rule .big { font-size:42px; color:var(--blue); width:190px; text-align:center; flex:none; white-space:nowrap; }
#s05 .rule p { font:700 22px/1.32 Montserrat; color:var(--ink); }
#s05 .rule p small { display:block; font:700 15px 'JetBrains Mono'; color:var(--muted); letter-spacing:.08em; margin-bottom:4px; }
#s05 .boxes { margin-top:16px; display:flex; gap:14px; }
#s05 .boxes .bx2 { flex:1; display:flex; align-items:center; gap:14px; padding:14px 18px; font:700 19px/1.3 Montserrat; color:var(--ink2); }
#s05 .boxes .bx2 .k { width:58px; height:58px; border-radius:12px; border:3px solid var(--ink); display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:26px; flex:none; }

/* ---- s06 yöntem A */
#s06 .tl { position:relative; margin-top:28px; height:300px; }
#s06 .tl svg { position:absolute; inset:0; }
#s06 .kn { position:absolute; top:0; height:300px; padding:16px 18px; border-radius:18px; }
#s06 .k1 { left:0; width:466px; background:var(--sky); border:3px solid var(--blue2); }
#s06 .k2 { left:494px; width:466px; background:#EAF7F0; border:3px solid var(--green); }
#s06 .kn .kh { display:flex; align-items:center; gap:10px; font:900 22px Montserrat; }
#s06 .k1 .kh { color:var(--blue); } #s06 .k2 .kh { color:var(--green); }
#s06 .kn .kh .big { font-size:30px; }
#s06 .slots { display:flex; gap:6px; margin-top:16px; }
#s06 .slots i { width:46px; height:46px; border-radius:10px; display:flex; align-items:center; justify-content:center; font:900 17px 'JetBrains Mono'; font-style:normal; color:#fff; }
#s06 .slots i.h { background:var(--blue2); } #s06 .slots i.v { background:var(--green); } #s06 .slots i.x { background:var(--ink); }
#s06 .kn .cap { font:700 18px/1.3 Montserrat; color:var(--ink2); margin-top:14px; }
#s06 .kn .cap b { color:var(--ink); }
#s06 .k2 .slots { margin-left:30px; }
#s06 .swap { position:absolute; left:426px; top:214px; width:108px; height:108px; border-radius:50%; background:var(--yellow); border:6px solid #fff;
  display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; font:900 15px/1.1 Montserrat; color:#2a1d00; box-shadow:0 10px 22px rgba(14,27,51,.2); z-index:2; }
#s06 .swap b { font-family:'Archivo Black'; font-size:30px; }
#s06 .sum { margin-top:18px; display:flex; align-items:center; justify-content:center; gap:18px; padding:16px; }
#s06 .sum .big { font-size:62px; }
#s06 .sum .op { font:900 40px Montserrat; color:var(--muted); }
#s06 .sum .c1 { color:var(--blue2); } #s06 .sum .c2 { color:var(--green); } #s06 .sum .c3 { color:var(--ink); }
#s06 .sum small { font:800 18px Montserrat; color:var(--muted); display:block; text-align:center; margin-top:4px; }
#s06 .recs { margin-top:16px; display:flex; gap:14px; }
#s06 .rec { flex:1; padding:14px 18px; }
#s06 .rec .rh { display:flex; align-items:center; gap:10px; font:900 17px Montserrat; color:var(--blue); letter-spacing:.04em; }
#s06 .rec p { font:600 18px/1.32 Montserrat; color:var(--ink2); margin-top:8px; }
#s06 .rec p b { color:var(--ink); }
#s06 .note { margin-top:14px; }

/* ---- s07 yöntem B */
#s07 .scene { position:relative; margin-top:22px; height:262px; border-radius:20px; background:linear-gradient(180deg,#EAF0FA 0 70%, var(--asph) 70%); overflow:hidden; border:2px solid var(--line); }
#s07 .scene .dash { position:absolute; left:0; right:0; top:232px; height:5px; background:repeating-linear-gradient(90deg,var(--yellow) 0 34px,transparent 34px 64px); }
#s07 .scene svg { position:absolute; left:84px; top:14px; }
#s07 .scene .ct { position:absolute; top:22px; font:900 16px Montserrat; letter-spacing:.06em; color:#fff; padding:6px 10px; border-radius:8px; }
#s07 .grid3 { margin-top:14px; display:grid; grid-template-columns:1fr 1fr; gap:12px; }
#s07 .gi { padding:14px 18px; }
#s07 .gi .rh { display:flex; align-items:center; gap:10px; font:900 19px/1.2 Montserrat; color:var(--ink); }
#s07 .gi .rh .ib { width:42px; height:42px; border-radius:11px; display:flex; align-items:center; justify-content:center; color:#fff; flex:none; }
#s07 .gi p { font:600 17px/1.32 Montserrat; color:var(--ink2); margin-top:8px; }
#s07 .gi p b { color:var(--ink); }
#s07 .gi .tag { margin-top:10px; }

#s07 .cmp { margin-top:12px; padding:4px 18px; }
#s07 .cr { display:grid; grid-template-columns:120px 1fr 1fr; gap:14px; align-items:center; min-height:48px; border-bottom:2px solid #E6EBF3; font:700 16px/1.3 Montserrat; color:var(--ink2); }
#s07 .cr:last-child { border-bottom:none; }
#s07 .cr > div:first-child { font:800 15px 'JetBrains Mono'; color:var(--muted); letter-spacing:.08em; text-transform:uppercase; }
#s07 .cr.ch { min-height:46px; font:900 17px Montserrat; color:var(--ink); letter-spacing:.06em; }
#s07 .cr.ch b { display:inline-flex; width:30px; height:30px; border-radius:8px; align-items:center; justify-content:center; color:#fff; margin-right:6px; }
#s07 .ca { background:var(--blue2); } #s07 .cb { background:var(--green); }
/* ---- s08 kurum adları */
#s08 .rn { margin-top:30px; padding:26px 26px; }
#s08 .rn .row { display:flex; align-items:center; gap:16px; }
#s08 .rn .nm { flex:1; padding:22px 20px; border-radius:14px; font:900 28px/1.22 Montserrat; }
#s08 .rn .nm.o { background:#FBF3F3; color:#8A96AA; text-decoration:line-through; text-decoration-color:var(--red); text-decoration-thickness:4px; border:2px solid #F2B4B4; }
#s08 .rn .nm.n { background:var(--grn2); color:var(--ink); border:2px solid #9ED9BA; }
#s08 .rn .nm.n em { font-style:normal; background:linear-gradient(transparent 55%, rgba(255,194,26,.75) 55%); }
#s08 .rn .arr { color:var(--blue); flex:none; }
#s08 .rn .where { margin-top:14px; display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
#s08 .rn .where small { font:800 16px 'JetBrains Mono'; color:var(--muted); letter-spacing:.08em; margin-right:4px; }
#s08 .rn .where span { font:700 17px 'JetBrains Mono'; color:var(--blue); background:var(--sky); border:1.5px solid #B9CCF0; border-radius:8px; padding:4px 9px; }
#s08 .rn .ttl { display:flex; align-items:center; gap:12px; font:900 20px Montserrat; color:var(--ink); margin-bottom:14px; letter-spacing:.03em; }
#s08 .rn .ttl .ib { width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; background:var(--blue); color:#fff; }

/* ---- s09 ekler & yürürlük */
#s09 .eks { margin-top:24px; display:flex; gap:14px; }
#s09 .ek { flex:1; padding:0 0 18px; overflow:hidden; }
#s09 .ek .et { background:var(--blue); color:#fff; padding:12px 18px; font-family:'Archivo Black'; font-size:28px; display:flex; align-items:center; justify-content:space-between; }
#s09 .ek .et .ic { opacity:.9; }
#s09 .ek b { display:block; font:900 22px/1.2 Montserrat; color:var(--ink); padding:14px 18px 0; }
#s09 .ek span { display:block; font:600 17px/1.3 Montserrat; color:var(--muted); padding:6px 18px 0; }
#s09 .tline { position:relative; margin-top:26px; padding:24px 26px 22px; }
#s09 .tline .bar { position:absolute; left:120px; right:120px; top:92px; height:6px; background:repeating-linear-gradient(90deg,var(--blue2) 0 18px,transparent 18px 28px); }
#s09 .tline .pts { position:relative; display:flex; justify-content:space-between; }
#s09 .tline .pt { width:280px; text-align:center; }
#s09 .tline .pt .dot { width:64px; height:64px; margin:0 auto; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; border:5px solid #fff; box-shadow:0 6px 14px rgba(14,27,51,.2); }
#s09 .tline .pt > b { display:block; font-family:'Archivo Black'; font-size:28px; color:var(--ink); margin-top:10px; }
#s09 .tline .pt > span { display:block; font:700 17px/1.3 Montserrat; color:var(--muted); margin-top:4px; }
#s09 .yy { margin-top:18px; display:flex; gap:14px; }
#s09 .yy .card { flex:1; padding:18px 20px; display:flex; align-items:center; gap:16px; }
#s09 .yy .ib { width:60px; height:60px; border-radius:16px; display:flex; align-items:center; justify-content:center; color:#fff; flex:none; }
#s09 .yy small { display:block; font:800 15px 'JetBrains Mono'; color:var(--muted); letter-spacing:.1em; }
#s09 .yy b { display:block; font:900 25px/1.2 Montserrat; color:var(--ink); margin-top:4px; }

#s09 .stats { margin-top:18px; display:grid; grid-template-columns:repeat(4,1fr); gap:12px; }
#s09 .stt { padding:16px 14px; text-align:center; }
#s09 .stt .big { display:block; font-size:58px; color:var(--blue); }
#s09 .stt span:last-child { display:block; font:800 17px/1.25 Montserrat; color:var(--ink2); margin-top:6px; }
#s09 .stt small { font:700 13px 'JetBrains Mono'; color:var(--muted); }
/* ---- s10 clean sheet */
#s10 .sheet { margin-top:22px; padding:8px 0; }
#s10 .tr { display:grid; grid-template-columns:118px 150px 1fr; align-items:center; gap:0; border-bottom:2px solid #E6EBF3; min-height:84px; }
#s10 .tr:last-child { border-bottom:none; }
#s10 .tr.th { min-height:52px; border-bottom:3px solid var(--ink); }
#s10 .tr.th > div { font:800 15px 'JetBrains Mono'; color:var(--muted); letter-spacing:.12em; }
#s10 .tr > div { padding:0 16px; }
#s10 .tr .m { font-family:'Archivo Black'; font-size:24px; color:var(--blue); }
#s10 .tr .w { font:700 17px 'JetBrains Mono'; color:var(--ink2); }
#s10 .tr .d { font:700 20px/1.3 Montserrat; color:var(--ink); }
#s10 .tr .d em { font-style:normal; background:linear-gradient(transparent 55%, rgba(255,194,26,.7) 55%); font-weight:900; }
#s10 .tr .d small { display:block; font:600 16px Montserrat; color:var(--muted); margin-top:2px; }

/* ---- s11 quiz + cta */
#s11 .qs { margin-top:22px; display:flex; flex-direction:column; gap:12px; }
#s11 .q { display:flex; align-items:center; gap:16px; padding:14px 18px; }
#s11 .q .n { width:42px; height:42px; border-radius:50%; background:var(--ink); color:#fff; display:flex; align-items:center; justify-content:center; font:900 20px Montserrat; flex:none; }
#s11 .q p { flex:1; font:700 20px/1.3 Montserrat; color:var(--ink); }
#s11 .q p small { display:block; font:600 16px/1.3 Montserrat; color:var(--muted); margin-top:3px; }
#s11 .q .a { width:56px; height:56px; border-radius:14px; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:28px; color:#fff; flex:none; }
#s11 .q .a.d { background:var(--green); } #s11 .q .a.y { background:var(--red); }
#s11 .cta { margin-top:18px; display:flex; align-items:center; gap:16px; }
#s11 .cta .btn { display:flex; align-items:center; gap:10px; padding:16px 22px; border-radius:14px; font:900 22px Montserrat; }
#s11 .cta .b1 { background:var(--blue); color:#fff; } #s11 .cta .b2 { background:#fff; color:var(--ink); border:2px solid var(--line); }
#s11 .cta .src { margin-left:6px; text-align:left; font:700 15px/1.4 'JetBrains Mono'; color:var(--muted); }
#s11 .koc { position:absolute; right:-30px; bottom:-24px; height:330px; filter:drop-shadow(0 12px 18px rgba(14,27,51,.2)); }
"""


def hdr(i, label):
    return (f'<div class="hdr"><div class="sign"><span class="sh">TIR</span>TIR İŞLEMLERİ · SERİ NO: 9</div>'
            f'<div class="pg">{label}<b>{i:02d}/{N:02d}</b></div></div>')


def road(i):
    x = round(150 + (i - 1) / (N - 1) * 640)
    last = i == N
    sw = '' if last else f'<div class="swipe">KAYDIR {ic("arrow", 24, sw=3)}</div>'
    km = "".join(f'<span class="km" style="left:{round(150 + k / (N - 1) * 640 + 70)}px">{k + 1:02d}</span>' for k in range(N) if k + 1 != i)
    return (f'<div class="road"><div class="lane"></div>{km}<div class="logo"><img src="img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu"/></div>'
            f'<div style="position:absolute;left:{x}px;top:-30px">{truck(176)}</div>{sw}</div>')


def slide(i, label, body):
    return f'<section class="slide" id="s{i:02d}">{hdr(i, label)}<div class="c">{body}</div>{road(i)}</section>'


S = []

# ------------------------------------------------------------ 01 kapak
S.append(slide(1, "KAPAK", f'''
{plate(340)}
<div class="rg card"><div class="r1">RESMÎ GAZETE · TİCARET BAKANLIĞI</div><div class="r2"><b>4 Temmuz 2026</b> · Sayı 33300</div></div>
<div class="ttl"><small>Gümrük Genel Tebliği (TIR İşlemleri)</small><div class="big">Seri No: <em>9</em></div>
  <div class="sub">Seri No: 1'de <span>neler değişti?</span></div></div>
<div class="nums">
  <div class="num card"><span class="md">md. 3 · 15</span><div class="v"><s>2</s> → 3 yıl</div><div class="l">Taşıt onay belgesinin geçerlilik süresi</div></div>
  <div class="num card"><span class="md">md. 20/1</span><div class="v">≤ 8</div><div class="l">Hareket + varış gümrük idaresi toplamı</div></div>
  <div class="num card"><span class="md">md. 20/3-a</span><div class="v">15 idare</div><div class="l">Art arda iki TIR karnesiyle</div></div>
  <div class="num card"><span class="md">md. 8/4</span><div class="v">RİSK</div><div class="l">Süre aşımında fiziki kontrol risk değerlendirmesine bağlı</div></div>
</div>
<div class="bub card">8 maddelik tebliğ, <em>11 sayfada</em> şema şema!</div>
<img class="koc" src="img/koc-cutout.png" alt="Gümrük Koçu"/>
'''))

# ------------------------------------------------------------ 02 mind map
NODES = [  # (x, y, color, icon, title, md, text)
    (0, 0, "#14935A", "cert", "Taşıt onay belgesi", "MD. 1 · 3 → 3/1-u · 15/3", "Geçerlilik <em>2 yıl → 3 yıl</em>"),
    (0, 330, "#D63A3A", "clock", "Süre aşımı", "MD. 2 → 8/4", "Fiziki kontrol <em>risk bazlı</em>: gerekli görülürse"),
    (0, 660, "#2E6BD6", "flag", "İdare sayısı", "MD. 4 → 20/1", "Hareket + varış toplamı <em>≤ 8</em>; sınır 3 ≤ n &lt; 7"),
    (660, 0, "#0F3E96", "layers", "8'den fazla idare", "MD. 4 → 20/3", "<em>A:</em> art arda 2 karne (15)<br/><em>B:</em> her taşıta ayrı karne"),
    (660, 330, "#7A4CD9", "building", "Kurum adları", "MD. 5", "Gümrük ve <em>Dış</em> Ticaret BM · Ulaştırma ve Altyapı Bak."),
    (660, 660, "#E08A00", "doc", "Ekler · yürürlük", "MD. 6 · 7 · 8", "EK-3, EK-4, EK-10 yenilendi · <em>yayımında</em> yürürlükte"),
]
wires = []
for x, y, col, *_ in NODES:
    sx, sy = (330, 485) if x == 0 else (630, 485)
    ex, ey = (x + 300, y + 95) if x == 0 else (x, y + 95)
    mx = (sx + ex) / 2
    wires.append(f'<path d="M{sx} {sy} C{mx} {sy} {mx} {ey} {ex} {ey}" stroke="{col}" stroke-width="5" fill="none" stroke-linecap="round"/>'
                 f'<circle cx="{ex}" cy="{ey}" r="8" fill="{col}"/><circle cx="{sx}" cy="{sy}" r="7" fill="#fff" stroke="{col}" stroke-width="4"/>')
nodes = "".join(
    f'<div class="node card" style="left:{x}px;top:{y}px;border-color:{col}"><div class="nh"><span class="ib" style="background:{col}">{ic(icn, 26)}</span><b>{t}</b></div>'
    f'<div class="md">{md}</div><div class="tx">{tx}</div></div>' for x, y, col, icn, t, md, tx in NODES)
S.append(slide(2, "ZİHİN HARİTASI", f'''
<div class="kick">DEĞİŞİKLİK HARİTASI</div><div class="h2">6 başlıkta <em>Seri No: 9</em></div>
<div class="map"><svg class="wires" viewBox="0 0 960 980">{"".join(wires)}</svg>
  <div class="hub">{plate(260)}<b>SERİ NO: 1 DEĞİŞİYOR</b></div>{nodes}</div>
'''))

# ------------------------------------------------------------ 03 taşıt onay belgesi
S.append(slide(3, "TAŞIT ONAY BELGESİ", f'''
<div class="kick"><span class="md">MD. 1 · MD. 3</span>md. 3/1-(u) · md. 15/3</div><div class="h2">Taşıt onay belgesi<br/>artık <em>3 yıl</em> geçerli</div>
<div class="hero">
  <div class="doc"><span class="ek">EK-3</span><div class="dh">TAŞIT ONAY<br/>BELGESİ<small>TIR SÖZL. EK-4 ÖRNEĞİ</small></div>
    <div class="ln" style="width:86%"></div><div class="ln" style="width:70%"></div><div class="ln" style="width:78%"></div><div class="ln" style="width:52%"></div>
    <div class="seal"><b>3</b><span>YIL</span></div></div>
  <div class="yrs">
    <div class="yr o card"><span class="tag t-old">ESKİ</span><span class="big">2</span><div class="d"><b>yıl geçerlilik</b><span>“iki” ibaresi</span></div></div>
    <div class="yr n card"><span class="tag t-new">YENİ</span><span class="big">3</span><div class="d"><b>yıl geçerlilik</b><span>“üç” — tanım + düzenleme</span></div></div>
  </div>
</div>
<div class="flow">
  <div class="st card"><div class="ib">{ic("check", 26)}</div><b>Tezkiyeli firma</b><span>adına kayıtlı taşıt</span></div>
  <div class="st card"><div class="ib">{ic("scan", 26)}</div><b>Ek-2 teknik şart</b><span>TIR Sözleşmesi</span></div>
  <div class="st card"><div class="ib">{ic("building", 26)}</div><b>3 kişilik komisyon</b><span>ETOBS · yetkili idare</span></div>
  <div class="st card"><div class="ib">{ic("cert", 26)}</div><b>Belge: 3 yıl</b><span>ek-4 örneğine uygun</span></div>
</div>
<div class="notes">
  <div class="note n-y"><span class="tag t-onemli">{ic("star", 18)} ÖNEMLİ</span><div>Değişiklik iki yerde birlikte yapıldı: <b>tanım (3/1-u)</b> ve <b>düzenleme (15/3)</b> — ikisi de artık “üç yıl”.</div></div>
  <div class="note n-b"><span class="tag t-same">DEĞİŞMEDİ</span><div>Belge <b>en fazla 3 defa</b> yenilenebilir (md. 16/4); süre yurt dışında biterse <b>bir defalık 30 gün</b> ek süre (md. 16/1).</div></div>
</div>
'''))

# ------------------------------------------------------------ 04 süre aşımı
S.append(slide(4, "SÜRE AŞIMI", f'''
<div class="kick"><span class="md">MD. 2</span>md. 8/4</div><div class="h2">Süre aşımında fiziki kontrol<br/>artık <em>risk bazlı</em></div>
<div class="sea">
  <div class="sc card"><span class="big">120<small>saat</small></span><div class="m"><b>NİSAN → EYLÜL</b>azami güzergâh kat etme süresi</div></div>
  <div class="sc card"><span class="big">168<small>saat</small></span><div class="m"><b>EKİM → MART</b>azami güzergâh kat etme süresi</div></div>
</div>
<div class="chain">
  <div class="step card"><span class="ib" style="background:var(--red)">{ic("clock", 30)}</span><div><b>Süre aşıldı</b><span>Taşıt varış / çıkış idaresine geç geldi</span></div><span class="tag t-same">md. 8/4</span></div>
  <div class="dn">{ic("arrow", 34, sw=3).replace('viewBox', 'style="transform:rotate(90deg)" viewBox')}</div>
  <div class="step card"><span class="ib" style="background:var(--ink)">{ic("gavel", 30)}</span><div><b>Para cezası — GK md. 241</b><span>İlgili fıkralar uyarınca uygulanmaya devam eder</span></div><span class="tag t-same">DEĞİŞMEDİ</span></div>
  <div class="dn">{ic("arrow", 34, sw=3).replace('viewBox', 'style="transform:rotate(90deg)" viewBox')}</div>
  <div class="fk">
    <div class="side card o"><span class="tag t-old">ESKİ</span><p>“Ayrıca, bu taşıtlar fiziki kontrole tabi tutulur.” → <b>her durumda</b></p></div>
    <div class="side card n"><span class="tag t-new">YENİ</span><p>Bu taşıtlar <em>diğer risk unsurları da dikkate alınarak gerekli görülmesi halinde</em> fiziki kontrole tabi tutulur.</p></div>
  </div>
</div>
<div class="note n-r" style="margin-top:18px"><span class="tag t-tuzak">TUZAK</span><div>Ceza kalkmadı! Değişen yalnızca <b>fiziki kontrol</b>; süre aşımında <b>GK 241 para cezası</b> aynen uygulanır.</div></div>
'''))

# ------------------------------------------------------------ 05 8 idare
posts = [("H1", "h"), ("H2", "h"), ("H3", "h"), ("V1", "v"), ("V2", "v"), ("V3", "v"), ("V4", "v"), ("V5", "v")]
lane = "".join(f'<div class="post" style="left:{22 + k * 96}px"><div class="bx {c}">{t}</div><div class="pole"></div><i>{k + 1}</i></div>' for k, (t, c) in enumerate(posts))
S.append(slide(5, "İDARE SAYISI", f'''
<div class="kick"><span class="md">MD. 4</span>md. 20/1</div><div class="h2">Bir TIR taşımasında<br/>en fazla <em>8 idare</em></div>
<div class="lane"><div class="dash"></div>{lane}<div class="lim">8</div></div>
<div class="leg"><span><i style="background:var(--blue2)"></i>Hareket (H)</span><span><i style="background:var(--green)"></i>Varış (V)</span><span>örnek: 3 H + 5 V = 8</span></div>
<div class="rules">
  <div class="rule card"><span class="big">H+V ≤ 8</span><p><small>KURAL</small>Hareket ve varış gümrük idarelerinin <b>toplam sayısı sekizi geçemez</b>.</p></div>
  <div class="rule card"><span class="big">3≤n&lt;7</span><p><small>İDARELERİN SINIRLAMA YETKİSİ</small>Hareket (veya varış) idarelerinin azami sayısı <b>üçten az olmamak üzere yediden az</b> sınırlandırılabilir.</p></div>
  <div class="rule card"><span class="big">H → V</span><p><small>SIRA</small>Karne, varış idaresine ancak <b>hareket idaresi/idareleri kabul ettiyse</b> sunulur.</p></div>
</div>
<div class="boxes">
  <div class="bx2 card"><span class="k">2</span><div><b>2 no.lu kutu</b><br/>hareket idaresi/idareleri</div></div>
  <div class="bx2 card"><span class="k">12</span><div><b>12 no.lu kutu</b><br/>varış idareleri + boşaltılacak miktar</div></div>
</div>
'''))

# ------------------------------------------------------------ 06 yöntem A
k1 = "".join(f'<i class="{c}">{t}</i>' for t, c in [("H1", "h"), ("H2", "h"), ("V1", "v"), ("V2", "v"), ("V3", "v"), ("V4", "v"), ("V5", "v"), ("8", "x")])
k2 = "".join(f'<i class="v">V{k}</i>' for k in range(1, 8))
S.append(slide(6, "YÖNTEM A", f'''
<div class="kick"><span class="md">MD. 4</span>md. 20/3-(a)</div><div class="h2">8'den fazla idare:<br/><em>art arda iki karne</em></div>
<div class="tl">
  <div class="kn k1"><div class="kh">{ic("doc", 28)}1. KARNE <span class="big">≤ 8</span></div><div class="slots">{k1}</div>
    <div class="cap">8. idarede <b>sonlandırılır</b>; son varışın eşyası boşaltılır, kalan eşya 2. karneye kaydedilir.</div></div>
  <div class="kn k2"><div class="kh" style="justify-content:flex-end">2. KARNE <span class="big">≤ 7 V</span>{ic("doc", 28)}</div><div class="slots">{k2}</div>
    <div class="cap" style="padding-left:30px">1. karnenin son varışı = 2. karnenin <b>hareket</b> idaresi</div></div>
  <div class="swap"><b>8.</b>idare<br/>devir</div>
</div>
<div class="sum card"><div><span class="big c1">8</span><small>1. karne</small></div><span class="op">+</span><div><span class="big c2">7</span><small>2. karne</small></div><span class="op">=</span><div><span class="big c3">15</span><small>toplam idare</small></div></div>
<div class="recs">
  <div class="rec card"><div class="rh">{ic("pen", 22)} 1. KARNE · TÜM YAPRAKLAR</div><p>2 no.lu kutunun altındaki <b>“resmi kullanım için”</b> bölümüne → <b>yeni karnenin no'su</b></p></div>
  <div class="rec card"><div class="rh">{ic("scan", 22)} TIR/TRANSİT TAKİP · VOLET-1</div><p><b>“referans karne no”</b> alanına → <b>1. karnenin no'su</b>; her iki karneye durum kaydı</p></div>
</div>
<div class="note n-r"><span class="tag t-dikkat">{ic("warn", 18)} DİKKAT</span><div>TIR Sözleşmesi md. 2 gereği <b>her iki TIR taşıması da en az bir sınır geçilerek</b> yapılmalı.</div></div>
'''))

# ------------------------------------------------------------ 07 yöntem B
cont = ('<svg viewBox="0 0 900 250" width="792" height="220" aria-hidden="true">'
        '<rect x="20" y="40" width="250" height="150" rx="6" fill="#2E6BD6"/><rect x="290" y="40" width="250" height="150" rx="6" fill="#14935A"/>'
        '<rect x="560" y="40" width="200" height="150" rx="6" fill="#E08A00"/>'
        + "".join(f'<path d="M{x} 52v126" stroke="rgba(255,255,255,.35)" stroke-width="5"/>' for x in list(range(44, 260, 26)) + list(range(314, 530, 26)) + list(range(584, 750, 26)))
        + '<path d="M770 190V96h60l46 46v48z" fill="#0F3E96" stroke="#0E1B33" stroke-width="4" stroke-linejoin="round"/><path d="M784 106h40l32 32h-72z" fill="#BFD3F5"/>'
        + '<rect x="20" y="190" width="856" height="12" fill="#0E1B33"/>'
        + "".join(f'<circle cx="{x}" cy="214" r="22" fill="#1A1F29"/><circle cx="{x}" cy="214" r="9" fill="#B8C2D3"/>' for x in (70, 130, 340, 400, 600, 680, 840))
        + "".join(f'<g transform="translate({x},74)"><rect width="92" height="62" rx="8" fill="#fff"/><text x="46" y="27" text-anchor="middle" font-family="Archivo Black" font-size="17" fill="#0E1B33">KARNE</text><text x="46" y="51" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="18" fill="#0F3E96">#{n}</text></g>'
                  for x, n in ((99, 1), (369, 2), (614, 3)))
        + '</svg>')
S.append(slide(7, "YÖNTEM B", f'''
<div class="kick"><span class="md">MD. 4</span>md. 20/3-(b)</div><div class="h2">Aynı anda <em>birden fazla</em><br/>TIR taşıması</div>
<div class="scene">{cont}<div class="dash"></div></div>
<div class="grid3">
  <div class="gi card"><div class="rh"><span class="ib" style="background:var(--blue2)">{ic("box", 24)}</span>Ne zaman?</div><p><b>Taşıt dizisi</b> veya <b>birden fazla konteyner</b> ile TIR taşıması</p></div>
  <div class="gi card"><div class="rh"><span class="ib" style="background:var(--green)">{ic("doc", 24)}</span>Nasıl?</div><p>Her taşıt veya konteyner için <b>ayrı TIR karnesi</b> düzenlenebilir (TIR Sözl. md. 17/1)</p></div>
  <div class="gi card"><div class="rh"><span class="ib" style="background:var(--ink)">{ic("link", 24)}</span>Çapraz kayıt</div><p>Hareket idaresi, her karnenin 2 no.lu kutu altına ve Volet-1 <b>“referans karne no”</b> alanına <b>diğer karnelerin no'larını</b> yazar</p></div>
  <div class="gi card"><div class="rh"><span class="ib" style="background:#E08A00">{ic("unload", 24)}</span>Her iki yöntemde</div><p>Eşya, diğerlerini <b>boşaltıp yeniden yüklemeyi gerektirmeyecek</b> şekilde ayrılabilir yüklenir; bir karnenin işlemleri diğerlerinde de yapılır.</p><span class="tag t-same">DEĞİŞMEDİ · 20/4-5</span></div>
</div>
<div class="cmp card"><div class="cr ch"><div></div><div><b class="ca">A</b> ART ARDA</div><div><b class="cb">B</b> AYNI ANDA</div></div>
  <div class="cr"><div>Karneler</div><div>Sıralı: 1. biter, 2. başlar</div><div>Paralel: taşıt/konteyner başına bir karne</div></div>
  <div class="cr"><div>Kayıt</div><div>1. karneye yeni no · Volet-1'e 1. karne no</div><div>Her karneye diğerlerinin no'ları</div></div>
  <div class="cr"><div>Dayanak</div><div>15 idare · her taşıma ≥ 1 sınır (Sözl. md. 2)</div><div>TIR Sözl. md. 17/1</div></div></div>
'''))

# ------------------------------------------------------------ 08 kurum adları
S.append(slide(8, "KURUM ADLARI", f'''
<div class="kick"><span class="md">MD. 5</span>ibare değişiklikleri</div><div class="h2">Kurum adları <em>güncellendi</em></div>
<div class="rn card"><div class="ttl"><span class="ib">{ic("building", 26)}</span>BÖLGE MÜDÜRLÜKLERİ</div>
  <div class="row"><div class="nm o">Gümrük ve Ticaret Bölge Müdürlükleri</div><span class="arr">{ic("arrow", 44, sw=3)}</span><div class="nm n">Gümrük ve <em>Dış</em> Ticaret Bölge Müdürlükleri</div></div>
  <div class="where"><small>NEREDE:</small><span>3/1-(u)</span><span>15/1</span><span>18/6-(b)</span><span>45/1</span></div></div>
<div class="rn card"><div class="ttl"><span class="ib">{ic("route", 26)}</span>ULAŞTIRMA BAKANLIĞI</div>
  <div class="row"><div class="nm o">Ulaştırma, Denizcilik ve Haberleşme Bakanlığı</div><span class="arr">{ic("arrow", 44, sw=3)}</span><div class="nm n">Ulaştırma ve <em>Altyapı</em> Bakanlığı</div></div>
  <div class="where"><small>NEREDE:</small><span>3/1-(r)</span><span>3/1-(hh)</span><span>4/2</span><span>8/2</span><span>10/1</span><span>63/1</span><span>65/2</span></div></div>
<div class="note n-g" style="margin-top:24px"><span class="tag t-new">{ic("check", 18)} BİLGİ</span><div>Md. 5 <b>yalnızca kurum adlarını</b> günceller; değişen ibarelerin geçtiği hükümlerin içeriği aynı kalır.</div></div>
<div class="note n-b" style="margin-top:14px"><span class="tag t-onemli">{ic("star", 18)} ÖNEMLİ</span><div>Özel izin belgesi ve <b>özel yük taşıma izin belgesi</b> artık “Ulaştırma ve Altyapı Bakanlığı”ndan; uluslararası taşıma <b>yetki belgesi</b> de aynı bakanlıktan alınır (md. 3/1-r, 10/1).</div></div>
'''))

# ------------------------------------------------------------ 09 ekler & yürürlük
S.append(slide(9, "EKLER · YÜRÜRLÜK", f'''
<div class="kick"><span class="md">MD. 6 · 7 · 8</span>ekler, yürürlük, yürütme</div><div class="h2">Yenilenen ekler ve<br/><em>yürürlük</em></div>
<div class="eks">
  <div class="ek card"><div class="et">EK-3 {ic("cert", 30)}</div><b>Taşıt onay belgesi</b><span>Örnek belge yenilendi (3 yıllık süre)</span></div>
  <div class="ek card"><div class="et">EK-4 {ic("doc", 30)}</div><b>TIR karnesi</b><span>TIR Sözl. ek-1 örneğine uygun karne</span></div>
  <div class="ek card"><div class="et">EK-10 {ic("x", 30)}</div><b>İçki-sigara listesi</b><span>Normal karneyle (Model 1) taşınamayan eşya</span></div>
</div>
<div class="tline card"><div class="bar"></div><div class="pts">
  <div class="pt"><div class="dot" style="background:#8A96AA">{ic("doc", 28)}</div><b>31.12.2010</b><span>Seri No: 1 yayımlandı<br/>RG 27802 (5. mük.)</span></div>
  <div class="pt"><div class="dot" style="background:var(--blue)">{ic("calendar", 28)}</div><b>04.07.2026</b><span>Seri No: 9 · RG 33300<br/>yayım = <b>yürürlük</b></span></div>
</div></div>
<div class="stats">
  <div class="stt card"><span class="big">8</span><span>madde</span></div>
  <div class="stt card"><span class="big">4</span><span>hüküm yeniden yazıldı<br/><small>3/1-u · 8/4 · 15/3 · 20</small></span></div>
  <div class="stt card"><span class="big">11</span><span>kurum adı ibaresi</span></div>
  <div class="stt card"><span class="big">3</span><span>ek yenilendi</span></div>
</div>
<div class="yy">
  <div class="card"><span class="ib" style="background:var(--green)">{ic("check", 32)}</span><div><small>MD. 7 · YÜRÜRLÜK</small><b>Yayımı tarihinde</b></div></div>
  <div class="card"><span class="ib" style="background:var(--blue)">{ic("building", 32)}</span><div><small>MD. 8 · YÜRÜTME</small><b>Ticaret Bakanı</b></div></div>
</div>
'''))

# ------------------------------------------------------------ 10 clean sheet
ROWS = [("Md. 1", "3/1-(u)", "Taşıt onay belgesi geçerliliği <em>iki → üç yıl</em>", "tanım hükmü"),
        ("Md. 2", "8/4", "Süre aşımında fiziki kontrol <em>risk unsurlarına göre</em>", "GK 241 para cezası aynen"),
        ("Md. 3", "15/3", "Belge <em>üç yıl</em> geçerli düzenlenir", "3 kişilik komisyon · ETOBS"),
        ("Md. 4", "20/1", "H + V idare toplamı <em>≤ 8</em>; sınırlama 3 ≤ n &lt; 7", "karne önce hareketçe kabul edilir"),
        ("Md. 4", "20/3", "8'den fazla: <em>(a)</em> art arda 2 karne = 15 · <em>(b)</em> ayrı karneler", "her taşıma en az bir sınır geçer"),
        ("Md. 5", "çeşitli", "Kurum adları: <em>Dış Ticaret</em> BM · <em>Ulaştırma ve Altyapı</em> Bak.", "11 ibare değişti"),
        ("Md. 6", "Ekler", "<em>EK-3 · EK-4 · EK-10</em> yenilendi", "belge · karne · içki-sigara listesi"),
        ("Md. 7·8", "—", "<em>Yayımında</em> yürürlükte · yürütme <em>Ticaret Bakanı</em>", "RG 04.07.2026 / 33300")]
rows = "".join(f'<div class="tr"><div class="m">{m}</div><div class="w">{w}</div><div class="d">{d}<small>{s}</small></div></div>' for m, w, d, s in ROWS)
S.append(slide(10, "CLEAN SHEET", f'''
<div class="kick">TEK SAYFA ÖZET · KAYDET</div><div class="h2">Seri No: 9 <em>clean sheet</em></div>
<div class="sheet card"><div class="tr th"><div>MADDE</div><div>YER</div><div>NE DEĞİŞTİ</div></div>{rows}</div>
'''))

# ------------------------------------------------------------ 11 quiz + cta
QS = [("Taşıt onay belgesi artık 3 yıl geçerli.", "md. 3/1-(u) ve 15/3", "d", "D"),
      ("Süre aşan her taşıt mutlaka fiziki kontrole tabi tutulur.", "Hayır: risk unsurları dikkate alınarak gerekli görülürse (8/4)", "y", "Y"),
      ("Süre aşımında GK 241 para cezası kaldırıldı.", "Hayır: ceza aynen uygulanır", "y", "Y"),
      ("Hareket + varış idaresi toplamı en fazla 8'dir.", "md. 20/1", "d", "D"),
      ("Art arda iki karneyle toplam 16 idarede işlem yapılır.", "Hayır: 8 + 7 = 15 (20/3-a)", "y", "Y"),
      ("Taşıt dizisinde her taşıt için ayrı karne düzenlenebilir.", "TIR Sözl. md. 17/1 · 20/3-(b)", "d", "D")]
qs = "".join(f'<div class="q card"><span class="n">{k + 1}</span><p>{t}<small>{w}</small></p><span class="a {c}">{a}</span></div>' for k, (t, w, c, a) in enumerate(QS))
S.append(slide(11, "KENDİNİ TEST ET", f'''
<img class="koc" src="img/koc-dikkat.png" alt="Gümrük Koçu"/>
<div class="kick">DOĞRU MU · YANLIŞ MI?</div><div class="h2">Kendini <em>test et</em></div>
<div class="qs">{qs}</div>
<div class="cta"><div class="btn b1">{ic("save", 26)} KAYDET</div><div class="btn b2">{ic("share", 26)} PAYLAŞ</div>
  <div class="src">Kaynak: RG 04.07.2026 / 33300<br/>Gümrük Genel Tebliği (TIR İşl.) Seri No: 1</div></div>
'''))

HTML = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"/><title>TIR İşlemleri Seri No: 9 — carousel</title>
<link rel="stylesheet" href="fonts/fonts.css"/><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>"""
(D / "carousel.html").write_text(HTML)
print("slides:", len(S))
