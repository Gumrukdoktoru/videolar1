"""Tarife Dersi 4: çakmak taşı (36.06), taşıma konteyneri (86.09), alkolsüz bira (22.02)."""
from kit import S, intro, qscene, sol_classify, trap, coach, answer_key

intro("s01", 4, "Çakmak taşı, konteyner, alkolsüz içecek",
      [("flame", "Çakmak taşları", "96.13 neyi hariç tutar?", "çakmak"),
       ("container", "Konteynerler", "madde mi, işlev mi?", "konteynerler"),
       ("bottle", "Alkolsüz içecekler", "sınır kaç?", "alkolsüz")], "dördüncüsüne")

qscene("s02", 1,
       '<mark>Çakmaklarda kullanılmak üzere</mark> küçük silindirler hâlinde hazırlanmış, ferroseryum alaşımından çakmak taşları hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>96.13</b>", "<b>28.46</b>", "<b>72.02</b>", "<b>36.06</b>", "<b>38.24</b>"],
       stem_word="Çakmaklarda", topic="Kimya · çakmaklar", mono=True)

sol_classify("s03", "D", "<b>36.06</b> · ferroseryum / piroforik alaşım",
             dict(icon="flame", name="Ferroseryum çakmak taşı (küçük silindir)", at="Doksan",
                  chips=[("çakmakta kullanılır", "çakmakları"), ("ferroseryum alaşımı", "Ferroseryum"), ("kıvılcım çıkarır", "kıvılcım")]),
             [("x", "96.13 değil", "metin: çakmak taşları hariç", "hariç"),
              ("flame", "Piroforik alaşım", "sürtünce kıvılcım çıkarır", "piroforik"),
              ("doc", "Her şekilde", "ambalajlı olsun olmasın", "her")],
             dict(code="36.06", title="Ferroseryum ve piroforik alaşımlar", at=("otuz", 1)),
             [("96.13", "çakmaklar ve aksamı", False), ("28.46", "nadir toprak bileşikleri", False), ("72.02", "ferro alyajlar", False),
              ("36.06", "piroforik alaşımlar", True), ("38.24", "diğer kimyasal ürünler", False)],
             cand_at="perakende")

trap("s04", "Adında “ferro” var ≠ 72.02", ("cano", 430),
     "Adında ferro var… o zaman <em>72.02!</em>",
     dict(code="72.02", title="Ferro alyajlar", sub="isme bakıp karar ✗", icon="box"),
     dict(code="36.06", title="Piroforik alaşımlar", sub="ferroseryum, çakmak taşı ✓", icon="flame"),
     "İsme değil, metne bak!",
     note=("dikkat", "Çakmak <em>aksamı</em> gaz kartuşu → <b>96.13</b> · ≤ 300 cm³ kapta çakmak gazı → <b>3606.10</b>"),
     at=dict(tuzak="Tuzak", who="Cano", bub="ferro", hayir="Hayır", wrong="alyajları", right=("otuz", 1), note="dikkat", tag=("otuz", 2)))

qscene("s05", 2,
       '<mark>Alüminyumdan</mark> yapılmış, kara ve hava yoluyla taşımaya göre özel olarak donatılmış, kancaları ve küçük tekerlekleri bulunan, bozulabilir gıdalar için yalıtımlı konteyner hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>86.09</b>", "<b>76.11</b>", "<b>76.12</b>", "<b>84.18</b>", "<b>87.16</b>"],
       stem_word="Alüminyumdan", topic="Taşıma · konteynerler", mono=True)

sol_classify("s06", "A", "<b>86.09</b> · taşıma konteynerleri",
             dict(icon="container", name="Alüminyum, yalıtımlı taşıma konteyneri", at="Seksen",
                  chips=[("taşıma şekline göre", "taşıma"), ("metal ya da ahşap", "metal"), ("yalıtımlı · bozulabilir gıda", "yalıtımlı")]),
             [("doc", "Pozisyon metni", "taşıma şekline göre yapılmış, donatılmış", "donatılmış"),
              ("box", "Madde önemsiz", "metal ya da ahşap olabilir", "madde"),
              ("check", "İzahname", "yalıtımlı konteynerler sayılır", "İzahname")],
             dict(code="86.09", title="Taşıma konteynerleri (sıvı için olanlar dahil)", at="konteynerleri"),
             [("86.09", "taşıma konteynerleri", True), ("76.11", "alüminyum depo > 300 l", False), ("76.12", "alüminyum kap ≤ 300 l", False),
              ("84.18", "soğutucu cihazlar", False), ("87.16", "römorklar", False)],
             cand_at="Kancalar")

