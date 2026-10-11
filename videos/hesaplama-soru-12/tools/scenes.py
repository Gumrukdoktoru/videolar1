"""Vergi Hesaplama Dersi 12: kısmi muafiyetle geçici ithalat — serbest dolaşım vergilerinin her ay için %3'ü; ay kesri tam ay."""
import hkit
from hkit import S, intro, question, options, keys, calc, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["VERGİLER", "AYLIK %3", "SÜRE", "SONUÇ"]
OPTS = [("A", "216.000"), ("B", "478.800"), ("C", "504.000"), ("D", "506.160"), ("E", "547.200")]

intro("s01", 12, "ikincisine", "KONU · KISMİ MUAFİYET", "Geçici ithalat · <em>aylık %3</em>",
      [("Aylık %3", "Her"), ("Vergilerin %3'ü", "neyin"), ("Ay kesri = tam ay", "kesirleri")],
      "Ama <b>neyin yüzde üçü?</b>", art="clock", at_qq="ama", at_tz="kesirleri")

question("s02", "Kısmi muafiyetle vinç",
         dict(icon="truck", head="V firması · kiralık mobil vinç", sub="menşe: <em>Çin</em> · kısmi muafiyetle <em>geçici ithalat</em>",
              stamp="KISMİ<br/>MUAFİYET", at="firması", at_stamp="kısmi"),
         [("GÜMRÜK KIYMETİ", "150.000 $", "1 $ = <b>40 TL</b> · tescil tarihinde", "doc", "Beyannamenin"),
          ("REJİMDE SÜRE", "7 ay 12 gün", "sonra <b>yeniden ihraç</b>", "clock", "Vinç")],
         [("GÜMRÜK VERGİSİ", "%5", "gv", ("gümrük", 2)), ("İLAVE GV", "%10", "igv", "ilave"), ("KDV", "%20", "kdv", "KDV")],
         dict(char="cano", bubble="Kıymetin yüzde üçü <i>değil mi?</i>", at="firması", at_bub="Vinç"),
         ("İstenen: <b>rejim süresince vergiler</b> = ? <em>TL</em>", "Soru"))

options("s03", OPTS, "TL")

keys("s04", [("calc", "Serbest dolaşım vergileri", "GV + İGV + KDV — <b>tescil tarihindeki</b> oran ve kurla", "GK md. 130", "Bir", "tescil"),
             ("percent", "Aylık %3", "Her ay için <b>vergilerin %3'ü</b> — kıymetin değil", "AYLIK %3", "İki", "kıymetin"),
             ("clock", "Ay kesri", "Bir aydan az süre <b>tam ay</b> sayılır", "AY KESRİ = 1 AY", ("üç", 2), "tam")],
     ["kıymet", "GV + İGV + KDV", "× %3", "× ay"])

calc("s05", 1, "ADIM 1 · SERBEST DOLAŞIM VERGİLERİ",
     [("KIYMET", "150.000 $ × 40", 6000000, "k", "Kıymet", ("milyon", 1)),
      ("GV", "6.000.000 × %5", 300000, "g", "Gümrük", ("üç", 1)),
      ("İLAVE GV", "6.000.000 × %10", 600000, "r", "ilave", ("altı", 2)),
      ("KDV MATRAHI", "6.000.000 + 300.000 + 600.000", 6900000, "m", "KDV", "dokuz"),
      ("KDV", "6.900.000 × %20", 1380000, "d", "Yüzde", "seksen")],
     sum_row=("TOPLAM VERGİ", 2280000, "TL", "Toplam", ("iki", 1)), at_start="Birinci")

calc("s06", 2, "ADIM 2 · AYLIK TUTAR",
     [("AYLIK TUTAR", "2.280.000 × %3", 68400, "o", "iki", "altmış")],
     side=("law", "KISMİ MUAFİYET", "GK md. 130", "Her ay için, eşya serbest dolaşımda olsaydı alınacak <b>vergilerin %3'ü</b>", "Her"),
     dik=("dikkat", "vergiler"), at_start="İkinci",
     note=("<b>Vergilerin</b> %3'ü alınır — kıymetin <em>değil!</em>", "vergiler"))

