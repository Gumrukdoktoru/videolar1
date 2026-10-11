"""Vergi Hesaplama Dersi 13: dampinge karşı vergi — menşeye göre (yükleme ülkesine göre değil), kg başına net ağırlık; GV matrahına girmez, KDV matrahına girer."""
import hkit
from hkit import S, intro, question, options, keys, calc, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["GV", "DAMPİNG", "KDV", "SONUÇ"]
OPTS = [("A", "1.210.880"), ("B", "1.226.880"), ("C", "1.232.480"), ("D", "1.233.920"), ("E", "1.498.880")]

intro("s01", 13, "üçüncüsüne", "KONU · DAMPİNGE KARŞI VERGİ", "Önlem <em>menşeye</em> göre",
      [("Yükleme ülkesi", "yüklenmiş"), ("Menşe ülke", "malı"), ("Hangi önlem?", "önlemi"), ("Net / brüt kg", "ağırlık")],
      "Hangi ülkenin <b>önlemi</b> uygulanır?", art="globe", at_qq="Hangi", at_tz="ağırlık")

question("s02", "Polyester elyafta damping",
         dict(icon="ship", head="D firması · polyester elyaf", sub="yükleme: <em>Malezya</em> · menşe: <em>Çin</em>",
              stamp="MENŞE<br/>ÇİN", at="firması", at_stamp="menşe"),
         [("CIF KIYMET", "64.000 $", "kur <b>40 TL</b>", "doc", "CIF"),
          ("NET AĞIRLIK", "40.000 kg", "brüt <b>41.500 kg</b>", "scale", "Net"),
          ("TESCİL SONRASI", "2.000 $", "fabrikaya <b>nakliye</b>", "truck", "Tescilden")],
         [("GÜMRÜK VERGİSİ", "%4", "gv", "Gümrük"), ("DAMPİNG · ÇİN", "0,30 $", "igv", ("Çin", 2)),
          ("DAMPİNG · MALEZYA", "0,45 $", "usd", "Malezya"), ("KDV", "%20", "kdv", "KDV")],
         dict(char="yardimci", bubble="Malezya'dan geldi, <i>Malezya oranı?</i>", at="firması", at_bub="Malezya"),
         ("İstenen: <b>GV + dampinge karşı vergi + KDV</b> = ? <em>TL</em>", "Soru"))

options("s03", OPTS, "TL")

keys("s04", [("globe", "Menşe belirler", "Önlem <b>menşeye</b> göre — yüklendiği ülkeye göre değil", "MENŞE", "Bir", "değil"),
             ("scale", "Net ağırlık", "Kilogram başına tutar <b>net ağırlıkla</b> çarpılır", "NET KG", "İki", "net"),
             ("layers", "Matrah", "GV matrahına <b>girmez</b> · KDV matrahına <b>eklenir</b>; tescil sonrası gider <b>girmez</b>", "KDV K. md. 21", ("üç", 2), "tescilden")],
     ["menşe", "GV", "damping × net kg", "KDV"])

calc("s05", 1, "ADIM 1 · GÜMRÜK VERGİSİ",
     [("GV", "64.000 $ × %4", 2560, "g", "Altmış", "iki")],
     side=("ledger", [("GV", "2.560 $", "")], ["iki"], "$"), at_start="Birinci",
     note=("Dampinge karşı vergi GV matrahına <em>girmez</em>.", "Dampinge"))

calc("s06", 2, "ADIM 2 · DAMPİNGE KARŞI VERGİ",
     [("ORAN · $/KG", "menşe Çin", 0.3, "o", "Çin", ("otuz", 1), 2),
      ("DAMPİNG", "40.000 kg × 0,30 $", 12000, "r", "Net", ("on", 1))],
     side=("law", "MENŞE ŞAHADETNAMESİ", "ÇİN", "Yükleme: <b>Malezya</b><br/>Menşe: <b>Çin</b><br/>→ <b>Çin oranı</b> uygulanır", "Malezya'dan"),
     dik=("dikkat", "menşei"), at_start="İkinci",
     note=("Kilogram başına tutar × <b>net ağırlık</b>.", "Net"))

