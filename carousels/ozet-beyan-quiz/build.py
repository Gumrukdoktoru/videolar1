"""Özet beyan & gümrük gözetimi quiz carousel — "Gümrük Radarı" theme. Writes carousel.html."""
import pathlib, sys
from theme import radar_bg, stamp, ic, W, H

D = pathlib.Path(__file__).resolve().parent
TOTAL = 15

CSS = r"""
:root { --cyan:#2FE6D2; --cyan2:#9FF8EE; --amber:#FFB020; --green:#2EE07A; --red:#FF4D6D; --ink:#0B1A33; --ink2:#3A4A66; --muted:#6B7A93;
  --paper:#F4F9FB; --glass:rgba(8,24,46,.80); --line:rgba(47,230,210,.38); --txt:#E6F4FA; }
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#1d1d1d; font-family:Montserrat, sans-serif; color:var(--txt); }
.slide { position:relative; width:1080px; height:1350px; overflow:hidden; margin:0 auto 40px; background:#081528; }
.bgsvg { position:absolute; inset:0; }
.ic { display:block; flex:none; }

/* HUD chrome */
.hud { position:absolute; left:56px; right:56px; top:42px; height:58px; display:flex; align-items:center; justify-content:space-between;
  font:700 18px 'JetBrains Mono'; letter-spacing:.16em; color:var(--cyan); }
.hud .l { display:flex; align-items:center; gap:12px; }
.hud .dot { width:13px; height:13px; border-radius:50%; background:var(--red); box-shadow:0 0 0 4px rgba(255,77,109,.25), 0 0 14px var(--red); }
.hud .l em { font-style:normal; color:rgba(230,244,250,.55); }
.hud .r { border:1.5px solid var(--line); padding:9px 14px; border-radius:8px; background:rgba(4,10,22,.55); }
.hud .r b { color:#fff; }
.c { position:absolute; left:56px; right:56px; top:126px; height:1090px; }
.foot { position:absolute; left:56px; right:56px; bottom:30px; height:64px; display:flex; align-items:center; justify-content:space-between; }
.foot .logo { background:#fff; border-radius:12px; padding:9px 14px; box-shadow:0 0 0 3px rgba(47,230,210,.25); }
.foot .logo img { height:34px; display:block; }
.prog { display:flex; gap:12px; align-items:center; font:700 15px 'JetBrains Mono'; color:var(--cyan); letter-spacing:.14em; }
.prog i { width:18px; height:18px; border-radius:50%; border:2px solid var(--cyan); opacity:.55; }
.prog i.done { background:var(--cyan); opacity:.45; }
.prog i.on { background:var(--cyan); opacity:1; box-shadow:0 0 0 5px rgba(47,230,210,.22), 0 0 18px var(--cyan); }
.swipe { font:800 20px Montserrat; letter-spacing:.14em; color:var(--cyan); display:flex; align-items:center; gap:8px; }

/* HUD corner brackets */
.brk { position:relative; border:1.5px solid rgba(47,230,210,.28); background:
  linear-gradient(var(--cyan),var(--cyan)) left top/28px 3px no-repeat, linear-gradient(var(--cyan),var(--cyan)) left top/3px 28px no-repeat,
  linear-gradient(var(--cyan),var(--cyan)) right top/28px 3px no-repeat, linear-gradient(var(--cyan),var(--cyan)) right top/3px 28px no-repeat,
  linear-gradient(var(--cyan),var(--cyan)) left bottom/28px 3px no-repeat, linear-gradient(var(--cyan),var(--cyan)) left bottom/3px 28px no-repeat,
  linear-gradient(var(--cyan),var(--cyan)) right bottom/28px 3px no-repeat, linear-gradient(var(--cyan),var(--cyan)) right bottom/3px 28px no-repeat,
  var(--glass); }
.paper { background:var(--paper); color:var(--ink); border-radius:22px; box-shadow:0 22px 50px rgba(0,0,0,.45); position:relative; }
.mono { font-family:'JetBrains Mono'; font-weight:700; letter-spacing:.14em; }
.chip { display:inline-flex; align-items:center; gap:8px; font:700 17px 'JetBrains Mono'; letter-spacing:.14em; color:#04101F; background:var(--cyan); padding:7px 12px; border-radius:5px; }
.ref { display:inline-flex; align-items:center; gap:8px; font:700 18px 'JetBrains Mono'; letter-spacing:.08em; color:var(--cyan); border:1.5px solid var(--line);
  padding:7px 14px; border-radius:999px; background:rgba(4,10,22,.6); white-space:nowrap; }

/* optic-form bubbles */
.bub { flex:none; width:56px; height:56px; border-radius:50%; border:3px solid #BFE3EE; display:flex; align-items:center; justify-content:center;
  font:900 25px Unbounded; color:#fff; }
.bub.ok { background:var(--green); border-color:var(--green); color:#03200F; box-shadow:0 0 0 6px rgba(46,224,122,.22), 0 0 26px rgba(46,224,122,.55); }
.bub.trap { border-color:var(--amber); color:var(--amber); border-style:dashed; }
.bub.bad { border-color:var(--red); color:var(--red); }
.bub.ink { border-color:var(--ink); color:var(--ink); }

/* ---------- question slides ---------- */
.qhead { display:flex; align-items:flex-end; gap:28px; }
.qnum { line-height:.82; flex:none; }
.qnum small { display:block; font:700 18px 'JetBrains Mono'; letter-spacing:.34em; color:var(--cyan); margin:0 0 -10px 6px; }
.qnum b { font:900 150px Unbounded; color:transparent; -webkit-text-stroke:3px var(--cyan); text-shadow:0 0 34px rgba(47,230,210,.35); letter-spacing:-.02em; }
.qnum span { font:700 30px Unbounded; color:rgba(230,244,250,.5); margin-left:4px; }
.qtopic { padding-bottom:10px; }
.qtopic p { font:800 42px/1.12 Unbounded; color:#fff; margin-top:14px; letter-spacing:-.01em; }
.qtopic p em { font-style:normal; color:var(--amber); text-shadow:0 0 22px rgba(255,176,32,.35); }
.qcard { margin-top:24px; padding:24px 30px 24px 38px; font:600 29px/1.38 Montserrat; }
.qcard:before { content:""; position:absolute; left:0; top:22px; bottom:22px; width:9px; border-radius:0 6px 6px 0; background:var(--cyan); }
.qcard b { font-weight:800; text-decoration:underline; text-decoration-color:var(--amber); text-decoration-thickness:4px; text-underline-offset:5px; }
.qcard .law { display:block; font:700 15px 'JetBrains Mono'; letter-spacing:.16em; color:var(--muted); margin-bottom:8px; }
.qcard blockquote { margin-top:14px; padding:16px 20px; border-radius:14px; background:#E3F1F5; border:1.5px dashed #8DB8C4; font:600 28px/1.5 Montserrat; color:var(--ink); }
.blank { display:inline-block; min-width:150px; border-bottom:4px dashed var(--ink2); text-align:center; color:var(--ink2); font:900 24px Unbounded; line-height:1.1; margin:0 4px; }
.qcard ol { list-style:none; margin-top:12px; display:grid; gap:8px; }
.qcard ol li { display:flex; gap:14px; align-items:flex-start; font:600 26px/1.32 Montserrat; }
.qcard ol li i { flex:none; font:900 20px Unbounded; font-style:normal; color:#fff; background:var(--ink); border-radius:8px; min-width:52px; height:36px; display:flex; align-items:center; justify-content:center; margin-top:1px; }
.opts { margin-top:22px; display:flex; flex-direction:column; gap:12px; }
.opt { display:flex; gap:18px; align-items:center; padding:13px 22px 13px 14px; border-radius:16px; background:rgba(8,24,46,.84); border:1.5px solid rgba(47,230,210,.30); }
.opt p { font:600 26px/1.3 Montserrat; color:var(--txt); }
.q.long .opt p { font-size:22.5px; line-height:1.3; }
.q.long .opt { padding-top:11px; padding-bottom:11px; }
.q.long .qcard { font-size:27px; }
.opts.tbl { gap:7px; margin-top:16px; }
.q2 .qcard { font-size:27px; padding-top:20px; padding-bottom:20px; }
.q2 .qcard blockquote { font-size:26px; line-height:1.42; padding:12px 18px; margin-top:10px; }
.tblh { display:grid; grid-template-columns:62px 1fr 1fr; gap:14px; font:700 15px 'JetBrains Mono'; letter-spacing:.16em; color:var(--cyan); padding:0 22px 0 14px; }
.opts.tbl .opt { padding:6px 22px 6px 14px; }
.opts.tbl .opt p { flex:1; display:grid; grid-template-columns:1fr 1fr; gap:14px; }
.opts.tbl .opt p span + span { padding-left:14px; border-left:2px dashed rgba(47,230,210,.35); }
.opts.tbl .bub { width:46px; height:46px; font-size:20px; }
.q .qcard blockquote .blank { min-width:120px; }
.opts.six { flex-direction:row; gap:12px; }
.opts.six .opt { flex:1; flex-direction:column; gap:12px; padding:16px 8px 18px; text-align:center; }
.opts.six .opt p { font-size:25px; line-height:1.2; }
.cta { position:absolute; left:0; right:0; bottom:8px; display:flex; justify-content:center; }
.cta div { display:flex; align-items:center; gap:14px; font:700 23px Montserrat; color:#fff; padding:12px 24px; border-radius:999px; background:rgba(4,10,22,.72);
  border:1.5px solid var(--line); }
.cta div .ic { color:var(--amber); }
.cta div b { color:var(--cyan); }

/* ---------- cover ---------- */
.cov .kick { position:absolute; left:0; top:22px; }
.cov .ttl { position:absolute; left:-4px; top:80px; font:900 104px/0.98 Unbounded; color:#fff; letter-spacing:-.02em; }
.cov .ttl span { display:block; }
.cov .ttl .amp { color:var(--amber); }
.cov .ttl .cy { color:var(--cyan); text-shadow:0 0 36px rgba(47,230,210,.45); }
.cov .lead { position:absolute; left:0; top:420px; width:540px; font:600 29px/1.38 Montserrat; color:var(--txt); }
.cov .lead b { color:var(--amber); }
.cov .list { position:absolute; left:0; top:560px; width:520px; padding:22px 24px; }
.cov .list div { display:flex; align-items:center; gap:14px; font:700 25px/1.25 Montserrat; color:#fff; padding:9px 0; border-bottom:1px dashed rgba(47,230,210,.25); }
.cov .list div:last-child { border-bottom:0; }
.cov .list .n { flex:none; width:40px; height:40px; border-radius:50%; background:rgba(47,230,210,.15); border:2px solid var(--cyan); display:flex; align-items:center; justify-content:center; font:800 17px Unbounded; color:var(--cyan); }
.cov .tags { position:absolute; left:0; right:0; top:992px; display:flex; flex-wrap:wrap; gap:10px; }
.cov .tags span { font:700 18px 'JetBrains Mono'; color:#04101F; background:var(--cyan2); padding:7px 12px; border-radius:6px; }
.cov .av { position:absolute; left:470px; top:380px; width:640px; height:640px; filter:drop-shadow(0 0 2px rgba(159,248,238,.9)) drop-shadow(0 0 26px rgba(47,230,210,.45)); }
.cov .spot { position:absolute; left:530px; top:430px; width:520px; height:560px; border-radius:50%; background:radial-gradient(closest-side, rgba(47,230,210,.28), rgba(47,230,210,0)); }
.cov .st { position:absolute; left:752px; top:200px; }
.cov .bubble { position:absolute; left:624px; top:262px; width:344px; padding:16px 20px; border-radius:20px 20px 20px 4px; background:#fff; color:var(--ink); font:800 24px/1.3 Montserrat; box-shadow:0 14px 34px rgba(0,0,0,.4); }
.cov .bubble em { font-style:normal; color:#C26A00; }
"""

