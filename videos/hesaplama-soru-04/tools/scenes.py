"""Vergi Hesaplama Dersi 4: ilave gümrük vergisi — nispi tutar, en az / en çok (min–max) karşılaştırması, KDV matrahı."""
import hkit
from hkit import S, intro, question, options, keys, calc, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["GV + NİSPİ İGV", "MİN–MAX", "KDV", "SONUÇ"]

intro("s01", 4, "dördüncüsüne", "KONU · İLAVE GÜMRÜK VERGİSİ", "Nispi mi, <em>sınır tutar</em> mı?",
      [("Nispi %30", "yüzde"), ("En az $/kg", "az"), ("En çok $/kg", "çok"), ("KDV matrahı", "Hangisini")],
      "Hangisini <b>uygulayacağız?</b>", art="ruler", at_qq="Hangisini", at_tz="var")

question("s02", "Min–max'lı ilave vergi",
         dict(icon="box", head="K firması · plastik mutfak eşyası", sub="menşe: <em>Çin</em> · miktar: <em>4.000 kg</em>",
              stamp="İGV'DE<br/>MİN–MAX", at="firması", at_stamp="ancak"),
         [("MENŞE", "Çin", "ilave GV uygulanan menşe", "globe", "Çin"),
          ("MİKTAR", "4.000 kg", "kilogram başına sınır", "scale", "dört"),
          ("CIF KIYMET", "16.000 $", "= <b>gümrük kıymeti</b>", "doc", "CIF")],
         [("GÜMRÜK VERGİSİ", "%10", "gv", "Gümrük"), ("İGV · NİSPİ", "%30", "igv", "İlave"), ("EN AZ", "1,5 $/kg", "acc", "az"),
          ("EN ÇOK", "2,5 $/kg", "acc", "çok"), ("KDV", "%20", "kdv", "KDV")],
         dict(char="cano", bubble="Yüzde otuz yeter, <i>değil mi?</i>", at="firması", at_bub="ancak"),
         ("İstenen: <b>GV + İGV + KDV</b> toplamı = ? <em>$</em>", "Soru"))

options("s03", [("A", "10.880"), ("B", "11.120"), ("C", "12.320"), ("D", "17.120"), ("E", "18.080")], "$")

keys("s04", [("doc", "Matrah: gümrük kıymeti", "GV ve İGV, <b>CIF + yurt dışı giderler</b> üzerinden hesaplanır", "GVM = CIF + y.dışı", "Bir", "kıymetidir"),
             ("ruler", "Önce nispi, sonra min–max", "Nispi tutar aralığın dışındaysa <b>sınır tutar</b> uygulanır", "MİN ≤ NİSPİ ≤ MAX", "İki", "uygulanır"),
             ("percent", "KDV en son", "KDV matrahı = kıymet + <b>GV + İGV</b>", "KDV K. md. 21", ("üç", 2), "girer")],
     ["kıymet", "GV", "İGV (min–max)", "KDV"])

calc("s05", 1, "ADIM 1 · GV VE NİSPİ İGV",
     [("MATRAH", "CIF kıymeti", 16000, "k", "Matrah", "on"),
      ("GV", "16.000 × %10", 1600, "g", ("Gümrük", 1), ("bin", 2)),
      ("İGV · NİSPİ", "16.000 × %30", 4800, "r", "İlave", "dört")],
     side=("ledger", [("GV", "1.600", ""), ("İGV nispi", "4.800 ?", "q")], [("yüz", 1), ("yüz", 2)], "$"),
     dik=("dikkat", "dur"), at_start="Birinci",
     note=("Bu yalnızca <em>nispi</em> tutar: en az / en çok sınırıyla karşılaştırılmadan İGV kesinleşmez.", "Bu"))

calc("s06", 2, "ADIM 2 · EN AZ VE EN ÇOK TUTAR",
     [("EN AZ", "4.000 kg × 1,5 $", 6000, "d", ("dört", 1), ("altı", 1)),
      ("EN ÇOK", "4.000 kg × 2,5 $", 10000, "r", ("dört", 2), ("on", 1)),
      ("NİSPİ", "16.000 × %30", 4800, "g", "Nispi", ("dört", 3))],
     sum_row=("İGV =", 6000, "$", "halde", ("altı", 2)),
     side=("minmax", dict(head="KORİDOR: EN AZ – EN ÇOK",
                          bars=[("EN AZ · 1,5 $/kg", 6000, "lo win"), ("EN ÇOK · 2,5 $/kg", 10000, "hi"), ("NİSPİ · %30", 4800, "ni")],
                          at=[("altı", 1), ("on", 1), ("dört", 3), "halde"],
                          pick="UYGULANAN: EN AZ", why="Nispi 4.800 &lt; en az 6.000 → sınır tutar uygulanır")),
     dik=("dikkat", "altında"), at_start="İkinci")

