"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 12
META = "DERS · <b>VERGİ HESAPLAMA #12</b> · KISMİ MUAFİYET · GEÇİCİ İTHALAT"
TITLE = "Vergi Hesaplama Dersi 12 — Gümrük Koçu"
QUIZ = ["s02", "s03"]
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU & ŞIKLAR", ["s02", "s03"]), ("ANAHTAR KURAL", ["s04"]),
    ("ADIM ADIM ÇÖZÜM", ["s05", "s06", "s07", "s08"]), ("TUZAKLAR", ["s09"]), ("UYARI", ["s10"]),
    ("KOÇUN NOTU", ["s11"]), ("ÖZET", ["s12"]),
]
YT = ['Giriş', 'Soru ve şıklar', 'Üç anahtar: serbest dolaşım vergileri, aylık %3, ay kesri', 'Adım adım çözüm', 'Tuzak şıklar', 'Uyarı: sonradan serbest dolaşım ve tescil tarihi', 'Koçun notu: üç şeyi karıştırma', 'Özet']
KW = ['kısmi muafiyet', 'kısmi muafiyetle', 'Kısmi muafiyette', 'geçici ithalat', '%3', "%3'ü", "%3'ünü", 'vergilerin', 'kıymetin değil', 'tam ay', 'ay kesri', 'serbest dolaşıma',
      'tescil tarihindeki', '8 ay', 'E şıkkı', 'A şıkkına', 'B şıkkına', 'C şıkkına', 'D şıkkına', 'tuzaklara', 'değişmez']


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s04", T("s04", "anahtarı"), "dikkat"), ("s05", 0.0, "neutral"),
            ("s06", 0.0, "neutral"), ("s06", T("s06", "vergiler"), "dikkat"), ("s07", 0.0, "neutral"), ("s07", T("s07", "tam"), "dikkat"),
            ("s08", 0.0, "neutral"), ("s08", T("s08", "Doğru"), "cevap"), ("s09", 0.0, "tuzak"), ("s10", T("s10", "uyarı"), "uyari"),
            ("s11", 0.0, "neutral"), ("s11", T("s11", "Formülü"), "dikkat"), ("s12", 0.0, "neutral"), ("s12", T("s12", "E"), "cevap")]


DOC = {'title': 'Kısmi muafiyetle geçici ithalat: vergilerin aylık %3\'ü', 'short': 'Kısmi muafiyet',
       'question': "V firması, Çin'den kiraladığı bir mobil vinci kısmi muafiyet suretiyle geçici ithalat rejimine tabi tutuyor. Tescil tarihinde gümrük kıymeti 150.000 $, 1 $ = 40 TL; GV %5, İGV %10, KDV %20. Vinç rejimde 7 ay 12 gün kaldıktan sonra yeniden ihraç ediliyor. Rejim süresince ödenmesi gereken ithalat vergileri toplamı kaç TL?",
       'options': [('A', '216.000 TL'), ('B', '478.800 TL'), ('C', '504.000 TL'), ('D', '506.160 TL'), ('E', '547.200 TL')], 'answer': 'E',
       'solution': ['Kıymet 150.000 $ × 40 = 6.000.000 TL · GV %5 = 300.000 · İGV %10 = 600.000',
                    'KDV: (6.000.000 + 300.000 + 600.000) × %20 = 1.380.000 → vergiler toplamı 2.280.000 TL',
                    'Aylık: 2.280.000 × %3 = 68.400 TL · 7 ay 12 gün = 8 ay (ay kesri tam ay) → 68.400 × 8 = 547.200 TL'],
       'distractors': 'A 216.000 (KDV hesaba katılmadı), B 478.800 (12 gün atılıp 7 ay sayıldı), C 504.000 (KDV matrahına GV ve İGV eklenmedi), D 506.160 (gün kesri oranlanıp 7,4 ay sayıldı).',
       'guests': 'Cano — V firması adına (“Kıymetin yüzde üçü değil mi?”, “Oran düşerse tutar da düşer mi?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)',
       'extras': 'kısmi muafiyet damgası, sayaçlı hesap satırları ve toplam, GK md. 130 kartı, çözüm defteri, ödeme fişi, dört çeldirici analizi, sonradan serbest dolaşım kartı, tescil tarihi paneli, “üç şeyi karıştırma” notu, 5 adımlı formül, 5 sn geri sayım',
       'sources': 'Gümrük Kanunu md. 130: kısmi muafiyetle geçici ithalatta, eşya rejime tabi tutulduğu tarihte serbest dolaşıma girseydi alınacak vergilerin her ay veya ay kesri için %3\'ü; eşya sonradan serbest dolaşıma girerse ödenen tutar mahsup edilir (Gümrük Koçu vergi hesaplama derlemesi). Oranlar soruda veri olarak verilmiştir.',
       'yt_title': 'Kısmi Muafiyetle Geçici İthalat: Aylık %3 ve Ay Kesri (Mobil Vinç) | Vergi Hesaplama Dersi #12 | Gümrük Koçu',
       'yt_intro': 'Vergi hesaplama derslerinin on ikincisinde kısmi muafiyetle geçici ithalatı hesaplıyoruz: önce serbest dolaşım vergileri, sonra her ay için vergilerin yüzde üçü; ay kesri tam ay sayılır.',
       'tags': 'kısmi muafiyet, geçici ithalat, aylık yüzde üç, ay kesri, Gümrük Kanunu 130, mobil vinç, gümrük vergisi hesaplama, gümrük müşavirliği sınavı, Gümrük Koçu',
       'hashtags': '#gümrük #geçiciithalat #vergihesaplama #GümrükKoçu',
       'scenes': {'s01': 'Logo sting → VERGİ HESAPLAMA · DERS #12; konu kartı (aylık %3, vergilerin %3\'ü, ay kesri) + TUZAK rozeti.',
                  's02': 'Soru verileri: V firması (kiralık mobil vinç, Çin); kıymet 150.000 $ · kur 40; GV %5 · İGV %10 · KDV %20; 7 ay 12 gün; Cano “Kıymetin yüzde üçü değil mi?”',
                  's03': 'Beş şık (216.000 · 478.800 · 504.000 · 506.160 · 547.200 TL) + 5 sn geri sayım.',
                  's04': 'ÖNEMLİ · 3 anahtar: serbest dolaşım vergileri · vergilerin aylık %3\'ü · ay kesri tam ay.',
                  's05': 'Adım 1: kıymet 6.000.000 · GV 300.000 · İGV 600.000 · KDV 1.380.000 → toplam 2.280.000 TL.',
                  's06': 'Adım 2: 2.280.000 × %3 = 68.400 TL; GK md. 130 kartı; DİKKAT.',
                  's07': 'Adım 3: 7 ay 12 gün → 8 ay · 68.400 × 8 = 547.200 TL; defter + not.',
                  's08': 'Ödeme fişi: 2.280.000 → 68.400 → × 8 = 547.200 TL; doğru şık E yeşil + CEVAP: E damgası.',
                  's09': 'TUZAK · dört çeldirici (A KDV yok, B 7 ay, C KDV matrahı eksik, D 7,4 ay) + Gümrükçü Baba.',
                  's10': 'UYARI · sonradan serbest dolaşım (mahsup) + tescil tarihi paneli; Cano “Oran düşerse tutar da düşer mi?” → HAYIR!',
                  's11': 'İPUCU · Koçun notu: üç şeyi karıştırma + “Yukarı yuvarla” + 5 adımlı formül.',
                  's12': 'Özet: vergiler × %3 · 8 ay · cevap E 547.200 TL; abone ol / paylaş; logo.'}}
