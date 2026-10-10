"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 4
META = "DERS · <b>TARİFE #4</b> · ÇAKMAK TAŞI, KONTEYNER, ALKOLSÜZ İÇECEK"
TITLE = "Tarife Dersi 4 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · ÇAKMAK TAŞI", ["s02", "s03", "s04"]), ("SORU 2 · KONTEYNER", ["s05", "s06", "s07"]),
    ("SORU 3 · ALKOLSÜZ BİRA", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Ferroseryum çakmak taşı hangi pozisyonda?", "Soru 2: Alüminyum yalıtımlı konteyner hangi pozisyonda?",
      "Soru 3: %0,4 alkollü malt içeceği hangi pozisyonda?", "Koçun notu", "Cevap anahtarı"]
KW = [r"hariç", r"Ferroseryum", r"ferroseryum", r"piroforik", r"çakmak taşları", r"İsme değil", r"kartuşu", r"konteynerleri", r"işlevine",
      r"yalıtımlı", r"madde önemli değil", r"tank konteynerler", r"alkolsüz içecek", r"alkolsüz biralar", r"sınırın altında", r"Sınır değerini",
      r"A şıkkı", r"B şıkkı", r"C şıkkı", r"D şıkkı", r"E şıkkı", r"Dikkat:", r"dikkat:", r"Hayır!"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s03", T("s03", "Cevap"), "cevap"), ("s03", T("s03", "hariç"), "dikkat"),
            ("s03", T("s03", "Ferroseryum"), "neutral"), ("s04", 0.0, "tuzak"), ("s04", T("s04", "dikkat"), "dikkat"), ("s05", 0.0, "soru"),
            ("s06", T("s06", "Cevap"), "cevap"), ("s06", T("s06", "Yapıldığı"), "neutral"), ("s07", 0.0, "tuzak"), ("s07", T("s07", "Dikkat"), "uyari"),
            ("s08", 0.0, "soru"), ("s09", T("s09", "Cevap"), "cevap"), ("s09", T("s09", "Yirmi"), "neutral"), ("s09", T("s09", "sınırın"), "dikkat"),
            ("s10", 0.0, "tuzak"), ("s11", 0.0, "neutral"), ("s11", T("s11", "Üç"), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Çakmak taşı, konteyner, alkolsüz içecek",
    message="Çakmak taşı 36.06 (D) · yalıtımlı taşıma konteyneri 86.09 (A) · %0,4 alkollü malt içeceği 22.02 (C).",
    intent="Ölçülen bilgi alanları: çakmaklar ve çakmak taşlarının yeri (96.13 / 36.06), taşıma konteynerleri (86.09) ve alkolsüz içecek sınırı (Fasıl 22 Not 3).",
    team="Cano (adında ferro var → 72.02 → HAYIR) · Yardımcı (alüminyum → 76.11 → HAYIR) · Stajyer (bira yazıyor → 22.03 → HAYIR) ve Gümrükçü Baba (“≤ %0,5 → 22.02, üstü → 22.03”).",
    visuals="sınıflandırma yolu (ürün kartı → 3 adım → pozisyon) ve beş aday pozisyonun ✓/✗ şeridi, tuzak karşılaştırma kartları (≠), DİKKAT/UYARI kartları (çakmak aksamı kartuş 96.13 · ≤300 cm³ çakmak gazı 3606.10, tank konteyner şartı, 20 °C ölçüm), koçun notu zihin haritası, cevap anahtarı",
    sources="96.13 pozisyon metni (çakmak taşları ve fitilleri hariç), 36.06 pozisyon metni ve izahnamesi (ferroseryum ve piroforik alaşımlar; ≤300 cm³ kaplarda çakmak yakıtı 3606.10; çakmak aksamı kartuşlar 96.13), 86.09 pozisyon metni ve izahnamesi (yalıtımlı konteynerler; sıvı konteynerlerinin şartı), Fasıl 22 Not 2–3 (20 °C; alkolsüz ≤ %0,5) ve 2202.91 (alkolsüz biralar).",
    yt_title="Çakmak Taşı (36.06), Taşıma Konteyneri (86.09), Alkolsüz Bira (22.02) | Tarife Dersi #4 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin dördüncüsünde yine 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, 36.06, çakmak taşı, 96.13, 86.09, konteyner, 22.02, alkolsüz bira, Fasıl 22 notu, GTİP, gümrük müşavirliği sınavı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Çakmaklarda kullanılmak üzere küçük silindirler hâlinde hazırlanmış, ferroseryum alaşımından çakmak taşları hangi tarife pozisyonunda sınıflandırılır?",
             options=["96.13", "28.46", "72.02", "36.06", "38.24"], answer="D",
             why="96.13 çakmakları ve aksamını kapsar ama çakmak taşları ve fitilleri hariç tutar. Ferroseryum ve diğer piroforik alaşımlar her şekilde 36.06'dadır. Adındaki 'ferro' 72.02'ye götürmez.",
             ref="96.13 ve 36.06 pozisyon metinleri", yt="Ferroseryum çakmak taşı: 96.13 mü, 72.02 mi, 36.06 mı? Pozisyon metnindeki 'hariç' ifadesi."),
        dict(stem="Alüminyumdan yapılmış, kara ve hava yoluyla taşımaya göre özel olarak donatılmış, kancaları ve küçük tekerlekleri bulunan, bozulabilir gıdalar için yalıtımlı konteyner hangi tarife pozisyonunda sınıflandırılır?",
             options=["86.09", "76.11", "76.12", "84.18", "87.16"], answer="A",
             why="86.09 bir veya daha fazla taşıma şekline göre yapılmış ve donatılmış konteynerleri, yapıldığı maddeye bakmaksızın kapsar; izahname yalıtımlı konteynerleri sayar. Tank konteynerler ancak taşıta göre yapılıp bağlanıyorsa 86.09'dadır.",
             ref="86.09 izahnamesi", yt="Alüminyum yalıtımlı konteyner: 76.11 mi 86.09 mu? Konteyner işlevle tanınır."),
        dict(stem="Hacmen %0,4 alkol içeren, maltlı alkolsüz bira hangi tarife pozisyonunda sınıflandırılır?",
             options=["22.03", "22.06", "22.02", "22.01", "20.09"], answer="C",
             why="Fasıl 22 Not 3'e göre alkolsüz içecek, hacmen alkol derecesi %0,5'i geçmeyen içecektir (20 °C'de). %0,4 alkollü malt içeceği 22.02'de (2202.91 alkolsüz biralar); %0,5'in üstü 22.03.",
             ref="Fasıl 22 Not 3, 2202.91", yt="%0,4 alkollü 'alkolsüz bira': 22.02 mi 22.03 mü? Sınır %0,5."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #4; 3 konu kartı; ekip tanıtımı.",
        s02="SORU 1/3 — ferroseryum çakmak taşı; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s03="CEVAP D; 96.13 değil (taşlar hariç) → piroforik alaşım → her şekilde → 36.06; 5 aday ✓/✗.",
        s04="TUZAK — Cano 'adında ferro var' → 72.02 → HAYIR; DİKKAT: aksam kartuş 96.13 · ≤300 cm³ çakmak gazı 3606.10.",
        s05="SORU 2/3 — alüminyum, yalıtımlı taşıma konteyneri; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP A; pozisyon metni → madde önemsiz → izahname → 86.09; 5 aday ✓/✗.",
        s07="TUZAK — Yardımcı 76.11 der → HAYIR; DİKKAT: tank konteyner şartı.",
        s08="SORU 3/3 — %0,4 alkollü malt içeceği; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s09="CEVAP C; Fasıl 22 Not 3 → %0,4 < %0,5 → 2202.91 → 22.02; 5 aday ✓/✗.",
        s10="TUZAK — Stajyer 22.03 der → Gümrükçü Baba '≤ %0,5 → 22.02'; UYARI: 20 °C'de ölçüm.",
        s11="İPUCU · Koçun notu — zihin haritası: hariç'e bak · işlev > madde · sayısal sınır.",
        s12="ÖNEMLİ · Cevap anahtarı D · A · C; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
