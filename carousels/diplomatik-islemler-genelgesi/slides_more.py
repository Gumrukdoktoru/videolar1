"""Slides 3-12, 14, 15 for the Diplomatik İşlemler carousel."""
from theme import stamp, seal, ic, pouch, emblem, cover_bg, mrz


def build(page, TOTAL):
    S = {}

    # ---------------------------------------------------------------- 3 Tanımlar
    defs = [
        ("id", "Diplomatik üye", "Misyon mensupları listesinde adı geçen; diplomatik ajan, konsolosluk memuru, uluslararası kuruluş memuru.", "1. SINIF KART"),
        ("id", "İdari ve teknik personel", "Yabancı misyonlarda görevli, ikinci sınıf kart hamili personel.", "2. SINIF KART"),
        ("doc", "Takrir", "Misyon, misyon şefi veya heyet başkanınca düzenlenen; Dışişleri onaylı muafiyet belgesi.", "DIŞİŞLERİ ONAYLI"),
        ("flag", "Yabancı misyon", "Türkiye'deki diplomatik ve konsüler misyonlar ile uluslararası kuruluşlar ve temsilcilikleri.", "BÜYÜKELÇİLİK · KONSOLOSLUK · UK"),
        ("bag", "Kurye mektubu", "Kuryeye teslim edilen resmî ve gizli evrak için her seferinde düzenlenen belge.", "BEYANNAME YERİNE GEÇER"),
        ("box", "Diplomatik paket", "Misyonların resmî ihtiyaçları için yurt dışından temin ettiği eşya gönderileri.", "RESMÎ İHTİYAÇ"),
    ]
    cards = "".join(
        f'<div class="card dc"><div class="strip"></div><div class="hd">{ic(i, 40)}<b>{t}</b></div><p>{d}</p><span class="chip">{c}</span></div>'
        for i, t, d, c in defs)
    S[3] = page(3, f'''<span class="kick">TANIMLAR</span><div class="t" style="font-size:58px">Genelgenin <em>sözlüğü</em></div>
      <div class="dgrid">{cards}</div>''', cls="df")

    # ---------------------------------------------------------------- 4 Karşılıklılık + altın kural
    S[4] = page(4, f'''<span class="kick">KARŞILIKLILIK İLKESİ</span><div class="t" style="font-size:56px">Ne kadar tanınırsa, <em>o kadar</em></div>
      <div class="scale card">
        <svg width="420" height="256" viewBox="-24 0 468 262" aria-hidden="true">
          <path d="M210 30 V 210 M140 222 H280 M60 70 H360" stroke="#10224F" stroke-width="7" stroke-linecap="round"/>
          <circle cx="210" cy="30" r="13" fill="#B8893B"/>
          <path d="M60 70 L20 150 H100 Z M360 70 L320 150 H400 Z" fill="none" stroke="#10224F" stroke-width="4" stroke-linejoin="round"/>
          <path d="M14 150 Q60 190 106 150 Z" fill="#7A1428"/><path d="M314 150 Q360 190 406 150 Z" fill="#0F7C7C"/>
          <text x="60" y="222" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="17" fill="#7A1428">Türk misyonuna</text>
          <text x="60" y="242" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="17" fill="#7A1428">o ülkede tanınan</text>
          <text x="360" y="222" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="17" fill="#0F7C7C">Genelgedeki</text>
          <text x="360" y="242" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="17" fill="#0F7C7C">ayrıcalık</text>
        </svg>
      </div>
      <div class="outs">
        <div class="o g"><b>≥</b><p><strong>Eşit veya fazla</strong> → Genelge hükümleri uygulanır</p></div>
        <div class="o r"><b>&lt;</b><p><strong>Daha kısıtlı</strong> → Aynı kısıtlama o ülkenin misyonuna da uygulanır</p></div>
        <div class="o b"><b>↑</b><p><strong>Genişletme</strong> → Karşılıklılık gereği haklar genişletilebilir</p></div>
      </div>
      <div class="who"><span class="pill">{ic("globe", 24)} Tespit ve teyit: Dışişleri Bakanlığı</span><span class="pill">{ic("doc", 24)} Uluslararası kuruluşlar: kuruluş anlaşmaları</span></div>
      <div class="gold card"><div class="gst">{stamp("onemli", "ALTIN KURAL", rot=-7, scale=0.7)}</div>
        <div class="gr"><span class="tag s">SATIŞ</span>{ic("arrow", 40)}<p>Yalnızca <b>muafiyetten yararlanmayan</b> kişiye</p></div>
        <div class="gr"><span class="tag d">DEVİR</span>{ic("arrow", 40)}<p>Yalnızca <b>muafiyetten yararlanan</b> kişiye</p></div>
        <small>Araçlar ile kişisel eşya ve ev eşyası için geçerli genel hüküm</small></div>''', cls="kr")

    # ---------------------------------------------------------------- 5 Araç ithalatı
    who = [("car", "Özel araç", "Diplomatik üye ile idari ve teknik personel · Takrir (Ek-1 / Form B)"),
           ("id", "Eş için 2. araç", "Kendi adına kayıtlı olmak şartıyla, karşılıklılık çerçevesinde"),
           ("flag", "Hizmet aracı", "Yabancı misyon · makul sayıda · kotayı Dışişleri belirler"),
           ("check", "Yurt içinden muaf alım", "Dışişleri uygun görürse, aynı şartlarla")]
    S[5] = page(5, f'''<span class="kick">A · ARAÇLAR</span><div class="t" style="font-size:56px">Araç ithalatı: <em>kim, nasıl?</em></div>
      <div class="wl">{"".join(f'<div class="card w">{ic(i, 40)}<div><b>{t}</b><p>{d}</p></div></div>' for i, t, d in who)}</div>
      <div class="card tlx"><div class="mini">GÜMRÜĞE TESLİM SÜRESİ</div>
        <div class="step"><span class="dot"></span><div><b>İrsaliye düzenlenir</b><p>Araç gümrük idaresine sevk edilir</p></div></div>
        <div class="dur">7 GÜN</div>
        <div class="step"><span class="dot fill"></span><div><b>Gümrüğe teslim</b><p>İrsaliye tarihinden itibaren</p></div></div>
        <div class="ext"><b>Uzatma:</b> irsaliye tarihini izleyen <b>15 gün</b> içinde Dışişleri'ne başvuru; uygun bulunursa doğrudan gümrüğe bildirilir.</div>
        <div class="ext2"><b>Takrire:</b> sahiplik belgesi / fatura / ruhsat (asıl yoksa nüsha) + aksesuarlar, giriş tarihi ve yeri.</div></div>
      <div class="card warn">{stamp("dikkat", "3 YAŞ ŞERHİ", rot=-8, scale=0.62)}
        <p>Alındığı tarihte <b>3 yaşından büyük</b> araç: takrire <b>“Vergi muafiyeti olmayan kişilere satılamaz.”</b> şerhi düşülür; Taşıt Takip Programına “Takrir” seçeneğiyle kaydedilir. Motor / şasi no düzeltmesi: <b>nota → Dışişleri uygunluğu → gümrük</b>.</p></div>''', cls="ai")

    # ---------------------------------------------------------------- 6 Satış süreleri
    def trackrow(label, sub, start, note, color):
        x = 40 + start * 160
        return (f'<div class="tr"><div class="lab"><b>{label}</b><span>{sub}</span></div>'
                f'<svg width="880" height="70" viewBox="0 0 880 70" aria-hidden="true">'
                f'<defs><pattern id="h{start}" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="12" fill="#C9C1AE"/></pattern></defs>'
                f'<rect x="40" y="22" width="{x - 40}" height="26" rx="6" fill="url(#h{start})"/>'
                f'<rect x="{x}" y="22" width="{840 - x}" height="26" rx="6" fill="{color}"/>'
                f'<circle cx="{x}" cy="35" r="17" fill="#fff" stroke="{color}" stroke-width="6"/>'
                f'<text x="{min(x + 30, 700)}" y="41" font-family="Montserrat" font-weight="800" font-size="19" fill="#fff">{note}</text></svg></div>')
    axis = "".join(f'<span style="left:{40 + i * 160}px">{i} yıl</span>' for i in range(6))
    S[6] = page(6, f'''<span class="kick">A · ARAÇ SATIŞI</span><div class="t" style="font-size:56px">Ne zaman <em>satılabilir?</em></div>
      <div class="card tl6"><div class="mini">İTHAL TARİHİNDEN İTİBAREN · MUAFİYETTEN YARARLANMAYANA SATIŞ</div>
        {trackrow("Özel araç · kesin ayrılış", "zorunlu hâlde daha da kısa", 1, "1 yıl sonra", "#0F7C7C")}
        {trackrow("Özel araç", "Dışişleri ön izniyle", 2, "2 yıl sonra satış izni", "#10224F")}
        {trackrow("Hizmet aracı", "alındığında 3 yaşından küçükse", 5, "", "#7A1428")}
        <div class="ax">{axis}</div>
        <div class="leg"><span><i class="hz"></i>Satış izni yok</span><span><i style="background:#10224F"></i>Satış izni mümkün</span><span class="h5">Hizmet aracı: 5. yıl sonunda (kısaltılabilir)</span></div></div>
      <div class="rules">
        <div class="card ru tz">{stamp("tuzak", "3 YAŞ", rot=-6, scale=0.55)}<p>Alındığında <b>3 yaşından büyük</b> özel araç muafiyetsize <b>satılamaz</b> → ihraç, devir veya terk. (3 yaşından küçük olduğu belgelenirse satılabilir.)</p></div>
        <div class="card ru">{ic("car", 36)}<p>Görev süresince muafiyetsize <b>en fazla 1 araç</b> satılabilir; misyon şefi kesin ayrılışta <b>2. aracını</b> da satabilir.</p></div>
        <div class="card ru">{ic("x", 36)}<p><b>Otobüs, minibüs, kamyon, kamyonet, treyler</b> muafiyetsize satılamaz; yalnızca devredilir.</p></div>
        <div class="card ru">{ic("doc", 36)}<p>Süre kısaltılırsa: satış izninden sonra <b>2 ay içinde</b> tüm işlemler tamamlanır.</p></div>
      </div>''', cls="sl")

    # ---------------------------------------------------------------- 7 Satış işlemi
    steps = [("Nota ile izin talebi", "İthal takririnin işlem görmüş sureti, son sigorta poliçesi, ruhsat nüshası"),
             ("Dışişleri satış izni", "2 ay geçerli · süre dolmadan nota ile 1 kez +2 ay"),
             ("Araç gümrüğe teslim", "İl Emniyet'e yazı: plaka ve ruhsat iadesi, ilişik kesme"),
             ("Belgeler Dışişleri'ne", "İlişik Kesme Belgesi + Teslim Tesellüm Belgesi"),
             ("Kesin satış belgesi", "Dışişleri düzenler: alıcının adı ve adresi"),
             ("Vergiler ödenir", "Tüm vergiler ve mali yükümlülükler tahsil edilir"),
             ("Alıcıya teslim", "Gümrük; ithal gümrüğüne ve Dışişleri'ne bildirir")]
    flow = "".join(
        f'<div class="fs {"l" if k % 2 == 0 else "r"}"><div class="n">{k + 1}</div><div class="card fb"><b>{t}</b><p>{d}</p></div></div>'
        for k, (t, d) in enumerate(steps))
    S[7] = page(7, f'''<span class="kick">A · SATIŞ İŞLEMİ</span><div class="t" style="font-size:56px">Satış <em>7 adımda</em></div>
      <div class="fl"><svg class="spine" width="80" height="840" viewBox="0 0 80 840" aria-hidden="true"><path d="M40 10 V 830" stroke="#B8893B" stroke-width="6" stroke-dasharray="2 12" stroke-linecap="round"/><path d="M40 10 V 830" stroke="#7A1428" stroke-width="2.5"/></svg>{flow}</div>
      <div class="sst">{stamp("ok", "TESLİM", rot=10, scale=0.6)}</div>''', cls="sp")

    # ---------------------------------------------------------------- 8 Elden çıkarma yolları
    ways = [("plane", "İHRAÇ", "Önce Dışişleri'ne nota (özellikler, sahip, plaka, ihraç tarihi) → <b>Taşıt İhraç İzin Belgesi</b> elden teslim → gümrükte kesin ihraç."),
            ("id", "DEVİR", "Yalnız muafiyetten yararlananlara · <b>süre kısıtı yok</b> → <b>Taşıt Devir İzni Belgesi</b>. Yeni sahibin kayıt tarihi = yeni ithal tarihi."),
            ("flag", "GÜMRÜĞE TERK", "Hazineye <b>masrafsız</b>. Nota (terk edilecek gümrük) → plaka ve ruhsat iadesi, <b>İlişik Kesme Belgesi</b> → araç teslim."),
            ("x", "ÇALINMA · KAZA · HURDA", "Mahkeme, savcı, mülki amir veya emniyet yazısı · <b>Dışişleri ön izni</b> → terk ya da hurda vergilendirmesiyle ithal. Yeni araç Dışişleri takdirinde.")]
    S[8] = page(8, f'''<span class="kick">A · ELDEN ÇIKARMA</span><div class="t" style="font-size:56px">Aracın <em>4 çıkış kapısı</em></div>
      <div class="ways">{"".join(f'<div class="card wy"><div class="hd">{ic(i, 40)}<b>{t}</b></div><p>{d}</p></div>' for i, t, d in ways)}</div>
      <div class="card cross">{stamp("uyari", "ÇAPRAZ DEVİR YOK", rot=-6, scale=0.55)}
        <div class="cx"><span class="dc1">Geçici Giriş Belgesi · Karne · Form · NATO Beyannamesi</span><b>⇄</b><span class="dc2">Takrir (Form B)</span></div>
        <p>Bu belgelerle girmiş araç takrirle devralınamaz; takrirle girmiş araç da karne, form veya geçici giriş belgesiyle devralınamaz.</p></div>''', cls="ec")

    # ---------------------------------------------------------------- 9 Diğer araçlar
    S[9] = page(9, f'''<span class="kick">A · DİĞER ARAÇLAR</span><div class="t" style="font-size:56px">Yat, motosiklet, <em>karavan</em></div>
      <div class="nums"><div class="card nb"><span class="big">1</span><b>BEKÂR ÜYE</b><p>araç</p></div><div class="card nb"><span class="big">2</span><b>EVLİ ÜYE</b><p>araç</p></div>
        <div class="card nb plus"><span class="big">+</span><b>YAT · MOTOSİKLET</b><p>karşılıklılık esas; adedi Dışişleri belirler</p></div></div>
      <div class="vx">
        <div class="card vv">{ic("ship", 64)}<b>Yat ve deniz motoru</b><p>Özel araç kuralları uygulanır. Sahibi ayrıldıktan sonra Türk limanlarında <strong>en fazla 5 yıl</strong> bekletilebilir.</p></div>
        <div class="card vv">{ic("moto", 64)}<b>Motosiklet</b><p>Özel araç kuralları uygulanır; adet karşılıklılığa göre Dışişleri'nce belirlenir.</p></div>
        <div class="card vv">{ic("caravan", 64)}<b>Motorsuz karavan</b><p>Araç hükümleri <strong>uygulanmaz</strong>; satış, devir veya ihraç için Dışişleri onayı yeterli.</p></div>
      </div>''', cls="da")

    # ---------------------------------------------------------------- 10 Kişisel ve ev eşyası
    S[10] = page(10, f'''<span class="kick">A · KİŞİSEL &amp; EV EŞYASI</span><div class="t" style="font-size:56px">Ev eşyası ve <em>yıllık kotalar</em></div>
      <div class="card fa"><div>{ic("doc", 48)}</div><div><b>Takrir (Ek-2 / Form A) + eşya listesi</b><p>Elektrikli ve elektronik eşya listede ayrıntılı yazılır. Çamaşır makinesi, buzdolabı, TV vb. her türden <strong>makul ölçüde</strong>.</p></div></div>
      <div class="quota">
        <div class="card q">{ic("glass", 56)}<span class="big">240 L</span><b>içki</b><p>%22 ve üzeri alkollü</p></div>
        <div class="card q">{ic("cig", 56)}<span class="big">200</span><b>karton sigara</b><p>en fazla</p></div>
        <div class="card qn"><div class="mini">KOTA KİMİN İÇİN?</div><p>Diplomatik üye ile idari ve teknik personel · <b>takvim yılı başına</b></p><p>Şarap, bira, tütün: <b>makul düzey</b></p><p>Yabancı misyon kotadan <b>muaf tutulabilir</b> · Kontrol: Dışişleri</p></div>
      </div>
      <div class="card tk"><div class="mini">TAKRİR KURALLARI</div>
        <div class="tkr"><span class="cnt">4</span><p>nüsha · tüketim eşyası</p><span class="cnt">5</span><p>nüsha · dayanıklı eşya (model, tip, boyut, ağırlık, fiyat)</p></div>
        <p class="tkn">Takrir eşya gümrüğe <b>vardıktan sonra</b> hazırlanır; konşimento veya gümrük belgesi eklenir. Misyon şefi ve resmî kullanım takrirlerini misyon şefi ya da tayin ettiği kişi imzalar.</p></div>''', cls="ke")

    # ---------------------------------------------------------------- 11 3 yıl kuralı
    S[11] = page(11, f'''<span class="kick">A · SERBEST DOLAŞIM</span><div class="t" style="font-size:56px">3 yıl kuralı: <em>karar ağacı</em></div>
      <div class="q0 card">{ic("globe", 40)}<p>Ülke, <b>“3 yıl sonra serbest dolaşım”</b> karşılıklılık listesinde mi?<small>Güncel listeleri Dışişleri iletir</small></p></div>
      <svg class="br" width="952" height="80" viewBox="0 0 952 80" aria-hidden="true"><path d="M476 0 V 26 H 230 V 80 M476 26 H 722 V 80" fill="none" stroke="#10224F" stroke-width="4"/></svg>
      <div class="cols">
        <div class="col y"><div class="yn">EVET</div>
          <div class="card ci"><b>3 yıl sonra serbest dolaşım</b><p>Kişisel ve ev eşyası, ithal tarihinden 3 yıl sonra serbest dolaşımda sayılır.</p></div>
          <div class="card ci"><b>Yabancıdan alınan eşya</b><p>Görevdeyken başka yabancıdan alınan eşyada süre satın alma tarihinden başlar.</p></div>
          <div class="card ci"><b>Görev bitiminde</b><p>Elden çıkarılmayan eşya ihraç edilir; satılan/devredilen eşya listesi eklenir.</p></div></div>
        <div class="col n"><div class="yn">HAYIR</div>
          <div class="card ci"><b>İlke: ihraç</b><p>Dayanıklı eşya ilke olarak ihraç edilir (nota + onaylı takrir örneği).</p></div>
          <div class="card ci"><b>Muafiyetsize satış</b><p>Yalnızca kesin terk hâlinde veya Dışişleri ön izniyle 5 yıl sonunda.</p></div>
          <div class="card ci"><b>Satış gümrükte</b><p>Vergiler eşya alıcıya teslim edilmeden önce ödenir.</p></div></div>
      </div>
      <div class="card tz2">{stamp("tuzak", "ÖZELLİKLİ EŞYA", rot=-6, scale=0.55)}<p>Kişisel ve ev eşyası dışındaki <b>özellikli eşya</b> süreyle serbest dolaşıma <b>girmez</b> → yurt dışı, devir ya da terk.</p></div>''', cls="ty")

    # ---------------------------------------------------------------- 12 Makine, sergi, bağış, kültür
    S[12] = page(12, f'''<span class="kick">A · ÖZEL DURUMLAR</span><div class="t" style="font-size:56px">Makine, sergi, bağış, <em>kültür varlığı</em></div>
      <div class="ways">
        <div class="card wy">{'<div class="hd">' + ic("gear", 40) + '<b>MAKİNE VE TEÇHİZAT</b></div>'}<p><b>Dışişleri ön izni</b> şart. Takrirde cins, değer, miktar, seri no, tip, model, kullanım yeri ve amacı; broşür eklenir.</p></div>
        <div class="card wy">{'<div class="hd">' + ic("frame", 40) + '<b>SERGİ</b></div>'}<p><b>Misyon binasında:</b> Form A + liste, sonunda ihraç. <b>Bina dışı fuar:</b> genel hükümler; Dışişleri Yurtdışı Tanıtım ve Kültürel İlişkiler GM'ye nota → geçici ithalat garanti mektubu.</p></div>
        <div class="card wy">{'<div class="hd">' + ic("gift", 40) + '<b>BAĞIŞ</b></div>'}<p>Araç ve dayanıklı eşyanın yerel kurum ve kuruluşlara bağışı <b>Dışişleri onayına</b> tabidir.</p></div>
        <div class="card wy kv">{'<div class="hd">' + ic("column", 40) + '<b>KÜLTÜR VARLIĞI</b></div>'}<p>Takrirle getirilen yabancı kökenli eser <b>satılamaz, devredilemez</b> → ayniyet tespitiyle ihraç ya da devlet müzesine bağış. Türkiye'de edinilen eser yalnız <b>devlet müzesine bağışlanır</b>.</p></div>
      </div>
      <div class="kst">{stamp("uyari", "KÜLTÜR VARLIĞI", rot=8, scale=0.55)}</div>''', cls="ec ms")

    # ---------------------------------------------------------------- 14 Kurye güvenliği
    chk = [("seal", "Mühür", "Kaplar ilgili Dışişleri veya temsilciliğin mührüyle kapalı olmalı.", "ok"),
           ("bag", "Sayı", "Taşınan kap sayısı, kurye mektubundaki sayıdan fazla olamaz.", "ok"),
           ("xray", "X-ray", "Diplomatik kurye kapları ilke olarak X-ray'den geçirilmez.", "no"),
           ("search", "Şüphe", "Makul ölçüden büyük veya ciddi şüpheli kap: Dışişleri onayıyla, temsilcilik görevlisi önünde açılabilir.", "warn"),
           ("flag", "İtiraz", "Temsilcilik itiraz ederse kap, Dışişleri görüşüyle ülkeye sokulmadan gönderen devlete iade edilir.", "warn")]
    rows = "".join(
        f'<div class="card ck {s}"><div class="i">{ic(i if i != "search" else "globe", 40)}</div><div><b>{t}</b><p>{d}</p></div></div>' for i, t, d, s in chk)
    S[14] = page(14, f'''<span class="kick">B · KURYE GÜVENLİĞİ</span><div class="t" style="font-size:56px">Gümrükte <em>kontrol noktası</em></div>
      <div class="cl">{rows}</div>
      <div class="pp">{pouch(300)}</div>
      <div class="card pl">{ic("plane", 48)}<p><b>Pilot:</b> kendisine emanet edilen kurye çantasını gümrüksüz bölgede, temsilciliğin havalimanı giriş kartlı yetkilisine teslim eder. <b>Gümrükten geçiremez.</b></p></div>
      <div class="pst">{stamp("uyari", "X-RAY YOK", rot=9, scale=0.6)}</div>''', cls="ks")

    # ---------------------------------------------------------------- 15 Özet (arka kapak)
    items = ["Dayanak: GK m.167/1-2 ve m.60/5-(b)", "Karşılıklılık: tespit Dışişleri'nde",
             "Satış muafiyetsize, devir muafiyetliye", "Araç: 7 gün teslim · 2 yıl satış izni",
             "Eşya: 3 yıl kuralı · 240 L / 200 karton", "Kurye: günde 5 kap × 30 kg · Form C/D",
             "Kaldırılan: 2000/21 ve 2015/10 genelgeler"]
    lis = "".join(f'<div class="li"><span>{ic("check", 26)}</span><p>{x}</p></div>' for x in items)
    S[15] = f'''<section class="slide cov back" id="p15">
  {cover_bg()}
  <div class="bt"><div class="mini2">ÖZET · KONTROL LİSTESİ</div><div class="bh">7 maddede<br/>genelge</div></div>
  <div class="bl">{lis}</div>
  <div class="cta"><span>{ic("doc", 26)} Kaydet</span><span>{ic("arrow", 26)} Paylaş</span><span>{ic("flag", 26)} Takip et</span></div>
  <img class="av" src="img/koc-cutout.png" alt="Gümrük Koçu"/>
  <div class="bsrc">Kaynak: Ticaret Bakanlığı GGM, 05.10.2026 tarihli, E-18723479-153.99-00127017053 sayılı Diplomatik İşlemler Genelgesi (2026/11). Bilgilendirme amaçlıdır.</div>
  <div class="lg"><img src="img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu"/></div>
</section>'''
    return S


