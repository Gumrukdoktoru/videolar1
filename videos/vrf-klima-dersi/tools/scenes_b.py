"""Scenes 06-10."""
from lib import T, D, icon, badge, odu, idu, valve

S = {}

# ---------------------------------------------------------------- s06 Önemli
S["s06"] = dict(
    sfx=[("impact-bass-1", T("s06", "önemli") + 0.1, 0.35), ("error", T("s06", "belirleyici") + 0.1, 0.18),
         ("chime", T("s06", "fiili"), 0.22)],
    keys=dict(
        onemli=T("s06", "önemli"), esy=T("s06", "eşyanın"), ms=T("s06", "multi"), bir2=T("s06", "bir", 2),
        bag=T("s06", "bağlanabilmesi"), tarife=T("s06", "tarife"), belir=T("s06", "belirleyici"), degil=T("s06", "değil"),
        esas=T("s06", "esas"), fiili=T("s06", "fiili"), calisma=T("s06", "çalışma"),
    ),
    css=r"""
#s06 .bdg { position:absolute; left:600px; top:134px; }
#s06 .h1 { position:absolute; left:1034px; top:152px; margin:0; font-size:52px; width:790px; white-space:nowrap; }
#s06 .colt { position:absolute; left:600px; top:318px; font:700 24px 'JetBrains Mono'; letter-spacing:.16em; color:var(--uyari); }
#s06 .it { position:absolute; left:600px; width:490px; height:160px; padding:22px 28px; overflow:hidden; }
#s06 .i1 { top:362px; } #s06 .i2 { top:550px; }
#s06 .it .mono { font:700 20px 'JetBrains Mono'; letter-spacing:.14em; color:var(--muted); }
#s06 .it .big { font-family:'Archivo Black'; font-size:56px; color:var(--ms); margin-top:8px; }
#s06 .it .row { display:flex; align-items:center; gap:18px; margin-top:10px; font:700 28px/1.2 Montserrat; color:var(--fg); }
#s06 .it .sk { position:absolute; left:18px; right:18px; top:50%; height:8px; background:var(--uyari); border-radius:4px; transform-origin:left center; box-shadow:0 0 18px rgba(255,77,94,.6); }
#s06 .it .xx { position:absolute; right:14px; top:12px; color:var(--uyari); }
#s06 .arr { position:absolute; left:1100px; top:500px; color:var(--vrf); }
#s06 .esas { position:absolute; left:1166px; top:362px; width:390px; height:348px; padding:26px 30px; border-color:var(--vrf) !important; }
#s06 .esas .t { font:700 24px 'JetBrains Mono'; letter-spacing:.16em; color:var(--vrf); }
#s06 .esas .r { display:flex; align-items:center; gap:16px; margin-top:34px; font:900 36px/1.15 Montserrat; color:var(--fg); }
#s06 .esas .r .ico { color:var(--vrf); }
#s06 .baba { position:absolute; left:1590px; top:452px; height:600px; }
#s06 .bub { position:absolute; left:1166px; top:742px; width:400px; padding:18px 24px; background:#F4F7FF; color:#14204a; border-radius:20px;
  font:700 27px/1.25 Montserrat; box-shadow:0 18px 40px rgba(0,0,0,.4); }
#s06 .bub:after { content:""; position:absolute; right:-26px; top:26px; border-width:16px 0 16px 30px; border-style:solid; border-color:transparent transparent transparent #F4F7FF; }
#s06 .bub b { color:#C6283A; }
""",
    body=r"""
<div class="bdg">BADGE</div>
<div class="h1">Tarifede belirleyici olan ne?</div>
<div class="colt">BELİRLEYİCİ DEĞİL</div>
<div class="it card i1"><div class="mono">FATURA · TİCARİ AD</div><div class="big">MULTI-SPLIT</div><i class="sk"></i><span class="xx">XI</span></div>
<div class="it card i2"><div class="mono">BAĞLANTI SAYISI</div><div class="row">MINI<span>1 dış ünite → birden fazla iç ünite</span></div><i class="sk"></i><span class="xx">XI</span></div>
<div class="arr">ARR</div>
<div class="esas card"><div class="t">ESAS ALINAN</div>
  <div class="r r1">CHK Fiili teknik yapı</div>
  <div class="r r2">CHK Çalışma prensibi</div>
</div>
<img class="baba" src="assets/img/baba-crop.png" alt="Gümrükçü Baba" />
<div class="bub">Faturadaki <b>isme</b> değil, cihazın <b>kendisine</b> bakarım!</div>
""".replace("BADGE", badge("onemli", big=True)).replace("XI", icon("x", 44)).replace("ARR", icon("arrow", 64))
    .replace("CHK", icon("check", 44))
    .replace("MINI", '<svg width="130" height="80" viewBox="0 0 640 400">' + odu(235, 0, w=170, h=110)
             + "".join(idu(x, 330, w=110, h=44) for x in (0, 130, 260, 390, 520))
             + '<path d="M320 112 V 230 M55 230 H 575 M55 230 V 325 M185 230 V 325 M315 230 V 325 M445 230 V 325 M575 230 V 325" fill="none" stroke="#8FB2FF" stroke-width="12" stroke-linecap="round"/></svg>'),
    js=r"""
slam(".bdg .badge", K.onemli - 0.25);
tl.fromTo(q(".bdg .badge"), { boxShadow: "0 10px 0 rgba(0,0,0,.28), 0 0 0 rgba(255,197,61,0)" }, { boxShadow: "0 10px 0 rgba(0,0,0,.28), 0 0 60px rgba(255,197,61,.8)", duration: 0.5, yoyo: true, repeat: 3 }, K.onemli + 0.3);
tl.fromTo(q(".h1"), { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, Math.max(0.1, K.onemli - 0.9));
rise(".colt", K.esy, 0, 16);
slideX(".i1", K.ms - 0.2, -70);
slideX(".i2", K.bir2, -70);
tl.fromTo(q(".baba"), { x: 260, opacity: 0 }, { x: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }, K.tarife);
strike(".i1 .sk", K.belir, 0.35);
strike(".i2 .sk", K.belir + 0.3, 0.35);
pop(".it .xx", K.belir + 0.2, 0.3);
tl.to(q(".it"), { opacity: 0.55, duration: 0.4 }, K.degil + 0.3);
tl.fromTo(q(".bub"), { scale: 0.3, opacity: 0, transformOrigin: "100% 20%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }, K.degil);
tl.fromTo(q(".baba"), { rotation: 0, transformOrigin: "50% 100%" }, { rotation: -2.5, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut" }, K.degil);
tl.fromTo(q(".arr"), { x: -40, opacity: 0 }, { x: 0, opacity: 1, duration: 0.5, ease: "power3.out" }, K.esas);
tl.fromTo(q(".arr .ico"), { x: 0 }, { x: 14, duration: 0.35, yoyo: true, repeat: 5, ease: "sine.inOut" }, K.esas + 0.5);
pop(".esas", K.esas + 0.2);
slideX(".esas .r1", K.fiili, 40);
slideX(".esas .r2", K.calisma, 40);
tl.fromTo(q(".esas"), { boxShadow: "0 0 0 rgba(51,217,178,0)" }, { boxShadow: "0 0 70px rgba(51,217,178,.55)", duration: 0.6, yoyo: true, repeat: 1 }, K.calisma + 0.3);
""",
)

