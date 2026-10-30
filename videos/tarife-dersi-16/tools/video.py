"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 16
META = "DERS · <b>TARİFE #16</b> · 3 SORU · FASIL 84 · 29 · 30"
TITLE = "Tarife Dersi 16 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · SATIŞ OTOMATI", ["s02", "s03", "s04"]), ("SORU 2 · KRİKO", ["s05", "s06", "s07"]),
    ("SORU 3 · ASPİRİN", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Hangisi 84.76'da değil? Ödeme almayan içecek makinesi", "Soru 2: Araba krikosu 87.08 mi, 84.25 mi?",
      "Soru 3: Saf aspirin etken maddesi hangi fasılda?", "Koçun notu", "Cevap anahtarı"]
KW = ["otomatik satış", "esas işlev satıştır", "ödemeyi kabul edecek", "Para alıyor mu?",
      "ağır yük kaldırıcısıdır", "adıyla", "taşıt parçası", "Makine mi", "parça mı",
      "izole edilmiş", "organik bileşiktir", "safsızlık", "açıklama notunda", "Saf mı", "karışım mı", "doz mu",
      "A şıkkı", "B şıkkı", "C şıkkı", "D şıkkı", "E şıkkı", "dikkat:", "Hayır!"]


def cues(T):
    out = [("s01", 0.2, "neutral")]
    for q, s, t in (("s02", "s03", "s04"), ("s05", "s06", "s07"), ("s08", "s09", "s10")):
        out += [(q, 0.0, "soru"), (s, T(s, "Cevap"), "cevap"), (s, T(s, "Cevap") + 3.0, "neutral"), (t, 0.0, "tuzak"), (t, T(t, "dikkat"), "dikkat")]
    return out + [("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Satış otomatları, araba krikosu ve aspirin",
    message="Ödeme tertibatı olmayan sıcak içecek makinesi 84.19, 84.76'da değil (E) · portatif hidrolik kriko 84.25, 87.08 değil (B) · saf o-asetilsalisilik asit 29.18, diğerleri Fasıl 30 (A).",
    intent="Bu derste 3 soru var. Ölçülen bilgi alanları: 84.76 otomatik satış makinelerinin kapsamı (para bozma makineleri dahil, ısıtma-soğutma veya hazırlama tertibatı sonucu değiştirmez; ödemeyi kabul edecek tertibatı olmayan sıcak veya soğuk içecek verme makineleri 84.19); krikoların 84.25'te adıyla yer alması ve Bölüm XVII Not 2(e) ile 84.01–84.79 makinelerinin taşıt aksam ve parçası sayılmaması (82.05 başka yerde yer almayan el aletleri); Fasıl 29 Not 1 ile kimyaca belirli izole organik bileşiklerin Fasıl 29'da (2918.22 o-asetilsalisilik asit), dolgu maddeli karışımların, tıbbi bitki karışımlarının ve tıbbi tuzların 30.03'te, dozlandırılmış ilaçların 30.04'te yer alması.",
    team="Stajyer (soğutucusu var diye otomatı 84.18 sanır → HAYIR, 84.76) ve Gümrükçü Baba (“para alıyor mu?”) · Cano (kriko arabayla kullanılır diye 87.08 → HAYIR, 84.25) · Yardımcı (bitki karışımını ilaç saymaz → HAYIR, 30.03) ve Gümrükçü Baba (“saf mı, karışım mı, doz mu?”).",
    visuals="yanlış ifade + DOĞRUSU kartı + dört doğru şık (iki soruda), ürün kartı + 3 adımlı gerekçe + 5 aday şeridi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: 84.76 ve izahnamesi (8476.21 ısıtma veya soğutma tertibatı olanlar; posta pulu, tren bileti vb. otomatlar; para bozma makineleri dahil; ödemeyi kabul edecek tertibatı olmayan sıcak veya soğuk içecek verme makineleri hariç, 84.19), 84.18, 84.19; 84.25 (krikolar) ve izahnamesi (otomobiller için portatif krikolar), 82.05, 84.28, 84.79, 87.08, Bölüm XVII Not 2(e); Fasıl 29 Not 1(a), 2918.22 (o-asetilsalisilik asit, tuzları ve esterleri), 30.03 ve izahnamesi (dolgu maddeli müstahzarlar, 12.11 bitkilerinin tıbbi karışımları, tabii mineral sularından elde edilen tıbbi tuzlar), 30.04.",
    yt_title="Otomat 84.76 mı 84.19 mu? · Araba Krikosu 84.25 · Saf Aspirin 29.18 | Tarife Dersi #16 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin on altıncısında 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, 84.76, satış otomatı, para bozma makinesi, 84.19, 84.18, kriko, 84.25, 87.08, Bölüm XVII Not 2, aspirin, o-asetilsalisilik asit, 29.18, 30.03, 30.04, Fasıl 29 Not 1, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Aşağıdakilerden hangisi 84.76 pozisyonunda sınıflandırılmaz?",
             options=["Bozuk para veya kartla çalışan, soğutma tertibatlı kutu içecek satış otomatı", "Para bozma makinesi",
                      "Jetonla çalışan tren bileti satış makinesi", "Jetonla çalışan, kahve ve süt karıştırıcısı olan sıcak içecek otomatı",
                      "Ödeme tertibatı olmayan, ofislerde kullanılan sıcak içecek verme makinesi"],
             answer="E", why="84.76 otomatik satış makinelerinin pozisyonudur; posta pulu, tren bileti, yiyecek ve içecek otomatları ve izahnameye göre para bozma makineleri de buradadır. Isıtma, soğutma ya da kahve-süt karıştırma tertibatı sonucu değiştirmez (8476.21). Ödemeyi kabul edecek tertibatı olmayan sıcak veya soğuk içecek verme makineleri ise izahnamede pozisyon dışında bırakılır: 84.19.",
             ref="84.76 izahnamesi · 84.19", yt="Satış otomatları: hangisi 84.76'da değil?"),
        dict(stem="Otomobilin lastiğini değiştirmek için kullanılan, elle çalıştırılan portatif hidrolik kriko hangi tarife pozisyonunda sınıflandırılır?",
             options=["82.05", "84.25", "84.28", "84.79", "87.08"], answer="B",
             why="84.25 krikoları adıyla sayar; izahnamesi otomobiller için portatif krikoları da bu pozisyona koyar. Bölüm XVII Not 2(e), 84.01–84.79 pozisyonlarına giren makineleri taşıt aksam ve parçası saymadığından 87.08'e girmez. 82.05 tarifenin başka yerinde yer almayan el aletleri içindir.",
             ref="84.25 · Bölüm XVII Not 2(e)", yt="Araba krikosu: taşıt parçası mı, 84.25 mi?"),
        dict(stem="Aşağıdakilerden hangisi tarife cetvelinde diğerlerinden farklı bir fasılda sınıflandırılır?",
             options=["Hiçbir maddeyle karıştırılmamış, dökme hâldeki saf o-asetilsalisilik asit", "Bir dolgu maddesiyle karıştırılmış, dozlandırılmamış, dökme aspirin",
                      "Dozlandırılmış, perakende satışa hazır aspirin tabletleri", "Tabii maden sularının buharlaştırılmasıyla elde edilen tıbbi tuzlar",
                      "Dökme hâlde, tıbbi amaçla karıştırılmış şifalı bitkiler"], answer="A",
             why="Saf o-asetilsalisilik asit kimyaca belirli, izole bir organik bileşiktir; Fasıl 29 Not 1 ile Fasıl 29'da, 2918.22'de yer alır. Dolgu maddeli dökme aspirin, tıbbi bitki karışımları ve maden sularından elde edilen tıbbi tuzlar 30.03'te (izahnamede adıyla), dozlandırılmış aspirin tabletleri 30.04'tedir.",
             ref="Fasıl 29 Not 1 · 2918.22 · 30.03 izahnamesi", yt="Aspirin: saf etken madde Fasıl 29, ilaç Fasıl 30."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #16; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — 84.76'da 'sınıflandırılmaz' altı çizili; 5 makine şıkkı; 3 sn geri sayım.",
        s03="CEVAP E; ödemesiz içecek makinesi üstü çizili → DOĞRUSU 84.19; dört doğru şık 84.76.",
        s04="TUZAK — Stajyer soğutmalı otomatı 84.18 sanır → HAYIR, 84.76; DİKKAT: ödemesiz sıcak içecek makinesi 84.19; Gümrükçü Baba 'para alıyor mu?'.",
        s05="SORU 2/3 — portatif hidrolik kriko; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP B; kriko kartı → 84.25 metni, açıklama notu, Bölüm XVII Not 2 → 84.25; aday şeridi.",
        s07="TUZAK — Cano krikoyu araba parçası sanır, 87.08 → HAYIR, 84.25; DİKKAT: taşıttaki pompa ve kompresörler de Fasıl 84.",
        s08="SORU 3/3 — 'farklı' altı çizili; saf etken madde, karışım, tablet, tıbbi tuz, bitki karışımı; 3 sn geri sayım.",
        s09="CEVAP A; 'saf madde → Fasıl 30' üstü çizili → DOĞRUSU 29.18; dört eşya Fasıl 30.",
        s10="TUZAK — Yardımcı bitki karışımını ilaç saymaz → HAYIR, 30.03; DİKKAT: dozlandırılınca 30.04; Gümrükçü Baba 'saf mı, karışım mı, doz mu?'.",
        s11="İPUCU · Koçun notu — zihin haritası: para alıyor mu · taşıt parçası mı · saf mı karışım mı.",
        s12="ÖNEMLİ · Cevap anahtarı E · B · A; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