calc("s07", 3, "ADIM 3 · KDV",
     [("KDV MATRAHI", "16.000 + 1.600 + 6.000", 23600, "m", "matrahı", ("yirmi", 1)),
      ("KDV", "23.600 × %20", 4720, "d", "Bunun", "dört")],
     side=("ledger", [("GV", "1.600", ""), ("İGV", "6.000", ""), ("KDV", "4.720", "")], [None, None, ("dört", 1)], "$"),
     dik=("dikkat", ("artı", 2)), at_start="Üçüncü",
     note=("KDV matrahına <b>GV</b> ile birlikte <b>İGV</b> de girer: kıymet + GV + İGV.", ("artı", 1)))

result("s08", [("Gümrük vergisi", "16.000 × %10", "1.600", "bin"), ("İlave GV", "en az tutar · 4.000 × 1,5", "6.000", ("artı", 1)),
               ("KDV", "23.600 × %20", "4.720", ("artı", 2))],
       (12320, 0), "ABD doları", [("A", "10.880"), ("B", "11.120"), ("C", "12.320"), ("D", "17.120"), ("E", "18.080")], "C",
       sub="SORU · USD · GV + İGV + KDV", at=dict(son="sonuç", od="Ödenecek", cnt=("on", 1), dogru="Doğru", L="C"))

traps("s09", [("A", "10.880", "Min karşılaştırması yok, nispi yazıldı", [("İGV nispi", "4.800", ""), ("KDV: 22.400 × %20", "4.480", "")], "10.880"),
              ("B", "11.120", "İGV, KDV matrahına eklenmedi", [("KDV: 17.600 × %20", "3.520", ""), ("GV + İGV", "7.600", "")], "11.120"),
              ("D", "17.120", "En çok tutar uygulandı", [("İGV: 4.000 × 2,5", "10.000", ""), ("KDV: 27.600 × %20", "5.520", "")], "17.120"),
              ("E", "18.080", "Nispi + en az toplandı", [("İGV: 4.800 + 6.000", "10.800", ""), ("KDV: 28.400 × %20", "5.680", "")], "18.080")],
      "$", "Doğrusu <i>C: 12.320 $!</i>",
      at=[(("en", 1), "A"), ("İlave", "B"), (("en", 2), "D"), (("nispi", 2), "E")])

warn("s10", "MİN–MAX KURALI",
     dict(head="İGV · NİSPİ + MAKTU", ref="KARŞILAŞTIR", conds=[("Nispi <b>aralıkta</b> → nispi tutar", "içindeyse"),
                                                            ("Nispi <b>en azın altında</b> → en az tutar", "altındaysa"),
                                                            ("Nispi <b>en çoğun üstünde</b> → en çok tutar", "üstündeyse")],
          res=None, at="Nispi", at_res=None),
     dict(head="KİLOGRAM BAŞINA TUTAR · HANGİ AĞIRLIK?", items=[("pc", "Brüt kg verildiyse", "BRÜTLE ÇARP", "kg × $", "brüt"),
                                                              ("pc", "Net kg verildiyse", "NETLE ÇARP", "kg × $", "net")], at=("Bir", 2)),
     dict(char="cano", bubble="Nispi ile en azı <em>toplayalım mı?</em>", at="uyarı", at_bub=("en", 1)), hayir="toplanmaz")

coach("s11", dict(head="KORİDOR KURALI", icon="ruler", at="Min",
                  opts=[("ok", "İçinde → nispi tutar", "ARALIKTA", "içindeyse"), ("ok", "Altında → en az tutar", "SOL DUVAR", "dışındaysa"),
                        ("ok", "Üstünde → en çok tutar", "SAĞ DUVAR", "duvar")]),
      dict(head="SINIRLAR", big="Toplanmaz, <em>karşılaştırılır</em>", p="En az ve en çok tutar nispi vergiye eklenmez; yalnızca onu sınırlar.",
           ref="İGV · nispi + maktu", at="En", at_pulse="duvarıdır"),
      [("Matrahı bul", "doc", "Matrahı"), ("Nispiyi hesapla", "percent", "nispiyi"), ("Sınırla karşılaştır", "ruler", "sınırlarla"),
       ("KDV matrahına ekle", "arrow", ("KDV", 1)), ("Toplamı yaz", "check", "toplamı")])

closing("s12", "ÖZET · İLAVE GÜMRÜK VERGİSİ",
        [("İGV: en az tutar uygulandı", "4.000 kg × 1,5 = 6.000 $", "İlave"), ("GV + KDV", "1.600 + 4.720 = 6.320 $", "Gümrük")],
        ("C", "12.320", "$"), ("ruler", "Nispi 4.800 &lt; en az 6.000<br/><em>sınır tutar</em>", "altında"))
