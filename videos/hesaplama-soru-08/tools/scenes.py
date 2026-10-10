"""Vergi Hesaplama Dersi 8: vergi zinciri — GV → TRT bandrol → ÖTV → KDV; her vergi bir sonrakinin matrahına girer."""
import hkit
from hkit import S, intro, question, options, keys, calc, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["KIYMET + GV", "BANDROL + ÖTV", "KDV", "SONUÇ"]

intro("s01", 8, "sekizincisine", "KONU · VERGİ ZİNCİRİ", "GV → bandrol → <em>ÖTV → KDV</em>",
      [("GV", "zinciri"), ("TRT bandrol", "TRT"), ("ÖTV", "özel"), ("KDV", "KDV")],
      "Sırayı <b>karıştırma!</b>", art="layers", at_qq="Sırayı", at_tz="değişir")

question("s02", "Dört vergilik zincir",
         dict(icon="chip", head="M firması · 100 cep telefonu", sub="menşe: <em>Çin</em> · CIF <em>20.000 $</em>",
              stamp="4 VERGİ<br/>ZİNCİRİ", at="firması", at_stamp="Gümrük"),
         [("ADET", "100", "cep telefonu", "chip", "yüz"), ("CIF KIYMET", "20.000 $", "= gümrük kıymeti", "doc", "CIF"),
          ("KUR", "40 TL", "1 $ = 40 TL", "lira", "kur")],
         [("GÜMRÜK VERGİSİ", "%5", "gv", "Gümrük"), ("TRT BANDROL", "%10", "igv", "TRT"), ("ÖTV", "%20", "acc", "özel"), ("KDV", "%20", "kdv", "KDV")],
         dict(char="yardimci", bubble="Hepsini kıymetten <i>hesaplasak?</i>", at="firması", at_bub="TRT"),
         ("İstenen: <b>GV + bandrol + ÖTV + KDV</b> = ? <em>TL</em>", "Soru"))

options("s03", [("A", "467.200"), ("B", "493.600"), ("C", "510.400"), ("D", "524.800"), ("E", "530.560")], "TL")

keys("s04", [("sort", "Sıra sabit", "GV → <b>bandrol</b> → <b>ÖTV</b> → KDV (en son)", "HESAP SIRASI", "Bir", "KDV"),
             ("radio", "Bandrol matrahı", "<b>ÖTV hariç KDV matrahı</b> = kıymet + GV", "TRT bandrol", "İki", ("vergisi", 2)),
             ("layers", "Zincir", "Her vergi <b>bir sonrakinin</b> matrahına girer", "KDV K. md. 21", ("üç", 2), "girer")],
     ["kıymet", "GV", "bandrol", "ÖTV", "KDV"])

calc("s05", 1, "ADIM 1 · KIYMET VE GV",
     [("KIYMET", "20.000 $ × 40", 800000, "k", "Yirmi", "sekiz"),
      ("GV", "800.000 × %5", 40000, "g", ("gümrük", 2), ("kırk", 2))],
     side=("ledger", [("Kıymet", "800.000", ""), ("GV", "40.000", "")], ["sekiz", ("kırk", 2)], "TL"), at_start="Birinci",
     note=("Gümrük vergisinin matrahı yalnızca <b>gümrük kıymeti</b>dir.", ("gümrük", 2)))

calc("s06", 2, "ADIM 2 · BANDROL VE ÖTV",
     [("BANDROL MATR.", "800.000 + 40.000", 840000, "m", ("bandrol", 2), ("sekiz", 2)),
      ("BANDROL", "840.000 × %10", 84000, "r", ("yüzde", 1), "seksen"),
      ("ÖTV MATR.", "840.000 + 84.000", 924000, "m", ("ÖTV", 2), "dokuz"),
      ("ÖTV", "924.000 × %20", 184800, "o", ("yüzde", 2), "yirmisi")],
     side=("ledger", [("Kıymet", "800.000", ""), ("GV", "40.000", ""), ("Bandrol", "84.000", ""), ("ÖTV", "184.800", "")],
           [None, None, "seksen", "yirmisi"], "TL"),
     dik=("dikkat", ("ÖTV", 2)), at_start="İkinci")

