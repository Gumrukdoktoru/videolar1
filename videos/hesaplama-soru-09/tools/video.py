"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 9
META = "DERS · <b>VERGİ HESAPLAMA #9</b> · TARIM PAYI · BİLEŞİM KODU"
TITLE = "Vergi Hesaplama Dersi 9 — Gümrük Koçu"
QUIZ = ["s02", "s03"]
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU & ŞIKLAR", ["s02", "s03"]), ("ANAHTAR KURAL", ["s04"]),
    ("ADIM ADIM ÇÖZÜM", ["s05", "s06", "s07", "s08"]), ("TUZAKLAR", ["s09"]), ("UYARI", ["s10"]),
    ("KOÇUN NOTU", ["s11"]), ("ÖZET", ["s12"]),
]
YT = ['Giriş', 'Soru ve şıklar', 'Üç anahtar: menşe, net ağırlık, matrah', 'Adım adım çözüm', 'Tuzak şıklar', 'Uyarı: bileşim kodu ve AB menşeli eşya', 'Koçun notu: tarım payında 3 soru', 'Özet']
KW = ['tarım payı', 'Tarım payı', 'tarım payını', 'Tarım payını', 'bileşim kodu', 'Bileşim kodunu', 'bileşim kodunu', 'T1', 'T2', 'net ağırlık', 'Net ağırlık', 'brüt ağırlık', 'Brüt ağırlığı',
      'KDV matrahına', 'gümrük vergisi matrahına', 'girmez', 'eklenir', 'Avrupa Birliği', 'C şıkkı', 'A şıkkına', 'B şıkkına', 'D şıkkına', 'E şıkkına', 'tuzaklara']


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s04", T("s04", "anahtarı"), "dikkat"), ("s05", 0.0, "neutral"),
            ("s06", 0.0, "neutral"), ("s06", T("s06", "te", 1), "dikkat"), ("s07", 0.0, "neutral"), ("s08", 0.0, "neutral"),
            ("s08", T("s08", "Doğru"), "cevap"), ("s09", 0.0, "tuzak"), ("s10", T("s10", "uyarı"), "uyari"), ("s11", 0.0, "neutral"),
            ("s11", T("s11", "Formülü"), "dikkat"), ("s12", 0.0, "neutral"), ("s12", T("s12", "C"), "cevap")]


DOC = {'title': 'Tarım payı: bileşim kodu, T1 tutarı ve 100 kg net', 'short': 'Tarım payı',
       'question': "B firması, Malezya menşeli ve Malezya'dan gelen gofret ithal ediyor; CIF kıymet 24.000 €, net ağırlık 6.000 kg, brüt ağırlık 6.300 kg. Bileşim tablosuna göre tarım payı kodu 7225: T1 tutarı 100 kg başına 40 €, T2 tutarı 25 €. GV %8, KDV %10, 1 € = 45 TL. Ödenecek GV + tarım payı + KDV toplamı kaç TL?",
       'options': [('A', '277.290 TL'), ('B', '311.040 TL'), ('C', '321.840 TL'), ('D', '327.780 TL'), ('E', '331.344 TL')], 'answer': 'C',
       'solution': ['Kıymet 24.000 € × 45 = 1.080.000 TL · GV %8 = 86.400 TL (tarım payı GV matrahına girmez)',
                    'Tarım payı: AB dışı menşe → T1; 6.000 kg net ÷ 100 = 60 × 40 € = 2.400 € × 45 = 108.000 TL',
                    'KDV: (1.080.000 + 86.400 + 108.000) × %10 = 127.440 → toplam 86.400 + 108.000 + 127.440 = 321.840 TL'],
       'distractors': 'A 277.290 (AB menşeine ait T2 tutarı kullanıldı), B 311.040 (tarım payı KDV matrahına eklenmedi), D 327.780 (brüt ağırlık kullanıldı), E 331.344 (tarım payı GV matrahına da katıldı).',
       'guests': 'Cano — B firması adına (“Brüt ağırlığı mı alsak?”, “GV sıfırsa tarım payı da sıfır mı?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)',
       'extras': 'bileşim kodu damgası, sayaçlı hesap satırları, çözüm defteri, bileşim kodu kartı, ödeme fişi, dört çeldirici analizi, “bileşim kodu nasıl bulunur?” kartı, AB menşeli eşya paneli, tarımda 3 soru notu, 5 adımlı formül, 5 sn geri sayım',
       'sources': 'Tarım payı (bileşim kodu, T1/T2 tutarları, 100 kg net ağırlık esası; GV matrahına girmez, KDV matrahına girer — KDV K. md. 21); Gümrük Koçu ders notu. Tutarlar ve oranlar soruda veri olarak verilmiştir.',
       'yt_title': 'Tarım Payı Hesabı: Bileşim Kodu, T1 / T2 ve 100 kg Net (Gofret) | Vergi Hesaplama Dersi #9 | Gümrük Koçu',
       'yt_intro': 'Vergi hesaplama derslerinin dokuzuncusunda tarım payını hesaplıyoruz: bileşim kodu, menşee göre T1 ya da T2 tutarı, 100 kg net ağırlık ve KDV matrahı. Küçük bir seçim sonucu değiştirir; brüt ağırlık ya da yanlış tutar seçen yanlış şıkka düşer.',
       'tags': 'tarım payı, bileşim kodu, T1 T2 tutarı, net ağırlık, KDV matrahı, gofret ithalatı, gümrük vergisi hesaplama, gümrük müşavirliği sınavı, Gümrük Koçu',
       'hashtags': '#gümrük #tarımpayı #vergihesaplama #GümrükKoçu',
       'scenes': {'s01': 'Logo sting → VERGİ HESAPLAMA · DERS #9; konu kartı (bileşim kodu, T1/T2, net kg, KDV matrahı) + TUZAK rozeti.',
                  's02': 'Soru verileri: B firması (gofret, Malezya, CIF 24.000 €); net 6.000 / brüt 6.300 kg; kod 7225 · T1 40 € · T2 25 €; GV %8 · KDV %10 · kur 45; Cano “Brüt ağırlığı mı alsak?”',
                  's03': 'Beş şık (277.290 · 311.040 · 321.840 · 327.780 · 331.344 TL) + 5 sn geri sayım.',
                  's04': 'ÖNEMLİ · 3 anahtar: menşe belirler (T1/T2) · 100 kg net · GV matrahına girmez, KDV matrahına girer.',
                  's05': 'Adım 1: 24.000 € × 45 = 1.080.000 TL · GV 86.400 TL; defter + not.',
                  's06': 'Adım 2: 6.000 ÷ 100 = 60 birim × 40 € = 2.400 € × 45 = 108.000 TL; bileşim kodu kartı; DİKKAT.',
                  's07': 'Adım 3: KDV matrahı 1.274.400 → KDV 127.440; defter + not.',
                  's08': 'Ödeme fişi: 86.400 + 108.000 + 127.440 = 321.840 TL; doğru şık C yeşil + CEVAP: C damgası.',
                  's09': 'TUZAK · dört çeldirici (A T2, B KDV matrahı dışı, D brüt, E GV matrahına katıldı) + Gümrükçü Baba.',
                  's10': 'UYARI · bileşim kodu nasıl bulunur + AB menşeli eşya paneli; Cano “GV sıfırsa tarım payı da sıfır mı?” → HAYIR!',
                  's11': 'İPUCU · Koçun notu: tarımda 3 soru + “GV’ye girmez” + 5 adımlı formül.',
                  's12': 'Özet: GV + tarım payı · KDV · cevap C 321.840 TL; abone ol / paylaş; logo.'}}