HUD_L = '<span class="dot"></span>GÜMRÜK RADARI <em>·</em> ÖZET BEYAN &amp; GÖZETİM'


def prog(active):
    dots = "".join(f'<i class="{"on" if k == active else "done" if k < active else ""}"></i>' for k in range(1, 7))
    return f'<div class="prog">{dots}</div>'


def page(n, body, cls="", hud_r="", active=0, bg=None, swipe=True):
    bg = bg or {}
    return f'''<section class="slide {cls}" id="p{n}">
  {radar_bg(f"s{n}", **bg)}
  <div class="hud"><div class="l">{HUD_L}</div><div class="r">{hud_r}</div></div>
  <div class="c">{body}</div>
  <div class="foot"><div class="logo"><img src="img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu"/></div>{prog(active)}
    <div class="swipe">{"KAYDIR" if swipe else "KAYDET"} {ic("arrow" if swipe else "bookmark", 26)}</div></div>
</section>'''


S = {}

# ---------------------------------------------------------------- cover
cov_blips = [(170, 960, 6, "#2FE6D2", "S1"), (330, 800, 6, "#2FE6D2", "S2"), (255, 1050, 6, "#FFB020", "S3"),
             (430, 900, 6, "#2FE6D2", "S4"), (120, 760, 6, "#FF4D6D", "S5"), (390, 1060, 6, "#2FE6D2", "S6")]
