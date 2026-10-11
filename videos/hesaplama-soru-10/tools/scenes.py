"""Vergi Hesaplama Dersi 10: ÖTV (III) sayılı liste (A) — bira ve şarap; nispi vergi ile asgari maktu vergiden yüksek olan."""
import hkit
from hkit import S, intro, question, options, keys, calc, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["LİTRE", "BİRA", "ŞARAP", "SONUÇ"]
OPTS = [("A", "112.800"), ("B", "124.500"), ("C", "189.000"), ("D", "200.700"), ("E", "313.500")]

intro("s01", 10, "onuncusuna", "KONU · ÖTV (III) SAYILI LİSTE (A)", "Nispi ↔ <em>asgari maktu</em>",
      [("Nispi %", "nispi"), ("Asgari maktu", "asgari"), ("Bira ≠ şarap", "Bira"), ("Yüksek olan", "yüksekse")],
      "<b>Hangisi yüksekse</b> o alınır!", art="bottle", at_qq="Hangisi", at_tz="aynı")

question("s02", "Bira ve şarapta ÖTV",
         dict(icon="bottle", head="R firması · tek beyanname", sub="<em>bira</em> + <em>şarap</em> · ÖTV (III) sayılı liste (A)",
              stamp="2 ÜRÜN<br/>1 BEYANNAME", at="firması", at_stamp="aynı"),
         [("BİRA", "12.000 kutu", "33 cl · <b>%5</b> alkol · <b>5 TL</b> / kutu", "bottle", "Birincisi"),
          ("ŞARAP", "4.000 şişe", "75 cl · <b>%13</b> alkol · <b>60 TL</b> / şişe", "bottle", "İkincisi")],
         [("NİSPİ ÖTV", "%63", "gv", "Nispi"), ("AMV · BİRA", "2,50 TL", "acc", ("bira", 2)), ("AMV · ŞARAP", "25 TL", "usd", ("şarap", 2))],
         dict(char="stajyer", bubble="Nispi ile maktuyu <i>toplasak?</i>", at="firması", at_bub="Nispi"),
         ("İstenen: <b>toplam ÖTV</b> = ? <em>TL</em>", "Soru"))

options("s03", OPTS, "TL")

keys("s04", [("scale", "Yüksek olan alınır", "Nispi ve asgari maktu <b>ayrı ayrı</b> hesaplanır; <b>yüksek olan</b> alınır", "YÜKSEK OLAN", "Bir", "yüksekse"),
             ("bottle", "Formül içkiye göre", "Bira: L × <b>derece</b> × tutar · Şarap: L × tutar (<b>derece yok</b>)", "III-A CETVELİ", "İki", "Şarapta"),
             ("ruler", "Birim", "<b>100 cl = 1 L</b> · 33 cl = 0,33 L · 75 cl = 0,75 L", "cl → L", ("üç", 2), "santilitre")],
     ["cl → L", "nispi", "asgari maktu", "yüksek olan", "topla"])

calc("s05", 1, "ADIM 1 · LİTRE",
     [("BİRA", "0,33 L × 12.000", 3960, "k", "Bira", ("üç", 2)),
      ("ŞARAP", "0,75 L × 4.000", 3000, "k", "Şarap", ("üç", 3))],
     side=("ledger", [("Bira", "3.960 L", ""), ("Şarap", "3.000 L", "")], [("üç", 2), ("üç", 3)], "LİTRE"), at_start="Birinci",
     note=("<b>100 cl = 1 L</b>: 33 cl = 0,33 L · 75 cl = 0,75 L", "Bira"))

calc("s06", 2, "ADIM 2 · BİRA",
     [("NİSPİ MATRAH", "12.000 × 5 TL", 60000, "m", "Nispi", ("altmış", 1)),
      ("NİSPİ ÖTV", "60.000 × %63", 37800, "r", "yüzde", "otuz"),
      ("ASGARİ MAKTU", "3.960 × 5° × 2,50", 49500, "o", "Asgari", ("kırk", 1))],
     side=("ledger", [("Nispi ÖTV", "37.800", "out"), ("Asgari maktu", "49.500", ""), ("Bira ÖTV", "49.500", "q")],
           ["otuz", ("kırk", 1), ("kırk", 2)], "TL"),
     dik=("dikkat", "derece"), at_start="İkinci",
     note=("Birada <b>derece</b> çarpılır · asgari maktu <b>daha yüksek</b>", ("Asgari", 2)))