calc("s07", 3, "ADIM 3 · SÜRE",
     [("SÜRE (AY)", "7 ay + 12 gün → 7 + 1", 8, "m", "Bir", ("sekiz", 1)),
      ("TOPLAM", "68.400 × 8", 547200, "d", "Altmış", "beş")],
     side=("ledger", [("Aylık", "68.400", ""), ("Ay", "8", ""), ("Toplam", "547.200", "q")], [None, ("sekiz", 1), "beş"], "TL"),
     dik=("dikkat", "tam"), at_start="Üçüncü",
     note=("Ay kesri (12 gün) = <b>tam ay</b>.", "tam"))

result("s08", [("Vergiler toplamı", "GV + İGV + KDV", "2.280.000", "sonuç"), ("Aylık %3", "2.280.000 × %3", "68.400", "Aylık"),
               ("Süre", "7 ay 12 gün → 8 ay", "× 8", "sekiz")],
       (547200, 0), "Türk lirası", OPTS, "E",
       sub="SORU · KISMİ MUAFİYET", at=dict(son="sonuç", od="ödenecek", cnt="beş", dogru="Doğru", L="E"))

traps("s09", [("A", "216.000", "KDV hesaba katılmadı", [("Vergiler (KDV yok)", "900.000", ""), ("Aylık %3", "27.000", "")], "216.000"),
              ("B", "478.800", "12 gün atıldı → 7 ay", [("Aylık", "68.400", ""), ("Süre", "7 ay", "")], "478.800"),
              ("C", "504.000", "KDV matrahına GV + İGV eklenmedi", [("KDV: 6.000.000 × %20", "1.200.000", ""), ("Aylık: 2.100.000 × %3", "63.000", "")], "504.000"),
              ("D", "506.160", "Gün kesri oranlandı → 7,4 ay", [("Aylık", "68.400", ""), ("Süre", "7,4 ay", "")], "506.160")],
      "TL", "Doğrusu <i>E: 547.200 TL!</i>",
      at=[("KDV'yi", "A"), (("On", 2), "B"), ("KDV", "C"), ("Gün", "D")])

warn("s10", "KISMİ MUAFİYET",
     dict(head="SONRADAN SERBEST DOLAŞIMA GİRERSE", ref="MAHSUP",
          conds=[("Vergiler <b>yeniden hesaplanır</b>", "yeniden"), ("Ödenen kısmi muafiyet tutarı <b>düşülür</b>", "düşülür")],
          res=None, at="Eşya", at_res=None),
     dict(head="AYLIK TUTAR NEYE GÖRE?", items=[("pc", "Tescil tarihindeki oran ve kur", "ESAS", "✓", "tescil"),
                                              ("pv", "Sonradan oran değişirse", "DEĞİŞMEZ", "—", ("sonradan", 2))],
          at=("Bir", 2)),
     dict(char="cano", bubble="Oran düşerse tutar da <em>düşer</em> mi?", at="uyarı", at_bub="Eşya"), hayir="değişmez")

coach("s11", dict(head="ÜÇ ŞEYİ KARIŞTIRMA", icon="percent", at="Kısmi",
                  opts=[("no", "Kıymetin %3'ü", "YANLIŞ", "kıymetin"), ("ok", "Vergilerin %3'ü", "her ay", "vergilerin"),
                        ("ok", "Ay kesri", "tam ay", "kesri")]),
      dict(head="AY SAYISI", big="Yukarı <em>yuvarla</em>", p="7 ay 12 gün = 8 ay; gün kesri oranlanmaz.",
           ref="Gümrük Koçu ders notu", at="kesri", at_pulse="tam"),
      [("Kıymeti bul", "doc", "Kıymeti"), ("Vergileri hesapla", "calc", "serbest"), ("Toplamın %3'ü", "percent", "toplamın"),
       ("Ayı yukarı yuvarla", "clock", ("ay", 3)), ("İkisini çarp", "check", "ikisini")])

closing("s12", "ÖZET · KISMİ MUAFİYET",
        [("Vergiler × %3", "2.280.000 × %3 = 68.400 TL", "Vergiler"), ("Süre", "7 ay 12 gün → 8 ay", "süre")],
        ("E", "547.200", "TL"), ("clock", "68.400 × <em>8 ay</em>", "Toplam"))
