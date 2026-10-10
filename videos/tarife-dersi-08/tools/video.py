"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 8
META = "DERS · <b>TARİFE #8</b> · TUZ, NOTLAR, BAĞLAYICILIK"
TITLE = "Tarife Dersi 8 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · 25.01 KAPSAMI", ["s02", "s03", "s04"]), ("SORU 2 · CETVEL NOTLARI", ["s05", "s06", "s07"]),
    ("SORU 3 · BAĞLAYICI KAYNAKLAR", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Hangisi 25.01’de sınıflandırılmaz?", "Soru 2: Hangi not Armonize Sistemde yer almaz?",
      "Soru 3: Hangisi bağlayıcı bir kaynak değildir?", "Koçun notu", "Cevap anahtarı"]
KW = [r"tuzun pozisyonu\w*", r"fasıl dışında", r"Damıtılmış su", r"adına", r"Ek notlar", r"ek notlar", r"Kombine Nomanklatür\w*",
      r"ortaktır", r"Armonize Sistemindir", r"yardımcı bir referans", r"bağlayıcılığı yoktur", r"bağlayıcıdır", r"yol gösterir",
      r"tek başına", r"A şıkkı", r"B şıkkı", r"C şıkkı", r"D şıkkı", r"E şıkkı", r"dikkat:", r"Hayır!"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s03", T("s03", "Cevap"), "cevap"), ("s03", T("s03", "Yirmi", 3), "neutral"),
            ("s03", T("s03", "Pozisyon"), "dikkat"), ("s04", 0.0, "tuzak"), ("s04", T("s04", "dikkat"), "dikkat"), ("s05", 0.0, "soru"),
            ("s06", T("s06", "Cevap"), "cevap"), ("s06", T("s06", "Bölüm"), "neutral"), ("s07", 0.0, "tuzak"),
            ("s07", T("s07", "dikkat"), "dikkat"), ("s08", 0.0, "soru"), ("s09", T("s09", "Cevap"), "cevap"),
            ("s09", T("s09", "Gümrükler"), "dikkat"), ("s09", T("s09", "Diğerleri"), "neutral"), ("s10", 0.0, "tuzak"),
            ("s10", T("s10", "dikkat"), "uyari"), ("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Tuz ve deniz suyu, cetvel notları ve bağlayıcı kaynaklar",
    message="Maden suyu 22.01, 25.01 değil (A) · ek notlar Armonize Sistemde yok, KN ve ulusal tarifeye ait (C) · AB BTB’leri yalnız yardımcı referans (E).",
    intent="Ölçülen bilgi alanları: 25.01 pozisyonunun kapsamı (sofra ve denatüre tuz, saf sodyum klorür, deniz suyu; Fasıl 22 Not 1’in hariç tutmaları), tarife cetvelindeki not türlerinin hangi düzeye ait olduğu (bölüm, fasıl ve alt pozisyon notları Armonize Sistem; ek notlar Kombine Nomanklatür ve ulusal) ve tarife sınıflandırmasında bağlayıcı kaynaklar (AB BTB’lerinin yalnız yardımcı referans olması).",
    team="Cano (deniz suyu da sudur diye Fasıl 22 → HAYIR, 25.01) · Stajyer (alt pozisyonu ulusal açılım sanır → HAYIR, 6 haneli alt pozisyon Armonize Sistemin) ve Gümrükçü Baba (“notun hangi haneyi yorumladığına bak”) · Yardımcı (AB BTB’sine dayanarak sınıflandırır → HAYIR, yardımcı referans).",
    visuals="yanlış şıkkın üstü çizilip DOĞRUSU kartı + diğer dört şıkkın ✓ ve dayanakları, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı",
    sources="Gümrük Tarife Cetveli: 25.01 pozisyon metni (sofra tuzu ve denatüre tuz dahil tuz, saf sodyum klorür, sulu çözelti hâlinde olsun olmasın veya topaklaşmayı önleyici ya da akışkanlığı sağlayıcı madde katılmış olsun olmasın; deniz suyu), 22.01 (maden suları ve gazlı sular), Fasıl 22 Not 1(b) deniz suyu 25.01 ve Not 1(c) damıtılmış ve iletken su 28.53; Armonize Sistemin bölüm, fasıl ve alt pozisyon notları ile genel yorum kuralları, Kombine Nomanklatür ve ulusal tarifeye ait ek notlar; Gümrükler Genel Müdürlüğünün 23.03.2020 tarihli ve 53410847 sayılı yazısı (AB BTB’leri ülkemiz mevzuatında yardımcı bir referans kaynak olarak kullanılır, resmî bağlayıcılığı yoktur), Gümrük Genel Tebliği (Gümrük Tarife Cetveli İzahnamesi) ve Gümrük Genel Tebliğleri (Tarife-Sınıflandırma Kararları), 4458 sayılı Gümrük Kanunu md. 8 (BTB).",
    yt_title="Deniz Suyu 25.01 mi? Ek Notlar Armonize Sistemde mi? AB BTB Bağlayıcı mı? | Tarife Dersi #8 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin sekizincisinde yine 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, 25.01, tuz, deniz suyu, maden suyu, 22.01, ek notlar, alt pozisyon notları, Armonize Sistem, Kombine Nomanklatür, BTB, AB BTB, bağlayıcı tarife bilgisi, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Aşağıdakilerden hangisi 25.01 pozisyonunda sınıflandırılmaz?",
             options=["Gazlı doğal maden suyu", "Deniz suyu", "Saf sodyum klorür", "Denatüre tuz",
                      "Topaklaşmayı önleyici madde katılmış sofra tuzu"],
             answer="A", why="Maden suları ve gazlı sular 22.01’dedir. 25.01 pozisyon metni sofra tuzu ve denatüre tuz dahil tuzu, saf sodyum klorürü ve deniz suyunu adıyla sayar; topaklaşmayı önleyici madde katılmasına da izin verir. Deniz suyu Fasıl 22 Not 1(b) ile Fasıl 22 dışındadır; damıtılmış su ise Not 1(c) ile 28.53’tedir.",
             ref="25.01 pozisyon metni · Fasıl 22 Not 1", yt="Deniz suyu, saf sodyum klorür, maden suyu: hangisi 25.01’de değil?"),
        dict(stem="Türk Gümrük Tarife Cetvelinde yer alan aşağıdaki unsurlardan hangisi Armonize Sistem Nomanklatüründe yer almaz?",
             options=["Bölüm notları", "Fasıl notları", "Ek notlar", "Alt pozisyon notları", "Tarifenin yorumuna ilişkin genel kurallar"], answer="C",
             why="Bölüm, fasıl ve alt pozisyon notları ile genel yorum kuralları Armonize Sistemin parçasıdır ve bütün üye ülkelerde ortaktır. Ek notlar ise Kombine Nomanklatüre ve ulusal tarifeye aittir; 6 haneden sonraki ayrıntıyı yorumlar.",
             ref="Armonize Sistem Nomanklatürü · Kombine Nomanklatür", yt="Bölüm notu, alt pozisyon notu, ek not: hangisi Armonize Sistemde yok?"),
        dict(stem="Türkiye’de tarife sınıflandırması yapılırken aşağıdakilerden hangisi bağlayıcı bir kaynak değildir?",
             options=["Türk Gümrük Tarife Cetveli", "Tarifenin yorumuna ilişkin genel kurallar",
                      "Gümrük Genel Tebliği ile yayımlanan Gümrük Tarife Cetveli İzahnamesi",
                      "Gümrük Genel Tebliği ile yayımlanan tarife sınıflandırma kararları",
                      "AB Bağlayıcı Tarife Bilgisi veri tabanındaki kararlar"], answer="E",
             why="Gümrükler Genel Müdürlüğünün 2020 tarihli yazısına göre AB BTB’leri ülkemiz mevzuatında yalnızca yardımcı bir referans kaynaktır; resmî bağlayıcılığı yoktur. Tarife cetveli ve genel yorum kuralları cetvelin kendisidir; izahname ve sınıflandırma kararları Gümrük Genel Tebliği olarak yayımlanır.",
             ref="GGM yazısı, 23.03.2020 · Gümrük Genel Tebliğleri", yt="AB BTB’si bağlar mı? Tarife sınıflandırmasında bağlayıcı kaynaklar."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #8; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — 25.01’de sınıflandırılmayan; 'sınıflandırılmaz' altı çizili; 5 şık; 3 sn geri sayım.",
        s03="CEVAP A; maden suyu → 25.01 üstü çizilir, DOĞRUSU 22.01; diğer dört şık 25.01 dayanaklarıyla ✓.",
        s04="TUZAK — Cano 'deniz suyu da su' diye B → HAYIR; 22.01 ≠ 25.01 kartları; DİKKAT: damıtılmış su 28.53.",
        s05="SORU 2/3 — Armonize Sistemde yer almayan unsur; 'yer almaz' altı çizili; 5 şık; 3 sn geri sayım.",
        s06="CEVAP C; ek notlar → AS üstü çizilir, DOĞRUSU KN + ulusal; diğer dört not türü AS ✓.",
        s07="TUZAK — Stajyer alt pozisyonu ulusal sanır → HAYIR; DİKKAT: ek notlar 8+ hane; Gümrükçü Baba 'hangi haneyi yorumluyor'.",
        s08="SORU 3/3 — bağlayıcı olmayan kaynak; 'değildir' altı çizili; 5 şık; 3 sn geri sayım.",
        s09="CEVAP E; AB BTB → bağlayıcı üstü çizilir, DOĞRUSU yardımcı referans (GGM 2020); diğer dört kaynak ✓.",
        s10="TUZAK — Yardımcı AB BTB’sine dayanır → HAYIR; DİKKAT: Türkiye’de verilen BTB idareyi hak sahibine karşı bağlar.",
        s11="İPUCU · Koçun notu — zihin haritası: 25.01 · notlar · bağlayıcılık.",
        s12="ÖNEMLİ · Cevap anahtarı A · C · E; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
