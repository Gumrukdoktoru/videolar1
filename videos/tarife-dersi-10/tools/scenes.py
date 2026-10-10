"""Tarife Dersi 10: hava yastıklı taşıtlar (Bölüm XVII Not 5), gümüş sigara tabakası (71.13, Fasıl 71 Not 9), yolcu biniş köprüsü (84.79)."""
from kit import S, intro, qscene, sol_classify, sol_true, trap, coach, answer_key

intro("s01", 10, "Hava yastığı, kıymetli metal, biniş köprüsü",
      [("hover", "Hava yastıklı", "86 · 87 · 89 ?", "hava"),
       ("gem", "Kıymetli metal", "71.13 mü, 71.14 mü?", "kıymetli"),
       ("bridge", "Biniş köprüsü", "köprü mü, makine mi?", "yolcu")], "onuncusuna")

qscene("s02", 1,
       '<mark>Hava yastığı</mark> üzerinde hareket eden taşıtların sınıflandırılmasıyla ilgili aşağıdaki ifadelerden hangisi '
       '<span class="neg">doğrudur<i></i></span>?',
       ["Hava yastıklı taşıtların tamamı, hava taşıtlarıyla birlikte 88. fasılda sınıflandırılır.",
        "Kılavuz bir hat üzerinde gitmek üzere tasarlanmış hava trenleri 86. fasılda sınıflandırılır.",
        "Hem karada hem suda gidebilen hava yastıklı taşıtlar 89. fasılda sınıflandırılır.",
        "Yalnız su üzerinde giden, kıyıya çıkabilen hava yastıklı taşıtlar 87. fasılda sınıflandırılır.",
        "Hava yastıklı taşıtlar, benzedikleri taşıta bakılmaksızın 84. fasılda makine olarak sınıflandırılır."],
       stem_word="Hava", topic="Taşıtlar · Bölüm XVII", neg="doğrudur", small=True)

sol_true("s03", "B", "Hava treni → <em>Fasıl 86</em> · en çok benzediği taşıt",
         "Hava yastıklı taşıt <em>en çok benzediği taşıtla</em> sınıflandırılır; kılavuz hat üzerinde giden hava treni → "
         "<em>Fasıl 86</em>.", "BÖLÜM XVII NOT 5",
         [("A", "<s>Tamamı Fasıl 88</s> değil; benzediği taşıta göre <em>86, 87 veya 89</em>."),
          ("C", "<s>Fasıl 89</s> değil; karada ya da hem karada hem suda gidenler <em>Fasıl 87</em>."),
          ("D", "<s>Fasıl 87</s> değil; su üzerinde gidenler kıyıya çıksa da <em>Fasıl 89</em>."),
          ("E", "<s>Makine değil</s>; taşıt olarak <em>Bölüm XVII</em>’de sınıflandırılır.")],
         basis="Kılavuz", oth=["benzedikleri", "Karada", "su", "Hiçbiri"])

trap("s04", "Kıyıya çıkar ≠ Fasıl 87", ("cano", 430),
     "Kıyıya çıkıyor… <em>kara taşıtı!</em>",
     dict(code="Fasıl 87", title="Su üstü hava yastıklı tekne", sub="kıyıya çıkıyor diye ✗", icon="car"),
     dict(code="Fasıl 89", title="Su üstü hava yastıklı tekne", sub="kıyıya çıksa da gemi gibi ✓", icon="ship"),
     "Taşıt en çok neye benziyor?",
     note=("dikkat", "Hava treni hattının sabit malzemesi ve sinyal cihazları → <b>demiryolundaki karşılığı</b> gibi"),
     at=dict(tuzak="Tuzak", who="Cano", bub="kıyıya", hayir="Hayır", wrong="şıkkını", right="dokuzuncu", note="dikkat", tag="benziyor"))

qscene("s05", 2,
       '<mark>Gümüşten</mark> yapılmış, cepte taşınan türden sigara tabakası hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>71.13</b>", "<b>71.14</b>", "<b>71.17</b>", "<b>42.02</b>", "<b>96.14</b>"],
       stem_word="Gümüşten", topic="Kıymetli metaller · Fasıl 71", mono=True)

