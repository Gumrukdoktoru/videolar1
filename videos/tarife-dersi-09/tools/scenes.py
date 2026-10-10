"""Tarife Dersi 9: 87.03 / 87.05 taşıt çiftleri, kurşunlu baston (Fasıl 66 Not 1 → Fasıl 93), kauçuk motor contası (40.16)."""
from kit import S, intro, qscene, sol_classify, sol_statements, trap, coach, answer_key

intro("s01", 9, "Taşıtlar, silahlı bastonlar, kauçuk contalar",
      [("truck", "Özel taşıtlar", "87.03 mü, 87.05 mi?", "taşıtlar"),
       ("cane", "Silahlı baston", "Fasıl 66 mı, 93 mü?", "bastonlar"),
       ("ring", "Kauçuk conta", "motor parçası mı?", "contalar")], "dokuzuncusuna")

qscene("s02", 1,
       'Aşağıdaki <mark>taşıt çiftlerinden</mark> hangisinde iki taşıt <span class="neg">farklı<i></i></span> tarife pozisyonlarında sınıflandırılır?',
       ["Ambulans – İtfaiye aracı", "Cenaze arabası – Taksi", "Golf arabası – Motorlu karavan",
        "Beton mikser kamyonu – Vinçli kurtarıcı", "Hapishane minibüsü – Binek otomobili"],
       stem_word="Aşağıdaki", topic="Taşıtlar · Fasıl 87", neg="farklı")

sol_statements("s03", "A", "Ambulans <em>87.03</em> ≠ itfaiye aracı <em>87.05</em>",
               "Ambulans – İtfaiye aracı → aynı pozisyon",
               "Ambulans insan taşır → <em>87.03</em>; itfaiye aracı hizmet için donatılmıştır → <em>87.05</em>.", "87.03 ≠ 87.05",
               [("B", "Cenaze arabası – Taksi", "ikisi de 87.03 ✓"),
                ("C", "Golf arabası – Motorlu karavan", "ikisi de 87.03 ✓"),
                ("D", "Beton mikser – Vinçli kurtarıcı", "ikisi de 87.05 ✓"),
                ("E", "Hapishane minibüsü – Binek otomobili", "ikisi de 87.03 ✓")],
               strike="Ambulans", fix="İtfaiye", oth=["Cenaze", "golf", "beton", "hapishane"])

trap("s04", "Golf arabası ≠ spor eşyası", ("cano", 430),
     "Golf arabası spor… <em>95.06!</em>",
     dict(code="95.06", title="Golf arabası", sub="spor malzemesi sandı ✗", icon="star"),
     dict(code="87.03", title="Golf arabası", sub="insan taşır · açıklama notu ✓", icon="car"),
     "İnsan mı taşıyor, hizmet mi veriyor?",
     note=("dikkat", "Ambulans, cenaze arabası → <b>87.03</b> · itfaiye, kurtarıcı, beton mikser → <b>87.05</b>"),
     at=dict(tuzak="Tuzak", who="Cano", bub="spor", hayir="Hayır", wrong="şıkkını", right="taşır", note="dikkat", tag="hizmet"))

qscene("s05", 2,
       'İçine <mark>kurşun</mark> doldurularak ağırlaştırılmış, savunma amacıyla da kullanılabilen yürüyüş bastonu tarife cetvelinin hangi faslında sınıflandırılır?',
       ["<b>Fasıl 66</b>", "<b>Fasıl 95</b>", "<b>Fasıl 90</b>", "<b>Fasıl 93</b>", "<b>Fasıl 44</b>"],
       stem_word="İçine", topic="Şemsiye, baston · Fasıl 66", mono=True)

