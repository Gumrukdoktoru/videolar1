"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 12
META = "DERS · <b>TARİFE #12</b> · 3 SORU · FASIL 9 · 85 · 87"
TITLE = "Tarife Dersi 12 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · PUL BİBER", ["s02", "s03", "s04"]), ("SORU 2 · GÜNEŞ PANELİ", ["s05", "s06", "s07"]),
    ("SORU 3 · İKİ TEKERLEK", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Pul biber 07.12 mi, 09.04 mü?", "Soru 2: Güneş paneli 85.01 mi, 85.41 mi?",
      "Soru 3: Hangisi 87.11'de değil? Motorsuz skuter", "Koçun notu", "Cevap anahtarı"]
KW = ["kurutulup", "açıklama notu", "Açıklama notuna", "adıyla", "baharat", "kuruysa", "tazeyse",
      "yarı iletken", "fotovoltaik jeneratör", "Tek başına", "Panelin yanında",
      "yardımcı motorlu", "tekerlekli oyuncaklar", "Motor var mı?",
      "A şıkkı", "B şıkkı", "C şıkkı", "D şıkkı", "E şıkkı", "dikkat:", "Hayır!"]


def cues(T):
    out = [("s01", 0.2, "neutral")]
    for q, s, t in (("s02", "s03", "s04"), ("s05", "s06", "s07"), ("s08", "s09", "s10")):
        out += [(q, 0.0, "soru"), (s, T(s, "Cevap"), "cevap"), (s, T(s, "Cevap") + 3.0, "neutral"), (t, 0.0, "tuzak"), (t, T(t, "dikkat"), "dikkat")]
    return out + [("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Pul biber, güneş paneli ve iki tekerlekli taşıtlar",
    message="Pul biber 09.04, 07.12 değil (C) · yalnız hücrelerden oluşan güneş paneli 85.41, 85.01 değil (D) · motorsuz skuter 95.03, 87.11'de değil (B).",
    intent="Bu derste 3 soru var. Ölçülen bilgi alanları: Fasıl 7 açıklama notunun kurutulmuş, ezilmiş veya öğütülmüş Capsicum ve Pimenta biberlerini Fasıl 9'a (09.04) göndermesi (taze biber 07.09, kuru sebze 07.12, hazır ürünler Fasıl 20); fotovoltaik hücrelerin modül veya panel hâlinde de 85.41'de kalması, 85.01'in yalnız akü, invertör gibi cihazlarla birleşik fotovoltaik jeneratörleri alması (fotovoltaik LED aydınlatma 94.05); 87.11'in kapsamı (yardımcı motorlu bisiklet, mopet, kendini dengeleyen elektrikli araç, motosiklet sepeti) ve motorsuz skuterin 95.03'e gitmesi.",
    team="Cano (biber sebzedir diye 07.12 → HAYIR, 09.04) · Yardımcı (panel elektrik üretiyor diye 85.01 → HAYIR, 85.41) ve Gümrükçü Baba (“panelin yanında başka ne var?”) · Stajyer (bisiklet bisiklettir diye 87.12 → HAYIR, 87.11) ve Gümrükçü Baba (“motor var mı?”).",
    visuals="ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), yanlış ifade + DOĞRUSU kartı + dört doğru şık, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: Fasıl 7 genel açıklamaları (Capsicum ve Pimenta cinsi kurutulmuş, ezilmiş veya öğütülmüş biberler Fasıl 9), 07.09, 07.12, 09.04, 20.05, 21.03; 85.01 izahnamesi (fotovoltaik jeneratörler: akü, invertör gibi cihazlarla birleşik ya da gücü doğrudan bir motora veren elemanlarla donatılmış paneller), 85.04, 85.07, 85.41 (fotovoltaik hücreler, modül veya panel hâlinde), 94.05; 87.11 ve izahnamesi (yardımcı motorlu bisikletler, mopetler, kendini dengeleyen iki tekerlekli elektrikli araçlar, motosiklet sepetleri), 87.12, 95.03 (tekerlekli oyuncaklar, motorsuz skuterler, çocuk üç tekerlekli bisikletleri).",
    yt_title="Pul Biber 07.12 mi 09.04 mü? · Güneş Paneli 85.01 mi 85.41 mi? · Motorsuz Skuter 87.11 mi? | Tarife Dersi #12 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin on ikincisinde 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, pul biber, 09.04, 07.12, Capsicum, güneş paneli, fotovoltaik, 85.41, 85.01, 87.11, yardımcı motorlu bisiklet, skuter, 95.03, 87.12, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Kurutulup pul hâlinde ezilmiş, başka hiçbir madde katılmamış kırmızı biber, yani pul biber, hangi tarife pozisyonunda sınıflandırılır?",
             options=["07.09", "07.12", "09.04", "20.05", "21.03"], answer="C",
             why="Pul biber, Capsicum cinsi kırmızı biberin kurutulup ezilmiş hâlidir. Fasıl 7 açıklama notu Capsicum ve Pimenta cinsi biberlerin kurutulmuş, ezilmiş veya öğütülmüş meyvelerini fasıl dışında bırakır; 09.04 bunları adıyla sayar. Taze biber 07.09'dadır; 07.12 bu biberleri hariç tutar; salça, turşu gibi hazır ürünler Fasıl 20'ye gider.",
             ref="Fasıl 7 açıklama notu · 09.04", yt="Pul biber: kurutulmuş sebze mi, baharat mı?"),
        dict(stem="Yalnızca birbirine bağlanmış güneş pillerinden oluşan; invertör, akü veya bir motoru doğrudan besleyen başka bir eleman içermeyen fotovoltaik güneş paneli hangi tarife pozisyonunda sınıflandırılır?",
             options=["85.01", "85.04", "85.07", "85.41", "94.05"], answer="D",
             why="Fotovoltaik hücreler modül veya panel hâlinde birleştirilmiş olsalar da yarı iletken cihaz olarak 85.41'dedir. 85.01 izahnamesi yalnız akü, invertör gibi cihazlarla birleştirilmiş ya da gücü doğrudan bir motora veren elemanlarla donatılmış panelleri fotovoltaik jeneratör sayar. Fotovoltaik LED aydınlatma cihazları 94.05'tedir.",
             ref="85.41 · 85.01 izahnamesi", yt="Güneş paneli: jeneratör mü, yarı iletken cihaz mı?"),
        dict(stem="Aşağıdakilerden hangisi 87.11 pozisyonunda sınıflandırılmaz?",
             options=["Pedal çevrildiğinde devreye giren, yardımcı elektrik motorlu bisiklet", "Ayakla itilerek ilerleyen, yetişkinlerin de kullanabildiği motorsuz skuter",
                      "Kendi kendini dengeleyen, tek kişilik, iki tekerlekli elektrikli nakil aracı", "Hem motoru hem pedalı bulunan mopet", "Motosiklete takılan yan sepet"],
             answer="B", why="87.11 motosikletleri ve yardımcı motorlu bisikletleri kapsar; izahnameye göre mopetler, kendini dengeleyen iki tekerlekli elektrikli araçlar ve motosiklet sepetleri de buradadır. Motorsuz, ayakla itilen skuterler yetişkinler için tasarlanmış olsa bile 95.03'te tekerlekli oyuncaklar arasındadır. Yardımcı motoru olan bisiklet, motoru elektrikli olsa da 87.12'ye değil 87.11'e girer.",
             ref="87.11 izahnamesi · 95.03", yt="Elektrikli bisiklet, mopet, skuter, sepet: hangisi 87.11'de değil?"),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #12; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — pul biber; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s03="CEVAP C; pul biber kartı → Capsicum, Fasıl 7 notu, 09.04 metni → 09.04; aday şeridi.",
        s04="TUZAK — Cano biber sebzedir diye 07.12 → HAYIR, 09.04; DİKKAT: salça, turşu Fasıl 20.",
        s05="SORU 2/3 — yalnız hücrelerden oluşan güneş paneli; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP D; panel kartı → fotovoltaik hücre, yarı iletken, 85.01 notu → 85.41; aday şeridi.",
        s07="TUZAK — Yardımcı elektrik üretiyor diye 85.01 → HAYIR, 85.41; DİKKAT: fotovoltaik LED aydınlatma 94.05; Gümrükçü Baba 'panelin yanında ne var?'.",
        s08="SORU 3/3 — 87.11'de 'sınıflandırılmaz' altı çizili; 5 taşıt şıkkı; 3 sn geri sayım.",
        s09="CEVAP B; motorsuz skuter üstü çizili → DOĞRUSU 95.03; dört doğru şık 87.11.",
        s10="TUZAK — Stajyer yardımcı motorlu bisikleti 87.12 sanır → HAYIR, 87.11; DİKKAT: çocuk üç tekerlekli bisikleti 95.03; Gümrükçü Baba 'motor var mı?'.",
        s11="İPUCU · Koçun notu — zihin haritası: kuru mu taze mi · panel mi jeneratör mü · motor var mı.",
        s12="ÖNEMLİ · Cevap anahtarı C · D · B; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