sol_classify("s06", "A", "<b>71.13</b> · mücevherci eşyası (Fasıl 71 Not 9)",
             dict(icon="case", name="Gümüşten, cepte taşınan sigara tabakası", at="Yetmiş",
                  chips=[("cepte taşınır", "cepte"), ("sigara tabakası", "Sigara")]),
             [("doc", "Fasıl 71 Not 9", "mücevherci eşyası tanımı", "tanımlar"),
              ("search", "Kişisel eşya", "cepte, çantada taşınır", "kişisel"),
              ("check", "Kıymetli metal", "gümüş → 71.13", "Gümüşten")],
             dict(code="71.13", title="Mücevherci eşyası", at="pozisyonunda"),
             [("71.13", "mücevherci eşyası", True), ("71.14", "kuyumcu eşyası", False), ("71.17", "taklit mücevher", False),
              ("42.02", "deri, plastik tabaka", False), ("96.14", "pipo, ağızlık", False)],
             cand_at="Masada")

trap("s07", "Sigara gereci ≠ 71.14", ("stajyer", 470),
     "Sigara gereci… <em>kuyumcu eşyası!</em>",
     dict(code="71.14", title="Kuyumcu eşyası", sub="sigara gereci sandı ✗", icon="building"),
     dict(code="71.13", title="Mücevherci eşyası", sub="cepte taşınan kişisel eşya ✓", icon="gem"),
     "Cepte mi, masada mı?",
     note=("dikkat", "Adi metalden sigara tabakası <b>71.17</b> değil · taklit mücevher yalnız küçük süs eşyası"),
     who2=("baba", 470, "Cepte mi, masada mı? <i>Ona bak!</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="kuyumcu", hayir="Hayır", wrong="şıkkını", right="Cepte", note="dikkat",
             who2="Gümrükçü", tag=("masada", 2)))

qscene("s08", 3,
       'Bir yolcu limanında, kruvaziyer gemilere biniş için kullanılan, teleskopik hareketli bir tünelden oluşan '
       '<mark>yolcu biniş köprüsü</mark> hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>84.26</b>", "<b>73.08</b>", "<b>84.28</b>", "<b>84.79</b>", "<b>89.07</b>"],
       stem_word="Bir", topic="Makineler · Fasıl 84", mono=True)

sol_classify("s09", "D", "<b>84.79</b> · kendine özgü işlevli makine (8479.79)",
             dict(icon="bridge", name="Limanda teleskopik yolcu biniş köprüsü", at="Yolcu",
                  chips=[("tünel içinden geçiş", "tünel"), ("hareketli makine", "hareketli")]),
             [("search", "Eşya ne?", "hareketli biniş makinesi", "makinedir"),
              ("star", "Kendine özgü işlev", "başka pozisyonda yok", "Kendine"),
              ("doc", "Belirtilmemiş", "Fasıl 84’ün artık pozisyonu", "belirtilmemiştir")],
             dict(code="84.79", title="Kendine özgü işlevli makineler", at="yer"),
             [("84.26", "vinçler", False), ("73.08", "çelik köprüler", False), ("84.28", "yürüyen merdiven", False),
              ("84.79", "biniş köprüsü", True), ("89.07", "yüzer iskeleler", False)],
             cand_at="Armonize")

trap("s10", "Köprü adı ≠ 73.08", ("yardimci", 500),
     "Adı köprü… <em>73.08!</em>",
     dict(code="73.08", title="Çelik köprü", sub="adı köprü diye ✗", icon="building"),
     dict(code="84.79", title="Yolcu biniş köprüsü", sub="hareketli makine ✓", icon="gear"),
     "Adına değil, işlevine bak!",
     note=("dikkat", "Yürüyen merdiven ve yürüyen yol → <b>84.28</b>"),
     who2=("baba", 470, "Adına değil, <i>işlevine</i> bak!"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="köprü", hayir="Hayır", wrong="şıkkını", right="hareketli", note="dikkat",
             who2="Gümrükçü", tag="işlevine"))

coach("s11", [("HAVA YASTIKLI", ["hat → 86 · kara → 87", "su → 89"], "hover"),
              ("CEP / MASA", ["cepte → 71.13", "masada → 71.14"], "gem"),
              ("AD ≠ İŞLEV", ["biniş köprüsü → 84.79", "çelik köprü → 73.08"], "bridge")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("B", "Hava treni", "Fasıl 86 · Bölüm XVII Not 5"), ("A", "Gümüş sigara tabakası", "71.13 · mücevherci"),
                   ("D", "Yolcu biniş köprüsü", "84.79")], 11)
