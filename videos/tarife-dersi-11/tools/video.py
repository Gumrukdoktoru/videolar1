"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 11
META = "DERS · <b>TARİFE #11</b> · 5 SORU · BÖLÜM XII · XV · XVI"
TITLE = "Tarife Dersi 11 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · POZİSYON SIRASI", ["s02", "s03", "s04"]), ("SORU 2 · BORU BAĞLANTISI", ["s05", "s06", "s07"]),
    ("SORU 3 · ADİ METALLER", ["s08", "s09", "s10"]), ("SORU 4 · FÜNİKÜLER", ["s11", "s12", "s13"]),
    ("SORU 5 · MANYETİK AYNA", ["s14", "s15", "s16"]), ("KOÇUN NOTU", ["s17"]), ("CEVAP ANAHTARI", ["s18"]),
]
YT = ["Giriş", "Soru 1: Baret, şemsiye, kamçı, peruk — pozisyon sırası", "Soru 2: Hangisi 73.07'de değil? Hortum kelepçesi",
      "Soru 3: Hangi metalin ayrı faslı yok? Kobalt", "Soru 4: Hangisi 84.28'de değil? Füniküler vagonu",
      "Soru 5: Elektromanyetik torna aynası 84.66 mı, 85.05 mi?", "Koçun notu", "Cevap anahtarı"]
KW = ["koruyucu başlık", "bastonlarla birlikte", "malzemesi ne olursa olsun", "Malzemeye değil", "eşyaya bakın",
      "boru bağlantı parçaları", "açıklama notu", "Açıklama notu", "birleşmez", "ucunu kapatan", "bütünleşiyor",
      "kendi faslı", "kendi adını", "diğer adi metaller", "Diğer adi metallerin", "boştur",
      "çekiş mekanizmaları", "çekme mekanizması", "bucurgat", "vagonlar", "birer makinedir", "Vagon taşıttır",
      "adıyla", "Mekanik aynalar", "elektromanyetik aynalar", "Mıknatısla",
      "A şıkkı", "B şıkkı", "C şıkkı", "D şıkkı", "E şıkkı", "dikkat:", "Hayır!"]


def cues(T):
    out = [("s01", 0.2, "neutral")]
    for q, s, t in (("s02", "s03", "s04"), ("s05", "s06", "s07"), ("s08", "s09", "s10"), ("s11", "s12", "s13"), ("s14", "s15", "s16")):
        out += [(q, 0.0, "soru"), (s, T(s, "Cevap"), "cevap"), (s, T(s, "Cevap") + 3.0, "neutral"), (t, 0.0, "tuzak"), (t, T(t, "dikkat"), "dikkat")]
    return out + [("s17", 0.0, "neutral"), ("s17", T("s17", "Üç", 2), "dikkat"), ("s18", 0.0, "cevap")]


