"""Vergi Hesaplama Dersi 9: tarım payı — bileşim kodu, T1/T2 tutarı, 100 kg net ağırlık; GV matrahına girmez, KDV matrahına girer."""
import hkit
from hkit import S, intro, question, options, keys, calc, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["KIYMET + GV", "TARIM PAYI", "KDV", "SONUÇ"]
OPTS = [("A", "277.290"), ("B", "311.040"), ("C", "321.840"), ("D", "327.780"), ("E", "331.344")]

intro("s01", 9, "dokuzuncusuna", "KONU · TARIM PAYI", "Bileşim kodu → <em>T1 / T2</em>",
      [("Bileşim kodu", "bileşim"), ("T1 / T2", "te"), ("Net kg", "net"), ("KDV matrahı", "KDV")],
      "Küçük bir seçim, <b>sonucu değiştirir!</b>", art="wheat", at_qq="Küçük", at_tz="değiştirir")

question("s02", "Gofrette tarım payı",
         dict(icon="box", head="B firması · gofret", sub="menşe: <em>Malezya</em> · CIF <em>24.000 €</em>",
              stamp="BİLEŞİM<br/>KODU 7225", at="firması", at_stamp="Bileşim"),
         [("NET AĞIRLIK", "6.000 kg", "brüt <b>6.300 kg</b>", "scale", "Net"),
          ("TARIM PAYI / 100 KG", "T1 40 €", "T2 <b>25 €</b>", "wheat", ("te", 1)),
          ("KUR", "45 TL", "1 € = 45 TL", "lira", "kur")],
         [("GÜMRÜK VERGİSİ", "%8", "gv", "Gümrük"), ("T1 TUTARI", "40 €", "acc", ("te", 1)), ("T2 TUTARI", "25 €", "usd", ("te", 2)),
          ("KDV", "%10", "kdv", "KDV")],
         dict(char="cano", bubble="Brüt ağırlığı mı <i>alsak?</i>", at="firması", at_bub="brüt"),
         ("İstenen: <b>GV + tarım payı + KDV</b> = ? <em>TL</em>", "Soru"))

options("s03", OPTS, "TL")

keys("s04", [("globe", "Menşe belirler", "AB menşeli → <b>T2</b> · diğer ülkeler → <b>T1</b>", "BİLEŞİM KODU", "Bir", "uygulanır"),
             ("scale", "Net ağırlık", "Tutar <b>her 100 kg net</b> için verilir; brüt kullanılmaz", "100 KG NET", "İki", "kullanılmaz"),
             ("layers", "Matrah", "GV matrahına <b>girmez</b> · KDV matrahına <b>eklenir</b>", "KDV K. md. 21", ("üç", 2), "eklenir")],
     ["kıymet", "GV", "tarım payı", "KDV"])

calc("s05", 1, "ADIM 1 · KIYMET VE GV",
     [("KIYMET", "24.000 € × 45", 1080000, "k", "Yirmi", "milyon"),
      ("GV", "1.080.000 × %8", 86400, "g", ("gümrük", 2), ("seksen", 2))],
     side=("ledger", [("Kıymet", "1.080.000", ""), ("GV", "86.400", "")], ["milyon", ("seksen", 2)], "TL"), at_start="Birinci",
     note=("Tarım payı gümrük vergisi matrahına <em>girmez</em>.", "Tarım"))

calc("s06", 2, "ADIM 2 · TARIM PAYI",
     [("BİRİM", "6.000 kg ÷ 100", 60, "m", "Net", ("altmış", 1)),
      ("TARIM PAYI €", "60 × 40 €", 2400, "r", ("altmış", 2), "iki"),
      ("TARIM PAYI TL", "2.400 € × 45", 108000, "o", ("kırk", 3), "sekiz")],
     side=("law", "BİLEŞİM KODU 7225", "T1 · AB DIŞI", "Menşe <b>Malezya</b> → AB dışı → <b>T1 = 40 €</b><br/>her <b>100 kg net</b> için", "Malezya"),
     dik=("dikkat", ("te", 1)), at_start="İkinci")

