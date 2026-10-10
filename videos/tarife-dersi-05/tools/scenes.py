"""Tarife Dersi 5: mineral mumlar (27.12), telsiz uzaktan kumanda (85.26), 42.02 kapsamı (deri kemer 42.03)."""
from kit import S, intro, qscene, sol_classify, sol_statements, trap, coach, answer_key

intro("s01", 5, "Mineral mumlar, telsiz kumanda, deri eşya",
      [("layers", "Mineral mumlar", "mumun kaynağı ne?", "mineral"),
       ("radio", "Telsiz kumanda", "aksam mı, kendi pozisyonu mu?", "telsiz"),
       ("box", "Deri eşya", "42.02 mi, 42.03 mü?", "deri")], "beşincisine")

qscene("s02", 1,
       '<mark>Petrolden elde edilen</mark>, mikrokristal bünyeli petrol mumu hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>34.04</b>", "<b>27.12</b>", "<b>15.21</b>", "<b>27.10</b>", "<b>33.04</b>"],
       stem_word="Petrolden", topic="Mineral ürünler · Fasıl 27", mono=True)

sol_classify("s03", "B", "<b>27.12</b> · vazelin, parafin, mineral mumlar",
             dict(icon="layers", name="Mikrokristal bünyeli petrol mumu", at="Cevap",
                  chips=[("petrol kökenli", "petrol"), ("ozokerit, linyit mumu ile aynı grup", "ozokerit"), ("mineral mum", "mineral")]),
             [("doc", "Pozisyon metni", "vazelin, parafin, mikrokristal mum…", "adıyla"),
              ("star", "Kaynak: mineral", "petrol ve mineral kökenli", "kökenli"),
              ("check", "Renk önemsiz", "renklendirilmiş olsun olmasın", "renklendirilmiş")],
             dict(code="27.12", title="Vazelin, parafin, mineral mumlar", at="Yirmi"),
             [("34.04", "suni ve müstahzar mumlar", False), ("27.12", "vazelin, mineral mumlar", True), ("15.21", "bitkisel mum, balmumu", False),
              ("27.10", "petrol yağları", False), ("33.04", "kozmetik müstahzarlar", False)],
             cand_at="kaynağı")