# ---------------------------------------------------------------- s07 Kriterler
TILES = [("valve", "EEV", "Ayrı genleşme vanası"), ("pipes", "Ortak hat", "Ortak borulama ağı"),
         ("gauge", "Kapasite", "Değişken kontrol"), ("net", "Haberleşme", "Adresleme yapısı")]
S["s07"] = dict(
    sfx=[("pop", T("s07", "kriter"), 0.3)],
    keys=dict(peki=T("s07", "peki"), yazida=T("s07", "yazıda"), dort=T("s07", "dört"), kriter=T("s07", "kriter")),
    css=r"""
#s07 .q { position:absolute; left:600px; top:160px; width:1220px; text-align:center; font-family:'Archivo Black'; font-size:50px; line-height:1.1; color:var(--fg); }
#s07 .q span { color:var(--vrf); }
#s07 .four { position:absolute; left:600px; top:290px; width:1220px; display:flex; align-items:center; justify-content:center; gap:34px; }
#s07 .four .n { font-family:'Archivo Black'; font-size:300px; line-height:.9; color:var(--vrf); text-shadow:0 0 60px rgba(51,217,178,.45); }
#s07 .four .t { font-family:'Archivo Black'; font-size:92px; line-height:1; color:var(--fg); }
#s07 .four .t small { display:block; font:700 30px Montserrat; color:var(--muted); margin-top:12px; }
#s07 .tiles { position:absolute; left:600px; top:640px; width:1220px; display:flex; gap:22px; }
#s07 .tile { flex:1; height:220px; padding:24px; display:flex; flex-direction:column; gap:10px; }
#s07 .tile .ico { color:var(--vrf); }
#s07 .tile .k { font:700 22px 'JetBrains Mono'; color:var(--accent2); letter-spacing:.12em; }
#s07 .tile .l { font:900 34px Montserrat; color:var(--fg); }
#s07 .tile .s { font:400 22px Montserrat; color:var(--muted); }
""",
    body=r"""
<div class="q">VRF'yi diğer klimalardan <span>nasıl ayırırız?</span></div>
<div class="four"><div class="n">4</div><div class="t">TEKNİK<br/>KRİTER<small>yazıda sayılan ayırt edici özellikler</small></div></div>
<div class="tiles">TILES</div>
""".replace("TILES", "".join(f'<div class="tile card">{icon(ic, 64)}<div class="k">KRİTER {i + 1}</div><div class="l">{l}</div><div class="s">{s}</div></div>' for i, (ic, l, s) in enumerate(TILES))),
    js=r"""
tl.fromTo(q(".q"), { y: 50, opacity: 0, scale: 0.96 }, { y: 0, opacity: 1, scale: 1, duration: 0.7, ease: "expo.out" }, K.peki - 0.2);
tl.fromTo(q(".four .n"), { scale: 0.2, opacity: 0, rotation: -20, transformOrigin: "50% 60%" }, { scale: 1, opacity: 1, rotation: 0, duration: 0.6, ease: "back.out(2)" }, K.dort - 0.15);
slideX(".four .t", K.dort + 0.15, 60);
tl.fromTo(q(".tile"), { y: 120, opacity: 0, rotationX: -40, transformPerspective: 900 }, { y: 0, opacity: 1, rotationX: 0, duration: 0.6, ease: "back.out(1.6)", stagger: 0.12 }, K.kriter);
tl.fromTo(q(".tile .ico"), { rotation: -12 }, { rotation: 0, duration: 0.6, ease: "elastic.out(1,0.4)", stagger: 0.12 }, K.kriter + 0.3);
""",
)