S[1] = page(1, f'''
  <span class="chip kick">{ic("radar", 22)} SINAV RADARI · 6 SORU · 6 ÇÖZÜM</span>
  <div class="ttl"><span>ÖZET</span><span>BEYAN <span class="amp" style="display:inline">&amp;</span></span><span class="cy">GÖZETİM</span></div>
  <div class="spot"></div>
  <img class="av" src="img/koc-cutout.png" alt="Gümrük Koçu"/>
  <div class="bubble">Önce <em>kendin çöz</em>, sonra kaydır. Tuzakları birlikte yakalayalım!</div>
  <div class="lead">4458 sayılı Gümrük Kanunu ve Gümrük Yönetmeliği'nden <b>6 soru</b>: çözüm, şema ve <b>tuzak analizi</b>.</div>
  <div class="brk list">
    <div><span class="n">1</span>Kimden özet beyan istenmez?</div>
    <div><span class="n">2</span>Gözetim ne zaman başlar?</div>
    <div><span class="n">3</span>Gözetim nasıl sona erer?</div>
    <div><span class="n">4</span>Nereye, ne zaman verilir?</div>
    <div><span class="n">5</span>Hazırlama &amp; vazgeçme</div>
    <div><span class="n">6</span>Değişiklik ne zaman kapanır?</div>
  </div>
  <div class="tags"><span>GK 35/A</span><span>35/B</span><span>35/C</span><span>36</span><span>47</span><span>152</span><span>165/D</span><span>GY 67</span><span>GY 74</span></div>
''', cls="cov", hud_r="HEDEF <b>06</b> · TARAMA", bg=dict(cx=300, cy=900, R=330, sweep=-30, blips=cov_blips))

