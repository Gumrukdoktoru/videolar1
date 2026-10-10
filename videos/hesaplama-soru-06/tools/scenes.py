"""Vergi Hesaplama Dersi 6: demuraj ve liman giderleri — varıştan önce kıymete, varıştan sonra yalnız KDV matrahına."""
import hkit
from hkit import S, intro, question, options, keys, calc, sorter, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["KIYMET", "GİDER NEREYE?", "KDV", "SONUÇ"]

intro("s01", 6, "altıncısına", "KONU · DEMURAJ VE LİMAN GİDERLERİ", "Kıymete mi, <em>KDV'ye</em> mi?",
      [("Demuraj", "demuraj"), ("Yükleme limanı", "yükleme"), ("Türkiye'deki liman", "Türkiye'deki"), ("KDV matrahı", "KDV")],
      "Gider <b>nereye yazılır?</b>", art="ship", at_qq="unutmayacağız", at_tz="beklerse")

question("s02", "İki liman, iki demuraj",
         dict(icon="ship", head="Y firması · 100 ton çelik sac", sub="Güney Kore → <em>Mersin</em> · CFR <em>600 $/ton</em>",
              stamp="2 LİMAN<br/>2 DEMURAJ", at="firması", at_stamp="Gemi"),
         [("FİYAT · CFR", "60.000 $", "100 t × 600 $ · navlun dahil", "doc", "Fiyat"),
          ("YÜKLEME LİMANI", "1.600 $", "demuraj · Güney Kore", "ship", "yükleme"),
          ("MERSİN LİMANI", "3.000 $", "demuraj 2.000 + tahmil–tahliye 1.000", "container", "Mersin")],
         [("SİGORTA", "400 $", "acc", "Sigorta"), ("GÜMRÜK VERGİSİ", "%10", "gv", "Gümrük"), ("KDV", "%20", "kdv", "KDV")],
         dict(char="stajyer", bubble="Demuraj demurajdır, <i>hepsi kıymete!</i>", at="firması", at_bub="Mersin"),
         ("İstenen: <b>GV + KDV</b> toplamı = ? <em>$</em>", "Soru"))

options("s03", [("A", "19.200"), ("B", "19.840"), ("C", "19.928"), ("D", "20.440"), ("E", "20.800")], "$")

keys("s04", [("ship", "Varıştan önce: kıymete ekle", "Giriş yerine kadar nakliye, sigorta ve <b>yükleme limanı demurajı</b>", "GK md. 27/1-e", "Bir", "dahildir"),
             ("x", "Varıştan sonra: kıymete girmez", "Türkiye'deki demuraj ve <b>tahmil–tahliye</b> gümrük kıymeti dışında", "GK md. 28", "İki", "girmez"),
             ("percent", "Ama KDV matrahına ekle", "Yurt içi giderler <b>KDV matrahına</b> mutlaka girer", "KDV K. md. 21", ("üç", 2), ("eklenir", 2))],
     ["kıymet", "GV", "KDV matrahı (+ yurt içi)", "KDV"])

calc("s05", 1, "ADIM 1 · GÜMRÜK KIYMETİ",
     [("CFR FİYAT", "100 t × 600 $", 60000, "k", "Yüz", "altmış"),
      ("SİGORTA", "giriş yerine kadar", 400, "g", "Sigorta", "dört"),
      ("YÜKL. DEMURAJI", "varıştan önce", 1600, "g", "Yükleme", ("bin", 2))],
     sum_row=("GÜMRÜK KIYMETİ", 62000, "$", ("gümrük", 2), ("altmış", 2)),
     side=("law", "GENELGE 2009/32", "DEMURAJ · özet",
           "Giriş yerine <b>varıştan önceki</b> demuraj kıymete dahildir. <b>Varıştan sonraki</b> demuraj kıymete değil, KDV matrahına girer.", "Yükleme"),
     at_start="Birinci")

sorter("s06", 2, "ADIM 2 · HANGİ GİDER NEREYE?",
       [("CFR fiyat (navlun dahil)", "60.000 $", "in", "Fiyat", "kıymette", "100 t × 600 $"),
        ("Sigorta", "400 $", "gk", "Sigorta", "eklendi", "giriş yerine kadar"),
        ("Yükleme limanı demurajı", "1.600 $", "gk", "yükleme", "eklendi", "varıştan önce"),
        ("Mersin demurajı", "2.000 $", "kdv", "Mersin'deki", "yalnızca", "varıştan sonra"),
        ("Tahmil–tahliye", "1.000 $", "kdv", "tahmil", "yalnızca", "Mersin Limanı")],
       total=("GV = <b>62.000 × %10</b>", 6200, "$", "Gümrük", "altı"), at_start="İkinci")