# ---------------------------------------------------------------- criterion scaffold
def crit(n, title, sub, question, extra_css, diagram, js, keys, sfx):
    sid = f"s{7 + n:02d}"
    steps = "".join(
        f'<div class="st st{i}"><div class="c">{icon("check", 34) if i < n else i}</div><div class="lb">{["EEV", "Ortak hat", "Kapasite", "Haberleşme"][i - 1]}</div></div>'
        for i in range(1, 5)
    )
    css = rf"""
#{sid} .rail {{ position:absolute; left:600px; top:300px; width:96px; height:520px; }}
#{sid} .rail .ln {{ position:absolute; left:46px; top:40px; width:4px; height:420px; background:rgba(143,178,255,.3); }}
#{sid} .st {{ position:absolute; left:-14px; width:124px; display:flex; flex-direction:column; align-items:center; gap:6px; }}
#{sid} .st1 {{ top:0; }} #{sid} .st2 {{ top:140px; }} #{sid} .st3 {{ top:280px; }} #{sid} .st4 {{ top:420px; }}
#{sid} .st .c {{ width:84px; height:84px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:40px;
  background:var(--bg2); border:4px solid rgba(143,178,255,.45); color:var(--muted); }}
#{sid} .st .lb {{ font:700 18px 'JetBrains Mono'; color:var(--muted); letter-spacing:.04em; white-space:nowrap; }}
#{sid} .st.done .c {{ background:var(--ok); border-color:var(--ok); color:#06221a; }}
#{sid} .st.cur .c {{ background:var(--vrf); border-color:#BFF5E6; color:#062a22; box-shadow:0 0 40px rgba(51,217,178,.6); }}
#{sid} .st.cur .lb {{ color:var(--fg); }}
#{sid} .hdr {{ position:absolute; left:740px; top:132px; width:1080px; }}
#{sid} .sub {{ font:400 30px/1.3 Montserrat; color:var(--muted); margin-top:10px; white-space:nowrap; }}
#{sid} .hdr .h1 {{ font-size:62px; white-space:nowrap; }}
#{sid} .dg {{ position:absolute; left:740px; top:330px; width:1080px; height:440px; }}
#{sid} .qq {{ position:absolute; left:740px; top:792px; width:1080px; display:flex; align-items:center; gap:18px; padding:16px 24px; }}
#{sid} .qq .t {{ font:700 30px/1.2 Montserrat; color:var(--fg); flex:1; }}
#{sid} .qq .ok {{ display:flex; align-items:center; gap:10px; font:900 24px Montserrat; color:#06221a; background:var(--ok); padding:10px 18px; border-radius:12px; white-space:nowrap; }}
{extra_css}
"""
    body = f"""
<div class="rail"><div class="ln"></div>{steps}</div>
<div class="hdr"><div class="kicker">KRİTER {n} / 4</div><div class="h1">{title}</div><div class="sub">{sub}</div></div>
<div class="dg">{diagram}</div>
<div class="qq card">{badge("soru")}<div class="t">{question}</div><div class="ok">{icon("check", 28)} VRF GÖSTERGESİ</div></div>
"""
    q_at = keys.pop("_q")
    for i in range(1, 5):
        pass
    js_full = (
        "q('.st').forEach((e, i) => { if (i < %d) e.classList.add('done'); if (i === %d) e.classList.add('cur'); });\n" % (n - 1, n - 1)
        + "rise('.rail .st', 0.05, 0.06, 20);\n"
        + "tl.fromTo(q('.st.cur .c'), { scale: 0.6 }, { scale: 1.12, duration: 0.45, ease: 'back.out(3)' }, 0.4);\n"
        + "tl.to(q('.st.cur .c'), { scale: 1, duration: 0.3 }, 0.85);\n"
        + "rise('.hdr .kicker', 0.1, 0, 16);\n"
        + "tl.fromTo(q('.hdr .h1'), { y: 46, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'expo.out' }, 0.25);\n"
        + "rise('.hdr .sub', 0.6, 0, 20);\n"
        + js
        + f"\nrise('.qq', {q_at}, 0, 30);\npop('.qq .ok', {keys.get('_ok', q_at + 1.0)});\n"
    )
    keys.pop("_ok", None)
    return sid, dict(css=css, body=body, js=js_full, keys=keys, sfx=sfx)


