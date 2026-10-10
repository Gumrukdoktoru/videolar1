"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 4
META = "DERS · <b>VERGİ HESAPLAMA #4</b> · İLAVE GV &amp; MİN–MAX"
TITLE = "Vergi Hesaplama Dersi 4 — Gümrük Koçu"
QUIZ = ["s02", "s03"]
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU & ŞIKLAR", ["s02", "s03"]), ("ANAHTAR KURAL", ["s04"]),
    ("ADIM ADIM ÇÖZÜM", ["s05", "s06", "s07", "s08"]), ("TUZAKLAR", ["s09"]), ("UYARI", ["s10"]),
    ("KOÇUN NOTU", ["s11"]), ("ÖZET", ["s12"]),
]
YT = ["Giriş", "Soru ve şıklar", "Üç anahtar: matrah, min–max, KDV", "Adım adım çözüm", "Tuzak şıklar",
      "Uyarı: sınırlar toplanmaz, karşılaştırılır", "Koçun notu: koridor kuralı", "Özet"]
KW = [r"ilave gümrük vergisi", r"İlave gümrük vergisi", r"ilave gümrük vergisinin", r"İlave gümrük vergisinin", r"ilave gümrük vergisini",
      r"İlave gümrük vergisini", r"nispi", r"Nispi", r"en az tutar", r"en az", r"en çok tutar", r"en çok", r"En az", r"En çok",
      r"KDV matrahına", r"KDV matrahı", r"gümrük kıymetidir", r"karşılaştırılır", r"toplanmaz", r"koridor", r"koridorun",
      r"C şıkkı", r"A şıkkına", r"B şıkkına", r"D şıkkına", r"E şıkkına", r"tuzaklara", r"dur!", r"brüt", r"net"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s04", T("s04", "anahtarı"), "dikkat"), ("s05", 0.0, "neutral"),
            ("s05", T("s05", "dur"), "dikkat"), ("s06", 0.0, "neutral"), ("s06", T("s06", "altında"), "uyari"), ("s07", 0.0, "neutral"),
            ("s08", 0.0, "neutral"), ("s08", T("s08", "Doğru"), "cevap"), ("s09", 0.0, "tuzak"), ("s10", T("s10", "uyarı"), "uyari"),
            ("s11", 0.0, "neutral"), ("s11", T("s11", "Formülü"), "dikkat"), ("s12", 0.0, "neutral"), ("s12", T("s12", "C"), "cevap")]


DOC = dict(
    title="İlave gümrük vergisi: nispi tutar ve en az / en çok sınırı",
    short="İGV min–max",
    question=("K firması, Çin menşeli 4.000 kg plastik mutfak eşyası ithal ediyor. CIF kıymet 16.000 $. GV %10; İGV %30, ancak kg başına "
              "en az 1,5 $, en çok 2,5 $; KDV %20. Ödenecek GV + İGV + KDV toplamı kaç $?"),
    options=[("A", "10.880 $"), ("B", "11.120 $"), ("C", "12.320 $"), ("D", "17.120 $"), ("E", "18.080 $")], answer="C",
    solution=["GV: 16.000 × %10 = 1.600 $ · İGV nispi: 16.000 × %30 = 4.800 $",
              "En az: 4.000 × 1,5 = 6.000 $ · en çok: 4.000 × 2,5 = 10.000 $ → nispi en azın altında → İGV = 6.000 $",
              "KDV: (16.000 + 1.600 + 6.000) × %20 = 4.720 $ → toplam 1.600 + 6.000 + 4.720 = 12.320 $"],
    distractors="A 10.880 (min karşılaştırması yapılmadı, nispi yazıldı), B 11.120 (İGV KDV matrahına eklenmedi), D 17.120 (en çok tutar uygulandı), E 18.080 (nispi + en az toplandı).",
    guests="Cano — K firması temsilcisi (“Yüzde otuz yeter, değil mi?”, “Nispi ile en azı toplayalım mı?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)",
    extras="min–max koridor çubukları (EN AZ / NİSPİ / EN ÇOK, uygulanan tutar vurgusu), sayaçlı hesap satırları, çözüm defteri, ödeme fişi, dört çeldirici analizi, min–max kural kartı, brüt/net ağırlık uyarısı, 5 adımlı formül zinciri, 5 sn geri sayım",
    sources="Gümrük vergileri hesaplama sırası ve matrah kademeleri (GV/İGV matrahı = CIF + yurt dışı giderler; KDV matrahı = kıymet + ithalatta alınan vergiler, KDV K. md. 21), İGV nispi–maktu (min–max) karşılaştırma kuralı (Gümrük Koçu ders notu).",
    yt_title="İlave Gümrük Vergisi Min–Max Hesabı: Nispi mi, En Az Tutar mı? | Vergi Hesaplama Dersi #4 | Gümrük Koçu",
    yt_intro="Vergi hesaplama derslerinin dördüncüsünde ilave gümrük vergisinin nispi tutarını kilogram başına en az ve en çok tutarla karşılaştırıyoruz. Soruyu okuyoruz, 5 saniye düşünme süresi veriyoruz, sonra adım adım çözüp tuzak şıkları tek tek açıklıyoruz.",
    tags="gümrük vergisi hesaplama, ilave gümrük vergisi, İGV, min max, nispi vergi, maktu vergi, KDV matrahı, gümrük kıymeti, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, Gümrük Koçu",
    hashtags="#gümrük #vergihesaplama #İGV #GümrükKoçu",
    scenes=dict(
        s01="Logo sting → VERGİ HESAPLAMA · DERS #4; konu kartı (nispi %30, en az, en çok, KDV matrahı) + TUZAK rozeti.",
        s02="Soru verileri: K firması (Çin, 4.000 kg, CIF 16.000 $); oran kartları GV %10 · İGV %30 · en az 1,5 $/kg · en çok 2,5 $/kg · KDV %20; Cano “Yüzde otuz yeter, değil mi?”",
        s03="Beş şık (10.880 · 11.120 · 12.320 · 17.120 · 18.080 $) + 5 sn geri sayım halkası.",
        s04="ÖNEMLİ · 3 anahtar: matrah = gümrük kıymeti · önce nispi sonra min–max · KDV en son.",
        s05="Adım 1: GV 1.600 $ · nispi İGV 4.800 $ (sayaçlı) + çözüm defteri; DİKKAT “dur!”.",
        s06="Adım 2: en az 6.000 $, en çok 10.000 $; koridor çubukları → UYGULANAN: EN AZ; İGV = 6.000 $.",
        s07="Adım 3: KDV matrahı 23.600 $ → KDV 4.720 $; defter tamamlanır.",
        s08="Ödeme fişi: 1.600 + 6.000 + 4.720 = 12.320 $; doğru şık C yeşil + CEVAP: C damgası.",
        s09="TUZAK · dört çeldirici kartı (A nispi, B İGV KDV dışı, D en çok, E nispi + en az) + Gümrükçü Baba.",
        s10="UYARI · min–max kural kartı (aralıkta / altında / üstünde) + brüt–net ağırlık paneli; Cano “toplayalım mı?” → HAYIR!",
        s11="İPUCU · Koçun notu: koridor kuralı + “Toplanmaz, karşılaştırılır” + 5 adımlı formül zinciri.",
        s12="Özet: İGV en az tutar · GV + KDV · cevap C 12.320 $; abone ol / paylaş; logo.",
    ),
)
