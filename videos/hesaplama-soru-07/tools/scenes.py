"""Vergi Hesaplama Dersi 7: KKDF — fatura bedeli, döviz alış kuru, GV matrahına girmez, KDV matrahına girer."""
import hkit
from hkit import S, intro, question, options, keys, calc, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["KIYMET + GV", "KKDF", "KDV", "SONUÇ"]

intro("s01", 7, "yedincisine", "KONU · KKDF", "Fon, kur ve <em>KDV matrahı</em>",
      [("KKDF %6", "KKDF"), ("Fatura bedeli", "matrahı"), ("Alış kuru", "kuru"), ("KDV matrahı", "KDV")],
      "KDV matrahına <b>girer mi?</b>", art="lira", at_qq="Peki", at_tz="farklı")

question("s02", "Vadeli ithalat, iki kur",
         dict(icon="gear", head="Z firması · ambalaj makinesi", sub="ödeme: <em>kabul kredili</em> · FOB <em>30.000 $</em>",
              stamp="VADELİ<br/>ÖDEME", at="firması", at_stamp="kabul"),
         [("FATURA · FOB", "30.000 $", "teslim şekli: FOB", "doc", "Fatura"),
          ("NAVLUN + SİGORTA", "2.000 $", "1.500 + 500 → CIF 32.000 $", "ship", "Navlun"),
          ("TCMB KURLARI", "40 / 39,50", "satış / alış · TL", "lira", "Merkez")],
         [("GÜMRÜK VERGİSİ", "%5", "gv", "Gümrük"), ("KKDF", "%6", "igv", "KKDF"), ("KDV", "%20", "kdv", "KDV"),
          ("SATIŞ KURU", "40 TL", "acc", "satış"), ("ALIŞ KURU", "39,50 TL", "acc", "alış")],
         dict(char="cano", bubble="Tek kur yeter, <i>değil mi?</i>", at="firması", at_bub="alış"),
         ("İstenen: ithalatta ödenecek <b>KDV</b> = ? <em>TL</em>", "Soru"))

options("s03", [("A", "268.800"), ("B", "283.020"), ("C", "283.200"), ("D", "283.731"), ("E", "283.968")], "TL")

keys("s04", [("lira", "Kıymet: satış kuru", "Gümrük kıymeti <b>TCMB döviz satış kuru</b> ile TL'ye çevrilir", "GK md. 30", "Bir", "çevrilir"),
             ("percent", "KKDF: fatura + alış kuru", "<b>Fatura bedeli</b> × %6 × <b>döviz alış kuru</b>; GV matrahına girmez", "KKDF %6", "İki", "girmez"),
             ("arrow", "KDV matrahına ekle", "İthalatta ödenen fon → <b>KDV matrahına</b> girer", "KDV K. md. 21", ("üç", 2), "eklenir")],
     ["kıymet (satış kuru)", "GV", "KKDF (alış kuru)", "KDV"])

calc("s05", 1, "ADIM 1 · KIYMET VE GV",
     [("CIF", "30.000 + 1.500 + 500 $", 32000, "k", "Otuz", ("otuz", 2)),
      ("KIYMET (TL)", "32.000 × 40 (satış)", 1280000, "m", "Satış", "milyon"),
      ("GV", "1.280.000 × %5", 64000, "g", ("gümrük", 3), "altmış")],
     side=("ledger", [("Kıymet", "1.280.000", ""), ("GV", "64.000", "")], ["milyon", "altmış"], "TL"), at_start="Birinci",
     note=("Kıymet ve vergiler için <b>satış kuru</b> kullanılır.", "Satış"))

calc("s06", 2, "ADIM 2 · KKDF",
     [("MATRAH", "fatura bedeli (FOB)", 30000, "k", "Matrah", "otuz"),
      ("KKDF ($)", "30.000 × %6", 1800, "r", "Yüzde", ("bin", 2)),
      ("KKDF (TL)", "1.800 × 39,50 (alış)", 71100, "o", "çarpı", "yetmiş")],
     side=("law", "KKDF", "ÖZET KURAL",
           "KKDF <b>fatura bedeli</b> üzerinden hesaplanır; TL karşılığı <b>TCMB döviz alış kuru</b> ile bulunur. Gümrük vergisi matrahına girmez.", "Matrah"),
     dik=("dikkat", "alış"), at_start="İkinci",
     note=("Kıymette <b>satış kuru</b>, KKDF'de <em>alış kuru</em>: aynı soruda iki ayrı kur!", "alış"))