# ---------------------------------------------------------------- s08 Kriter 1: EEV
_k1_x = (330, 630, 930)
_k1 = (
    '<svg viewBox="0 0 1080 440" width="1080" height="440">'
    + "".join(f'<g class="zone"><rect x="{x - 135}" y="150" width="270" height="276" rx="20" fill="rgba(51,217,178,.06)" stroke="#33D9B2" stroke-width="3" stroke-dasharray="10 8"/>'
              f'<text x="{x - 115}" y="182" class="svgt" style="fill:#33D9B2">BÖLGE {i + 1}</text></g>' for i, x in enumerate(_k1_x))
    + odu(0, 20, w=170, h=120)
    + '<path class="pm" d="M170 80 H 1000" fill="none" stroke="#7FA6FF" stroke-width="12" stroke-linecap="round"/>'
    + "".join(f'<path class="pb" d="M{x} 80 V 336" fill="none" stroke="#7FA6FF" stroke-width="9" stroke-linecap="round"/>' for x in _k1_x)
    + '<path class="pmf" d="M170 80 H 1000" fill="none" stroke="#E0ECFF" stroke-width="4" stroke-dasharray="8 16" stroke-linecap="round"/>'
    + "".join(f'<path class="pbf" d="M{x} 80 V 336" fill="none" stroke="#E0ECFF" stroke-width="3" stroke-dasharray="6 12"/>' for x in _k1_x)
    + "".join(valve(x, 250, cls="vv", s=1.3) for x in _k1_x)
    + "".join(f'<g><g class="vt"><rect x="{x + 30}" y="226" width="78" height="36" rx="10" fill="#FFC53D"/><text x="{x + 69}" y="252" text-anchor="middle" class="svga" style="fill:#2a1d00">EEV</text></g></g>' for x in _k1_x)
    + "".join(idu(x - 95, 340, w=190, h=56) for x in _k1_x)
    + "</svg>"
)
sid, d = crit(
    1, "Her bölgeye ayrı EEV", "Soğutucu akışkan ölçme ve kısma elemanı: Elektronik Genleşme Vanası",
    "Her iç ünite ya da bölge için ayrı bir Elektronik Genleşme Vanası var mı?", "", _k1,
    r"""
fadeIn(".dg .odu", 0.5);
draw(".dg .pm", K.her - 0.2, 0.7);
draw(".dg .pb", K.her + 0.3, 0.5);
pop(".dg .idu", K.her + 0.5, 0.1);
tl.fromTo(q(".zone"), { opacity: 0 }, { opacity: 1, duration: 0.4, stagger: 0.15 }, K.bolge);
pop(".dg .vv", K.ayri, 0.15);
tl.fromTo(q(".dg .vv"), { scale: 1 }, { scale: 1.25, duration: 0.25, yoyo: true, repeat: 3, transformOrigin: "50% 50%", stagger: 0.1 }, K.kisma);
fadeIn(".dg .pmf, .dg .pbf", K.olcme, 0.3);
flow(".dg .pmf", K.olcme, D, 80);
flow(".dg .pbf", K.olcme, D, [20, 60, 40]);
pop(".dg .vt", K.elektronik, 0.12);
spinFans(0, D, 1.1);
""",
    dict(her=T("s08", "her"), bolge=T("s08", "bölge"), ayri=T("s08", "ayrı"), olcme=T("s08", "ölçme"), kisma=T("s08", "kısma"),
         elektronik=T("s08", "elektronik"), _q=T("s08", "elektronik", off=-0.6), _ok=T("s08", "var")),
    [("pop", T("s08", "ayrı"), 0.3), ("ping", T("s08", "var"), 0.25)],
)
S[sid] = d

