"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 13
META = "DERS · <b>VERGİ HESAPLAMA #13</b> · DAMPİNGE KARŞI VERGİ · MENŞE"
TITLE = "Vergi Hesaplama Dersi 13 — Gümrük Koçu"
QUIZ = ["s02", "s03"]
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU & ŞIKLAR", ["s02", "s03"]), ("ANAHTAR KURAL", ["s04"]),
    ("ADIM ADIM ÇÖZÜM", ["s05", "s06", "s07", "s08"]), ("TUZAKLAR", ["s09"]), ("UYARI", ["s10"]),
    ("KOÇUN NOTU", ["s11"]), ("ÖZET", ["s12"]),
]
YT = ['Giriş', 'Soru ve şıklar', 'Üç anahtar: menşe, net ağırlık, matrah', 'Adım adım çözüm', 'Tuzak şıklar', 'Uyarı: önlem hangi ülkeye uygulanır?', 'Koçun notu: menşe şahadetnamesine bak', 'Özet']
KW = ['dampinge karşı vergi', 'Dampinge karşı vergi', 'Dampinge karşı vergiyi', 'dampinge karşı vergiyi', 'menşe şahadetnamesi', 'menşe şahadetnamesine', 'menşei', 'menşeye göre',
      'net ağırlık', 'Net ağırlık', 'net ağırlıkla', 'Brüt ağırlığı', 'Çin oranı', 'Tescilden sonraki', 'girmez', 'eklenir', 'A şıkkı', 'B şıkkına', 'C şıkkına', 'D şıkkına', 'E şıkkına', 'tuzaklara']


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s04", T("s04", "anahtarı"), "dikkat"), ("s05", 0.0, "neutral"),
            ("s06", 0.0, "neutral"), ("s06", T("s06", "menşei"), "dikkat"), ("s07", 0.0, "neutral"), ("s07", T("s07", "Tescilden"), "dikkat"),
            ("s08", 0.0, "neutral"), ("s08", T("s08", "Doğru"), "cevap"), ("s09", 0.0, "tuzak"), ("s10", T("s10", "uyarı"), "uyari"),
            ("s11", 0.0, "neutral"), ("s11", T("s11", "Formülü"), "dikkat"), ("s12", 0.0, "neutral"), ("s12", T("s12", "A"), "cevap")]