sol_classify("s06", "D", "<b>Fasıl 93</b> · kurşunlu baston silah sayılır",
             dict(icon="cane", name="Kurşunla ağırlaştırılmış yürüyüş bastonu", at="Altmış",
                  chips=[("kurşunlu baston", "kurşunlu"), ("silah niteliği", "silah")]),
             [("doc", "Fasıl 66 Not 1", "silahlı bastonlar fasıl dışı", "birinci"),
              ("x", "Baston faslı değil", "66.02’ye girmez", "gönderir"),
              ("check", "Silah niteliği", "içindeki kurşun ağırlık", "ağırlık")],
             dict(code="93", title="Silahlar · Fasıl 93", at="silahlar"),
             [("66", "şemsiye, baston", False), ("95", "spor sopaları", False), ("90", "ölçü gösteren baston", False),
              ("93", "silahlar", True), ("44", "baston taslağı", False)],
             cand_at="Diğer")

trap("s07", "Baston ≠ Fasıl 66", ("stajyer", 470),
     "Baston bastondur… <em>66.02!</em>",
     dict(code="66.02", title="Baston", sub="içine bakmadan ✗", icon="cane"),
     dict(code="Fasıl 93", title="Kurşunlu baston", sub="Fasıl 66 Not 1 · silah ✓", icon="shield"),
     "Bastonun içinde ne var?",
     note=("dikkat", "Ölçü gösteren baston → <b>90.17</b> · Fasıl 66’ya girmez"),
     who2=("baba", 470, "Bastonun <i>içinde</i> ne var? Ona bak!"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="bastondur", hayir="Hayır", wrong="şıkkını", right="silah", note="dikkat",
             who2="Gümrükçü", tag="içinde"))

qscene("s08", 3,
       'Bir otomobil motoruna ait, <mark>sertleştirilmemiş vulkanize kauçuktan</mark> yapılmış subap kapağı contası hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>84.09</b>", "<b>87.08</b>", "<b>40.16</b>", "<b>84.84</b>", "<b>40.17</b>"],
       stem_word="Bir", topic="Kauçuk eşya · Fasıl 40", mono=True)

sol_classify("s09", "C", "<b>40.16</b> · vulkanize kauçuktan diğer eşya",
             dict(icon="ring", name="Vulkanize kauçuktan subap kapağı contası", at="On",
                  chips=[("sertleştirilmemiş", "sertleştirilmemiş"), ("motora ait", "motora")]),
             [("doc", "Bölüm XVI Not 1", "kauçuk teknik eşya → 40.16", "birinci"),
              ("x", "Aksam pozisyonu değil", "84.09 / 87.08 almaz", "aksamına"),
              ("check", "Sert kauçuk değil", "40.17’ye gitmez", "Sertleştirilmiş")],
             dict(code="40.16", title="Diğer vulkanize kauçuk eşya", at="Doğru"),
             [("84.09", "motor aksamı", False), ("87.08", "taşıt aksamı", False), ("40.16", "kauçuk eşya", True),
              ("84.84", "conta takımları", False), ("40.17", "sert kauçuk", False)],
             cand_at="artık")

trap("s10", "Motor parçası ≠ 84.09", ("yardimci", 500),
     "Motordan söküldü… <em>84.09!</em>",
     dict(code="84.09", title="Motor aksamı", sub="motora ait diye ✗", icon="gear"),
     dict(code="40.16", title="Kauçuk conta", sub="Bölüm XVI Not 1 ✓", icon="ring"),
     "Önce malzemenin notu, sonra makine!",
     note=("dikkat", "Farklı malzemeden contalar poşette takım hâlinde → <b>84.84</b>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="motordan", hayir="Hayır", wrong="şıkkını", right="kauçuk", note="dikkat", tag="malzemenin"))

coach("s11", [("87.03 / 87.05", ["insan taşır → 87.03", "hizmet verir → 87.05"], "car"),
              ("BASTON", ["kurşunlu, kılıçlı → Fasıl 93", "ölçü gösteren → 90.17"], "cane"),
              ("KAUÇUK CONTA", ["motor parçası olsa da", "→ 40.16"], "ring")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("A", "Ambulans – İtfaiye", "87.03 ≠ 87.05"), ("D", "Kurşunlu baston", "Fasıl 93 · silah"),
                   ("C", "Kauçuk motor contası", "40.16")], 10)
