"""Vergi Hesaplama Dersi 11: çevre katkı payı — hurdada binde beş, kontrole tabi yakıt ve atıkta yüzde bir; matrah CIF bedel."""
import hkit
from hkit import S, intro, question, options, keys, calc, result, traps, warn, coach, closing

hkit.STEP_NAMES = ["CIF BEDELİ", "HURDA ‰5", "YAKIT %1", "SONUÇ"]
OPTS = [("A", "152.000"), ("B", "170.000"), ("C", "174.000"), ("D", "280.000"), ("E", "300.000")]

intro("s01", 11, "birincisine", "KONU · ÇEVRE KATKI PAYI", "Hurda <em>‰5</em> · yakıt / atık <em>%1</em>",
      [("Hurda ‰5", "Hurdada"), ("Yakıt / atık %1", "yakıt"), ("Matrah CIF", "Matrah"), ("Oranı seç", "Oranları")],
      "Oranları karıştırırsanız <b>sonuç değişir!</b>", art="bin", at_qq="Oranları", at_tz="değişir")

question("s02", "İki kalemde çevre katkı payı",
         dict(icon="ship", head="Ç firması · FOB · tek beyanname", sub="menşe: <em>ABD</em> · <em>2 kalem</em> · kontrole tabi",
              stamp="FOB<br/>TESLİM", at="firması", at_stamp="FOB"),
         [("1 · HURDA", "600.000 $", "FOB · navlun <b>45.000</b> · sig. <b>5.000</b>", "gear", "Birinci"),
          ("LİMAN (TÜRKİYE)", "20.000 $", "tahmil tahliye", "ship", "Türkiye'deki"),
          ("2 · PETROL KOKU", "80.000 $", "FOB · navlun <b>18.000</b> · sig. <b>2.000</b>", "flame", "İkinci")],
         [("KUR", "1 $ = 40 TL", "usd", "Kur"), ("ÇKP ORANI", "?", "gv", "çevre"), ("MATRAH", "?", "kdv", "çevre")],
         dict(char="yardimci", bubble="Hurdaya da <i>yüzde beş</i> mi?", at="firması", at_bub="Kur"),
         ("İstenen: <b>toplam çevre katkı payı</b> = ? <em>TL</em>", "Soru"))

options("s03", OPTS, "TL")

keys("s04", [("gear", "Hurda", "CIF bedelin <b>binde beşi (‰5)</b>", "ÇKP · HURDA", "Bir", "beşidir"),
             ("flame", "Yakıt ve atık", "Kontrole tabi yakıt ve atıkta CIF bedelin <b>yüzde biri (%1)</b>", "ÇKP · YAKIT / ATIK", "İki", "biridir"),
             ("ship", "Matrah = CIF", "FOB'a <b>navlun + sigorta</b> eklenir; Türkiye'deki liman gideri <b>eklenmez</b>", "CIF BEDEL", ("üç", 2), "eklenmez")],
     ["FOB", "+ navlun", "+ sigorta", "= CIF", "× oran", "× kur"])

calc("s05", 1, "ADIM 1 · CIF BEDELLER",
     [("HURDA CIF", "600.000 + 45.000 + 5.000", 650000, "k", "Hurda", ("elli", 1)),
      ("PETROL KOKU CIF", "80.000 + 18.000 + 2.000", 100000, "k", "Petrol", ("yüz", 3))],
     side=("ledger", [("Hurda", "650.000", ""), ("Petrol koku", "100.000", "")], [("elli", 1), ("yüz", 3)], "CIF $"),
     dik=("dikkat", "girmez"), at_start="Birinci",
     note=("Türkiye'deki tahmil tahliye (20.000 $) CIF'e <em>girmez</em>.", "Türkiye'deki"))

calc("s06", 2, "ADIM 2 · HURDA",
     [("HURDA ÇKP", "650.000 $ × ‰5", 3250, "r", "Altı", "üç")],
     side=("law", "ÇEVRE KATKI PAYI", "HURDA", "Hurdada oran <b>binde beş</b>:<br/>‰5 = <b>%0,5</b><br/>‰5 ≠ %5", ("binde", 2)),
     dik=("dikkat", "karıştırmayın"), at_start="İkinci",
     note=("<b>‰5 = %0,5</b> — yüzde beşle <em>karıştırmayın</em>.", ("binde", 2)))

