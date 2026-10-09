"""Tarife Dersi 3: dolgulu yatak takımı (94.04), deniz memelisi eti (02.08), paten takılmış bot (95.06)."""
from kit import S, intro, qscene, sol_classify, trap, coach, answer_key

intro("s01", 3, "Yatak takımı, deniz memelileri, patenler",
      [("bed", "Yatak takımı eşyası", "dolgu ne demek?", "yatak"),
       ("fish", "Deniz memelileri", "Fasıl 2 mi, 3 mü?", "deniz"),
       ("skate", "Paten takılmış bot", "Fasıl 64 notu", "paten")], "üçüncüsüne")

qscene("s02", 1,
       'Dış yüzü pamuklu dokunmuş mensucattan, <mark>içi kaz tüyüyle doldurulmuş</mark> yorgan hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>63.01</b>", "<b>63.02</b>", "<b>94.04</b>", "<b>52.08</b>", "<b>05.05</b>"],
       stem_word="Dış", topic="Mefruşat · yatak takımı", mono=True)

sol_classify("s03", "C", "<b>94.04</b> · dolgulu yatak takımı eşyası",
             dict(icon="bed", name="Kaz tüyü dolgulu yorgan (dış yüzü pamuklu)", at="Bu",
                  chips=[("içi doldurulmuş", "doldurulmuş"), ("yatak takımı eşyası", "yatak"), ("dış yüz: pamuklu", "pamuklu")]),
             [("bed", "Pozisyon metni", "şilte, yorgan, yastık, uyku tulumu", "şilteleri"),
              ("doc", "Kaplama önemsiz", "“kaplanmış olsun olmasın”", "kaplanmış"),
              ("star", "Belirleyici", "dolgulu yatak takımı eşyası", "Belirleyici")],
             dict(code="94.04", title="Şilte, yorgan, yastık, uyku tulumu…", at="Doksan"),
             [("63.01", "battaniyeler", False), ("63.02", "yatak çarşafları", False), ("94.04", "dolgulu yatak takımı", True),
              ("52.08", "pamuklu mensucat", False), ("05.05", "kuş tüyleri", False)],
             cand_at="değiştirmez")

