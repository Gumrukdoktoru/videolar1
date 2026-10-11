"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 10
META = "DERS · <b>VERGİ HESAPLAMA #10</b> · ÖTV · BİRA VE ŞARAP"
TITLE = "Vergi Hesaplama Dersi 10 — Gümrük Koçu"
QUIZ = ["s02", "s03"]
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU & ŞIKLAR", ["s02", "s03"]), ("ANAHTAR KURAL", ["s04"]),
    ("ADIM ADIM ÇÖZÜM", ["s05", "s06", "s07", "s08"]), ("TUZAKLAR", ["s09"]), ("UYARI", ["s10"]),
    ("KOÇUN NOTU", ["s11"]), ("ÖZET", ["s12"]),
]
YT = ['Giriş', 'Soru ve şıklar', 'Üç anahtar: yüksek olan, içkiye göre formül, cl → litre', 'Adım adım çözüm', 'Tuzak şıklar', 'Uyarı: asgari maktu formülü içkiye göre değişir', 'Koçun notu: bu hangi içki?', 'Özet']
KW = ['nispi vergi', 'Nispi vergi', 'asgari maktu', 'Asgari maktu', 'yüksek olanı', 'hangisi yüksekse', 'Hangisi yüksekse', 'alkol derecesi', 'derece', 'çarpılmaz',
      'Santilitreyi', 'litreye', 'asla toplamayın', 'D şıkkı', 'A şıkkına', 'B şıkkına', 'C şıkkına', 'E şıkkına', 'tuzaklara', 'maktu vergi']


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s04", T("s04", "anahtarı"), "dikkat"), ("s05", 0.0, "neutral"),
            ("s06", 0.0, "neutral"), ("s06", T("s06", "derece"), "dikkat"), ("s07", 0.0, "neutral"), ("s07", T("s07", "derecesi"), "dikkat"),
            ("s08", 0.0, "neutral"), ("s08", T("s08", "Doğru"), "cevap"), ("s09", 0.0, "tuzak"), ("s10", T("s10", "uyarı"), "uyari"),
            ("s11", 0.0, "neutral"), ("s11", T("s11", "Formülü"), "dikkat"), ("s12", 0.0, "neutral"), ("s12", T("s12", "D"), "cevap")]