calc("s07", 3, "ADIM 3 · ŞARAP",
     [("NİSPİ MATRAH", "4.000 × 60 TL", 240000, "m", "Nispi", ("kırk", 1)),
      ("NİSPİ ÖTV", "240.000 × %63", 151200, "r", "yüzde", "elli"),
      ("ASGARİ MAKTU", "3.000 L × 25 TL", 75000, "o", "Asgari", ("yetmiş", 1))],
     side=("ledger", [("Nispi ÖTV", "151.200", ""), ("Asgari maktu", "75.000", "out"), ("Şarap ÖTV", "151.200", "q")],
           ["elli", ("yetmiş", 1), ("elli", 2)], "TL"),
     dik=("dikkat", "derecesi"), at_start="Üçüncü",
     note=("Şarapta derece <em>çarpılmaz</em> · bu kez <b>nispi</b> daha yüksek", "derecesi"))

result("s08", [("Bira · asgari maktu", "3.960 × 5 × 2,50", "49.500", "birada"), ("Şarap · nispi", "240.000 × %63", "151.200", "şarapta")],
       (200700, 0), "Türk lirası", OPTS, "D",
       sub="SORU · TOPLAM ÖTV", at=dict(son="sonuç", od="Ödenecek", cnt=("iki", 2), dogru="Doğru", L="D"))

traps("s09", [("A", "112.800", "Her üründe düşük olan alındı", [("Bira · nispi", "37.800", ""), ("Şarap · asgari maktu", "75.000", "")], "112.800"),
              ("B", "124.500", "İkisinde de asgari maktu alındı", [("Bira · asgari maktu", "49.500", ""), ("Şarap · asgari maktu", "75.000", "")], "124.500"),
              ("C", "189.000", "İkisinde de nispi (ya da birada derece unutuldu)", [("Bira · nispi", "37.800", ""), ("Şarap · nispi", "151.200", "")], "189.000"),
              ("E", "313.500", "Nispi ile asgari maktu toplandı", [("Bira: 37.800 + 49.500", "87.300", ""), ("Şarap: 151.200 + 75.000", "226.200", "")], "313.500")],
      "TL", "Doğrusu <i>D: 200.700 TL!</i>",
      at=[(("Her", 2), "A"), (("İki", 2), "B"), (("İki", 3), "C"), ("toplayan", "E")])

warn("s10", "ASGARİ MAKTU FORMÜLÜ",
     dict(head="FORMÜL İÇKİYE GÖRE DEĞİŞİR", ref="III-A",
          conds=[("<b>Bira:</b> litre × derece × tutar", "Birada"), ("<b>Şarap:</b> litre × tutar", "şarapta"),
                 ("<b>Viski:</b> litre × tutar × derece / 100", "viskide")],
          res=None, at="Asgari", at_res=None),
     dict(head="SİGARADA · (III) SAYILI LİSTE (B)", items=[("pc", "Nispi ile asgari maktudan yüksek olan", "YÜKSEK", "↑", "Sigarada"),
                                                       ("pv", "Üstüne ayrıca maktu vergi", "EKLENİR", "+", "üstüne")],
          at=("Bir", 2)),
     dict(char="stajyer", bubble="Formül hepsinde <em>aynı</em> değil mi?", at="uyarı", at_bub="Asgari"), hayir="değişir")

coach("s11", dict(head="BU HANGİ İÇKİ?", icon="bottle", at="Alkollü",
                  opts=[("ok", "Bira", "derece çarpılır", "Bira"), ("ok", "Şarap", "derece çarpılmaz", "şarap"),
                        ("no", "İki vergiyi toplamak", "ASLA", "asla")]),
      dict(head="KURAL", big="Yüksek olan <em>alınır</em>", p="Nispi ile asgari maktu karşılaştırılır; ikisi asla toplanmaz.",
           ref="Gümrük Koçu ders notu", at="Sonra", at_pulse="yüksek"),
      [("cl → litre", "ruler", "Santilitreyi"), ("Nispi vergi", "percent", "nispi"), ("Asgari maktu", "bottle", "asgari"),
       ("Yüksek olanı seç", "check", ("yüksek", 2)), ("Ürünleri topla", "calc", "ürünleri")])

closing("s12", "ÖZET · ÖTV III-A",
        [("Bira · asgari maktu", "3.960 L × 5 × 2,50 = 49.500 TL", "Bira"), ("Şarap · nispi", "240.000 × %63 = 151.200 TL", "şarap")],
        ("D", "200.700", "TL"), ("bottle", "Nispi ↔ asgari maktu<br/>→ <em>yüksek olan</em>", "Toplam"))