# ---------------------------------------------------------------- questions
Q = {
    1: dict(chip="ÖZET BEYAN · KAPSAM", hook="Hangisi için özet beyan <em>gerekmez</em>?",
            stem="4458 sayılı Gümrük Kanunu'nun Türkiye Gümrük Bölgesine getirilen eşya için özet beyan verilmesine ilişkin hükümlerine göre aşağıdaki eşyadan hangisi için özet beyan verilmesi <b>gerekmez</b>?",
            opts=["Denizyoluyla Türkiye Gümrük Bölgesi dışından doğrudan bir serbest bölgeye getirilen eşya",
                  "Dökme hâlde denizyoluyla Türkiye'deki bir limana getirilen eşya",
                  "Demiryoluyla Türkiye Gümrük Bölgesine getirilen eşya",
                  "Uzun mesafeli bir uçuşla Türkiye'deki bir havalimanına getirilen eşya",
                  "Türkiye Gümrük Bölgesinin kara sularından durmaksızın geçen bir gemide taşınan eşya"]),
    2: dict(chip="GÜMRÜK GÖZETİMİ · BAŞLANGIÇ", hook="Boşlukları <em>doldur</em>",
            stem="4458 sayılı Gümrük Kanunu'nun Türkiye Gümrük Bölgesine getirilen eşyanın denetimine ilişkin hükmünde yer alan aşağıdaki cümlede boş bırakılan yerlere sırasıyla hangisi gelmelidir?"
                 "<blockquote>“Türkiye Gümrük Bölgesine getirilen eşya, <span class='blank'>①</span> itibaren <span class='blank'>②</span> tabidir. Bunlar, yürürlükteki hükümlere uygun olarak gümrük idareleri tarafından denetlenir.”</blockquote>",
            opts=["girişinden – gümrük gözetimine", "girişinden – gümrük kontrolüne", "gümrüğe sunulmasından – gümrük gözetimine",
                  "özet beyanın tescilinden – gümrük kontrolüne", "taşıttan boşaltılmasından – gümrük gözetimine"]),
    3: dict(chip="GÖZETİMİN SONA ERMESİ", hook="Hangisi listede <em>yok</em>?",
            stem="4458 sayılı Gümrük Kanunu'na göre Türkiye Gümrük Bölgesine getirilen serbest dolaşımda olmayan eşyanın gümrüğün gözetimi altında kalma süresinin sona erdiği hâller arasında aşağıdakilerden hangisi <b>yer almaz</b>?",
            opts=["Eşyanın gümrük statüsünün değişmesi", "Eşyanın geçici depolama yerine konulması", "Eşyanın serbest bölgeye girmesi",
                  "Eşyanın yeniden ihraç edilmesi", "Eşyanın imha edilmesi"]),
    4: dict(chip="ÖZET BEYAN · YER &amp; ZAMAN", hook="Hangisi <em>doğru</em>?", long=True,
            stem="4458 sayılı Gümrük Kanunu ve Gümrük Yönetmeliği'ne göre özet beyanın verileceği gümrük idaresi ve verilme zamanına ilişkin aşağıdaki ifadelerden hangisi <b>doğrudur</b>?",
            opts=["Özet beyan kural olarak eşyanın boşaltılacağı gümrük idaresine verilir; giriş gümrük idaresine verilmesine ancak istisnai durumlarda izin verilir.",
                  "Özet beyan, eşya Türkiye Gümrük Bölgesine getirildikten sonra ve gümrüğe sunulmadan önce verilir.",
                  "Karayolu taşımacılığında özet beyan bilgilerini de içeren transit beyanı, taşıtın giriş gümrük idaresine varmasından en az dört saat önce verilir.",
                  "Demiryolu taşımacılığında özet beyan, giriş gümrük idaresine varılmasından en az iki saat önce verilir.",
                  "Yükümlünün bilgisayar sistemindeki özet beyan bilgilerine erişilebilmesi hâlinde giriş gümrük idaresi, özet beyan yerine bir bildirimde bulunulmasını kabul edebilir."]),
    5: dict(chip="HAZIRLAMA &amp; VAZGEÇME", hook="Hangisi <em>yanlış</em>?", long=True,
            stem="4458 sayılı Gümrük Kanunu'nun özet beyanın hazırlanmasına ve özet beyan verilmesinden vazgeçilmesine ilişkin hükümlerine göre aşağıdaki ifadelerden hangisi <b>yanlıştır</b>?",
            opts=["Özet beyan verilmesinden vazgeçilmesi hâlinde gümrük beyannamesi, eşya gümrüğe sunuluncaya kadar özet beyan statüsüne sahiptir.",
                  "Özet beyan veri işleme tekniği kullanılarak hazırlanır; gerekli ayrıntıları içermesi hâlinde ticari bilgiler ile liman veya taşıma bilgileri kullanılabilir.",
                  "Müsteşarlık, istisnai durumlarda yazılı olarak düzenlenen özet beyanları, veri işleme tekniği kullanılarak hazırlanan özet beyanlar ile aynı düzeyde risk yönetimi uygulanmasına imkân verilmesi kaydıyla kabul edebilir.",
                  "Giriş gümrük idaresi, özet beyanın verilme süresi sona ermeden önce gümrük beyannamesi verilen eşya için özet beyan verilmesinden vazgeçebilir.",
                  "Özet beyan verilmesinden vazgeçilmesi hâlinde gümrük beyannamesi, özet beyanda bulunması gerekli asgari bilgileri içerir."]),
    6: dict(chip="ÖZET BEYANDA DEĞİŞİKLİK", hook="Değişiklik ne zaman <em>kapanır</em>?",
            stem="4458 sayılı Gümrük Kanunu'na göre Türkiye Gümrük Bölgesine getirilen eşya için verilen özet beyanda, talep üzerine bir veya daha fazla bilginin değiştirilmesine ilişkin olarak aşağıdaki durumlar verilmiştir:"
                 "<ol><li><i>I</i>Özet beyanı veren kişiye eşyanın muayene edileceğinin bildirilmesi</li>"
                 "<li><i>II</i>Özet beyanın gümrük idaresine verilmesi</li>"
                 "<li><i>III</i>Söz konusu bilgilerin yanlış olduğunun tespit edilmesi</li>"
                 "<li><i>IV</i>Eşyanın boşaltılmasına izin verilmesi</li></ol>"
                 "<div style='margin-top:12px'>Yukarıdaki durumlardan hangilerinin gerçekleşmesinden sonra özet beyanda değişiklik yapılmasına <b>izin verilmez</b>?</div>",
            opts=["I ve III", "II ve IV", "III ve IV", "I, III ve IV", "I, II, III ve IV"]),
}