# ---------------------------------------------------------------- s09 Kriter 2: Ortak hat
_k2_x = (430, 630, 830, 1030)
_k2 = (
    '<svg viewBox="0 0 1080 440" width="1080" height="440">'
    + '<g class="grp"><rect x="-10" y="0" width="400" height="190" rx="22" fill="rgba(143,178,255,.06)" stroke="#8FB2FF" stroke-width="3" stroke-dasharray="10 8"/>'
      '<text x="10" y="-12" class="svgt" style="fill:#8FB2FF">DIŞ ÜNİTE GRUBU</text></g>'
    + odu(10, 20, w=170, h=120) + odu(200, 20, w=170, h=120)
    + '<path class="pm" d="M95 140 V 230 M285 140 V 230 M95 230 H 1030" fill="none" stroke="#7FA6FF" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>'
    + '<path class="pmf" d="M95 140 V 230 H 1030 M285 140 V 230" fill="none" stroke="#E0ECFF" stroke-width="4" stroke-dasharray="8 16" stroke-linecap="round"/>'
    + "".join(f'<path class="pb" d="M{x} 230 V 336" fill="none" stroke="#7FA6FF" stroke-width="9" stroke-linecap="round"/>' for x in _k2_x)
    + "".join(f'<path class="pbf" d="M{x} 230 V 336" fill="none" stroke="#E0ECFF" stroke-width="3" stroke-dasharray="6 12"/>' for x in _k2_x)
    + "".join(f'<rect class="joint" x="{x - 9}" y="221" width="18" height="18" rx="3" transform="rotate(45 {x} 230)" fill="#FFC53D"/>' for x in _k2_x)
    + '<g class="mlab"><rect x="520" y="166" width="300" height="40" rx="12" fill="#FFC53D"/><text x="670" y="194" text-anchor="middle" class="svga" style="fill:#2a1d00;font-size:20px">ORTAK ANA HAT</text></g>'
    + "".join(idu(x - 85, 340, w=170, h=54) for x in _k2_x)
    + "</svg>"
)
sid, d = crit(
    2, "Ortak soğutucu akışkan hattı", "Aynı ana hat üzerinden birden fazla iç ünite / bölge beslenir",
    "Ortak bir soğutucu akışkan hattı / borulama ağı var mı?", "", _k2,
    r"""
tl.fromTo(q(".dg .odu"), { y: -30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "power3.out", stagger: 0.15 }, K.dis);
tl.fromTo(q(".dg .grp"), { opacity: 0 }, { opacity: 1, duration: 0.4 }, K.grubu - 0.3);
draw(".dg .pm", K.ayni, 0.9);
tl.fromTo(q(".dg .pm"), { filter: "drop-shadow(0 0 0px #FFC53D)" }, { filter: "drop-shadow(0 0 14px #FFC53D)", duration: 0.4, yoyo: true, repeat: 3 }, K.ana + 0.4);
pop(".dg .mlab", K.ana + 0.2);
draw(".dg .pb", K.birden, 0.5);
pop(".dg .joint", K.birden, 0.08);
pop(".dg .idu", K.birden + 0.3, 0.1);
fadeIn(".dg .pmf, .dg .pbf", K.besle, 0.3);
flow(".dg .pmf", K.besle, D, 80);
flow(".dg .pbf", K.besle, D, [30, 55, 20, 45]);
spinFans(0, D, 1.1);
""",
    dict(dis=T("s09", "dış"), grubu=T("s09", "grubu"), ayni=T("s09", "aynı"), ana=T("s09", "ana"), birden=T("s09", "birden"),
         besle=T("s09", "besleyebiliyor"), _q=T("s09", "yani", off=-0.3), _ok=T("s09", "borulama")),
    [("pop", T("s09", "ana"), 0.25), ("ping", T("s09", "borulama") + 0.3, 0.25)],
)
S[sid] = d

