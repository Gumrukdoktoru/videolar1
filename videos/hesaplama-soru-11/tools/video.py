"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 11
META = "DERS · <b>VERGİ HESAPLAMA #11</b> · ÇEVRE KATKI PAYI"
TITLE = "Vergi Hesaplama Dersi 11 — Gümrük Koçu"
QUIZ = ["s02", "s03"]
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU & ŞIKLAR", ["s02", "s03"]), ("ANAHTAR KURAL", ["s04"]),
    ("ADIM ADIM ÇÖZÜM", ["s05", "s06", "s07", "s08"]), ("TUZAKLAR", ["s09"]), ("UYARI", ["s10"]),
    ("KOÇUN NOTU", ["s11"]), ("ÖZET", ["s12"]),
]
YT = ['Giriş', 'Soru ve şıklar', 'Üç anahtar: hurda ‰5, yakıt ve atık %1, matrah CIF', 'Adım adım çözüm', 'Tuzak şıklar', 'Uyarı: ÇKP kimden alınır?', 'Koçun notu: ÇKP’de iki soru', 'Özet']
KW = ['çevre katkı payı', 'Çevre katkı payı', '‰5', "‰5'le", "‰5'idir", '%1', "%1'le", "%1'idir", 'CIF bedel', 'CIF bedelin', 'CIF bedeldir', 'hurda', 'Hurda', 'Hurdada',
      'yakıt', 'navlun', 'sigorta', 'tahmil tahliye', 'girmez', 'karıştırmayın', 'B şıkkı', 'A şıkkına', 'C şıkkına', 'D şıkkına', 'E şıkkına', 'tuzaklara']


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s04", T("s04", "anahtarı"), "dikkat"), ("s05", 0.0, "neutral"),
            ("s05", T("s05", "Türkiye'deki"), "dikkat"), ("s06", 0.0, "neutral"), ("s06", T("s06", "binde", 2), "uyari"), ("s07", 0.0, "neutral"),
            ("s08", 0.0, "neutral"), ("s08", T("s08", "Doğru"), "cevap"), ("s09", 0.0, "tuzak"), ("s10", T("s10", "uyarı"), "uyari"),
            ("s11", 0.0, "neutral"), ("s11", T("s11", "Formülü"), "dikkat"), ("s12", 0.0, "neutral"), ("s12", T("s12", "B"), "cevap")]