calc("s07", 3, "ADIM 3 · KDV",
     [("KDV MATRAHI", "64.000 + 2.560 + 12.000", 78560, "m", ("KDV", 2), "yetmiş"),
      ("KDV", "78.560 × %20", 15712, "d", "Yüzde", ("beş", 3))],
     side=("ledger", [("GV", "2.560", ""), ("Damping", "12.000", ""), ("KDV", "15.712", "")], [None, None, ("beş", 3)], "$"),
     dik=("dikkat", "Tescilden"), at_start="Üçüncü",
     note=("Tescil sonrası nakliye (2.000 $) KDV matrahına <em>girmez</em>.", "Tescilden"))

result("s08", [("Gümrük vergisi", "64.000 × %4", "2.560 $", "iki"), ("Dampinge karşı vergi", "40.000 kg × 0,30", "12.000 $", ("artı", 1)),
               ("KDV", "78.560 × %20", "15.712 $", ("artı", 2)), ("Toplam × kur", "30.272 $ × 40", "30.272 $", "toplam")],
       (1210880, 0), "Türk lirası", OPTS, "A",
       sub="SORU · GV + DAMPİNG + KDV", at=dict(son="sonuç", od="Kırk", cnt="bir", dogru="Doğru", L="A"))

traps("s09", [("B", "1.226.880", "Tescil sonrası nakliye KDV matrahına eklendi", [("KDV: 80.560 × %20", "16.112 $", ""), ("Toplam", "30.672 $", "")], "1.226.880"),
              ("C", "1.232.480", "Brüt ağırlık kullanıldı", [("Damping: 41.500 × 0,30", "12.450 $", ""), ("KDV: 79.010 × %20", "15.802 $", "")], "1.232.480"),
              ("D", "1.233.920", "Damping GV matrahına katıldı", [("GV: 76.000 × %4", "3.040 $", ""), ("KDV: 79.040 × %20", "15.808 $", "")], "1.233.920"),
              ("E", "1.498.880", "Yükleme ülkesinin (Malezya) oranı", [("Damping: 40.000 × 0,45", "18.000 $", ""), ("KDV: 84.560 × %20", "16.912 $", "")], "1.498.880")],
      "TL", "Doğrusu <i>A: 1.210.880 TL!</i>",
      at=[("Tescilden", "B"), ("Brüt", "C"), ("Dampinge", "D"), ("Yükleme", "E")])

warn("s10", "DAMPİNGE KARŞI VERGİ",
     dict(head="ÖNLEM HANGİ ÜLKEYE?", ref="MENŞE",
          conds=[("Yükleme ülkesi önlemsiz, <b>menşe önlemli</b> → vergi <b>alınır</b>", "Eşya"),
                 ("Önlem yalnız yükleme ülkesine, <b>menşe başka</b> → <b>uygulanmaz</b>", "Tersi")],
          res=None, at="Önlemin", at_res=None),
     dict(head="ÖNLEM NASIL KONULUR?", items=[("pc", "Kıymetin yüzdesi olarak", "NİSPİ", "%", "kıymetin"),
                                            ("pc", "Kilogram başına tutar", "MAKTU", "$/kg", "kilogram")],
          at=("Bir", 4)),
     dict(char="yardimci", bubble="Malezya'dan geldiyse <em>Malezya</em> önlemi?", at="uyarı", at_bub="Önlemin"), hayir="şahadetnamesi")

coach("s11", dict(head="NEREYE BAKILIR?", icon="search", at="Dampinge",
                  opts=[("ok", "Menşe şahadetnamesi", "MENŞE", "menşe"), ("no", "Konşimento", "YÜKLEME", "konşimentoya"),
                        ("ok", "Net ağırlık", "kg × tutar", "Kilogram")]),
      dict(head="ÖNEMLİ OLAN", big="Nerede <em>üretildi?</em>", p="Malın nereden geldiği değil, nerede üretildiği önemlidir.",
           ref="Gümrük Koçu ders notu", at="Malın", at_pulse="üretildiği"),
      [("Menşei belirle", "globe", "Menşei"), ("GV'yi hesapla", "percent", "gümrük"), ("Damping × net kg", "scale", ("dampinge", 2)),
       ("KDV matrahına ekle", "layers", "KDV"), ("KDV'yi hesapla", "check", "KDV'yi")])

closing("s12", "ÖZET · DAMPİNGE KARŞI VERGİ",
        [("GV + damping", "2.560 + 12.000 = 14.560 $", "Gümrük"), ("KDV", "78.560 × %20 = 15.712 $", "KDV")],
        ("A", "1.210.880", "TL"), ("globe", "Menşe <em>Çin</em> · net kg<br/>30.272 $ × 40", "Toplam"))