CSS2 = r"""
/* 3 tanımlar */
.df .dgrid { position:absolute; left:0; top:180px; width:952px; display:grid; grid-template-columns:1fr 1fr; gap:20px; }
.df .dc { position:relative; padding:20px 22px 18px 30px; height:262px; overflow:hidden; }
.df .dc .strip { position:absolute; left:0; top:0; bottom:0; width:10px; background:linear-gradient(180deg,#0F7C7C,#7A1428); }
.df .dc .hd { display:flex; align-items:center; gap:12px; color:var(--burg); }
.df .dc .hd b { font:900 26px Montserrat; color:var(--navy); }
.df .dc p { font:500 21px/1.38 Montserrat; color:var(--ink2); margin-top:10px; }
.df .dc .chip { position:absolute; left:30px; bottom:16px; font:700 15px 'JetBrains Mono'; letter-spacing:.1em; color:#fff; background:var(--navy); padding:6px 10px; border-radius:6px; }
/* 4 karşılıklılık */
.kr .scale { position:absolute; left:0; top:178px; width:452px; height:300px; padding:22px 16px; }
.kr .outs { position:absolute; left:476px; top:178px; width:476px; display:flex; flex-direction:column; gap:12px; }
.kr .o { display:flex; align-items:center; gap:14px; padding:12px 16px; border-radius:16px; border:2px solid; background:rgba(255,255,255,.93); }
.kr .o b { font-family:'Archivo Black'; font-size:40px; width:52px; text-align:center; flex:none; }
.kr .o p { font:500 20px/1.3 Montserrat; color:var(--ink2); } .kr .o p strong { color:var(--ink); font-weight:900; }
.kr .o.g { border-color:var(--green); } .kr .o.g b { color:var(--green); }
.kr .o.r { border-color:var(--red); } .kr .o.r b { color:var(--red); }
.kr .o.b { border-color:var(--teal); } .kr .o.b b { color:var(--teal); }
.kr .who { position:absolute; left:0; top:500px; width:952px; display:flex; gap:12px; flex-wrap:wrap; }
.kr .who .pill { font-size:19px; }
.kr .gold { position:absolute; left:0; top:600px; width:952px; padding:26px 28px 22px; border:3px solid var(--gold); background:linear-gradient(180deg,#FFFBEF,#FFF3D6); }
.kr .gst { position:absolute; right:12px; top:-62px; }
.kr .gr { display:flex; align-items:center; gap:18px; margin-top:16px; }
.kr .gr:first-of-type { margin-top:6px; }
.kr .gr .ic { color:var(--gold); }
.kr .gr p { font:600 26px Montserrat; color:var(--ink); } .kr .gr p b { font-weight:900; color:var(--burg); }
.kr .tag { font-family:'Archivo Black'; font-size:30px; padding:8px 18px; border-radius:10px; color:#fff; width:170px; text-align:center; }
.kr .tag.s { background:var(--burg); } .kr .tag.d { background:var(--teal); }
.kr .gold small { display:block; margin-top:18px; font:700 18px 'JetBrains Mono'; letter-spacing:.06em; color:var(--muted); }
/* 5 araç ithalatı */
.ai .wl { position:absolute; left:0; top:180px; width:470px; display:flex; flex-direction:column; gap:14px; }
.ai .w { display:flex; gap:14px; padding:16px 18px; align-items:flex-start; }
.ai .w .ic { color:var(--burg); margin-top:2px; }
.ai .w b { font:900 23px Montserrat; color:var(--navy); } .ai .w p { font:500 19px/1.35 Montserrat; color:var(--ink2); margin-top:4px; }
.ai .tlx { position:absolute; left:494px; top:180px; width:458px; padding:20px 22px; }
.ai .step { display:flex; gap:14px; align-items:flex-start; margin-top:14px; }
.ai .step .dot { width:24px; height:24px; border-radius:50%; border:5px solid var(--navy); flex:none; margin-top:4px; background:#fff; }
.ai .step .dot.fill { background:var(--burg); border-color:var(--burg); }
.ai .step b { font:900 22px Montserrat; color:var(--ink); } .ai .step p { font:500 18px Montserrat; color:var(--ink2); }
.ai .dur { margin:10px 0 0 4px; padding:6px 0 6px 28px; border-left:5px dashed var(--burg); font-family:'Archivo Black'; font-size:44px; color:var(--burg); }
.ai .ext { margin-top:16px; padding:12px 14px; background:#E3F2EF; border-radius:12px; font:500 18px/1.38 Montserrat; color:#0B3F3F; }
.ai .ext2 { margin-top:10px; padding:12px 14px; background:#F4ECDD; border-radius:12px; font:500 18px/1.38 Montserrat; color:#4A3A1C; }
.ai .warn { position:absolute; left:0; top:800px; width:952px; padding:18px 22px 18px 18px; display:flex; gap:12px; align-items:center; border-color:var(--amber); }
.ai .warn p { font:500 20px/1.38 Montserrat; color:var(--ink2); } .ai .warn p b { color:var(--ink); font-weight:800; }
/* 6 satış süreleri */
.sl .tl6 { position:absolute; left:0; top:180px; width:952px; padding:20px 22px 18px; }
.sl .tr { margin-top:12px; }
.sl .tr .lab { display:flex; align-items:baseline; gap:12px; margin-left:40px; }
.sl .tr .lab b { font:900 22px Montserrat; color:var(--navy); } .sl .tr .lab span { font:600 17px Montserrat; color:var(--muted); }
.sl .ax { position:relative; height:28px; margin-top:4px; }
.sl .ax span { position:absolute; transform:translateX(-50%); font:700 16px 'JetBrains Mono'; color:var(--muted); }
.sl .leg { display:flex; gap:20px; flex-wrap:wrap; margin-top:10px; font:700 17px Montserrat; color:var(--ink2); align-items:center; }
.sl .leg span { display:flex; align-items:center; gap:8px; } .sl .leg i { width:26px; height:14px; border-radius:3px; display:block; }
.sl .leg i.hz { background:repeating-linear-gradient(45deg,#C9C1AE 0 4px,transparent 4px 8px); border:1px solid #C9C1AE; }
.sl .leg .h5 { color:var(--burg); }
.sl .rules { position:absolute; left:0; top:640px; width:952px; display:grid; grid-template-columns:1fr 1fr; gap:14px; }
.sl .ru { display:flex; gap:10px; align-items:center; padding:12px 14px; min-height:150px; }
.sl .ru .ic { color:var(--burg); } .sl .ru p { font:500 18.5px/1.36 Montserrat; color:var(--ink2); } .sl .ru p b { color:var(--ink); font-weight:800; }
.sl .ru.tz { border-color:#5B21B6; }
/* 7 satış işlemi */
.sp .fl { position:absolute; left:0; top:170px; width:952px; height:850px; }
.sp .spine { position:absolute; left:436px; top:0; }
.sp .fs { position:absolute; width:952px; height:110px; }
.sp .fs .n { position:absolute; left:446px; top:30px; width:60px; height:60px; border-radius:50%; background:var(--burg); color:#FCEBD0; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:28px; box-shadow:0 0 0 6px rgba(184,137,59,.45); }
.sp .fs .fb { position:absolute; top:6px; width:410px; padding:12px 16px; }
.sp .fs.l .fb { left:0; } .sp .fs.r .fb { left:542px; }
.sp .fb b { font:900 22px Montserrat; color:var(--navy); } .sp .fb p { font:500 17.5px/1.32 Montserrat; color:var(--ink2); margin-top:3px; }
""" + "".join(f".sp .fs:nth-of-type({k + 1}) {{ top:{k * 118}px; }}\n" for k in range(7)) + r"""
.sp .sst { position:absolute; left:620px; top:888px; }
/* 8 / 12 cards */
.ec .ways { position:absolute; left:0; top:180px; width:952px; display:grid; grid-template-columns:1fr 1fr; gap:18px; }
.ec .wy { padding:20px 22px; min-height:258px; }
.ec .wy .hd { display:flex; gap:12px; align-items:center; color:var(--burg); }
.ec .wy .hd b { font-family:'Archivo Black'; font-size:24px; color:var(--navy); letter-spacing:.02em; }
.ec .wy p { font:500 20px/1.4 Montserrat; color:var(--ink2); margin-top:10px; } .ec .wy p b { color:var(--ink); font-weight:800; }
.ec .cross { position:absolute; left:0; top:752px; width:952px; padding:16px 20px; border-color:var(--red); }
.ec .cross .stamp { position:absolute; right:-10px; top:-66px; }
.ec .cx { display:flex; align-items:center; gap:16px; }
.ec .cx span { font:800 19px Montserrat; padding:8px 12px; border-radius:10px; }
.ec .cx .dc1 { background:#E3F2EF; color:#0B3F3F; } .ec .cx .dc2 { background:#F9E4E8; color:#5E0B1A; }
.ec .cx b { font-family:'Archivo Black'; font-size:40px; color:var(--red); position:relative; }
.ec .cx b:after { content:""; position:absolute; left:-4px; right:-4px; top:50%; height:5px; background:var(--red); transform:rotate(-35deg); }
.ec .cross p { font:500 19px/1.38 Montserrat; color:var(--ink2); margin-top:10px; }
.ms .wy.kv { border-color:var(--red); }
.ms .kst { position:absolute; right:20px; top:745px; }
/* 9 diğer araçlar */
.da .nums { position:absolute; left:0; top:180px; width:952px; display:grid; grid-template-columns:1fr 1fr 1.6fr; gap:18px; }
.da .nb { padding:18px 20px; text-align:center; }
.da .nb .big { font-size:96px; color:var(--burg); display:block; }
.da .nb b { display:block; font:900 22px Montserrat; color:var(--navy); margin-top:6px; letter-spacing:.06em; }
.da .nb p { font:600 19px/1.3 Montserrat; color:var(--ink2); margin-top:4px; }
.da .nb.plus .big { color:var(--teal); }
.da .vx { position:absolute; left:0; top:440px; width:952px; display:flex; flex-direction:column; gap:16px; }
.da .vv { display:grid; grid-template-columns:90px 1fr; grid-template-rows:auto auto; column-gap:16px; padding:18px 22px; align-items:center; }
.da .vv .ic { grid-row:1 / span 2; color:var(--burg); }
.da .vv b { font:900 25px Montserrat; color:var(--navy); } .da .vv p { font:500 20px/1.38 Montserrat; color:var(--ink2); margin-top:4px; }
.da .vv p strong { color:var(--burg); font-weight:900; }
/* 10 kişisel eşya */
.ke .fa { position:absolute; left:0; top:180px; width:952px; padding:18px 22px; display:flex; gap:16px; align-items:flex-start; }
.ke .fa .ic { color:var(--burg); }
.ke .fa b { font:900 24px Montserrat; color:var(--navy); } .ke .fa p { font:500 19px/1.38 Montserrat; color:var(--ink2); margin-top:4px; }
.ke .quota { position:absolute; left:0; top:350px; width:952px; display:grid; grid-template-columns:1fr 1fr 1.25fr; gap:16px; }
.ke .q { padding:20px; text-align:center; background:linear-gradient(180deg,#fff,#FFF4E6); }
.ke .q .ic { margin:0 auto; color:var(--burg); }
.ke .q .big { display:block; font-size:66px; color:var(--burg); margin-top:8px; }
.ke .q b { display:block; font:900 22px Montserrat; color:var(--navy); margin-top:4px; } .ke .q p { font:600 17px Montserrat; color:var(--muted); }
.ke .qn { padding:16px 18px; } .ke .qn p { font:500 18px/1.38 Montserrat; color:var(--ink2); margin-top:8px; } .ke .qn p b { color:var(--ink); }
.ke .tk { position:absolute; left:0; top:690px; width:952px; padding:18px 22px; }
.ke .tkr { display:flex; align-items:center; gap:12px; margin-top:8px; }
.ke .tkr .cnt { font-family:'Archivo Black'; font-size:44px; color:#fff; background:var(--teal); width:64px; height:64px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex:none; }
.ke .tkr p { font:700 18px/1.3 Montserrat; color:var(--ink2); max-width:300px; }
.ke .tkn { font:500 18px/1.4 Montserrat; color:var(--ink2); margin-top:12px; } .ke .tkn b { color:var(--ink); }
/* 11 3 yıl */
.ty .q0 { position:absolute; left:126px; top:176px; width:700px; padding:16px 20px; display:flex; gap:14px; align-items:center; border:3px solid var(--navy); }
.ty .q0 .ic { color:var(--teal); } .ty .q0 p { font:600 22px/1.3 Montserrat; color:var(--ink); } .ty .q0 p b { font-weight:900; }
.ty .q0 small { display:block; font:700 15px 'JetBrains Mono'; color:var(--muted); letter-spacing:.06em; margin-top:4px; }
.ty .br { position:absolute; left:0; top:290px; }
.ty .cols { position:absolute; left:0; top:370px; width:952px; display:grid; grid-template-columns:1fr 1fr; gap:22px; }
.ty .yn { font-family:'Archivo Black'; font-size:26px; color:#fff; padding:6px 16px; border-radius:8px; display:inline-block; margin-left:122px; }
.ty .col.y .yn { background:var(--green); } .ty .col.n .yn { background:var(--red); }
.ty .ci { padding:12px 16px; margin-top:12px; } .ty .col.y .ci { border-color:var(--green); } .ty .col.n .ci { border-color:var(--red); }
.ty .ci b { font:900 21px Montserrat; color:var(--navy); } .ty .ci p { font:500 18px/1.36 Montserrat; color:var(--ink2); margin-top:3px; }
.ty .tz2 { position:absolute; left:0; top:888px; width:952px; padding:12px 18px; display:flex; gap:12px; align-items:center; border-color:#5B21B6; }
.ty .tz2 p { font:500 19px/1.38 Montserrat; color:var(--ink2); } .ty .tz2 p b { color:var(--ink); font-weight:800; }
/* 14 kurye güvenliği */
.ks .cl { position:absolute; left:0; top:180px; width:600px; display:flex; flex-direction:column; gap:12px; }
.ks .ck { display:flex; gap:14px; padding:14px 16px; align-items:flex-start; }
.ks .ck .i { width:56px; height:56px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex:none; color:#fff; }
.ks .ck.ok .i { background:var(--green); } .ks .ck.no .i { background:var(--red); } .ks .ck.warn .i { background:var(--amber); }
.ks .ck b { font:900 22px Montserrat; color:var(--navy); } .ks .ck p { font:500 18px/1.36 Montserrat; color:var(--ink2); margin-top:2px; }
.ks .pp { position:absolute; left:640px; top:220px; }
.ks .pst { position:absolute; left:640px; top:560px; }
.ks .pl { position:absolute; left:0; top:860px; width:952px; padding:14px 18px; display:flex; gap:14px; align-items:center; border-color:var(--teal); }
.ks .pl .ic { color:var(--teal); } .ks .pl p { font:500 19px/1.38 Montserrat; color:var(--ink2); } .ks .pl p b { color:var(--ink); font-weight:800; }
/* 15 back cover */
.back .bt { position:absolute; left:96px; top:110px; }
.back .mini2 { font:700 20px 'JetBrains Mono'; letter-spacing:.2em; color:var(--gold2); }
.back .bh { font-family:Marcellus; font-size:76px; line-height:1.12; padding-bottom:12px; margin-top:10px; background:linear-gradient(180deg,#FBE7B5,#E2B865 50%,#B07E2E); -webkit-background-clip:text; background-clip:text; color:transparent; }
.back .bl { position:absolute; left:96px; top:330px; width:560px; }
.back .li { display:flex; gap:14px; align-items:center; padding:12px 0; border-bottom:1px solid rgba(233,199,126,.3); }
.back .li span { width:40px; height:40px; border-radius:50%; background:linear-gradient(180deg,#F8DFA3,#C9963F); display:flex; align-items:center; justify-content:center; color:#3E0812; flex:none; }
.back .li p { font:700 21px/1.3 Montserrat; color:#FBEBD3; }
.back .cta { position:absolute; left:96px; top:1000px; display:flex; gap:12px; }
.back .cta span { display:flex; align-items:center; gap:8px; font:900 21px Montserrat; color:#3E0812; background:linear-gradient(180deg,#F8DFA3,#D6A754); padding:12px 16px; border-radius:12px; }
.back .av { position:absolute; left:560px; top:560px; width:600px; }
.back .bsrc { position:absolute; left:96px; top:1086px; width:560px; font:500 15px/1.45 'JetBrains Mono'; color:#E9CFC2; opacity:.85; }
.back .lg { position:absolute; left:96px; top:1200px; right:auto; }
"""
