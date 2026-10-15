"""Tarife Dersi 14 (3 soru): lokanta tipi elektrikli semaver 84.19 (85.16 açıklama notu), kalem fener GYK 3(c) → 96.08,
pozisyon sırası 19.02 → 33.03 → 39.23 → 48.19."""
import kit
from kit import S, intro, qscene, sol_classify, sol_order, trap, coach, answer_key

kit.NQ = 3

intro("s01", 14, "Lokanta semaveri, kalem fener, pozisyon sırası",
      [("flame", "Lokanta semaveri", "84.19 · 85.16", "lokanta"),
       ("pen", "Kalem fener", "GYK 3 · 96.08", "kalem"),
       ("sort", "Pozisyon sırası", "19 · 33 · 39 · 48", "pozisyon")], "dördüncüsüne")

qscene("s02", 1,
       'Bir <mark>lokantanın mutfağında</mark> kullanılmak üzere ithal edilen, tezgâh tipi, elektrikle ısıtılan büyük çay semaveri '
       'hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>84.19</b>", "<b>85.14</b>", "<b>85.16</b>", "<b>85.43</b>", "<b>94.03</b>"],
       stem_word="Bir", topic="Isıtma cihazları · 84–85", mono=True)

sol_classify("s03", "A", "<b>84.19</b> · lokanta tipi semaver",
             dict(icon="flame", name="Lokanta tipi çay semaveri", at="Elektrikle",
                  chips=[("tezgâh tipi", "tezgâh"), ("evde kullanılmaz", "evlerde")]),
             [("building", "Akla gelen: 85.16", "ev tipi elektrikli cihaz", "ev"),
              ("doc", "85.16 açıklama notu", "lokanta tipi semaver → dışarıda", "lokantalarda"),
              ("check", "84.19", "ısıtma ve pişirme cihazları", "ısıtma")],
             dict(code="84.19", title="Isıtma, pişirme cihazları", at="Doğru"),
             [("84.19", "ısıtma cihazı", True), ("85.14", "sanayi fırını", False), ("85.16", "ev tipi cihaz", False),
              ("85.43", "diğer el. cihaz", False), ("94.03", "mobilya", False)],
             cand_at="Evde")

trap("s04", "Elektrikli ≠ hep 85.16", ("cano", 430),
     "Elektrikli ısıtıcı… <em>ev aleti!</em>",
     dict(code="85.16", title="Ev tipi elektrotermik", sub="elektrikli diye ✗", icon="x"),
     dict(code="84.19", title="Lokanta tipi semaver", sub="evde kullanılmaz ✓", icon="flame"),
     "Evde mi, lokantada mı?",
     note=("dikkat", "Restoran tipi <b>mikrodalga fırın</b> → <b>85.14</b>, 85.16 değil"),
     at=dict(tuzak="Tuzak", who="Cano", bub="ısıtıcı", hayir="Hayır", wrong="şıkkını", right="lokanta", note="dikkat", tag="Kısa"))

qscene("s05", 2,
       'Bir ucunda tükenmez kalem, diğer ucunda pille çalışan küçük bir LED el feneri bulunan kalem fener, perakende satışa sunuluyor. '
       '<mark>Esas niteliğinin belirlenemediği</mark> kabul edilirse, hangi kurala göre hangi pozisyonda sınıflandırılır?',
       ["<b>85.13</b> · GYK 1", "<b>85.13</b> · GYK 3(b)", "<b>96.08</b> · GYK 3(a)", "<b>96.08</b> · GYK 3(c)", "Ayrı ayrı · GYK 1"],
       stem_word="Bir", topic="Genel kurallar · GYK 3", mono=True)

sol_classify("s06", "D", "<b>96.08</b> · GYK 3(c), en son pozisyon",
             dict(icon="pen", name="Kalem fener", at="Kalem",
                  chips=[("tükenmez kalem", "tükenmez"), ("LED el feneri", "portatif")]),
             [("scale", "GYK 3(a)", "iki pozisyon eşit özel", "a'ya"),
              ("search", "GYK 3(b)", "esas nitelik belirlenemiyor", "nitelik"),
              ("sort", "GYK 3(c)", "numara sırasında en son", "ce")],
             dict(code="96.08", title="Tükenmez kalemler", at="yani"),
             [("85.13", "GYK 1", False), ("85.13", "GYK 3(b)", False), ("96.08", "GYK 3(a)", False),
              ("96.08", "GYK 3(c)", True), ("Ayrı", "GYK 1", False)],
             cand_at=("Ayrı", 2))

