"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 17
META = "DERS · <b>TARİFE #17</b> · 3 SORU · FASIL 15 · 34 · 95 · SIRALAMA"
TITLE = "Tarife Dersi 17 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · HİNT YAĞI", ["s02", "s03", "s04"]), ("SORU 2 · PORSELEN BEBEK", ["s05", "s06", "s07"]),
    ("SORU 3 · POZİSYON SIRASI", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Sülfonlanmış hint yağı 15.18 mi, 34.02 mi?", "Soru 2: Porselen salon bebeği 69.13 mü, 95.03 mü?",
      "Soru 3: Kondanse süt, yemek çubuğu, bisiklet pompası, para sayma makinesi — pozisyon sırası", "Koçun notu", "Cevap anahtarı"]
KW = ["yüzey aktif", "sülfonatlı yağları", "adıyla", "aynı şey değildir", "artık yağ değil",
      "salon bebekleri", "dekoratif amaçlı", "Bebekse", "biblosa",
      "hava pompasıdır", "büro makinesi", "taşıt parçası saymaz", "Makineyse",
      "A şıkkı", "B şıkkı", "C şıkkı", "D şıkkı", "E şıkkı", "dikkat:", "Hayır!"]


def cues(T):
    out = [("s01", 0.2, "neutral")]
    for q, s, t in (("s02", "s03", "s04"), ("s05", "s06", "s07"), ("s08", "s09", "s10")):
        out += [(q, 0.0, "soru"), (s, T(s, "Cevap"), "cevap"), (s, T(s, "Cevap") + 3.0, "neutral"), (t, 0.0, "tuzak"), (t, T(t, "dikkat"), "dikkat")]
    return out + [("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Sülfonlanmış hint yağı, porselen salon bebeği ve pozisyon sırası",
    message="Sülfonlanmış hint yağı 34.02, 15.18 değil (D) · porselen salon bebeği 95.03, 69.13 değil (C) · kondanse süt 04.02 → bambu yemek çubuğu 44.19 → bisiklet pompası 84.14 → para sayma makinesi 84.72 (B).",
    intent="Bu derste 3 soru var. Ölçülen bilgi alanları: Fasıl 15 Not 1 ve 15.18 izahnamesi ile sülfonlanmış yağların 34.02'ye gitmesi (kükürtlenmiş yağlar ≠ sülfonlanmış yağlar, işlem görmemiş hint yağı 15.15); 95.03 izahnamesinin salon ve maskot bebekleri gibi dekoratif yapma bebekleri de kapsaması, bebeklerin seramikten de yapılabilmesi ve Fasıl 69 Not 2(k) ile Fasıl 95 eşyasının hariç tutulması (vitrin mankeni 96.18, seramik süs eşyası 69.13); sıralama sorusunda faslı bulup dizme (04.02 konsantre ve şekerli süt, 4419.12 Çin usulü yemek çubukları, 8414.20 el veya ayakla çalışan hava pompaları — Bölüm XVII Not 2(e) ile 87.14 değil, 84.72 para ayırma, sayma veya paketleme makineleri — 84.70 değil).",
    team="Yardımcı (15.18 metninde kükürtlenmiş yazıyor diye 15.18 → HAYIR, 34.02) · Cano (çocuk oynamıyor diye süs eşyası 69.13 → HAYIR, 95.03) · Stajyer (bisiklet pompasını 87.14 sanıp sona koyar → HAYIR, 84.14) ve Gümrükçü Baba (“makineyse önce 84'e bak”).",
    visuals="ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), sıralama zinciri (4 eşya kartı) + dört yanlış sıralamanın ✗ gerekçesi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: Fasıl 15 Not 1 (sülfonatlı sıvı yağlar hariç), 15.15, 15.16, 15.18 ve izahnamesi (sülfonlanmış yağlar 34.02), 34.02 (yüzey aktif organik maddeler), 38.23; 95.03 izahnamesi (salon bebekleri, maskot bebekler; seramikten bebekler), Fasıl 69 Not 2(k), 69.11, 69.13, 96.18, 97.03; 04.02, 4419.12 (Çin usulü yemek çubukları), 8414.20 (el veya ayakla çalıştırılan hava pompaları), Bölüm XVII Not 2(e), 87.14, 84.70, 84.72 (para ayırma, sayma veya paketleme makineleri).",
    yt_title="Sülfonlanmış Hint Yağı 34.02 · Porselen Salon Bebeği 95.03 · Kondanse Süt, Çubuk, Pompa, Para Sayma Sırası | Tarife Dersi #17 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin on yedincisinde 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, hint yağı, sülfonlanmış yağ, Türk kırmızısı yağı, 34.02, 15.18, 15.15, salon bebeği, porselen bebek, 95.03, 69.13, Fasıl 69 Not 2, pozisyon sırası, 04.02, 44.19, 84.14, 84.72, 87.14, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Sülfürik asitle muamele edilerek sülfonlanmış hint yağı, yani Türk kırmızısı yağı, hangi tarife pozisyonunda sınıflandırılır?",
             options=["15.15", "15.16", "15.18", "34.02", "38.23"], answer="D",
             why="Hint yağı bitkisel sabit yağ olarak 15.15'tedir. Fasıl 15 Not 1 sülfonatlı sıvı yağları fasıl dışında bırakır; 15.18 izahnamesi de sülfonlanmış yağları (sülfürik asitle muamele edilmiş sıvı yağlar) adıyla 34.02'ye gönderir. 15.18 metnindeki 'kükürtlenmiş' yağlar sülfonlanmış yağlarla aynı şey değildir.",
             ref="Fasıl 15 Not 1 · 15.18 izahnamesi · 34.02", yt="Sülfonlanmış hint yağı: işlem görmüş yağ mı, yüzey aktif madde mi?"),
        dict(stem="Çocukların oynaması için değil, süs amacıyla yapılmış, giydirilmiş porselen salon bebeği hangi tarife pozisyonunda sınıflandırılır?",
             options=["69.11", "69.13", "95.03", "96.18", "97.03"], answer="C",
             why="95.03 izahnamesi yalnız çocukların eğlenmesine mahsus bebekleri değil, salon bebekleri ve maskot bebekler gibi dekoratif amaçlı yapma bebekleri de kapsar ve bebeklerin seramikten yapılabileceğini belirtir. Fasıl 69 Not 2(k) Fasıl 95 eşyasını hariç tutar. Seramikten bir hayvan biblosu 69.13'e, vitrin mankeni 96.18'e gider.",
             ref="95.03 izahnamesi · Fasıl 69 Not 2(k)", yt="Porselen salon bebeği: süs eşyası mı, 95.03 mü?"),
        dict(stem="Aşağıdakilerden hangisinde eşyalar, tarife cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru sıralanmıştır?",
             options=["Bambu yemek çubuğu, şekerli kondanse süt, ayakla çalışan bisiklet pompası, para sayma makinesi",
                      "Şekerli kondanse süt, bambu yemek çubuğu, ayakla çalışan bisiklet pompası, para sayma makinesi",
                      "Şekerli kondanse süt, bambu yemek çubuğu, para sayma makinesi, ayakla çalışan bisiklet pompası",
                      "Şekerli kondanse süt, ayakla çalışan bisiklet pompası, bambu yemek çubuğu, para sayma makinesi",
                      "Para sayma makinesi, şekerli kondanse süt, bambu yemek çubuğu, ayakla çalışan bisiklet pompası"], answer="B",
             why="Şekerli kondanse süt 04.02, bambudan Çin usulü yemek çubukları 44.19 (4419.12), ayakla çalışan bisiklet pompası el veya ayakla çalışan hava pompası olarak 84.14 (8414.20), para sayma makinesi 84.72. Bölüm XVII Not 2(e) 84.01–84.79 makinelerini taşıt parçası saymadığından pompa 87.14'e girmez; para sayma makinesi 84.70 (hesap makineleri) değil 84.72'dir.",
             ref="04.02 · 4419.12 · 8414.20 · 84.72", yt="Kondanse süt, yemek çubuğu, bisiklet pompası, para sayma makinesi: pozisyon sırası."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #17; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — sülfonlanmış hint yağı; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s03="CEVAP D; hint yağı kartı → sabit yağ 15.15, Fasıl 15 Not 1, 15.18 notu → 34.02; aday şeridi.",
        s04="TUZAK — Yardımcı 'kükürtlenmiş' kelimesine bakıp 15.18 → HAYIR, 34.02; DİKKAT: işlem görmemiş hint yağı 15.15.",
        s05="SORU 2/3 — porselen salon bebeği; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP C; bebek kartı → akla gelen 69.13, 95.03 notu, Fasıl 69 Not 2 → 95.03; aday şeridi.",
        s07="TUZAK — Cano süs eşyası diye 69.13 → HAYIR, 95.03; DİKKAT: seramik hayvan biblosu 69.13.",
        s08="SORU 3/3 — pozisyon sırası (kondanse süt, yemek çubuğu, bisiklet pompası, para sayma makinesi); 5 sıralama şıkkı; 3 sn geri sayım.",
        s09="CEVAP B; sıralama zinciri 04.02 → 44.19 → 84.14 → 84.72; dört yanlış sıralamanın ✗ gerekçesi.",
        s10="TUZAK — Stajyer pompayı 87.14 sanıp sona koyar → HAYIR, 84.14; DİKKAT: para sayma 84.72, 84.70 değil; Gümrükçü Baba 'makineyse önce 84'e bak'.",
        s11="İPUCU · Koçun notu — zihin haritası: sülfonlama · bebek = 95.03 · makine → 84.",
        s12="ÖNEMLİ · Cevap anahtarı D · C · B; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