DOC = {'title': 'Çevre katkı payı: hurdada binde beş, yakıtta yüzde bir', 'short': 'Çevre katkı payı',
       'question': "Ç firması ABD'den FOB teslim şekliyle aynı beyannamede iki kalem eşya ithal ediyor. 1. kalem kontrole tabi demir-çelik hurdası: FOB 600.000 $, navlun 45.000 $, sigorta 5.000 $; ayrıca Türkiye'deki boşaltma limanında 20.000 $ tahmil tahliye ödeniyor. 2. kalem kontrole tabi yakıt (petrol koku): FOB 80.000 $, navlun 18.000 $, sigorta 2.000 $. 1 $ = 40 TL. Ödenecek çevre katkı payı toplamı kaç TL?",
       'options': [('A', '152.000 TL'), ('B', '170.000 TL'), ('C', '174.000 TL'), ('D', '280.000 TL'), ('E', '300.000 TL')], 'answer': 'B',
       'solution': ['CIF: hurda 600.000 + 45.000 + 5.000 = 650.000 $ (Türkiye\'deki tahmil tahliye girmez) · petrol koku 80.000 + 18.000 + 2.000 = 100.000 $',
                    'Hurda ‰5: 650.000 × 0,005 = 3.250 $ · petrol koku %1: 100.000 × 0,01 = 1.000 $',
                    'Toplam 4.250 $ × 40 = 170.000 TL'],
       'distractors': 'A 152.000 (FOB üzerinden hesaplandı), C 174.000 (Türkiye\'deki tahmil tahliye hurdanın matrahına katıldı), D 280.000 (oranlar ters uygulandı), E 300.000 (ikisine de %1 uygulandı).',
       'guests': 'Yardımcı — Ç firması adına (“Hurdaya da yüzde beş mi?”, “Her ithalatta ÇKP alınır mı?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)',
       'extras': 'FOB teslim damgası, sayaçlı hesap satırları, çözüm defteri, “‰5 = %0,5” kartı, ödeme fişi, dört çeldirici analizi, “ÇKP kimden alınır?” kartı, CIF/FOB paneli, ÇKP’de 2 soru notu, 5 adımlı formül, 5 sn geri sayım',
       'sources': 'Çevre katkı payı: ithaline izin verilen kontrole tabi hurdada CIF bedelin binde beşi, kontrole tabi atık ve yakıtta yüzde biri (Gümrük Koçu vergi hesaplama derlemesi); matrah CIF bedel, Türkiye\'deki liman giderleri dahil edilmez. Oranlar soruda veri olarak kullanılmıştır.',
       'yt_title': 'Çevre Katkı Payı Hesabı: Hurdada Binde Beş, Yakıtta Yüzde Bir (CIF Matrah) | Vergi Hesaplama Dersi #11 | Gümrük Koçu',
       'yt_intro': 'Vergi hesaplama derslerinin on birincisinde çevre katkı payını hesaplıyoruz: aynı beyannamede hurda ve petrol koku. Hurdada binde beş, kontrole tabi yakıt ve atıkta yüzde bir; matrah her zaman CIF bedel.',
       'tags': 'çevre katkı payı, ÇKP, hurda ithalatı, binde beş, petrol koku, kontrole tabi atık, CIF bedel, gümrük vergisi hesaplama, gümrük müşavirliği sınavı, Gümrük Koçu',
       'hashtags': '#gümrük #çevrekatkıpayı #vergihesaplama #GümrükKoçu',
       'scenes': {'s01': 'Logo sting → VERGİ HESAPLAMA · DERS #11; konu kartı (hurda ‰5, yakıt/atık %1, matrah CIF, oran) + TUZAK rozeti.',
                  's02': 'Soru verileri: Ç firması (FOB, 2 kalem); hurda FOB 600.000 + navlun 45.000 + sigorta 5.000 · Türkiye limanı 20.000 · petrol koku FOB 80.000 + 18.000 + 2.000; kur 40; Yardımcı “Hurdaya da yüzde beş mi?”',
                  's03': 'Beş şık (152.000 · 170.000 · 174.000 · 280.000 · 300.000 TL) + 5 sn geri sayım.',
                  's04': 'ÖNEMLİ · 3 anahtar: hurda ‰5 · yakıt ve atık %1 · matrah CIF.',
                  's05': 'Adım 1: hurda CIF 650.000 $ · petrol koku CIF 100.000 $; DİKKAT (tahmil tahliye girmez).',
                  's06': 'Adım 2: 650.000 $ × ‰5 = 3.250 $; “‰5 = %0,5” kartı.',
                  's07': 'Adım 3: 100.000 $ × %1 = 1.000 $ · toplam 4.250 $ × 40 = 170.000 TL; defter.',
                  's08': 'Ödeme fişi: 3.250 $ + 1.000 $ = 4.250 $ × 40 = 170.000 TL; doğru şık B yeşil + CEVAP: B damgası.',
                  's09': 'TUZAK · dört çeldirici (A FOB, C tahmil tahliye, D ters oran, E ikisine %1) + Gümrükçü Baba.',
                  's10': 'UYARI · ÇKP kimden alınır + CIF/FOB paneli; Yardımcı “Her ithalatta ÇKP alınır mı?” → HAYIR!',
                  's11': 'İPUCU · Koçun notu: ÇKP’de 2 soru + “‰5 = %0,5” + 5 adımlı formül.',
                  's12': 'Özet: hurda ‰5 · petrol koku %1 · cevap B 170.000 TL; abone ol / paylaş; logo.'}}