trap("s04", "Adı “mum” ≠ 34.04", ("stajyer", 470),
     "Mum dediğine göre… <em>34.04!</em>",
     dict(code="34.04", title="Suni / müstahzar mumlar", sub="kökene bakmadan karar ✗", icon="box"),
     dict(code="27.12", title="Mineral mumlar", sub="vazelin, parafin, mikrokristal ✓", icon="layers"),
     "Önce mumun kaynağına bak!",
     note=("dikkat", "Cilt bakımı için <em>perakende</em> ambalajlı vazelin → <b>33.04</b>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="mum", hayir="Hayır", wrong="mumları", right="Mineral", note="dikkat", tag="kozmetik"))

qscene("s05", 2,
       '<mark>Radyo frekansıyla</mark> çalışan ve bir kule vincinin hareketlerini uzaktan kontrol etmeye yarayan telsiz kumanda cihazı hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>85.43</b>", "<b>84.31</b>", "<b>85.37</b>", "<b>85.17</b>", "<b>85.26</b>"],
       stem_word="Radyo", topic="Elektrikli cihazlar · Fasıl 85", mono=True)

sol_classify("s06", "E", "<b>85.26</b> · telsiz uzaktan kumanda (8526.92)",
             dict(icon="radio", name="Kule vinci için telsiz kumanda cihazı", at="Seksen",
                  chips=[("telsiz · radyo dalgası", "telsiz"), ("vinci uzaktan kontrol", "Vince")]),
             [("doc", "Pozisyon metni", "uzaktan kumandaya mahsus telsiz cihazlar", "adıyla"),
              ("check", "Telsiz mi?", "radyo dalgasıyla çalışıyor", "radyo"),
              ("star", "Bölüm XVI Not 2(a)", "kendi pozisyonu olan aksam → kendi pozisyonu", "notuna")],
             dict(code="85.26", title="Radar, telsiz seyrüsefer ve telsiz kumanda", at="kontrol"),
             [("85.43", "kendine özgü elektrikli cihazlar", False), ("84.31", "vinç aksamı", False), ("85.37", "kontrol panoları", False),
              ("85.17", "haberleşme cihazları", False), ("85.26", "telsiz uzaktan kumanda", True)],
             cand_at="kendi")

trap("s07", "Vinçle çalışır ≠ vinç aksamı", ("yardimci", 500),
     "Vincin parçası… o zaman <em>84.31!</em>",
     dict(code="84.31", title="Vinç aksamı", sub="kendi pozisyonu varken ✗", icon="gear"),
     dict(code="85.26", title="Telsiz uzaktan kumanda", sub="8526.92 · Bölüm XVI Not 2(a) ✓", icon="radio"),
     "Kendi pozisyonu olan parça kendine gider!",
     note=("dikkat", "TV <em>kızılötesi</em> kumandaları telsiz değil → <b>85.43</b> (Fasıl 85 Not 10)"),
     who2=("baba", 470, "TV’nin <em>kızılötesi</em> kumandası → <i>85.43</i>"),
     at=dict(tuzak=0.3, who="Yardımcımız", bub="vinçle", hayir="Hayır", wrong="aksamını", right="Aksam", who2="Gümrükçü", note="kızılötesi", tag=("seksen", 2)))

qscene("s08", 3,
       'Aşağıdakilerden hangisi <mark>42.02</mark> pozisyonunda <span class="neg">sınıflandırılmaz<i></i></span>?',
       ["Dış yüzü dokumaya elverişli maddeden sırt çantası", "Alüminyumdan yapılmış, tekerlekli valiz", "Tabii deriden bel kemeri",
        "Vulkanize liften evrak çantası", "Plastik madde yaprağından tuvalet çantası"],
       stem_word="Aşağıdakilerden", topic="Deri eşya · Fasıl 42", neg="sınıflandırılmaz")

sol_statements("s09", "C", "Deri bel kemeri → <em>42.03</em> · 42.02 değil",
               "Tabii deriden bel kemeri → 42.02",
               "Deri bel kemeri <em>giyim aksesuarıdır</em> → 42.03 (4203.30 bel kemerleri). 42.02 çanta ve mahfazalar içindir.", "42.03",
               [("A", "Dokumaya elverişli maddeden sırt çantası", "2. grup · tekstil ✓"),
                ("B", "Alüminyumdan tekerlekli valiz", "1. grup · her madde ✓"),
                ("D", "Vulkanize liften evrak çantası", "1. grup ✓"),
                ("E", "Plastik yapraktan tuvalet çantası", "2. grup · plastik yaprak ✓")],
               strike=("deri", 2), fix="giyim", oth=["sırt", "Birinci", "evrak", "tuvalet"])

trap("s10", "Deriden ≠ 42.02", ("cano", 430),
     "Deriyse… o zaman <em>42.02!</em>",
     dict(code="42.02", title="Çanta ve mahfazalar", sub="her deri eşya değil ✗", icon="box"),
     dict(code="42.03", title="Deri giyim aksesuarı", sub="4203.30 bel kemerleri ✓", icon="shield"),
     "Önce eşyanın türü, sonra maddesi!",
     note=("dikkat", "<em>Ahşap</em> mücevher kutusu → 42.02 değil, <b>44.20</b>"),
     at=dict(tuzak=0.3, who="Cano", bub="deriden", hayir="Hayır", wrong="çantalar", right="giyim", note="dikkat", tag="listede"))

coach("s11", [("MUMUN KAYNAĞI", ["Mineral mum → 27.12", "Suni / müstahzar → 34.04"], "layers"),
              ("KENDİ POZİSYONU", ["Telsiz kumanda → 85.26", "aksam pozisyonu değil"], "radio"),
              ("42.02’NİN 2 GRUBU", ["1. grup: her madde", "2. grup: madde şartı"], "box")],
      at_motto="kuralı", br=["Bir", "İki", "Üç"])

answer_key("s12", [("B", "Mikrokristal mum", "27.12 · mineral mumlar"), ("E", "Vinç kumandası", "85.26 · telsiz kumanda"),
                   ("C", "Deri bel kemeri", "42.03 · giyim aksesuarı")], 6)
