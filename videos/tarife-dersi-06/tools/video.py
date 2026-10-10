"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 6
META = "DERS · <b>TARİFE #6</b> · DAYANAK, KOD, MEYVE"
TITLE = "Tarife Dersi 6 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · YASAL DAYANAK", ["s02", "s03", "s04"]), ("SORU 2 · KOD SEVİYELERİ", ["s05", "s06", "s07"]),
    ("SORU 3 · FASIL 8", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Tarife cetvelinin dayanağı ve değiştirme yetkisi — hangisi doğru?", "Soru 2: Hangi kod Armonize Sistem alt pozisyonu?",
      "Soru 3: Hangisi 8. fasılda sınıflandırılmaz?", "Koçun notu", "Cevap anahtarı"]
KW = [r"Armonize Sistem Nomanklatürü", r"Cumhurbaşkanı", r"Cumhurbaşkanına", r"Brüksel Nomanklatürü", r"eski sistemdir", r"iki yarısını",
      r"alt pozisyonudur", r"ortaktır", r"6 hanede biter", r"Kombine Nomanklatür\w*", r"hane sayısını", r"yağlı tohum\w*", r"Yer fıstığı",
      r"Kavrulmuş", r"A şıkkı", r"B şıkkı", r"C şıkkı", r"D şıkkı", r"E şıkkı", r"dikkat:", r"Hayır!"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s03", T("s03", "Cevap"), "cevap"), ("s03", T("s03", "Pozisyonları"), "neutral"),
            ("s03", T("s03", "Diğerleri"), "dikkat"), ("s04", 0.0, "tuzak"), ("s04", T("s04", "dikkat"), "dikkat"), ("s05", 0.0, "soru"),
            ("s06", T("s06", "Cevap"), "cevap"), ("s06", T("s06", "Kod"), "neutral"), ("s06", T("s06", "Seksen"), "dikkat"),
            ("s07", 0.0, "tuzak"), ("s07", T("s07", "Yedinci"), "dikkat"), ("s08", 0.0, "soru"), ("s09", T("s09", "Cevap"), "cevap"),
            ("s09", T("s09", "Susam"), "dikkat"), ("s09", T("s09", "Diğerleri"), "neutral"), ("s10", 0.0, "tuzak"), ("s10", T("s10", "dikkat"), "uyari"),
            ("s11", 0.0, "neutral"), ("s11", T("s11", "Üç"), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Yasal dayanak, kod seviyeleri ve meyve faslı",
    message="Cetvel AS esaslı, yetki Cumhurbaşkanında (D) · 8501.10 AS alt pozisyonu (B) · susam 12.07, Fasıl 8 değil (A).",
    intent="Ölçülen bilgi alanları: Gümrük Giriş Tarife Cetvelinin yasal dayanağı ve değiştirme yetkisi, 12 haneli kod yapısının seviyeleri (fasıl, pozisyon, alt pozisyon, KN, GTİP) ve Fasıl 8 ile Fasıl 12 ayrımı (yağlı tohumlar).",
    team="Cano (cetveli bakanlık yayımlıyor diye B → HAYIR) · Stajyer (en uzun kod en ayrıntılı diye 12 hane → HAYIR) ve Gümrükçü Baba (“hangi sistem geçiyorsa o sistemin hanesini say”) · Yardımcı (çerez gibi yenir diye susamı Fasıl 8'e koyar → HAYIR).",
    visuals="doğru ifade kartı + dört yanlış ifadenin ✗ ve düzeltmeleri, 2 → 4 → 6 → 8 → 12 hane kod merdiveni (doğru basamak yeşil), yanlış şıkkın üstü çizilip DOĞRUSU kartı + diğer dört ürünün pozisyonları, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı",
    sources="Gümrük Giriş Tarife Cetveli Hakkında Kanun (cetvel Armonize Sistem Nomanklatürü esas alınarak düzenlenmiş; pozisyon, not ve genel kuralları genişletme, açma, değiştirme yetkisi Cumhurbaşkanında), TGTC'nin yıllık Cumhurbaşkanı kararıyla yayımlanması, DGÖ — Armonize Sistem ilk 6 hane ortak, 12 haneli GTİP'te 7–8. hanelerin Kombine Nomanklatür olması, Fasıl 8 pozisyon metinleri (08.01 kaju, 08.02 badem, 08.04 avokado, 08.13 kurutulmuş meyveler), Fasıl 12 notu (12.07 susam; 08.01/08.02 ürünleri hariç), 12.02 (kavrulmamış yer fıstığı) ve 20.08 (kavrulmuş/hazırlanmış yer fıstığı).",
    yt_title="Tarife Cetvelinin Dayanağı, Kod Seviyeleri (8501.10) ve Susam Fasıl 8 mi? | Tarife Dersi #6 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin altıncısında yine 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, Gümrük Giriş Tarife Cetveli, Armonize Sistem, Kombine Nomanklatür, GTİP, alt pozisyon, Fasıl 8, Fasıl 12, 12.07, susam, tarife sınıflandırma, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Gümrük Giriş Tarife Cetveli ile ilgili aşağıdaki ifadelerden hangisi doğrudur?",
             options=["Cetvel Brüksel Nomanklatürü esas alınarak düzenlenmiştir; pozisyonlarını değiştirmeye Cumhurbaşkanı yetkilidir.",
                      "Cetvel Armonize Sistem Nomanklatürü esas alınarak düzenlenmiştir; pozisyonlarını değiştirmeye Ticaret Bakanlığı yetkilidir.",
                      "Cetvel Dünya Gümrük Örgütü tarafından yayımlanır; ülkeler pozisyonlarını değiştiremez.",
                      "Cetvel Armonize Sistem Nomanklatürü esas alınarak düzenlenmiştir; pozisyonlarını ve notlarını değiştirmeye Cumhurbaşkanı yetkilidir.",
                      "Cetvelin ilk altı hanesi ulusal düzeyde belirlenir; Armonize Sistem yalnızca fasılları belirler."],
             answer="D", why="Kanuna göre cetvel Armonize Sistem Nomanklatürü esas alınarak düzenlenmiştir; pozisyon, not ve genel kuralları genişletmeye, açmaya ve değiştirmeye Cumhurbaşkanı yetkilidir. A: Brüksel Nomanklatürü eski sistem; B: yetki bakanlıkta değil; C: cetvel ulusaldır, DGÖ yayımlamaz; E: ilk 6 hane bütün AS ülkelerinde ortaktır.",
             ref="Gümrük Giriş Tarife Cetveli Hakkında Kanun", yt="Tarife cetveli neye dayanır, değiştirme yetkisi kimde? Her şıkkın iki yarısını da kontrol etmek."),
        dict(stem="Aşağıdaki kodlardan hangisi bir Armonize Sistem alt pozisyonudur?",
             options=["85.01", "8501.10", "85", "8501.10.10.00.00", "8501.10.10"], answer="B",
             why="İlk 2 hane fasıl, 4 hane pozisyon, 6 hane Armonize Sistem alt pozisyonu (bütün AS ülkelerinde ortak); 8 hane AB Kombine Nomanklatürü, 12 hane GTİP.",
             ref="TGTC kod yapısı", yt="Kod merdiveni: 2 · 4 · 6 · 8 · 12 hane. En uzun kod neden doğru cevap değil?"),
        dict(stem="Aşağıdakilerden hangisi tarife cetvelinin 8. faslında sınıflandırılmaz?",
             options=["Susam tohumu", "Kabuğu soyulmuş badem", "Taze avokado", "Kurutulmuş kayısı", "Kaju cevizi"], answer="A",
             why="Fasıl 8 yenilen meyveleri ve sert kabuklu meyveleri kapsar (badem 08.02, avokado 08.04, kaju 08.01, kurutulmuş kayısı 08.13). Susam yağlı tohumdur: Fasıl 12, 12.07. Yer fıstığı 12.02; kavrulmuşsa Fasıl 20.",
             ref="Fasıl 12 notu · 12.07", yt="Susam, badem, kaju: hangisi meyve faslında değil? Yağlı tohumlar ve yer fıstığı tuzağı."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #6; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — tarife cetveli, 'doğrudur' altı çizili + DİKKAT · dikkatli oku!; 5 iki parçalı şık; 3 sn geri sayım.",
        s03="CEVAP D; doğru ifade kartı (Tarife Cetveli Kanunu etiketi); dört yanlış ifade ✗ ve düzeltmeleri.",
        s04="TUZAK — Cano 'bakanlık yayımlıyor' diye B → HAYIR; B ≠ D kartları; DİKKAT: Brüksel Nomanklatürü eski sistem.",
        s05="SORU 2/3 — Armonize Sistem alt pozisyonu; 5 kod şıkkı (2–12 hane); 3 sn geri sayım.",
        s06="CEVAP B; kod merdiveni 85 → 85.01 → 8501.10 ✓ → 8501.10.10 → 8501.10.10.00.00; DİKKAT: ilk 6 hane ortak.",
        s07="TUZAK — Stajyer 12 haneyi seçer → HAYIR; 12 hane ≠ 6 hane; DİKKAT: 7.–8. hane KN; Gümrükçü Baba 'hanesini say'.",
        s08="SORU 3/3 — 8. fasılda sınıflandırılmayan; 'sınıflandırılmaz' altı çizili; 5 ürün şıkkı; 3 sn geri sayım.",
        s09="CEVAP A; susam üstü çizilir, DOĞRUSU kartı (12.07); diğer dört ürün Fasıl 8 pozisyonlarıyla ✓.",
        s10="TUZAK — Yardımcı 'çerez gibi yenir' diye Fasıl 8 → HAYIR; Fasıl 8 ≠ 12.07; DİKKAT: yer fıstığı 12.02, kavrulmuş Fasıl 20.",
        s11="İPUCU · Koçun notu — zihin haritası: yasal dayanak · kod merdiveni · yağlı tohumlar.",
        s12="ÖNEMLİ · Cevap anahtarı D · B · A; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