trap("s07", "Alüminyum ≠ alüminyum faslı", ("yardimci", 500),
     "Alüminyumdan… o zaman <em>76.11!</em>",
     dict(code="76.11", title="Alüminyum depolar", sub="maddeye bakıp karar ✗", icon="box"),
     dict(code="86.09", title="Taşıma konteynerleri", sub="taşıma şekline göre donatılmış ✓", icon="container"),
     "Konteyner işlevle tanınır!",
     note=("dikkat", "<em>Tank konteyner:</em> taşıta göre yapılıp bağlanıyorsa <b>86.09</b>, değilse maddesine göre"),
     at=dict(tuzak=0.3, who="Yardımcımız", bub="alüminyum", hayir="Hayır", wrong="depoları", right="işlevine", note="Dikkat", tag=("maddeye", 2)))

qscene("s08", 3,
       'Hacmen <mark>%0,4 alkol</mark> içeren, maltlı alkolsüz bira hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>22.03</b>", "<b>22.06</b>", "<b>22.02</b>", "<b>22.01</b>", "<b>20.09</b>"],
       stem_word="Hacmen", topic="İçecekler · Fasıl 22", mono=True)

sol_classify("s09", "C", "<b>22.02</b> · alkolsüz bira (≤ %0,5)",
             dict(icon="bottle", name="Maltlı alkolsüz bira · hacmen %0,4 alkol", at="Yirmi",
                  chips=[("hacmen %0,4 alkol", ("dört", 1)), ("sınır: %0,5", "beşi")]),
             [("doc", "Fasıl 22 Not 3", "alkolsüz = hacmen ≤ %0,5", "notuna"),
              ("check", "%0,4 < %0,5", "sınırın altında → alkolsüz", "sınırın"),
              ("star", "Alt pozisyon 2202.91", "alkolsüz biralar", "biralar")],
             dict(code="22.02", title="Sular ve alkolsüz içecekler", at=("yirmi", 2)),
             [("22.03", "malt biraları", False), ("22.06", "diğer fermente içkiler", False), ("22.02", "alkolsüz içecekler", True),
              ("22.01", "sular", False), ("20.09", "meyve suları", False)],
             cand_at=("alkol", 3))

trap("s10", "Adı bira ≠ 22.03", ("stajyer", 470),
     "Bira yazıyor… o zaman <em>22.03!</em>",
     dict(code="22.03", title="Biralar (malttan)", sub="isme bakıp karar ✗", icon="bottle"),
     dict(code="22.02", title="Alkolsüz içecekler", sub="2202.91 alkolsüz biralar ✓", icon="shield"),
     "Sınır değeri bil: %0,5!",
     note=("uyari", "Alkol derecesi <em>20 °C</em>’de ölçülür · sınır <b>%0,5</b>"),
     who2=("baba", 470, "≤ %0,5 → <i>22.02</i> · üstü → <em>22.03</em>"),
     at=dict(tuzak=0.3, who="Stajyerimiz", bub="bira", hayir="Hayır", wrong="seçti", right="alkolsüz", who2="Gümrükçü", note="Alkol", tag="Sınır"))

coach("s11", [("HARİÇ’E BAK", ["96.13: çakmak taşı hariç", "taş → 36.06"], "x"),
              ("İŞLEV > MADDE", ["Konteyner işlevle tanınır", "alüminyum da olsa 86.09"], "container"),
              ("SAYISAL SINIR", ["Alkolsüz: hacmen ≤ %0,5", "Fasıl 22 Not 3"], "percent")],
      at_motto="kuralı", br=["Bir", "İki", "Üç"])

answer_key("s12", [("D", "Çakmak taşı", "36.06 · piroforik alaşım"), ("A", "Yalıtımlı konteyner", "86.09 · taşıma konteyneri"),
                   ("C", "Alkolsüz bira", "22.02 · ≤ %0,5 alkol")], 5)
