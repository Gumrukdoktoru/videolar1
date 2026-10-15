"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 14
META = "DERS · <b>TARİFE #14</b> · 3 SORU · 84.19 · GYK 3 · SIRALAMA"
TITLE = "Tarife Dersi 14 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · LOKANTA SEMAVERİ", ["s02", "s03", "s04"]), ("SORU 2 · KALEM FENER", ["s05", "s06", "s07"]),
    ("SORU 3 · POZİSYON SIRASI", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Lokanta tipi elektrikli semaver 85.16 mı, 84.19 mu?", "Soru 2: Kalem fener — hangi kural, hangi pozisyon?",
      "Soru 3: Erişte, kolonya, plastik şişe, kâğıt torba — pozisyon sırası", "Koçun notu", "Cevap anahtarı"]
KW = ["ilk bakışta", "açıklama notu", "evlerde kullanılmayan", "lokantalarda", "ısıtma ve pişirme", "Evde mi", "lokantada mı",
      "eşit derecede özel", "esas nitelik", "numara sırasına göre en son", "sıra atlanmaz",
      "makarnadır", "tuvalet suyudur", "plastik eşyadır", "kâğıttan önce", "Önce faslı bul",
      "A şıkkı", "B şıkkı", "C şıkkı", "D şıkkı", "E şıkkı", "dikkat:", "Hayır!"]