DOC = {'title': 'ÖTV (III-A): bira ve şarapta nispi vergi mi, asgari maktu mu?', 'short': 'ÖTV bira ve şarap',
       'question': "R firması aynı beyannameyle iki ürün ithal ediyor: 33 cl'lik 12.000 kutu bira (alkol %5, ÖTV'ye esas birim değer kutu başına 5 TL) ve 75 cl'lik 4.000 şişe şarap (alkol %13, şişe başına 60 TL). Nispi ÖTV oranı ikisinde de %63; asgari maktu vergi tutarı bira için 2,50 TL, şarap için 25 TL. Ödenecek toplam ÖTV kaç TL?",
       'options': [('A', '112.800 TL'), ('B', '124.500 TL'), ('C', '189.000 TL'), ('D', '200.700 TL'), ('E', '313.500 TL')], 'answer': 'D',
       'solution': ['Litre: bira 0,33 × 12.000 = 3.960 L · şarap 0,75 × 4.000 = 3.000 L',
                    'Bira: nispi 60.000 × %63 = 37.800 · asgari maktu 3.960 × 5 × 2,50 = 49.500 → 49.500 TL (yüksek olan)',
                    'Şarap: nispi 240.000 × %63 = 151.200 · asgari maktu 3.000 × 25 = 75.000 → 151.200 TL · toplam 49.500 + 151.200 = 200.700 TL'],
       'distractors': 'A 112.800 (her üründe düşük olan alındı), B 124.500 (ikisinde de asgari maktu), C 189.000 (ikisinde de nispi; birada derece unutulursa da buraya düşülür), E 313.500 (nispi ile asgari maktu toplandı).',
       'guests': 'Stajyer — R firması adına (“Nispi ile maktuyu toplasak?”, “Formül hepsinde aynı değil mi?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)',
       'extras': 'iki ürün kartı, sayaçlı hesap satırları, çözüm defteri (düşük olan üstü çizili), ödeme fişi, dört çeldirici analizi, “formül içkiye göre değişir” kartı, sigara paneli, “bu hangi içki?” notu, 5 adımlı formül, 5 sn geri sayım',
       'sources': 'ÖTV Kanunu (III) sayılı liste (A) cetveli: asgari maktu vergi tutarından az olmamak üzere nispi vergi; bira formülü litre × alkol derecesi × tutar, şarapta litre × tutar, viskide litre × tutar × alkol oranı; sigarada (B cetveli) yüksek olanın üzerine maktu vergi eklenir (Gümrük Koçu vergi hesaplama derlemesi). Oranlar ve tutarlar soruda veri olarak verilmiştir.',
       'yt_title': 'ÖTV Hesabı: Bira ve Şarapta Nispi Vergi mi, Asgari Maktu mu? | Vergi Hesaplama Dersi #10 | Gümrük Koçu',
       'yt_intro': 'Vergi hesaplama derslerinin onuncusunda alkollü içkilerde ÖTV hesaplıyoruz: aynı beyannamede bira ve şarap. Nispi vergi ile asgari maktu vergi ayrı ayrı hesaplanır, yüksek olan alınır; ama formül içkiye göre değişir.',
       'tags': 'ÖTV, özel tüketim vergisi, III sayılı liste, asgari maktu vergi, nispi vergi, bira ÖTV, şarap ÖTV, alkollü içki ithalatı, gümrük müşavirliği sınavı, Gümrük Koçu',
       'hashtags': '#gümrük #ÖTV #vergihesaplama #GümrükKoçu',
       'scenes': {'s01': 'Logo sting → VERGİ HESAPLAMA · DERS #10; konu kartı (nispi, asgari maktu, bira ≠ şarap, yüksek olan) + TUZAK rozeti.',
                  's02': 'Soru verileri: R firması (tek beyanname); bira 12.000 kutu 33 cl %5 5 TL · şarap 4.000 şişe 75 cl %13 60 TL; nispi %63 · AMV 2,50 / 25 TL; Stajyer “Nispi ile maktuyu toplasak?”',
                  's03': 'Beş şık (112.800 · 124.500 · 189.000 · 200.700 · 313.500 TL) + 5 sn geri sayım.',
                  's04': 'ÖNEMLİ · 3 anahtar: yüksek olan alınır · formül içkiye göre · 100 cl = 1 L.',
                  's05': 'Adım 1: bira 3.960 L · şarap 3.000 L; defter + not.',
                  's06': 'Adım 2 (bira): nispi 37.800 · asgari maktu 49.500 → 49.500 TL; DİKKAT (derece).',
                  's07': 'Adım 3 (şarap): nispi 151.200 · asgari maktu 75.000 → 151.200 TL; DİKKAT (derece çarpılmaz).',
                  's08': 'Ödeme fişi: 49.500 + 151.200 = 200.700 TL; doğru şık D yeşil + CEVAP: D damgası.',
                  's09': 'TUZAK · dört çeldirici (A düşük olanlar, B ikisi de AMV, C ikisi de nispi, E toplama) + Gümrükçü Baba.',
                  's10': 'UYARI · asgari maktu formülü (bira, şarap, viski) + sigara paneli; Stajyer “Formül hepsinde aynı değil mi?” → HAYIR!',
                  's11': 'İPUCU · Koçun notu: bu hangi içki? + “Yüksek olan alınır” + 5 adımlı formül.',
                  's12': 'Özet: bira asgari maktu · şarap nispi · cevap D 200.700 TL; abone ol / paylaş; logo.'}}