# ---------------------------------------------------------------- s10 Kriter 3: Değişken kapasite
sid, d = crit(
    3, "Değişken kapasite kontrolü", "Kompresör yalnızca aç / kapa mantığıyla değil, ihtiyaca göre çalışmalı",
    "Kapasite ihtiyaca göre artırılıp azaltılabiliyor mu?",
    r"""
#s10 .ch { position:absolute; top:0; height:430px; padding:22px 26px; }
#s10 .ca { left:0; width:500px; }
#s10 .cb { left:530px; width:550px; border-color:var(--vrf) !important; }
#s10 .ch .hd { display:flex; align-items:center; justify-content:space-between; }
#s10 .ch .tt { font-family:'Archivo Black'; font-size:36px; color:var(--fg); }
#s10 .ca .no { display:flex; align-items:center; gap:8px; font:900 22px Montserrat; color:#2a0a0e; background:var(--uyari); padding:8px 14px; border-radius:10px; }
#s10 .ch svg { position:absolute; left:26px; top:96px; }
#s10 .lg { position:absolute; left:26px; bottom:18px; display:flex; gap:18px; font:700 22px Montserrat; }
#s10 .lg span { display:flex; align-items:center; gap:8px; }
#s10 .lg i { display:block; width:28px; height:6px; border-radius:3px; }
#s10 .ud { position:absolute; right:26px; top:22px; display:flex; gap:10px; }
#s10 .ud span { font:900 22px Montserrat; padding:8px 14px; border-radius:10px; color:#062a22; background:var(--vrf); }
""",
    r"""
<div class="ch card ca"><div class="hd"><div class="tt">AÇ / KAPA</div><div class="no">XI YETERSİZ</div></div>
  <svg width="450" height="250" viewBox="0 0 450 250">
    <path d="M30 10 V 220 H 440" fill="none" stroke="#5B6FA8" stroke-width="3"/>
    <text x="0" y="30" class="svgl">%100</text><text x="10" y="224" class="svgl">%0</text>
    <path class="sq" d="M30 210 H 80 V 30 H 170 V 210 H 230 V 30 H 320 V 210 H 370 V 30 H 440" fill="none" stroke="#FF4D5E" stroke-width="6" stroke-linejoin="round"/>
  </svg>
  <div class="lg"><span><i style="background:#FF4D5E"></i>Sadece %0 ↔ %100</span></div>
</div>
<div class="ch card cb"><div class="hd"><div class="tt">DEĞİŞKEN</div></div>
  <div class="ud"><span class="up">▲ ARTIR</span><span class="dn">▼ AZALT</span></div>
  <svg width="500" height="250" viewBox="0 0 500 250">
    <path d="M30 10 V 220 H 490" fill="none" stroke="#5B6FA8" stroke-width="3"/>
    <text x="0" y="30" class="svgl">%100</text><text x="10" y="224" class="svgl">%0</text>
    <path class="stp" d="M30 160 H 130 V 100 H 230 V 40 H 320 V 100 H 400 V 160 H 490" fill="none" stroke="#FFC53D" stroke-width="5" stroke-dasharray="12 8"/>
    <path class="inv" d="" fill="none" stroke="#33D9B2" stroke-width="7" stroke-linecap="round"/>
    <circle class="dot" cx="30" cy="150" r="13" fill="#FFFFFF" stroke="#33D9B2" stroke-width="5"/>
  </svg>
  <div class="lg"><span><i style="background:#33D9B2"></i>İnverter</span><span><i style="background:#FFC53D"></i>En az 3 kademe</span></div>
</div>
""".replace("XI", icon("x", 24)),
    r"""
const f = (x) => 125 - 70 * Math.sin((x - 30) / 460 * Math.PI * 1.6) - 18 * Math.sin((x - 30) / 460 * Math.PI * 5.2);
let dd = "M30 " + f(30).toFixed(1);
for (let x = 34; x <= 490; x += 4) dd += " L" + x + " " + f(x).toFixed(1);
q(".inv")[0].setAttribute("d", dd);
tl.fromTo(q(".ca"), { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.komp);
draw(".ca .sq", K.ac, 1.0, "none");
pop(".ca .no", K.yoksa - 0.3);
tl.fromTo(q(".cb"), { x: 60, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, K.yoksa);
tl.to(q(".ca"), { opacity: 0.6, scale: 0.97, duration: 0.4 }, K.inverter);
draw(".cb .inv", K.inverter, 1.2, "power1.inOut");
draw(".cb .stp", K.kademeli - 0.3, 0.9, "none");
const dotSt = { x: 30 };
const dot = q(".dot")[0];
tl.fromTo(dotSt, { x: 30 }, { x: 490, duration: D - 0.6 - K.kapasiteyi, ease: "none",
  onUpdate: () => { dot.setAttribute("cx", dotSt.x.toFixed(1)); dot.setAttribute("cy", f(dotSt.x).toFixed(1)); } }, K.kapasiteyi);
tl.fromTo(q(".dot"), { opacity: 0 }, { opacity: 1, duration: 0.2 }, K.kapasiteyi);
pop(".ud .up", K.artirip);
pop(".ud .dn", K.azalt);
""",
    dict(komp=T("s10", "kompresör"), ac=T("s10", "aç"), yoksa=T("s10", "yoksa"), inverter=T("s10", "inverter"),
         kademeli=T("s10", "kademeli"), kapasiteyi=T("s10", "kapasiteyi"), artirip=T("s10", "artırıp"),
         azalt=T("s10", "azaltabiliyor"), _q=T("s10", "kapasiteyi", off=-0.4), _ok=T("s10", "azaltabiliyor", off=0.6)),
    [("error", T("s10", "yoksa") - 0.3, 0.15), ("ping", T("s10", "azaltabiliyor", off=0.6), 0.25)],
)
S[sid] = d