trap("s07", "Esas nitelik yoksa 3(c)", ("yardimci", 500),
     "Işık veren kısım… <em>daha önemli!</em>",
     dict(code="85.13", title="Portatif lamba", sub="ışık daha önemli diye ✗", icon="bulb"),
     dict(code="96.08", title="Kalem fener", sub="GYK 3(c) · en son pozisyon ✓", icon="pen"),
     "Önce 3(a), sonra 3(b), en son 3(c)!",
     note=("dikkat", "<b>3(c)</b>'ye ancak <b>3(a)</b> ve <b>3(b)</b> sonuç vermezse geçilir"),
     who2=("baba", 470, "Önce 3(a), sonra 3(b), <i>en son 3(c)</i>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="önemli", hayir="Hayır", wrong="şıkkını", right="ce", note="dikkat",
             who2="Gümrükçü", tag="Önce"))

qscene("s08", 3,
       'Aşağıdakilerden hangisinde eşyalar, tarife cetvelindeki <mark>pozisyon numaralarına göre küçükten büyüğe</mark> doğru sıralanmıştır?',
       ["Kolonya, yumurtalı erişte, plastik su şişesi, kâğıt alışveriş torbası",
        "Yumurtalı erişte, kolonya, kâğıt alışveriş torbası, plastik su şişesi",
        "Plastik su şişesi, kolonya, yumurtalı erişte, kâğıt alışveriş torbası",
        "Yumurtalı erişte, plastik su şişesi, kolonya, kâğıt alışveriş torbası",
        "Yumurtalı erişte, kolonya, plastik su şişesi, kâğıt alışveriş torbası"],
       stem_word="Aşağıdakilerden", topic="Sıralama · Fasıl 19–48", small=True)

sol_order("s09", "E", "<b>19.02</b> → <b>33.03</b> → <b>39.23</b> → <b>48.19</b>",
          [("19.02", "Yumurtalı erişte", "makarnalar", "wheat", "Yumurtalı"),
           ("33.03", "Kolonya", "tuvalet suları", "drop", "Kolonya"),
           ("39.23", "Plastik su şişesi", "ambalaj eşyası", "bottle", "Plastik"),
           ("48.19", "Kâğıt torba", "kâğıt torbalar", "box", "Kâğıt")],
          [("A", "Kolonya → erişte → şişe → torba", "33.03, 19.02'den önce olamaz"),
           ("B", "Erişte → kolonya → torba → şişe", "48.19, 39.23'ten önce olamaz"),
           ("C", "Şişe → kolonya → erişte → torba", "39.23 en başta olamaz"),
           ("D", "Erişte → şişe → kolonya → torba", "39.23, 33.03'ten önce olamaz")],
          at_wrong="Diğer")

trap("s10", "Ambalaj ≠ en sona", ("stajyer", 470),
     "Ambalajlar <em>en sona!</em>",
     dict(code="B şıkkı", title="Torba → şişe", sub="ambalajlar sona diye ✗", icon="x"),
     dict(code="39 → 48", title="Şişe → torba", sub="plastik kâğıttan önce ✓", icon="sort"),
     "Önce faslı bul, sonra sırala!",
     note=("dikkat", "Kolonya <b>Fasıl 22</b>'ye değil → <b>33.03</b>, tuvalet suları"),
     who2=("baba", 470, "Önce faslı bul, <i>sonra sırala</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="ambalajlar", hayir="Hayır", wrong="şıkkını", right=("plastik", 2), note="dikkat",
             who2="Gümrükçü", tag="Önce"))

coach("s11", [("EV Mİ, LOKANTA MI?", ["ev semaveri → 85.16", "lokanta → 84.19"], "flame"),
              ("KURAL 3 SIRASI", ["3(a) → 3(b) → 3(c)", "kalem fener → 96.08"], "layers"),
              ("ÖNCE FASIL", ["19 · 33 · 39 · 48", "sonra sırala"], "sort")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("A", "Lokanta semaveri", "84.19"), ("D", "Kalem fener", "96.08 · GYK 3(c)"), ("E", "Pozisyon sırası", "19.02 → 48.19")], 15)
