"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 9
META = "DERS · <b>TARİFE #9</b> · TAŞIT, BASTON, CONTA"
TITLE = "Tarife Dersi 9 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · 87.03 / 87.05", ["s02", "s03", "s04"]), ("SORU 2 · SİLAHLI BASTON", ["s05", "s06", "s07"]),
    ("SORU 3 · KAUÇUK CONTA", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Hangi taşıt çifti farklı pozisyonda?", "Soru 2: Kurşunlu baston hangi fasılda?",
      "Soru 3: Kauçuk motor contası hangi pozisyonda?", "Koçun notu", "Cevap anahtarı"]
KW = [r"insan taşımaya mahsus", r"özel amaçlı", r"hizmeti?", r"aynı pozisyondadır", r"insan taşır", r"adıyla",
      r"fasıl dışında", r"silah niteliği", r"silahlar faslında", r"dışarıda", r"ölçü işaretleri", r"bölüm dışında",
      r"motor aksamına", r"artık pozisyonu", r"takım hâlinde", r"A şıkkı", r"B şıkkı", r"C şıkkı", r"D şıkkı", r"E şıkkı",
      r"dikkat:", r"Hayır!"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s03", T("s03", "Cevap"), "cevap"), ("s03", T("s03", "İtfaiye"), "dikkat"),
            ("s03", T("s03", "Diğer"), "neutral"), ("s04", 0.0, "tuzak"), ("s04", T("s04", "dikkat"), "dikkat"), ("s05", 0.0, "soru"),
            ("s06", T("s06", "Cevap"), "cevap"), ("s06", T("s06", "Bu"), "dikkat"), ("s06", T("s06", "Diğer"), "neutral"),
            ("s07", 0.0, "tuzak"), ("s07", T("s07", "dikkat"), "dikkat"), ("s08", 0.0, "soru"), ("s09", T("s09", "Cevap"), "cevap"),
            ("s09", T("s09", "Bu"), "dikkat"), ("s09", T("s09", "Doğru"), "neutral"), ("s10", 0.0, "tuzak"),
            ("s10", T("s10", "dikkat"), "uyari"), ("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Özel amaçlı taşıtlar, silahlı bastonlar ve kauçuk contalar",
    message="Ambulans 87.03, itfaiye aracı 87.05 (A) · kurşunlu baston Fasıl 66 Not 1 ile Fasıl 93 (D) · vulkanize kauçuk motor contası 40.16 (C).",
    intent="Ölçülen bilgi alanları: 87.03 (esas itibarıyla insan taşımak üzere imal edilmiş taşıtlar) ile 87.05 (özel amaçlı taşıtlar) ayrımı, Fasıl 66 Not 1 hariç tutmaları (silahlı bastonlar Fasıl 93, ölçü gösteren bastonlar 90.17) ve Bölüm XVI Not 1 gereği sertleştirilmemiş vulkanize kauçuktan teknik eşyanın 40.16’da sınıflandırılması.",
    team="Cano (golf arabası spor malzemesidir diye 95.06 → HAYIR, 87.03) · Stajyer (baston bastondur diye 66.02 → HAYIR, Fasıl 93) ve Gümrükçü Baba (“bastonun içinde ne var”) · Yardımcı (motordan söküldü diye 84.09 → HAYIR, 40.16).",
    visuals="yanlış çiftin üstü çizilip DOĞRUSU kartı + diğer dört çiftin pozisyonları, ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (doğru olan yeşil), tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: 87.03 pozisyon metni ve açıklama notu (ambulans, cenaze arabası, hapishane minibüsü, motorlu karavan, golf arabası, taksi ve binek otomobilleri), 87.05 pozisyon metni ve açıklama notu (kurtarıcı, vinçli, itfaiye, beton mikser kamyonları gibi özel amaçlı taşıtlar; motorlu karavan hariç), 95.06 spor eşyası; Fasıl 66 Not 1 (a) ölçü gösteren bastonlar 90.17, (b) tüfekli, kılıçlı, kurşunlu bastonlar Fasıl 93; 66.02 bastonlar, 44.04 baston taslakları; Bölüm XVI Not 1(a) (sertleştirilmemiş vulkanize kauçuktan teknik eşya 40.16), Bölüm XVII Not 2(a), 40.16 (contalar), 40.17 (sert kauçuk), 84.84 (farklı malzemeden contaların poşette takımları), 84.09 ve 87.08 aksam pozisyonları.",
    yt_title="Ambulans 87.03 mü? Kurşunlu Baston Fasıl 93 mü? Kauçuk Conta 40.16 mı? | Tarife Dersi #9 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin dokuzuncusunda yine 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, 87.03, 87.05, ambulans, itfaiye aracı, golf arabası, Fasıl 66, Fasıl 93, kurşunlu baston, kılıçlı baston, 40.16, conta, vulkanize kauçuk, 84.84, Bölüm XVI Not 1, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Aşağıdaki taşıt çiftlerinden hangisinde iki taşıt farklı tarife pozisyonlarında sınıflandırılır?",
             options=["Ambulans – İtfaiye aracı", "Cenaze arabası – Taksi", "Golf arabası – Motorlu karavan",
                      "Beton mikser kamyonu – Vinçli kurtarıcı", "Hapishane minibüsü – Binek otomobili"],
             answer="A", why="Ambulans insan taşımaya mahsus taşıt olarak 87.03’tedir; itfaiye aracı ise yangın söndürme hizmeti için donatılmış özel amaçlı taşıt olarak 87.05’tedir. Cenaze arabası, taksi, golf arabası, motorlu karavan, hapishane minibüsü ve binek otomobili 87.03’te; beton mikser ve vinçli kurtarıcı 87.05’tedir.",
             ref="87.03 ve 87.05 açıklama notları", yt="Ambulans, itfaiye, golf arabası: hangi çift farklı pozisyonda? İnsan mı taşıyor, hizmet mi veriyor?"),
        dict(stem="İçine kurşun doldurularak ağırlaştırılmış, savunma amacıyla da kullanılabilen yürüyüş bastonu tarife cetvelinin hangi faslında sınıflandırılır?",
             options=["66", "95", "90", "93", "44"], answer="D",
             why="Fasıl 66 Not 1, tüfekli, kılıçlı ve kurşunlu bastonları fasıl dışında bırakıp Fasıl 93’e gönderir. Ölçü gösteren bastonlar 90.17’de, spor sopaları 95.06’da, ahşap baston taslakları 44.04’tedir.",
             ref="Fasıl 66 Not 1", yt="Baston bastondur mu? Silahlı ve ölçülü bastonların tarifedeki yeri."),
        dict(stem="Bir otomobil motoruna ait, sertleştirilmemiş vulkanize kauçuktan yapılmış subap kapağı contası hangi tarife pozisyonunda sınıflandırılır?",
             options=["84.09", "87.08", "40.16", "84.84", "40.17"], answer="C",
             why="Bölüm XVI Not 1, sertleştirilmemiş vulkanize kauçuktan teknik eşyayı bölüm dışında bırakıp 40.16’ya gönderir; bu yüzden conta motora ait olsa da 84.09’a ya da 87.08’e girmez. Sert kauçuk olmadığı için 40.17 de değildir. Farklı malzemeden contaların poşette takımı ise 84.84’tedir.",
             ref="Bölüm XVI Not 1 · 40.16", yt="Motordan sökülen kauçuk conta motor aksamı mı? 40.16 ve 84.84 ayrımı."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #9; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — farklı pozisyondaki taşıt çifti; 'farklı' altı çizili; 5 çift şık; 3 sn geri sayım.",
        s03="CEVAP A; ambulans – itfaiye 'aynı pozisyon' üstü çizilir, DOĞRUSU 87.03 ≠ 87.05; diğer dört çift ✓.",
        s04="TUZAK — Cano golf arabasını spor eşyası sanar → HAYIR; 95.06 ≠ 87.03 kartları; DİKKAT: ambulans 87.03, itfaiye 87.05.",
        s05="SORU 2/3 — kurşunlu baston hangi fasılda; 5 fasıl şıkkı; 3 sn geri sayım.",
        s06="CEVAP D; baston kartı → Fasıl 66 Not 1, baston faslı değil, silah niteliği → Fasıl 93; aday şeridi 66 · 95 · 90 · 93 ✓ · 44.",
        s07="TUZAK — Stajyer 'baston bastondur' diye 66.02 → HAYIR; DİKKAT: ölçü gösteren baston 90.17; Gümrükçü Baba 'içinde ne var'.",
        s08="SORU 3/3 — vulkanize kauçuk subap kapağı contası; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s09="CEVAP C; conta kartı → Bölüm XVI Not 1, aksam pozisyonu değil, sert kauçuk değil → 40.16; aday şeridi.",
        s10="TUZAK — Yardımcı motor aksamı 84.09 der → HAYIR; DİKKAT: farklı malzemeden conta takımı 84.84.",
        s11="İPUCU · Koçun notu — zihin haritası: 87.03 / 87.05 · baston · kauçuk conta.",
        s12="ÖNEMLİ · Cevap anahtarı A · D · C; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
