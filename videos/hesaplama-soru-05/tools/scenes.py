"""Vergi Hesaplama Dersi 5: gümrük kıymeti — satış/satın alma komisyonu, yurt dışı tasarım, Türkiye'de çoğaltma hakkı, montaj."""
import hkit
from hkit import S, intro, question, options, keys, calc, sorter, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["FİYAT + NAKLİYE", "EKLE / EKLEME", "TL'YE ÇEVİR", "SONUÇ"]

intro("s01", 5, "beşincisine", "KONU · GÜMRÜK KIYMETİ", "Ekle mi, <em>ekleme</em> mi?",
      [("Komisyon", "Komisyon"), ("Tasarım", "tasarım"), ("Çoğaltma hakkı", "çoğaltma"), ("Montaj", "montaj")],
      "Hangisi <b>kıymete girer?</b>", art="scale", at_qq="hangileri", at_tz="eklenmez")

question("s02", "Yedi kalem ödeme",
         dict(icon="gear", head="T firması · 50 dikiş makinesi", sub="satıcı: <em>Almanya</em> · FOB <em>1.200 €</em> / adet",
              stamp="7 KALEM<br/>ÖDEME", at="firması", at_stamp="ayrıca"),
         [("FATURA · FOB", "60.000 €", "50 × 1.200 €", "doc", "tanesi"),
          ("NAVLUN + SİGORTA", "3.000 €", "2.500 + 500 · TR'ye kadar", "ship", "navlun"),
          ("KUR", "40 TL", "1 € = 40 TL", "lira", ("kırk", 1))],
         [("SATIŞ KOM.", "3.000 €", "acc", "satış"), ("SATIN ALMA KOM.", "1.500 €", "acc", "satın"), ("TASARIM", "4.000 €", "acc", "tasarım"),
          ("ÇOĞALTMA", "6.000 €", "acc", "çoğaltılması"), ("MONTAJ", "2.000 €", "acc", "montaj")],
         dict(char="yardimci", bubble="Ödediğimiz her şeyi <i>ekleriz</i>, değil mi?", at="firması", at_bub="ayrıca"),
         ("İstenen: <b>gümrük kıymeti</b> = ? <em>TL</em>", "Soru"))

options("s03", [("A", "2.800.000"), ("B", "2.860.000"), ("C", "2.880.000"), ("D", "3.040.000"), ("E", "3.180.000")], "TL")

keys("s04", [("percent", "Komisyon: satış ✓ · satın alma ✗", "Satış komisyonu <b>eklenir</b>; <b>satın alma komisyonu hariç</b>", "GK md. 27/1-a", "Bir", "hariç"),
             ("pen", "Yurt dışı tasarım: ekle", "TR dışında yapılıp alıcının <b>bedelsiz verdiği</b> tasarım kıymete girer", "GK md. 27/1-b", "İki", ("eklenir", 2)),
             ("x", "Çoğaltma + montaj: ekleme", "<b>Ayrı gösterilen</b> montaj ve TR'de çoğaltma hakkı kıymete girmez", "GK md. 28", ("üç", 2), "girmez")],
     ["fiyat", "nakliye", "ekle / ekleme", "kura çevir"])

calc("s05", 1, "ADIM 1 · FİYAT VE NAKLİYE",
     [("FATURA", "50 × 1.200 €", 60000, "k", "Elli", "altmış"),
      ("NAVLUN", "TR giriş yerine kadar", 2500, "g", "navlun", ("iki", 2)),
      ("SİGORTA", "TR giriş yerine kadar", 500, "g", ("artı", 1), ("beş", 2))],
     sum_row=("ARA TOPLAM", 63000, "€", "Ara", "Ara"),
     side=("law", "GÜMRÜK KANUNU", "MADDE 27/1-e · özet",
           "Eşyanın <b>Türkiye'deki giriş yerine kadar</b> nakliye ve sigorta giderleri kıymete eklenir. FOB fiyatın içinde bunlar <b>yoktur</b>.", "FOB"),
     at_start="Birinci")

sorter("s06", 2, "ADIM 2 · EKLE YA DA EKLEME",
       [("Satış komisyonu", "3.000 €", "gk", "Satıcının", ("ekle", 2), "satıcının acentesine · GK 27/1-a"),
        ("Satın alma komisyonu", "1.500 €", "no", "Kendi", ("ekleme", 2), "alıcının kendi temsilcisi"),
        ("Tasarım çalışması", "4.000 €", "gk", "İtalya'da", ("ekle", 3), "İtalya · bedelsiz · GK 27/1-b"),
        ("Türkiye'de çoğaltma hakkı", "6.000 €", "no", "Türkiye'de", ("ekleme", 3), "GK md. 28"),
        ("Montaj (ayrı gösterilmiş)", "2.000 €", "no", "Ayrı", ("ekleme", 4), "ithalattan sonra · GK md. 28")],
       total=("KIYMET: <b>63.000 + 3.000 + 4.000</b>", 70000, "€", "Kıymet", "Kıymet"), at_start="İkinci")