QBG = {1: dict(cx=900, cy=260, R=520, sweep=-150), 2: dict(cx=160, cy=300, R=560, sweep=-20), 3: dict(cx=940, cy=1000, R=600, sweep=200),
       4: dict(cx=980, cy=200, R=480, sweep=150), 5: dict(cx=120, cy=1000, R=620, sweep=-60), 6: dict(cx=900, cy=700, R=640, sweep=-120)}

for k, q in Q.items():
    if k == 2:
        opts = '<div class="tblh"><span></span><span>① BOŞLUK</span><span>② BOŞLUK</span></div>' + "".join(
            f'<div class="opt"><span class="bub">{L}</span><p>{"".join(f"<span>{x}</span>" for x in o.split(" – "))}</p></div>' for L, o in zip("ABCDE", q["opts"]))
    else:
        opts = "".join(f'<div class="opt"><span class="bub">{L}</span><p>{o}</p></div>' for L, o in zip("ABCDE", q["opts"]))
    S[2 * k] = page(2 * k, f'''
  <div class="qhead"><div class="qnum"><small>SORU</small><b>0{k}</b><span>/06</span></div>
    <div class="qtopic"><span class="chip">{q["chip"]}</span><p>{q["hook"]}</p></div></div>
  <div class="paper qcard"><span class="law">4458 S. GÜMRÜK KANUNU{" · GÜMRÜK YÖNETMELİĞİ" if k == 4 else ""}</span>{q["stem"]}</div>
  <div class="opts{" six" if k == 6 else " tbl" if k == 2 else ""}">{opts}</div>
  <div class="cta"><div>{ic("comment", 30)}Cevabını yorumlara yaz · <b>çözüm sonraki sayfada</b></div></div>
''', cls=f"q q{k}" + (" long" if q.get("long") else ""), hud_r=f"SORU <b>0{k}</b>/06", active=k, bg=QBG[k])

