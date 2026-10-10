"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 5
META = "DERS · <b>TARİFE #5</b> · MUM, KUMANDA, DERİ EŞYA"
TITLE = "Tarife Dersi 5 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · MİNERAL MUMLAR", ["s02", "s03", "s04"]), ("SORU 2 · TELSİZ KUMANDA", ["s05", "s06", "s07"]),
    ("SORU 3 · 42.02 KAPSAMI", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Mikrokristal petrol mumu hangi pozisyonda?", "Soru 2: Vinç için telsiz kumanda hangi pozisyonda?",
      "Soru 3: Hangisi 42.02'de sınıflandırılmaz?", "Koçun notu", "Cevap anahtarı"]
KW = [r"mineral mumlar", r"Mineral kökenli", r"mineral kökenli", r"suni mumlar", r"perakende", r"kozmetik", r"telsiz", r"radyo dalgalarıyla",
      r"kendi pozisyonu", r"kendi pozisyonlarında", r"kızılötesi", r"giyim aksesuarıdır", r"giyim eşyası", r"Birinci gruptaki", r"İkinci gruptaki",
      r"Ahşaptan mücevher kutusu", r"madde şartı", r"A şıkkı", r"B şıkkı", r"C şıkkı", r"D şıkkı", r"E şıkkı", r"dikkat:", r"Hayır!"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s03", T("s03", "Cevap"), "cevap"), ("s03", T("s03", "Bunlar"), "neutral"),
            ("s03", T("s03", "Yani"), "dikkat"), ("s04", 0.0, "tuzak"), ("s04", T("s04", "dikkat"), "dikkat"), ("s05", 0.0, "soru"),
            ("s06", T("s06", "Cevap"), "cevap"), ("s06", T("s06", "Bu"), "neutral"), ("s06", T("s06", "Vince"), "dikkat"), ("s07", 0.0, "tuzak"),
            ("s08", 0.0, "soru"), ("s09", T("s09", "Cevap"), "cevap"), ("s09", T("s09", "Birinci"), "neutral"), ("s09", T("s09", "İkinci"), "dikkat"),
            ("s10", 0.0, "tuzak"), ("s11", 0.0, "neutral"), ("s11", T("s11", "Üç"), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Mineral mumlar, telsiz kumanda, deri eşya",
    message="Mikrokristal petrol mumu 27.12 (B) · vinç için telsiz kumanda 85.26 (E) · deri bel kemeri 42.02 değil (C).",
    intent="Ölçülen bilgi alanları: mineral mumlar ve vazelin (27.12), telsiz uzaktan kumanda cihazları (85.26) ve 42.02 pozisyonunun kapsamı.",
    team="Stajyer (mum → 34.04 → HAYIR) · Yardımcı (vinç aksamı 84.31 → HAYIR) ve Gümrükçü Baba (“TV'nin kızılötesi kumandası 85.43”) · Cano (deriyse 42.02 → HAYIR).",
    visuals="sınıflandırma yolu (ürün kartı → 3 adım → pozisyon), beş aday pozisyonun ✓/✗ şeridi, 'hangisi sınıflandırılmaz' çözümünde üstü çizilen şık + DOĞRUSU kartı + diğer şıkların grup etiketleri, tuzak karşılaştırma kartları (≠), DİKKAT kartları (perakende vazelin 33.04, TV kızılötesi kumanda 85.43, ahşap mücevher kutusu 44.20), koçun notu zihin haritası, cevap anahtarı",
    sources="27.12 pozisyon metni ve izahnamesi (vazelin, parafin, mikrokristal petrol mumu…; perakende cilt bakımı vazelini hariç → 33.04), 34.04 ve 15.21 pozisyon metinleri, 85.26 pozisyon metni (8526.92 uzaktan kumanda etmeye mahsus telsiz cihazları), Bölüm XVI Not 2(a), Fasıl 85 Not 10 (TV kızılötesi kumandaları 85.43), 42.02 pozisyon metni (iki grup), 4203.30 (bel kemerleri), 44.20 (ahşap mücevher kutuları).",
    yt_title="Mikrokristal Mum (27.12), Telsiz Kumanda (85.26), 42.02'nin Kapsamı | Tarife Dersi #5 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin beşincisinde yine 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, 27.12, vazelin, parafin, 85.26, telsiz kumanda, Bölüm XVI notu, 42.02, 42.03, deri eşya, GTİP, gümrük müşavirliği sınavı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Petrolden elde edilen, mikrokristal bünyeli petrol mumu hangi tarife pozisyonunda sınıflandırılır?",
             options=["34.04", "27.12", "15.21", "27.10", "33.04"], answer="B",
             why="27.12 vazelin, parafin, mikrokristal bünyeli petrol mumu ve diğer mineral mumları adıyla sayar (renklendirilmiş olsun olmasın). 34.04 suni ve müstahzar mumlar içindir; cilt bakımı için perakende vazelin 33.04.",
             ref="27.12 pozisyon metni", yt="Mikrokristal petrol mumu: 34.04 mü 27.12 mi? Mumun kaynağı belirleyici."),
        dict(stem="Radyo frekansıyla çalışan ve bir kule vincinin hareketlerini uzaktan kontrol etmeye yarayan telsiz kumanda cihazı hangi tarife pozisyonunda sınıflandırılır?",
             options=["85.43", "84.31", "85.37", "85.17", "85.26"], answer="E",
             why="85.26 uzaktan kumanda etmeye mahsus telsiz kontrol cihazlarını kapsar (8526.92). Bölüm XVI Not 2(a) gereği kendi pozisyonu olan aksam, ait olduğu makineye bakılmadan kendi pozisyonunda sınıflandırılır. TV kızılötesi kumandaları 85.43.",
             ref="85.26, Bölüm XVI Not 2(a)", yt="Vinç için telsiz kumanda: 84.31 aksam mı, 85.26 mı? Kendi pozisyonu olan parça kendine gider."),
        dict(stem="Aşağıdakilerden hangisi 42.02 pozisyonunda sınıflandırılmaz?",
             options=["Dış yüzü dokumaya elverişli maddeden sırt çantası", "Alüminyumdan yapılmış, tekerlekli valiz", "Tabii deriden bel kemeri",
                      "Vulkanize liften evrak çantası", "Plastik madde yaprağından tuvalet çantası"], answer="C",
             why="42.02'nin birinci grubu (bavul, valiz, evrak/okul çantası, gözlük kılıfı…) her maddeden olabilir; ikinci grubu (seyahat, sırt, tuvalet çantaları, cüzdan, mücevher kutusu…) yalnızca deri, plastik yaprak, tekstil, vulkanize lif veya kartondan. Deri bel kemeri giyim aksesuarıdır: 42.03 (4203.30). Ahşap mücevher kutusu 44.20.",
             ref="42.02 pozisyon metni, 4203.30", yt="Hangisi 42.02'de sınıflandırılmaz? 42.02'nin iki grubu ve deri bel kemeri."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #5; 3 konu kartı; ekip tanıtımı.",
        s02="SORU 1/3 — mikrokristal petrol mumu; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s03="CEVAP B; pozisyon metni → mineral kaynak → renk önemsiz → 27.12; 5 aday ✓/✗.",
        s04="TUZAK — Stajyer 34.04 der → HAYIR; DİKKAT: perakende cilt bakımı vazelini 33.04.",
        s05="SORU 2/3 — kule vinci telsiz kumandası; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP E; pozisyon metni → telsiz → Bölüm XVI Not 2(a) → 85.26; 5 aday ✓/✗.",
        s07="TUZAK — Yardımcı 84.31 der → Gümrükçü Baba: TV kızılötesi kumandası 85.43.",
        s08="SORU 3/3 — hangisi 42.02'de sınıflandırılmaz; DİKKAT · dikkatli oku!; 3 sn geri sayım.",
        s09="CEVAP C; 'deri bel kemeri' üstü çizilir, DOĞRUSU 42.03; diğer şıklar 1./2. grup etiketleriyle ✓.",
        s10="TUZAK — Cano 'deriyse 42.02' der → HAYIR; DİKKAT: ahşap mücevher kutusu 44.20.",
        s11="İPUCU · Koçun notu — zihin haritası: mumun kaynağı · kendi pozisyonu · 42.02'nin iki grubu.",
        s12="ÖNEMLİ · Cevap anahtarı B · E · C; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