calc("s07", 3, "ADIM 3 · KDV",
     [("KIYMET + GV", "62.000 + 6.200", 68200, "k", "matrahı", ("artı", 1)),
      ("+ YURT İÇİ", "2.000 + 1.000", 3000, "g", ("artı", 2), ("artı", 3)),
      ("KDV MATRAHI", "68.200 + 3.000", 71200, "m", "yetmiş", "yetmiş"),
      ("KDV", "71.200 × %20", 14240, "d", "Bunun", "on")],
     side=("ledger", [("Kıymet", "62.000", ""), ("GV", "6.200", ""), ("Yurt içi", "3.000", "q"), ("KDV", "14.240", "")],
           [None, None, ("artı", 2), "on"], "$"),
     dik=("dikkat", ("artı", 2)), at_start="Üçüncü",
     note=("Mersin'deki giderler <b>GV'yi</b> büyütmez ama <b>KDV matrahına</b> girer.", ("artı", 2)))

result("s08", [("Gümrük vergisi", "62.000 × %10", "6.200", "altı"), ("KDV", "71.200 × %20", "14.240", "artı")],
       (20440, 0), "ABD doları", [("A", "19.200"), ("B", "19.840"), ("C", "19.928"), ("D", "20.440"), ("E", "20.800")], "D",
       sub="SORU · USD · GV + KDV", at=dict(son="sonuç", od="Ödenecek", cnt="yirmi", dogru="Doğru", L="D"))

traps("s09", [("A", "19.200", "GV, KDV matrahına eklenmedi", [("KDV: 65.000 × %20", "13.000", ""), ("GV", "6.200", "")], "19.200"),
              ("B", "19.840", "Yurt içi giderler KDV'ye girmedi", [("KDV: 68.200 × %20", "13.640", ""), ("GV", "6.200", "")], "19.840"),
              ("C", "19.928", "Yükleme demurajı unutuldu", [("GV: 60.400 × %10", "6.040", ""), ("KDV: 69.440 × %20", "13.888", "")], "19.928"),
              ("E", "20.800", "Varış giderleri kıymete eklendi", [("GV: 65.000 × %10", "6.500", ""), ("KDV: 71.500 × %20", "14.300", "")], "20.800")],
      "$", "Doğrusu <i>D: 20.440 $!</i>",
      at=[("Gümrük", "A"), ("Yurt", "B"), ("Yükleme", "C"), ("Türkiye'deki", "E")])

warn("s10", "DEMURAJDA YER ÖNEMLİ",
     dict(head="DEMURAJ · GENELGE 2009/32", ref="YER",
          conds=[("Varıştan <b>önce</b> (yükleme limanı) → kıymete girer", "önceki"),
                 ("Varıştan <b>sonra</b> (Türkiye limanı) → kıymete girmez", "varıştan")],
          res="İKİSİ DE KDV MATRAHINDA", at="Demurajda", at_res="mutlaka"),
     dict(head="ARDİYE ÜCRETİ (ANTREPO)", items=[("pc", "Fiyattan ayrı gösterildi", "KIYMET DIŞI", "KDV'ye", "ayrı"),
                                                ("pv", "Fiyatla tek satırda", "KIYMETE DAHİL", "GV'ye", "ardiye")], at=("Bir", 2)),
     dict(char="stajyer", bubble="Demuraj demuraj, <em>hepsini ekleyelim!</em>", at="uyarı", at_bub="adı"), hayir="girmez")

coach("s11", dict(head="ÇİZGİ: GİRİŞ YERİ", icon="ship", at="Gider",
                  opts=[("ok", "Öncesi → gümrük kıymeti", "GV + KDV", "öncesi"), ("ok", "Sonrası → KDV matrahı", "YALNIZ KDV", "sonrası"),
                        ("no", "Sonrası → GV matrahı", "YANLIŞ", "yalnızca")]),
      dict(head="GÜMRÜK VERGİSİ", big="Yalnızca <em>kıymetten</em>", p="Yurt içi giderler GV'yi büyütmez; yalnızca KDV matrahına girer.",
           ref="GK md. 27–28 · KDV K. md. 21", at=("gümrük", 2), at_pulse="kıymetten"),
      [("Çizgiyi çiz", "ruler", ("çizgiyi", 2)), ("Öncesini kıymete ekle", "ship", "öncesini"), ("GV'yi hesapla", "percent", "vergiyi"),
       ("Sonrasını KDV'ye ekle", "arrow", "sonrasını"), ("KDV'yi hesapla", "check", "KDV'yi")])

closing("s12", "ÖZET · DEMURAJ VE KDV MATRAHI",
        [("Kıymet + GV", "62.000 $ · GV 6.200 $", "Yükleme"), ("KDV matrahı + yurt içi", "71.200 × %20 = 14.240 $", "Mersin'deki")],
        ("D", "20.440", "$"), ("ship", "Varıştan sonra →<br/><em>yalnız KDV</em>", "yalnızca"))