DOC = dict(
    title="Pozisyon sırası, boru bağlantı parçaları, diğer adi metaller, füniküler ve manyetik aynalar",
    message="Baret 65.06 → şemsiye 66.01 → kamçı 66.02 → peruk 67.04 (D) · hortum kelepçesi 73.26, 73.07 değil (B) · kobalt Fasıl 81, 81.05 (E) · füniküler vagonu 86.05, 84.28 değil (A) · elektromanyetik torna aynası 85.05 (C).",
    intent="Bu derste 5 soru var. Ölçülen bilgi alanları: Bölüm XII pozisyonlarının sırası (65.06 koruyucu başlıklar, 66.01 şemsiyeler, 66.02 bastonlar ve kamçılar, 67.04 peruklar; Fasıl 42 notlarının kamçıları, Fasıl 39 Not 2'nin Bölüm XII eşyasını hariç tutması), 73.07 boru bağlantı parçalarının kapsamı (hortum kelepçesi 73.26), Bölüm XV'te kendi faslı olan adi metaller ve Fasıl 81 (kobalt 81.05; Fasıl 77 boş), 84.28'de teleferik, telesiyej, teleski ve füniküler çekiş mekanizmaları (vagonlar 86.05), 85.05'te elektromanyetik aynalar (84.66 değil).",
    team="Cano (sapı deri diye kamçıyı saraciye sanır → HAYIR, 66.02) · Stajyer (kör tapa bağlamıyor diye 73.07 dışında sanır → HAYIR) ve Gümrükçü Baba (“boruyla bütünleşiyor mu?”) · Yardımcı (kobaltın da faslı var sanır → HAYIR, Fasıl 81) · Stajyer (telesiyeji spor eşyası sanır → HAYIR, 84.28) · Yardımcı (torna aynası tezgâh aksesuarı diye 84.66 → HAYIR, 85.05) ve Gümrükçü Baba (“mıknatısla mı tutuyor?”).",
    visuals="sıralama zinciri (4 eşya kartı) + dört yanlış sıralamanın ✗ gerekçesi, yanlış ifade + DOĞRUSU kartı + dört doğru şık, ürün kartı + 3 adımlı gerekçe + 5 aday şeridi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 5 soruluk cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: 65.06 (koruyucu başlıklar), 66.01 (şemsiyeler), 66.02 (bastonlar, kamçılar, kırbaçlar), 67.04 (peruklar); Fasıl 42 notları (kamçılar 66.02), Fasıl 39 Not 2 (Bölüm XII eşyası hariç); 73.07 ve izahnamesi (boruları birleştiren, cihaza bağlayan veya ucunu kapatan parçalar; hortum kelepçeleri, boru askıları ve destekleri hariç), 73.26; Bölüm XV: Fasıl 74 bakır, 75 nikel, 76 alüminyum, 78 kurşun, 79 çinko, 80 kalay, 81 diğer adi metaller (81.05 kobalt), Fasıl 77 boş; 84.28 ve 8428.40 (yürüyen merdivenler), 8428.60 (teleferikler, telesiyejler, teleskiler, füniküler çekiş mekanizmaları), izahname: füniküler vagonları 86.05, raylar 73.02, teçhizat 86.08; 95.06; 85.05 (elektromanyetik veya daimi mıknatıslı aynalar, kıskaçlar; elektromanyetik kavramalar, kaplinler, frenler), 84.66 (iş tutucular ve aynalar; elektromanyetik olanlar hariç), 84.58, 85.36, 85.43.",
    yt_title="Baret, Kamçı, Peruk Sırası · Hortum Kelepçesi 73.07 mi? · Kobalt Hangi Fasılda? · Füniküler Vagonu · Manyetik Ayna 85.05 | Tarife Dersi #11 · 5 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin on birincisinde bu kez 5 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, pozisyon sırası, 65.06, 66.02, 67.04, 73.07, boru bağlantı parçaları, hortum kelepçesi, 73.26, Fasıl 81, kobalt, 81.05, 84.28, füniküler, telesiyej, 86.05, 85.05, elektromanyetik ayna, 84.66, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Aşağıdakilerden hangisinde eşyalar, tarife cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru sıralanmıştır?",
             options=["Deri saplı kamçı, plastik baret, yağmur şemsiyesi, sentetik peruk", "Plastik baret, deri saplı kamçı, yağmur şemsiyesi, sentetik peruk",
                      "Sentetik peruk, plastik baret, yağmur şemsiyesi, deri saplı kamçı", "Plastik baret, yağmur şemsiyesi, deri saplı kamçı, sentetik peruk",
                      "Yağmur şemsiyesi, deri saplı kamçı, sentetik peruk, plastik baret"],
             answer="D", why="Plastik baret koruyucu başlık olarak 65.06, yağmur şemsiyesi 66.01, deri saplı kamçı bastonlarla birlikte 66.02, sentetik peruk 67.04. Kamçı, malzemesi ne olursa olsun 66.02'dedir (Fasıl 42 notları); plastik baret Fasıl 39'a girmez (Fasıl 39 Not 2).",
             ref="65.06 · 66.01 · 66.02 · 67.04", yt="Baret, şemsiye, kamçı, peruk: pozisyon numarasına göre sıralama."),
        dict(stem="Demir veya çelikten yapılmış aşağıdaki eşyadan hangisi 73.07 pozisyonunda, yani boru bağlantı parçaları arasında sınıflandırılmaz?",
             options=["Uç uca kaynak yapılacak dirsek", "Esnek hortumu sıkarak sabitleyen hortum kelepçesi", "Boruyu bir cihaza bağlayan flanş",
                      "İki farklı çaptaki boruyu birleştiren redüksiyon", "Borunun açık ucunu kapatan kör tapa"],
             answer="B", why="73.07 izahnamesi pozisyonu iki boruyu birleştiren, boruyu bir cihaza bağlayan ya da borunun ucunu kapatan parçalarla sınırlar. Hortum kelepçesi boruyla birleşmez, esnek hortumu sıkıp sabitler: 73.26. Kör tapa da bir boru bağlantı parçasıdır; boruyu duvara tutturan kanca ve destekler 73.07'de değildir.",
             ref="73.07 izahnamesi · 73.26", yt="Dirsek, flanş, redüksiyon, kör tapa, hortum kelepçesi: hangisi 73.07'de değil?"),
        dict(stem="Aşağıdaki adi metallerden hangisi için Armonize Sistemde ayrı bir fasıl açılmamıştır; bu metal ve ondan eşya 81. fasılda, diğer adi metaller arasında yer alır?",
             options=["Nikel", "Kurşun", "Çinko", "Kalay", "Kobalt"],
             answer="E", why="Bölüm XV'te kendi faslı olan adi metaller bakır (74), nikel (75), alüminyum (76), kurşun (78), çinko (79) ve kalaydır (80). Diğer adi metaller (tungsten, molibden, magnezyum, kobalt, titanyum vb.) Fasıl 81'dedir; kobalt 81.05. Fasıl 77 ileride kullanılmak üzere boş bırakılmıştır.",
             ref="Bölüm XV · Fasıl 81 · 81.05", yt="Nikel, kurşun, çinko, kalay, kobalt: hangisinin ayrı faslı yok?"),
        dict(stem="Aşağıdakilerden hangisi 84.28 pozisyonunda sınıflandırılmaz?",
             options=["Füniküler hattında kullanılan, kendinden hareketli olmayan yolcu vagonu", "Kayak merkezinde kullanılan telesiyej",
                      "Kayakçıları yamaç boyunca çeken teleski", "Füniküler hattının çekiş mekanizması ve bucurgatı",
                      "Alışveriş merkezinde kullanılan yürüyen merdiven"],
             answer="A", why="84.28 kaldırma ve taşıma makinelerini kapsar: teleferik, telesiyej, teleski ve füniküler çekiş mekanizmaları 8428.60, yürüyen merdivenler 8428.40. İzahnameye göre fünikülerde yalnız çekiş mekanizması ve bucurgat 84.28'dedir; vagonlar 86.05'te, raylar 73.02'de, teçhizat 86.08'de sınıflandırılır.",
             ref="84.28 izahnamesi · 8428.60 · 86.05", yt="Telesiyej, teleski, yürüyen merdiven, füniküler vagonu: hangisi 84.28'de değil?"),
        dict(stem="Bir torna tezgâhında iş parçasını mıknatıs gücüyle tutmaya yarayan elektromanyetik torna aynası, tezgâhtan ayrı olarak ithal ediliyor. Bu eşya hangi tarife pozisyonunda sınıflandırılır?",
             options=["84.58", "84.66", "85.05", "85.36", "85.43"], answer="C",
             why="85.05 pozisyon metni elektromanyetik veya daimi mıknatıslı aynaları, kıskaçları ve benzeri tespit tertibatını adıyla sayar. 84.66 tezgâhların iş tutucularını ve aynalarını kapsasa da izahname elektromanyetik aynaları dışarıda bırakıp 85.05'e gönderir. Elektromanyetik kavramalar, kaplinler ve frenler de 85.05'tedir.",
             ref="85.05 · 84.66 izahnamesi", yt="Elektromanyetik torna aynası: tezgâh aksesuarı 84.66 mı, 85.05 mi?"),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #11; 5 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/5 — pozisyon sırası (baret, şemsiye, kamçı, peruk); 5 sıralama şıkkı; 3 sn geri sayım.",
        s03="CEVAP D; sıralama zinciri 65.06 → 66.01 → 66.02 → 67.04; dört yanlış sıralamanın ✗ gerekçesi.",
        s04="TUZAK — Cano deri saplı kamçıyı saraciye sanar → HAYIR, 66.02; DİKKAT: plastik baret Fasıl 39 değil.",
        s05="SORU 2/5 — 73.07'de 'sınıflandırılmaz' altı çizili; 5 boru parçası şıkkı; 3 sn geri sayım.",
        s06="CEVAP B; yanlış kalem üstü çizili → DOĞRUSU 73.26; dört doğru şık (dirsek, flanş, redüksiyon, kör tapa) 73.07.",
        s07="TUZAK — Stajyer kör tapayı dışarıda sanar → HAYIR; DİKKAT: kanca ve destekler 73.07 değil; Gümrükçü Baba 'boruyla bütünleşiyor mu?'.",
        s08="SORU 3/5 — 'ayrı bir fasıl açılmamıştır' altı çizili; 5 metal şıkkı; 3 sn geri sayım.",
        s09="CEVAP E; kobalt kartı → kendi faslı olanlar, diğerleri, Fasıl 81 → 81.05; aday şeridi.",
        s10="TUZAK — Yardımcı kobaltın da faslı var sanır → HAYIR; DİKKAT: Fasıl 77 boş.",
        s11="SORU 4/5 — 84.28'de 'sınıflandırılmaz' altı çizili; 5 şık; 3 sn geri sayım.",
        s12="CEVAP A; füniküler vagonu üstü çizili → DOĞRUSU 86.05; telesiyej, teleski, çekiş mekanizması 8428.60 · yürüyen merdiven 8428.40.",
        s13="TUZAK — Stajyer telesiyeji spor eşyası sanar → HAYIR, 84.28; DİKKAT: raylar 73.02, teçhizat 86.08.",
        s14="SORU 5/5 — elektromanyetik torna aynası; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s15="CEVAP C; ayna kartı → 85.05 metni, 84.66 mı?, açıklama notu → 85.05; aday şeridi.",
        s16="TUZAK — Yardımcı tezgâh aksesuarı diye 84.66 → HAYIR, 85.05; DİKKAT: elektromanyetik kavrama/fren 85.05; Gümrükçü Baba 'mıknatısla mı tutuyor?'.",
        s17="İPUCU · Koçun notu — zihin haritası: eşyaya bak · notu oku · işleve bak.",
        s18="ÖNEMLİ · Cevap anahtarı D · B · E · A · C; 5 skor kutucuğu; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