trap("s04", "Pamuklu yüz ≠ battaniye", ("yardimci", 500),
     "Dış yüzü pamuklu… o zaman <em>63.01!</em>",
     dict(code="63.01", title="Battaniyeler", sub="dolgusuz örtüler ✗", icon="layers"),
     dict(code="94.04", title="Dolgulu yatak takımı", sub="yorgan, yastık, şilte ✓", icon="bed"),
     "Dolgu varsa önce 94.04!",
     note=("dikkat", "<em>Uyku tulumları</em> da aynı pozisyonda: <b>9404.30</b>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="pamuklu", hayir="Hayır", wrong="battaniyeleri", right="yorgan", note="Uyku", tag="Dolgu"))

qscene("s05", 2,
       '<mark>Dondurulmuş fok eti</mark> hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>02.08</b>", "<b>03.03</b>", "<b>02.06</b>", "<b>16.02</b>", "<b>03.04</b>"],
       stem_word="Dondurulmuş", topic="Etler · Fasıl 2–3", mono=True)

sol_classify("s06", "A", "<b>02.08</b> · diğer etler (deniz memelileri)",
             dict(icon="fish", name="Dondurulmuş fok eti", at="Fok",
                  chips=[("deniz canlısı", "deniz"), ("memeli · balık değil", "memeli")]),
             [("x", "Fasıl 3 değil", "yalnız balık, kabuklu, yumuşakça", "Üçüncü"),
              ("star", "Deniz memelisi", "eti Fasıl 2’de", "memelilerinin"),
              ("doc", "Alt pozisyon 0208.40", "balina, yunus, fok, deniz aslanı", "Alt")],
             dict(code="02.08", title="Diğer etler ve yenilen sakatat", at=("sıfır", 1)),
             [("02.08", "diğer etler", True), ("03.03", "dondurulmuş balık", False), ("02.06", "yenilen sakatat", False),
              ("16.02", "et müstahzarları", False), ("03.04", "balık filetoları", False)],
             cand_at="balinalar")

trap("s07", "Denizde yaşar ≠ balık", ("cano", 430),
     "Denizden çıkıyor… o zaman <em>balık!</em>",
     dict(code="03.03", title="Dondurulmuş balıklar", sub="yaşadığı yere göre karar ✗", icon="fish"),
     dict(code="02.08", title="Deniz memelisi eti", sub="0208.40 · fok, balina, yunus ✓", icon="shield"),
     "Önce hayvanın türüne bak!",
     note=("dikkat", "Deniz memelisi <em>yağları</em> → <b>15.04</b> (balık yağlarıyla birlikte)"),
     at=dict(tuzak=0.3, who="Cano", bub="denizden", hayir="Hayır", wrong="balıkları", right="memelidir", note="yağları", tag="sınıflandırılır"))

qscene("s08", 3,
       'Altına <mark>buz pateni bıçağı</mark> sökülemeyecek şekilde tutturulmuş, üst kısmı deri, dış tabanı kauçuk bot hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>64.03</b>", "<b>64.02</b>", "<b>95.03</b>", "<b>64.06</b>", "<b>95.06</b>"],
       stem_word="Altına", topic="Ayakkabı · spor eşyası", mono=True)

sol_classify("s09", "E", "<b>95.06</b> · paten takılmış botlar dahil",
             dict(icon="skate", name="Buz pateni bıçağı sabit, deri yüzlü bot", at="Normalde",
                  chips=[("üst: deri", "deri"), ("taban: kauçuk", "kauçuk"), ("paten bıçağı takılı", "paten")]),
             [("shoe", "İlk bakış", "deri yüz + kauçuk taban → 64.03", "gider"),
              ("doc", "Fasıl 64 Notu 1", "paten takılmış botlar hariç", "notu"),
              ("skate", "Alt pozisyon 9506.70", "paten takılmış botlar dahil", "alt")],
             dict(code="95.06", title="Spor eşyası · buz ve tekerlekli patenler", at="Doksan"),
             [("64.03", "deri yüzlü ayakkabı", False), ("64.02", "kauçuk/plastik ayakkabı", False), ("95.03", "oyuncaklar", False),
              ("64.06", "ayakkabı aksamı", False), ("95.06", "patenler · spor eşyası", True)],
             cand_at="dahil")

trap("s10", "Deri yüz ≠ ayakkabı faslı", ("stajyer", 470),
     "Üstü deri… o zaman <em>64.03!</em>",
     dict(code="64.03", title="Deri yüzlü ayakkabı", sub="paten takılıyken ✗", icon="shoe"),
     dict(code="95.06", title="Paten takılmış bot", sub="9506.70 ✓", icon="skate"),
     "Önce fasıl notunu oku!",
     note=("dikkat", "<em>Oyuncak</em> karakterli ayakkabılar → <b>95.03</b>"),
     who2=("baba", 470, "Bıçak takılıysa <i>95.06</i>; patensiz bot <i>Fasıl 64</i>."),
     at=dict(tuzak=0.3, who="Stajyerimiz", bub="deri", hayir="Hayır", wrong="seçti", right="spor", note="Oyuncak", who2="Gümrükçü", tag=("doksan", 2)))

coach("s11", [("DOLGU → 94.04", ["Yorgan, yastık, uyku tulumu", "dış yüz önemsiz"], "bed"),
              ("TÜRE BAK", ["Deniz memelisi ≠ balık", "fok eti → 02.08"], "fish"),
              ("NOT BELİRLER", ["Paten takılı bot → 95.06", "patensiz bot → Fasıl 64"], "doc")],
      at_motto="kuralı", br=["Bir", "İki", "Üç"])

answer_key("s12", [("C", "Kaz tüyü yorgan", "94.04 · dolgulu yatak takımı"), ("A", "Fok eti", "02.08 · deniz memelisi"),
                   ("E", "Patenli bot", "95.06 · Fasıl 64 notu")], 4)