import slides_a
S.update(slides_a.build(page, ic, stamp))
CSS += slides_a.CSS2

JS = r"""<script>
(() => {
  // Draw bezier connectors from each .hub to its .spoke siblings inside every .wire container.
  document.querySelectorAll(".wire").forEach((wr) => {
    const svg = wr.querySelector("svg.lines"); if (!svg) return;
    const base = svg.getBoundingClientRect();
    const box = (el) => { const b = el.getBoundingClientRect(); return { l: b.left - base.left, t: b.top - base.top, r: b.right - base.left, b: b.bottom - base.top, cx: (b.left + b.right) / 2 - base.left, cy: (b.top + b.bottom) / 2 - base.top }; };
    const hub = box(wr.querySelector(".hub")), col = wr.dataset.color || "#2FE6D2"; let d = "", dots = "";
    const round = wr.dataset.round === "1", rad = (hub.r - hub.l) / 2;
    wr.querySelectorAll(".spoke").forEach((s) => {
      const b = box(s); let sx, sy, ex, ey, c1x, c1y, c2x, c2y;
      if (b.l > hub.r - 4) { ex = b.l; ey = b.cy; }
      else if (b.r < hub.l + 4) { ex = b.r; ey = b.cy; }
      else { ex = b.cx; ey = b.t > hub.b ? b.t : b.b; }
      if (round) { const a = Math.atan2(ey - hub.cy, ex - hub.cx); sx = hub.cx + (rad + 6) * Math.cos(a); sy = hub.cy + (rad + 6) * Math.sin(a); }
      else { sx = ex > hub.r ? hub.r : ex < hub.l ? hub.l : hub.cx; sy = ex > hub.r || ex < hub.l ? Math.min(Math.max(ey, hub.t + 30), hub.b - 30) : (ey > hub.b ? hub.b : hub.t); }
      if (Math.abs(ex - sx) > Math.abs(ey - sy)) { const mx = (sx + ex) / 2; c1x = mx; c1y = sy; c2x = mx; c2y = ey; }
      else { const my = (sy + ey) / 2; c1x = sx; c1y = my; c2x = ex; c2y = my; }
      d += `M${sx} ${sy} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${ex} ${ey} `;
      dots += `<circle cx="${ex}" cy="${ey}" r="8" fill="${col}"/><circle cx="${sx}" cy="${sy}" r="6" fill="#081528" stroke="${col}" stroke-width="3"/>`;
    });
    svg.innerHTML = `<path d="${d}" fill="none" stroke="${col}" stroke-width="10" stroke-linecap="round" opacity=".18"/><path d="${d}" fill="none" stroke="${col}" stroke-width="3" stroke-dasharray="10 7"/>` + dots;
  });
})();
</script>"""

only = [int(x) for x in sys.argv[1:]] or sorted(S)
html = f'''<!doctype html><html lang="tr"><head><meta charset="UTF-8"/><title>Özet Beyan Quiz — Carousel</title>
<link rel="stylesheet" href="fonts/fonts.css"/><style>{CSS}</style></head><body>
{"".join(S[i] for i in only if i in S)}
{JS}
</body></html>'''
(D / "carousel.html").write_text(html)
print("slides:", [i for i in only if i in S])