DOC = {'title': 'Dampinge karşı vergi: menşe, net ağırlık ve KDV matrahı', 'short': 'Dampinge karşı vergi',
       'question': "D firması, Malezya'dan yüklenen ve menşe şahadetnamesine göre Çin menşeli polyester elyaf ithal ediyor; CIF kıymet 64.000 $, net 40.000 kg, brüt 41.500 kg. GV %4. Dampinge karşı vergi: Çin menşeli eşya için 0,30 $/kg, Malezya menşeli eşya için 0,45 $/kg. Tescilden sonra fabrikaya nakliye için 2.000 $ ödeniyor. KDV %20, 1 $ = 40 TL. Ödenecek GV + dampinge karşı vergi + KDV toplamı kaç TL?",
       'options': [('A', '1.210.880 TL'), ('B', '1.226.880 TL'), ('C', '1.232.480 TL'), ('D', '1.233.920 TL'), ('E', '1.498.880 TL')], 'answer': 'A',
       'solution': ['GV: 64.000 $ × %4 = 2.560 $ (damping GV matrahına girmez)',
                    'Dampinge karşı vergi: menşe Çin → 40.000 kg net × 0,30 $ = 12.000 $',
                    'KDV: (64.000 + 2.560 + 12.000) × %20 = 15.712 $ (tescil sonrası nakliye girmez) → toplam 30.272 $ × 40 = 1.210.880 TL'],
       'distractors': 'B 1.226.880 (tescil sonrası nakliye KDV matrahına eklendi), C 1.232.480 (brüt ağırlık kullanıldı), D 1.233.920 (damping GV matrahına katıldı), E 1.498.880 (yükleme ülkesi Malezya\'nın oranı uygulandı).',
       'guests': 'Yardımcı — D firması adına (“Malezya\'dan geldi, Malezya oranı?”, “Malezya\'dan geldiyse Malezya önlemi?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)',
       'extras': 'menşe damgası, sayaçlı hesap satırları, çözüm defteri, menşe şahadetnamesi kartı, ödeme fişi, dört çeldirici analizi, “önlem hangi ülkeye?” kartı, önlem türleri paneli, “nereye bakılır?” notu, 5 adımlı formül, 5 sn geri sayım',
       'sources': 'Dampinge karşı vergi menşeye göre uygulanır (menşe şahadetnamesi); kg başına tutar net ağırlıkla çarpılır; dampinge karşı vergi GV matrahına girmez, KDV matrahına girer; tescil sonrası giderler KDV matrahına girmez (KDV K. md. 21; Gümrük Koçu vergi hesaplama derlemesi). Tutarlar soruda veri olarak verilmiştir.',
       'yt_title': 'Dampinge Karşı Vergi Hesabı: Menşe mi, Yükleme Ülkesi mi? (Polyester Elyaf) | Vergi Hesaplama Dersi #13 | Gümrük Koçu',
       'yt_intro': 'Vergi hesaplama derslerinin on üçüncüsünde dampinge karşı vergiyi hesaplıyoruz: eşya Malezya\'dan yüklenmiş ama menşei Çin. Önlem menşeye göre uygulanır, tutar net ağırlıkla çarpılır, damping KDV matrahına girer.',
       'tags': 'dampinge karşı vergi, anti damping, menşe şahadetnamesi, net ağırlık, KDV matrahı, polyester elyaf, gümrük vergisi hesaplama, gümrük müşavirliği sınavı, Gümrük Koçu',
       'hashtags': '#gümrük #damping #vergihesaplama #GümrükKoçu',
       'scenes': {'s01': 'Logo sting → VERGİ HESAPLAMA · DERS #13; konu kartı (yükleme ülkesi, menşe, hangi önlem, net/brüt) + TUZAK rozeti.',
                  's02': 'Soru verileri: D firması (polyester elyaf; yükleme Malezya, menşe Çin); CIF 64.000 $ · net 40.000 / brüt 41.500 kg · tescil sonrası 2.000 $; GV %4 · damping Çin 0,30 / Malezya 0,45 $/kg · KDV %20; Yardımcı “Malezya oranı?”',
                  's03': 'Beş şık (1.210.880 · 1.226.880 · 1.232.480 · 1.233.920 · 1.498.880 TL) + 5 sn geri sayım.',
                  's04': 'ÖNEMLİ · 3 anahtar: menşe belirler · net ağırlık · matrah (GV’ye girmez, KDV’ye girer; tescil sonrası gider girmez).',
                  's05': 'Adım 1: 64.000 $ × %4 = 2.560 $; defter + not.',
                  's06': 'Adım 2: menşe Çin → 0,30 $/kg × 40.000 kg = 12.000 $; menşe şahadetnamesi kartı; DİKKAT.',
                  's07': 'Adım 3: KDV matrahı 78.560 $ → KDV 15.712 $; defter + not (tescil sonrası nakliye girmez).',
                  's08': 'Ödeme fişi: 2.560 + 12.000 + 15.712 = 30.272 $ × 40 = 1.210.880 TL; doğru şık A yeşil + CEVAP: A damgası.',
                  's09': 'TUZAK · dört çeldirici (B nakliye, C brüt, D GV matrahı, E Malezya oranı) + Gümrükçü Baba.',
                  's10': 'UYARI · önlem hangi ülkeye + önlem türleri paneli; Yardımcı “Malezya’dan geldiyse Malezya önlemi?” → HAYIR!',
                  's11': 'İPUCU · Koçun notu: nereye bakılır + “Nerede üretildi?” + 5 adımlı formül.',
                  's12': 'Özet: GV + damping · KDV · cevap A 1.210.880 TL; abone ol / paylaş; logo.'}}