calc("s07", 3, "ADIM 3 · KDV",
     [("KDV MATRAHI", "924.000 + 184.800", 1108800, "m", ("KDV", 2), "milyon"),
      ("KDV", "1.108.800 × %20", 221760, "d", "Yüzde", ("iki", 1))],
     side=("ledger", [("GV", "40.000", ""), ("Bandrol", "84.000", ""), ("ÖTV", "184.800", ""), ("KDV", "221.760", "")],
           [None, None, None, ("iki", 1)], "TL"),
     dik=("dikkat", ("ÖTV", 1)), at_start="Üçüncü",
     note=("KDV matrahı = kıymet + GV + bandrol + <b>ÖTV</b>: KDV hep en sonda.", ("KDV", 2)))

result("s08", [("Gümrük vergisi", "800.000 × %5", "40.000", "kırk"), ("TRT bandrol", "840.000 × %10", "84.000", ("artı", 1)),
               ("ÖTV", "924.000 × %20", "184.800", ("artı", 2)), ("KDV", "1.108.800 × %20", "221.760", ("artı", 3))],
       (530560, 0), "Türk lirası", [("A", "467.200"), ("B", "493.600"), ("C", "510.400"), ("D", "524.800"), ("E", "530.560")], "E",
       sub="SORU · GV + BANDROL + ÖTV + KDV", at=dict(son="sonuç", od="Ödenecek", cnt="beş", dogru="Doğru", L="E"))

traps("s09", [("A", "467.200", "GV hiç hesaplanmadı", [("Bandrol: 800.000 × %10", "80.000", ""), ("ÖTV: 880.000 × %20", "176.000", "")], "467.200"),
              ("B", "493.600", "ÖTV, KDV matrahına eklenmedi", [("KDV: 924.000 × %20", "184.800", ""), ("GV + bandrol + ÖTV", "308.800", "")], "493.600"),
              ("C", "510.400", "Bandrol, ÖTV matrahına eklenmedi", [("ÖTV: 840.000 × %20", "168.000", ""), ("KDV: 1.092.000 × %20", "218.400", "")], "510.400"),
              ("D", "524.800", "GV, bandrol matrahına eklenmedi", [("Bandrol: 800.000 × %10", "80.000", ""), ("ÖTV: 920.000 × %20", "184.000", "")], "524.800")],
      "TL", "Doğrusu <i>E: 530.560 TL!</i>",
      at=[("Gümrük", "A"), ("ÖTV'yi", "B"), ("Bandrolü", "C"), ("Bandrol", "D")])

warn("s10", "MATRAH ZİNCİRİ",
     dict(head="KİM KİMİN MATRAHINA GİRER?", ref="SIRA",
          conds=[("Bandrol matrahı = kıymet + GV <b>(ÖTV yok)</b>", "TRT"), ("ÖTV matrahı = … + bandrol <b>(KDV yok)</b>", ("ÖTV", 2)),
                 ("KDV matrahı = … + ÖTV <b>(en son)</b>", "Kural")],
          res=None, at="TRT", at_res=None),
     dict(head="KDV NEREYE GİRER?", items=[("pv", "Başka bir vergi matrahına", "GİRMEZ", "✗", "hiçbir"), ("pc", "Kendisi en son hesaplanır", "EN SON", "KDV", "son")],
          at=("Bir", 2)),
     dict(char="yardimci", bubble="Bandrolü <em>ÖTV'den sonra</em> mı hesaplasak?", at="uyarı", at_bub="çünkü"), hayir="önce")

coach("s11", dict(head="MERDİVEN", icon="layers", at="Vergi",
                  opts=[("ok", "Kıymet → en alt basamak", "1", "Kıymet"), ("ok", "GV → bandrol → ÖTV", "2 · 3 · 4", "basamak"),
                        ("ok", "KDV → en üst basamak", "5", "KDV")]),
      dict(head="SIRA BOZULURSA", big="Matrah <em>değişir</em>", p="Bandrol ÖTV'den önce; KDV her zaman en sonda hesaplanır.",
           ref="Gümrük Koçu ders notu", at="altındaki", at_pulse="üstte"),
      [("Kıymeti bul", "doc", "Kıymeti"), ("GV'yi ekle", "percent", "gümrük"), ("Bandrolü hesapla", "radio", "bandrolü"),
       ("ÖTV'yi hesapla", "calc", "ÖTV'yi"), ("KDV en son", "check", "KDV'yi")])

closing("s12", "ÖZET · VERGİ ZİNCİRİ",
        [("GV + bandrol", "40.000 + 84.000 = 124.000 TL", "Gümrük"), ("ÖTV + KDV", "184.800 + 221.760 = 406.560 TL", "ÖTV")],
        ("E", "530.560", "TL"), ("layers", "Sıra: GV → bandrol<br/>→ ÖTV → <em>KDV</em>", "Toplam"))