calc("s07", 3, "ADIM 3 · KDV",
     [("KIYMET + GV", "1.080.000 + 86.400", 1166400, "m", ("KDV", 2), "altı"),
      ("+ TARIM PAYI", "1.166.400 + 108.000", 1274400, "m", "tarım", ("milyon", 2)),
      ("KDV", "1.274.400 × %10", 127440, "d", "Yüzde", "kırk")],
     side=("ledger", [("GV", "86.400", ""), ("Tarım payı", "108.000", ""), ("KDV", "127.440", "")], [None, None, "kırk"], "TL"),
     dik=("dikkat", "tarım"), at_start="Üçüncü",
     note=("Tarım payı KDV matrahına <b>eklenir</b>.", ("milyon", 2)))

result("s08", [("Gümrük vergisi", "1.080.000 × %8", "86.400", "seksen"), ("Tarım payı", "60 × 40 € × 45", "108.000", ("artı", 1)),
               ("KDV", "1.274.400 × %10", "127.440", ("artı", 2))],
       (321840, 0), "Türk lirası", OPTS, "C",
       sub="SORU · GV + TARIM PAYI + KDV", at=dict(son="sonuç", od="Ödenecek", cnt="üç", dogru="Doğru", L="C"))

traps("s09", [("A", "277.290", "AB'ye ait T2 tutarı kullanıldı", [("TP: 60 × 25 € × 45", "67.500", ""), ("KDV: 1.233.900 × %10", "123.390", "")], "277.290"),
              ("B", "311.040", "Tarım payı KDV matrahına eklenmedi", [("Tarım payı", "108.000", ""), ("KDV: 1.166.400 × %10", "116.640", "")], "311.040"),
              ("D", "327.780", "Brüt ağırlık kullanıldı", [("TP: 63 × 40 € × 45", "113.400", ""), ("KDV: 1.279.800 × %10", "127.980", "")], "327.780"),
              ("E", "331.344", "Tarım payı GV matrahına da katıldı", [("GV: 1.188.000 × %8", "95.040", ""), ("KDV: 1.283.040 × %10", "128.304", "")], "331.344")],
      "TL", "Doğrusu <i>C: 321.840 TL!</i>",
      at=[("Avrupa", "A"), ("Tarım", "B"), ("Brüt", "D"), (("tarım", 2), "E")])

warn("s10", "BİLEŞİM KODU",
     dict(head="BİLEŞİM KODU NASIL BULUNUR?", ref="TABLO",
          conds=[("<b>Süt yağı</b> ve <b>süt proteini</b> oranı", "süt"), ("<b>Nişasta</b> ve <b>şeker</b> oranı", "nişasta")],
          res="Oranlar → <b>BİLEŞİM KODU</b>", at="Bileşim", at_res="seçilir"),
     dict(head="AB MENŞELİ EŞYADA", items=[("pv", "Gümrük vergisi sıfır olsa bile", "GV %0", "AB", "sıfır"),
                                         ("pc", "Tarım payı yine alınır", "ALINIR", "T2", "yine")],
          at=("Bir", 2)),
     dict(char="cano", bubble="GV sıfırsa tarım payı da <em>sıfır</em> mı?", at="uyarı", at_bub="Avrupa"), hayir="yine")

coach("s11", dict(head="TARIMDA 3 SORU", icon="question", at="Tarım",
                  opts=[("ok", "Eşya nereli?", "AB → T2 · diğer → T1", "nereli"), ("ok", "Ağırlık net mi?", "100 kg net", "Ağırlık"),
                        ("ok", "Nereye girer?", "KDV matrahı", "Nereye")]),
      dict(head="UNUTMA", big="GV'ye <em>girmez</em>", p="Tarım payı gümrük vergisi matrahına değil, KDV matrahına eklenir.",
           ref="Gümrük Koçu ders notu", at="Nereye", at_pulse="değil"),
      [("Kıymeti bul", "doc", "Kıymeti"), ("GV'yi hesapla", "percent", ("gümrük", 2)), ("Bileşim kodu", "wheat", "bileşim"),
       ("Net ÷ 100 × tutar", "scale", ("net", 3)), ("KDV'ye ekle", "check", "hepsini")])

closing("s12", "ÖZET · TARIM PAYI",
        [("GV + tarım payı", "86.400 + 108.000 = 194.400 TL", "Gümrük"), ("KDV", "1.274.400 × %10 = 127.440 TL", "KDV")],
        ("C", "321.840", "TL"), ("wheat", "Net kg ÷ 100 × <em>T1</em><br/>→ KDV matrahına", "Toplam"))