calc("s07", 3, "ADIM 3 · KDV",
     [("KIYMET + GV", "1.280.000 + 64.000", 1344000, "k", "matrahı", ("artı", 1)),
      ("+ KKDF", "alış kuruyla", 71100, "o", ("artı", 2), "yetmiş"),
      ("KDV MATRAHI", "1.344.000 + 71.100", 1415100, "m", ("bir", 3), ("dört", 2)),
      ("KDV", "1.415.100 × %20", 283020, "d", "Bunun", ("iki", 2))],
     side=("ledger", [("Kıymet", "1.280.000", ""), ("GV", "64.000", ""), ("KKDF", "71.100", ""), ("KDV", "283.020", "")],
           [None, None, None, ("iki", 2)], "TL"),
     dik=("dikkat", ("artı", 2)), at_start="Üçüncü")

result("s08", [("Gümrük kıymeti", "32.000 $ × 40", "1.280.000", "KDV"), ("Gümrük vergisi", "%5", "64.000", "KDV"),
               ("KKDF", "1.800 $ × 39,50", "71.100", "KDV"), ("KDV matrahı", "toplam", "1.415.100", ("bir", 1))],
       (283020, 0), "Türk lirası · %20", [("A", "268.800"), ("B", "283.020"), ("C", "283.200"), ("D", "283.731"), ("E", "283.968")], "B",
       sub="SORU · İTHALATTA KDV", at=dict(son="sonuç", od="yüzde", cnt=("iki", 1), dogru="Doğru", L="B"), total_label="KDV")

traps("s09", [("A", "268.800", "KKDF, KDV matrahına eklenmedi", [("KDV m.: 1.280.000 + 64.000", "1.344.000", ""), ("× %20", "268.800", "")], "268.800"),
              ("C", "283.200", "KKDF satış kuruyla çevrildi", [("KKDF: 1.800 × 40", "72.000", ""), ("KDV m.", "1.416.000", "")], "283.200"),
              ("D", "283.731", "KKDF, GV matrahına da katıldı", [("GV: 1.351.100 × %5", "67.555", ""), ("KDV m.", "1.418.655", "")], "283.731"),
              ("E", "283.968", "KKDF CIF üzerinden hesaplandı", [("KKDF: 1.920 × 39,50", "75.840", ""), ("KDV m.", "1.419.840", "")], "283.968")],
      "TL", "Doğrusu <i>B: 283.020 TL!</i>",
      at=[(("KKDF'yi", 1), "A"), (("KKDF'yi", 2), "C"), (("KKDF'yi", 3), "D"), (("KKDF'yi", 4), "E")])

warn("s10", "KKDF HER İTHALATTA YOK",
     dict(head="KKDF HANGİ ÖDEMEDE?", ref="VADELİ İTHALAT",
          conds=[("<b>Kabul kredili</b> ödeme", "kabul"), ("<b>Vadeli akreditif</b>", "vadeli"), ("<b>Mal mukabili</b>", "mal")],
          res=None, at="KKDF", at_res=None),
     dict(head="KKDF NEREYE GİRER?", items=[("pv", "Kıymet / GV matrahı", "GİRMEZ", "✗", "girmez"), ("pc", "KDV matrahı", "EKLENİR", "✓", "eklenir")],
          at=("Bir", 2)),
     dict(char="cano", bubble="Peşin ödedik, <em>KKDF var mı?</em>", at="uyarı", at_bub="Peşin"), hayir="değil")

coach("s11", dict(head="İKİ KUR, İKİ İŞ", icon="lira", at="Aynı",
                  opts=[("ok", "Kıymet + vergiler → satış kuru", "GK md. 30", "satış"), ("ok", "KKDF → alış kuru", "FON", "alış"),
                        ("ok", "KKDF matrahı → fatura bedeli", "CIF / FOB", "fatura")]),
      dict(head="TESLİM ŞEKLİ", big="CIF ise CIF, <em>FOB ise FOB</em>", p="KKDF faturadaki bedel üzerinden; navlun ayrıca eklenmez.",
           ref="KKDF · fatura bedeli", at="teslim", at_pulse=("FOB", 1)),
      [("Kıymet: satış kuru", "lira", "Kıymeti"), ("GV'yi hesapla", "percent", ("gümrük", 2)), ("KKDF: alış kuru", "calc", "KKDF'yi"),
       ("KDV matrahına ekle", "arrow", "hepsini"), ("KDV'yi hesapla", "check", "KDV'yi")])

closing("s12", "ÖZET · KKDF VE KDV",
        [("Kıymet + GV (satış kuru)", "1.280.000 + 64.000 TL", "Kıymet"), ("KKDF (alış kuru)", "30.000 × %6 × 39,50 = 71.100", "KKDF")],
        ("B", "283.020", "TL"), ("lira", "Satış kuru ≠ alış kuru<br/><em>iki ayrı kur</em>", "Hepsi"))