calc("s07", 3, "ADIM 3 · TÜRK LİRASINA ÇEVİR",
     [("KIYMET (€)", "63.000 + 3.000 + 4.000", 70000, "k", "Üçüncü", "Yetmiş"),
      ("KUR", "TCMB döviz satış kuru", 40, "g", "Merkez", "satış")],
     sum_row=("GÜMRÜK KIYMETİ", 2800000, "TL", "çarpı", "milyon"),
     side=("law", "GÜMRÜK KANUNU", "MADDE 30 · özet",
           "Yabancı paralar, yükümlülüğün başladığı tarihteki <b>TCMB döviz satış kuru</b> ile Türk lirasına çevrilir.", "Gümrük"),
     at_start="Üçüncü")

result("s08", [("Fatura (FOB)", "50 × 1.200", "60.000 €", "altmış"), ("Navlun + sigorta", "TR'ye kadar", "3.000 €", ("artı", 1)),
               ("Satış komisyonu", "GK 27/1-a", "3.000 €", ("artı", 2)), ("Tasarım", "TR dışı · bedelsiz", "4.000 €", ("artı", 3))],
       (2800000, 0), "Türk lirası · 70.000 € × 40",
       [("A", "2.800.000"), ("B", "2.860.000"), ("C", "2.880.000"), ("D", "3.040.000"), ("E", "3.180.000")], "A",
       sub="SORU · GÜMRÜK KIYMETİ", at=dict(son="sonuç", od="Toplam", cnt="milyon", dogru="Doğru", L="A"), total_label="KIYMET")

traps("s09", [("B", "2.860.000", "Satın alma komisyonu eklendi", [("Kıymet: 70.000 + 1.500", "71.500 €", ""), ("× 40", "2.860.000", "")], "2.860.000"),
              ("C", "2.880.000", "Ayrı gösterilen montaj eklendi", [("Kıymet: 70.000 + 2.000", "72.000 €", ""), ("× 40", "2.880.000", "")], "2.880.000"),
              ("D", "3.040.000", "TR'de çoğaltma hakkı eklendi", [("Kıymet: 70.000 + 6.000", "76.000 €", ""), ("× 40", "3.040.000", "")], "3.040.000"),
              ("E", "3.180.000", "Ödenen her şey eklendi", [("Kıymet: 70.000 + 9.500", "79.500 €", ""), ("× 40", "3.180.000", "")], "3.180.000")],
      "TL", "Doğrusu <i>A: 2.800.000 TL!</i>",
      at=[("Satın", "B"), ("Ayrı", "C"), ("Türkiye'deki", "D"), ("Ödenen", "E")])

warn("s10", "KOMİSYON TÜRLERİ",
     dict(head="KİME ÖDENDİ?", ref="GK md. 27/1-a",
          conds=[("Alıcının kendi temsilcisine → <b>satın alma komisyonu</b>: kıymete girmez", "temsilcisine"),
                 ("Satıcı tarafındaki acenteye → <b>satış komisyonu</b>: kıymete eklenir", "Satıcı")],
          res="İSME DEĞİL, KİME ÖDENDİĞİNE BAK!", at="Satın", at_res="eklenir"),
     dict(head="MONTAJ VE KURULUM GİDERİ", items=[("pc", "Fiyattan ayrı gösterildi", "KIYMET DIŞI", "2.000 €", "ayrı"),
                                                 ("pv", "Fiyatın içinde, ayrılmamış", "KIYMETE DAHİL", "?", "ancak")], at=("Bir", 2)),
     dict(char="yardimci", bubble="Komisyon komisyondur, <em>hepsini ekleyelim!</em>", at="uyarı", at_bub="karıştırmayın"), hayir="girmez")

coach("s11", dict(head="HER ÖDEMEYE 3 SORU", icon="question", at="Kıymet",
                  opts=[("ok", "Eşyayla ilgili mi?", "İLGİ", "ilgili"), ("ok", "Türkiye'ye girişten önce mi?", "ZAMAN", "önce"),
                        ("ok", "Satış koşulu / alıcının yükü mü?", "KOŞUL", "koşulu")]),
      dict(head="KANUNDA HARİÇ", big="Açıkça hariç = <em>hep dışarıda</em>", p="Satın alma komisyonu, TR'de çoğaltma hakkı, ayrı gösterilen montaj.",
           ref="GK md. 27/1-a · md. 28", at="Kanunda", at_pulse="dışarıda"),
      [("Fiyatı al", "doc", "Fiyatı"), ("Nakliyeyi ekle", "ship", "nakliyeyi"), ("Eklenecekleri ekle", "check", "eklenecekleri"),
       ("Hariçleri çıkar", "x", "hariçleri"), ("Kura çevir", "lira", "kura")])

closing("s12", "ÖZET · GÜMRÜK KIYMETİ",
        [("Kıymete eklenenler", "+ satış komisyonu 3.000 · tasarım 4.000 €", "satış"),
         ("Kıymete girmeyenler", "satın alma kom. · çoğaltma · montaj", "Satın")],
        ("A", "2.800.000", "TL"), ("lira", "70.000 € × 40<br/><em>satış kuru</em>", "Toplam"))