calc("s07", 3, "ADIM 3 · YAKIT VE TOPLAM",
     [("PETROL KOKU", "100.000 $ × %1", 1000, "o", "yüz", ("bin", 2)),
      ("TOPLAM", "3.250 + 1.000", 4250, "m", "İki", "dört"),
      ("ÇKP (TL)", "4.250 $ × 40", 170000, "d", "Kur", "yetmiş")],
     side=("ledger", [("Hurda", "3.250 $", ""), ("Petrol koku", "1.000 $", ""), ("Toplam", "170.000 TL", "q")], [None, ("bin", 2), "yetmiş"], "ÇKP"),
     dik=("dikkat", "yakıt"), at_start="Üçüncü",
     note=("Kontrole tabi <b>yakıt</b> → oran <b>%1</b>.", "Kontrole"))

result("s08", [("Hurda · ‰5", "650.000 $ × ‰5", "3.250 $", "hurdada"), ("Petrol koku · %1", "100.000 $ × %1", "1.000 $", "petrol"),
               ("Toplam × kur", "4.250 $ × 40", "170.000", "toplam")],
       (170000, 0), "Türk lirası", OPTS, "B",
       sub="SORU · TOPLAM ÇEVRE KATKI PAYI", at=dict(son="sonuç", od="ödenecek", cnt=("yüz", 3), dogru="Doğru", L="B"))

traps("s09", [("A", "152.000", "FOB üzerinden hesaplandı", [("Hurda: 600.000 × ‰5", "3.000 $", ""), ("Koku: 80.000 × %1", "800 $", "")], "152.000"),
              ("C", "174.000", "Türkiye'deki tahmil tahliye eklendi", [("Hurda: 670.000 × ‰5", "3.350 $", ""), ("Koku: 100.000 × %1", "1.000 $", "")], "174.000"),
              ("D", "280.000", "Oranlar ters uygulandı", [("Hurda: 650.000 × %1", "6.500 $", ""), ("Koku: 100.000 × ‰5", "500 $", "")], "280.000"),
              ("E", "300.000", "İkisine de %1 uygulandı", [("Hurda: 650.000 × %1", "6.500 $", ""), ("Koku: 100.000 × %1", "1.000 $", "")], "300.000")],
      "TL", "Doğrusu <i>B: 170.000 TL!</i>",
      at=[("Navlun", "A"), ("Türkiye'deki", "C"), ("Oranları", "D"), ("İkisine", "E")])

warn("s10", "ÇEVRE KATKI PAYI",
     dict(head="ÇKP KİMDEN ALINIR?", ref="KONTROLE TABİ",
          conds=[("İthaline izin verilen <b>hurda</b>", "hurda"), ("Kontrole tabi <b>atık</b> ve <b>yakıt</b>", "atık"),
                 ("Yetkili kurum: <b>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı</b>", "yetkili")],
          res=None, at="Yalnızca", at_res=None),
     dict(head="ORAN DEĞİŞİR, MATRAH DEĞİŞMEZ", items=[("pc", "Matrah her zaman CIF bedel", "DOĞRU", "CIF", "CIF"),
                                                     ("pv", "FOB üzerinden hesaplanmaz", "YANLIŞ", "FOB", "FOB")],
          at=("Bir", 2)),
     dict(char="yardimci", bubble="Her ithalatta ÇKP <em>alınır</em> mı?", at="uyarı", at_bub="Çevre"), hayir="alınmaz")

coach("s11", dict(head="ÇKP'DE 2 SORU", icon="question", at="Çevre",
                  opts=[("ok", "Eşya hurda mı?", "‰5", "hurda"), ("ok", "Yakıt ya da atık mı?", "%1", "Yakıt"),
                        ("ok", "Matrah?", "CIF bedel", "Sonra")]),
      dict(head="UNUTMA", big="‰5 = <em>%0,5</em>", p="Binde beş, yüzde beş değildir; FOB ise navlun ve sigorta eklenir.",
           ref="Gümrük Koçu ders notu", at="FOB", at_pulse="ekleyin"),
      [("Kalemleri ayır", "layers", "Kalemleri"), ("CIF bedeli bul", "ship", "CIF"), ("Oranı seç", "percent", "oranı"),
       ("Kalemleri topla", "calc", ("kalemleri", 2)), ("Kurla çarp", "lira", "kurla")])

closing("s12", "ÖZET · ÇEVRE KATKI PAYI",
        [("Hurda · ‰5", "650.000 $ × ‰5 = 3.250 $", "Hurda"), ("Petrol koku · %1", "100.000 $ × %1 = 1.000 $", "petrol")],
        ("B", "170.000", "TL"), ("bin", "4.250 $ × 40<br/>= <em>170.000 TL</em>", "Toplam"))
