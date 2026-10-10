"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 10
META = "DERS · <b>TARİFE #10</b> · HAVA YASTIĞI, GÜMÜŞ, KÖPRÜ"
TITLE = "Tarife Dersi 10 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · HAVA YASTIKLI TAŞIT", ["s02", "s03", "s04"]), ("SORU 2 · MÜCEVHERCİ EŞYASI", ["s05", "s06", "s07"]),
    ("SORU 3 · BİNİŞ KÖPRÜSÜ", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Hava yastıklı taşıtlar — hangisi doğru?", "Soru 2: Gümüş sigara tabakası hangi pozisyonda?",
      "Soru 3: Yolcu biniş köprüsü hangi pozisyonda?", "Koçun notu", "Cevap anahtarı"]
KW = [r"en çok benzedikleri", r"en çok benzediği", r"kıyıya çıkabil\w*", r"makine sayılmaz", r"demiryolundaki",
      r"mücevherci eşyası\w*", r"kuyumcu eşyası\w*", r"cepte", r"masada", r"taklit mücevher\w*", r"kendine özgü", r"Kendine özgü",
      r"inşaat aksamı", r"işlevine", r"A şıkkı", r"B şıkkı", r"C şıkkı", r"D şıkkı", r"E şıkkı", r"dikkat:", r"Hayır!"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s03", T("s03", "Cevap"), "cevap"), ("s03", T("s03", "Kılavuz"), "dikkat"),
            ("s03", T("s03", "Karada"), "neutral"), ("s04", 0.0, "tuzak"), ("s04", T("s04", "dikkat"), "dikkat"), ("s05", 0.0, "soru"),
            ("s06", T("s06", "Cevap"), "cevap"), ("s06", T("s06", "Sigara"), "dikkat"), ("s06", T("s06", "Masada"), "neutral"),
            ("s07", 0.0, "tuzak"), ("s07", T("s07", "dikkat"), "dikkat"), ("s08", 0.0, "soru"), ("s09", T("s09", "Cevap"), "cevap"),
            ("s09", T("s09", "Kendine"), "dikkat"), ("s09", T("s09", "Armonize"), "neutral"), ("s10", 0.0, "tuzak"),
            ("s10", T("s10", "dikkat"), "uyari"), ("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Hava yastıklı taşıtlar, kıymetli metalden eşya ve yolcu biniş köprüleri",
    message="Hava treni Fasıl 86, hava yastıklı taşıt en çok benzediği taşıtla (B) · cepte taşınan gümüş sigara tabakası 71.13 (A) · yolcu biniş köprüsü 84.79 (D).",
    intent="Ölçülen bilgi alanları: Bölüm XVII Not 5 (hava yastıklı taşıtlar en çok benzedikleri taşıtla: kılavuz hatlı Fasıl 86, kara veya kara-su Fasıl 87, su Fasıl 89), Fasıl 71 Not 9 ve Not 10 (mücevherci eşyası ile kuyumcu eşyası ayrımı; taklit mücevherin yalnız küçük süs eşyasını kapsaması) ve kendine özgü işlevli makinelerin 84.79’da sınıflandırılması (yolcu biniş köprüleri).",
    team="Cano (kıyıya çıkabiliyor diye su üstü hava yastıklı tekneyi Fasıl 87 sanır → HAYIR, Fasıl 89) · Stajyer (sigara gereci kuyumcu eşyası diye 71.14 → HAYIR, 71.13) ve Gümrükçü Baba (“cepte mi, masada mı?”) · Yardımcı (adı köprü diye 73.08 → HAYIR, 84.79) ve Gümrükçü Baba (“adına değil, işlevine bak”).",
    visuals="doğru ifade kartı + dört yanlış ifadenin ✗ ve düzeltmeleri, ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (doğru olan yeşil), tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: Bölüm XVII Not 5 (hava yastıklı taşıtlar: kılavuz hat üzerinde işleyenler Fasıl 86, karada veya hem karada hem suda işleyenler Fasıl 87, suda işleyenler — sahile ve iskeleye çıkabilsin veya buz üzerinde işleyebilsin, işlemesin — Fasıl 89; hava treni hatlarının sabit malzemesi ve sinyal-kumanda cihazları demiryolundaki karşılıkları gibi), Fasıl 71 Not 9 (mücevherci eşyası: küçük süs eşyası ile cepte, el çantasında veya üstte taşınan kişisel eşya — sigara tabakası, pudralık, tespih), Not 10 (kuyumcu eşyası: süs, sofra, tuvalet eşyası, sigara içenlere ait gereçler), Not 11 (taklit mücevher yalnız Not 9(a) eşyası), 42.02 (deri veya plastikten sigara tabakası), 96.14 (pipolar, ağızlıklar); 84.79 ve 8479.71 / 8479.79 (yolcu biniş köprüleri), 73.08 (demir-çelikten köprüler ve inşaat aksamı), 84.26 (vinçler), 84.28 (yürüyen merdivenler ve yürüyen yollar), 89.07 (yüzer yapılar, iskeleler).",
    yt_title="Hava Treni Hangi Fasılda? Gümüş Sigara Tabakası 71.13 mü? Yolcu Biniş Köprüsü 84.79 mu? | Tarife Dersi #10 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin onuncusunda yine 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, hava yastıklı taşıt, hava treni, Bölüm XVII Not 5, Fasıl 86, Fasıl 89, Fasıl 71, mücevherci eşyası, kuyumcu eşyası, 71.13, 71.14, sigara tabakası, 84.79, yolcu biniş köprüsü, 73.08, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Hava yastığı üzerinde hareket eden taşıtların sınıflandırılmasıyla ilgili aşağıdaki ifadelerden hangisi doğrudur?",
             options=["Hava yastıklı taşıtların tamamı, hava taşıtlarıyla birlikte 88. fasılda sınıflandırılır.",
                      "Kılavuz bir hat üzerinde gitmek üzere tasarlanmış hava trenleri 86. fasılda sınıflandırılır.",
                      "Hem karada hem suda gidebilen hava yastıklı taşıtlar 89. fasılda sınıflandırılır.",
                      "Yalnız su üzerinde giden, kıyıya çıkabilen hava yastıklı taşıtlar 87. fasılda sınıflandırılır.",
                      "Hava yastıklı taşıtlar, benzedikleri taşıta bakılmaksızın 84. fasılda makine olarak sınıflandırılır."],
             answer="B", why="Bölüm XVII Not 5’e göre hava yastıklı taşıtlar en çok benzedikleri taşıtlarla sınıflandırılır: kılavuz hat üzerinde gidenler (hava trenleri) Fasıl 86, karada veya hem karada hem suda gidenler Fasıl 87, su üzerinde gidenler kıyıya çıkabilse de Fasıl 89. Hiçbiri Fasıl 84’te makine sayılmaz.",
             ref="Bölüm XVII Not 5", yt="Hava treni, hava yastıklı tekne: 86 mı, 87 mi, 89 mu? En çok benzediği taşıt kuralı."),
        dict(stem="Gümüşten yapılmış, cepte taşınan türden sigara tabakası hangi tarife pozisyonunda sınıflandırılır?",
             options=["71.13", "71.14", "71.17", "42.02", "96.14"], answer="A",
             why="Fasıl 71 Not 9’a göre mücevherci eşyası; küçük süs eşyası ile cepte, el çantasında veya üstte taşınan kişisel eşyayı (sigara tabakası, pudralık, tespih) kapsar. Gümüşten olduğu için 71.13’tedir. Masada duran gümüş sigara kutusu ve kül tablası kuyumcu eşyası olarak 71.14’tedir; adi metalden sigara tabakası taklit mücevher sayılmaz.",
             ref="Fasıl 71 Not 9, 10 ve 11", yt="Gümüş sigara tabakası mücevherci mi, kuyumcu eşyası mı? Cepte mi, masada mı?"),
        dict(stem="Bir yolcu limanında, kruvaziyer gemilere biniş için kullanılan, teleskopik hareketli bir tünelden oluşan yolcu biniş köprüsü hangi tarife pozisyonunda sınıflandırılır?",
             options=["84.26", "73.08", "84.28", "84.79", "89.07"], answer="D",
             why="Yolcu biniş köprüsü kendine özgü işlevi olan, başka pozisyonda belirtilmeyen bir makinedir: 84.79. Armonize Sistem havalimanında kullanılanlar için 8479.71, diğerleri için 8479.79 alt pozisyonlarını açar. 73.08 sabit çelik köprüler gibi inşaat aksamı içindir; yürüyen merdiven ve yürüyen yollar 84.28’dedir.",
             ref="84.79 · 8479.71 / 8479.79", yt="Adı köprü ama makine: yolcu biniş köprüsü 73.08 mi, 84.79 mu?"),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #10; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — hava yastıklı taşıtlar, 'doğrudur' altı çizili; 5 ifade şıkkı; 3 sn geri sayım.",
        s03="CEVAP B; doğru ifade kartı (Bölüm XVII Not 5 etiketi); dört yanlış ifade ✗ ve düzeltmeleri.",
        s04="TUZAK — Cano kıyıya çıkan su üstü taşıtı kara taşıtı sanar → HAYIR, Fasıl 89; DİKKAT: hava treni hattı demiryolu karşılığı.",
        s05="SORU 2/3 — gümüş sigara tabakası; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP A; tabaka kartı → Fasıl 71 Not 9, kişisel eşya, kıymetli metal → 71.13; aday şeridi 71.13 ✓ · 71.14 · 71.17 · 42.02 · 96.14.",
        s07="TUZAK — Stajyer sigara gerecini kuyumcu eşyası sanar → HAYIR; DİKKAT: adi metal tabaka taklit mücevher değil; Gümrükçü Baba 'cepte mi, masada mı'.",
        s08="SORU 3/3 — limanda yolcu biniş köprüsü; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s09="CEVAP D; köprü kartı → hareketli makine, kendine özgü işlev, başka yerde yok → 84.79; aday şeridi.",
        s10="TUZAK — Yardımcı adı köprü diye 73.08 → HAYIR; DİKKAT: yürüyen merdiven 84.28; Gümrükçü Baba 'adına değil, işlevine bak'.",
        s11="İPUCU · Koçun notu — zihin haritası: hava yastıklı · cep / masa · ad ≠ işlev.",
        s12="ÖNEMLİ · Cevap anahtarı B · A · D; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