def cues(T):
    out = [("s01", 0.2, "neutral")]
    for q, s, t in (("s02", "s03", "s04"), ("s05", "s06", "s07"), ("s08", "s09", "s10")):
        out += [(q, 0.0, "soru"), (s, T(s, "Cevap"), "cevap"), (s, T(s, "Cevap") + 3.0, "neutral"), (t, 0.0, "tuzak"), (t, T(t, "dikkat"), "dikkat")]
    return out + [("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Lokanta tipi semaver, kalem fener ve pozisyon sırası",
    message="Lokanta tipi elektrikli çay semaveri 84.19, 85.16 değil (A) · kalem fener esas nitelik belirlenemezse GYK 3(c) ile 96.08 (D) · erişte 19.02 → kolonya 33.03 → plastik şişe 39.23 → kâğıt torba 48.19 (E).",
    intent="Bu derste 3 soru var. Ölçülen bilgi alanları: 85.16 izahnamesinin lokantalarda kullanılan tezgâh tipi perkolatörleri, çay ve süt semaverlerini ve normalde evlerde kullanılmayan elektrotermik cihazları 84.19'a göndermesi (restoran tipi mikrodalga 85.14); iki ayrı pozisyondaki eşyanın birleşiminde GYK 3(a) → 3(b) → 3(c) sırası, esas nitelik belirlenemezse numara sırasına göre en son pozisyon (tükenmez kalem 96.08, portatif lamba 85.13); sıralama sorusunda faslı bulup dizme (19.02 makarnalar, 33.03 tuvalet suları, 39.23 plastik ambalaj eşyası, 48.19 kâğıt torbalar; kolonya Fasıl 22 değil).",
    team="Cano (elektrikli ısıtıcı ev aletidir diye 85.16 → HAYIR, 84.19) · Yardımcı (ışık veren kısım daha önemli diye 85.13 → HAYIR, GYK 3(c), 96.08) ve Gümrükçü Baba (“önce 3(a), sonra 3(b), en son 3(c)”) · Stajyer (ambalajlar en sona kalır diye torbayı şişeden önce koyar → HAYIR) ve Gümrükçü Baba (“önce faslı bul, sonra sırala”).",
    visuals="ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), sıralama zinciri (4 eşya kartı) + dört yanlış sıralamanın ✗ gerekçesi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: 85.16 izahnamesi (lokantalarda kullanılan tezgâh tipi kahve perkolatörleri, çay ve süt semaverleri ile normalde evlerde kullanılmayan elektrotermik cihazlar 84.19; restoran tipi mikrodalga fırınlar 85.14), 84.19 (ısıtma ve pişirme cihazları), 85.43, 94.03; Genel Yorum Kuralları 1, 3(a), 3(b), 3(c); 85.13 (kendi enerji kaynağı olan portatif lambalar), 96.08 (tükenmez kalemler); 19.02 (makarnalar), 33.03 (parfümler ve tuvalet suları), 39.23 (eşya taşıma veya ambalajlamaya mahsus plastik eşya), 48.19 (kâğıttan torbalar), Fasıl 22.",
    yt_title="Lokanta Semaveri 85.16 mı 84.19 mu? · Kalem Fener GYK 3(c) · Erişte, Kolonya, Şişe, Torba Sırası | Tarife Dersi #14 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin on dördüncüsünde 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, semaver, 84.19, 85.16, 85.14, genel yorum kuralları, GYK 3(c), kalem fener, 96.08, 85.13, pozisyon sırası, 19.02, 33.03, kolonya, 39.23, 48.19, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Bir lokantanın mutfağında kullanılmak üzere ithal edilen, tezgâh tipi, elektrikle ısıtılan büyük çay semaveri hangi tarife pozisyonunda sınıflandırılır?",
             options=["84.19", "85.14", "85.16", "85.43", "94.03"], answer="A",
             why="85.16 ev tipi elektrotermik cihazları kapsar; izahnamesi lokantalarda kullanılan tezgâh tipi kahve perkolatörlerini, çay ve süt semaverlerini ve normalde evlerde kullanılmayan diğer elektrotermik cihazları pozisyon dışında bırakır. Bunlar 84.19'da ısıtma ve pişirme cihazları arasındadır. Evde kullanılan küçük semaver 85.16'da kalır; restoran tipi mikrodalga fırın 85.14'tedir.",
             ref="85.16 izahnamesi · 84.19", yt="Elektrikli semaver: ev aleti mi, lokanta cihazı mı?"),
        dict(stem="Bir ucunda tükenmez kalem, diğer ucunda pille çalışan küçük bir LED el feneri bulunan kalem fener, perakende satışa sunuluyor. Eşyanın esas niteliğinin belirlenemediği kabul edilirse, hangi kurala göre hangi pozisyonda sınıflandırılır?",
             options=["85.13 · GYK 1", "85.13 · GYK 3(b)", "96.08 · GYK 3(a)", "96.08 · GYK 3(c)", "Ayrı ayrı · GYK 1"], answer="D",
             why="Kalem fener iki ayrı pozisyondaki eşyanın birleşimidir: tükenmez kalem 96.08, kendi pili olan portatif el feneri 85.13. GYK 3(a)'ya göre iki pozisyon da eşyanın yalnız bir kısmını tanımladığından eşit derecede özeldir; GYK 3(b) ile esas nitelik aranır ama belirlenemiyor; GYK 3(c) ile numara sırasına göre en son pozisyon, 96.08 seçilir. Eşya tek parça olduğundan ayrı ayrı sınıflandırılmaz.",
             ref="GYK 3(a) · 3(b) · 3(c)", yt="Kalem fener: GYK 3(c) ile en son pozisyon."),
        dict(stem="Aşağıdakilerden hangisinde eşyalar, tarife cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru sıralanmıştır?",
             options=["Kolonya, yumurtalı erişte, plastik su şişesi, kâğıt alışveriş torbası", "Yumurtalı erişte, kolonya, kâğıt alışveriş torbası, plastik su şişesi",
                      "Plastik su şişesi, kolonya, yumurtalı erişte, kâğıt alışveriş torbası", "Yumurtalı erişte, plastik su şişesi, kolonya, kâğıt alışveriş torbası",
                      "Yumurtalı erişte, kolonya, plastik su şişesi, kâğıt alışveriş torbası"], answer="E",
             why="Yumurtalı erişte makarna olarak 19.02, kolonya tuvalet suyu olarak 33.03 (alkol içerse de Fasıl 22 değil), plastik su şişesi ambalaj eşyası olarak 39.23, kâğıt alışveriş torbası 48.19. Plastik (Fasıl 39) kâğıttan (Fasıl 48) önce gelir.",
             ref="19.02 · 33.03 · 39.23 · 48.19", yt="Erişte, kolonya, plastik şişe, kâğıt torba: pozisyon sırası."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #14; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — lokanta tipi elektrikli çay semaveri; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s03="CEVAP A; semaver kartı → akla gelen 85.16, 85.16 notu, 84.19 → 84.19; aday şeridi.",
        s04="TUZAK — Cano elektrikli ısıtıcıyı ev aleti sanır, 85.16 → HAYIR, 84.19; DİKKAT: restoran mikrodalgası 85.14.",
        s05="SORU 2/3 — kalem fener, esas nitelik belirlenemiyor; 5 kural + pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP D; kalem fener kartı → GYK 3(a), 3(b), 3(c) → 96.08; aday şeridi.",
        s07="TUZAK — Yardımcı ışık veren kısım önemli diye 85.13 → HAYIR, GYK 3(c); DİKKAT: sıra atlanmaz; Gümrükçü Baba 'önce 3(a), sonra 3(b), en son 3(c)'.",
        s08="SORU 3/3 — pozisyon sırası (erişte, kolonya, plastik şişe, kâğıt torba); 5 sıralama şıkkı; 3 sn geri sayım.",
        s09="CEVAP E; sıralama zinciri 19.02 → 33.03 → 39.23 → 48.19; dört yanlış sıralamanın ✗ gerekçesi.",
        s10="TUZAK — Stajyer ambalajları sona koyar → HAYIR, plastik kâğıttan önce; DİKKAT: kolonya 33.03; Gümrükçü Baba 'önce faslı bul, sonra sırala'.",
        s11="İPUCU · Koçun notu — zihin haritası: ev mi lokanta mı · kural 3 sırası · önce fasıl.",
        s12="ÖNEMLİ · Cevap anahtarı A · D · E; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
