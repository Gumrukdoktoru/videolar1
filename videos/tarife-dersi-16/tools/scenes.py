"""Tarife Dersi 16 (3 soru): 84.76 kapsamı (ödeme tertibatı olmayan içecek makinesi 84.19), portatif hidrolik kriko 84.25
(Bölüm XVII Not 2, 87.08 değil), farklı fasıl: saf o-asetilsalisilik asit 29.18 (diğerleri Fasıl 30)."""
import kit
from kit import S, intro, qscene, sol_classify, sol_statements, trap, coach, answer_key

kit.NQ = 3

intro("s01", 16, "Satış otomatı, kriko, aspirin",
      [("lira", "Satış otomatı", "84.76 · 84.19", "otomatları"),
       ("car", "Araba krikosu", "84.25 · 87.08", "krikosu"),
       ("flask", "Aspirin", "29.18 · 30.03", "aspirin")], "altıncısına")

qscene("s02", 1,
       'Aşağıdakilerden hangisi <mark>84.76</mark> pozisyonunda <span class="neg">sınıflandırılmaz<i></i></span>?',
       ["Bozuk para veya kartla çalışan, soğutma tertibatlı kutu içecek satış otomatı", "Para bozma makinesi",
        "Jetonla çalışan tren bileti satış makinesi", "Jetonla çalışan, kahve ve süt karıştırıcısı olan sıcak içecek otomatı",
        "Ödeme tertibatı olmayan, ofislerde kullanılan sıcak içecek verme makinesi"],
       stem_word="Aşağıdakilerden", topic="Makineler · Fasıl 84", neg="sınıflandırılmaz", small=True)

sol_statements("s03", "E", "Ödeme almayan içecek makinesi → <b>84.19</b> · 84.76 değil",
               "Ödeme tertibatı olmayan sıcak içecek makinesi → 84.76",
               "Ödemeyi kabul eden tertibat yoksa <em>satış otomatı değildir</em> → <em>84.19</em>", "84.19",
               [("A", "Soğutmalı kutu içecek otomatı", "84.76 · 8476.21"), ("B", "Para bozma makinesi", "84.76 · açıklama notu"),
                ("C", "Tren bileti satış makinesi", "84.76"), ("D", "Kahve-süt karıştırıcılı sıcak içecek otomatı", "84.76")],
               strike="Ama", fix="ofisteki", oth=["soğutma", "para", "tren", "kahve"])

trap("s04", "Soğutucu ≠ 84.18", ("stajyer", 470),
     "Soğutucusu var… <em>84.18!</em>",
     dict(code="84.18", title="Soğutma cihazı", sub="soğutucusu var diye ✗", icon="x"),
     dict(code="84.76", title="Soğutmalı satış otomatı", sub="esas işlev satış ✓", icon="lira"),
     "Para alıyor mu?",
     note=("dikkat", "Ödeme almayan sıcak içecek makinesi → <b>84.19</b>"),
     who2=("baba", 470, "Para <i>alıyor mu?</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="soğutucusu", hayir="Hayır", wrong="şıkkını", right="esas", note="dikkat",
             who2="Gümrükçü", tag=("Para", 2)))

qscene("s05", 2,
       'Otomobilin lastiğini değiştirmek için kullanılan, <mark>elle çalıştırılan portatif hidrolik kriko</mark> hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>82.05</b>", "<b>84.25</b>", "<b>84.28</b>", "<b>84.79</b>", "<b>87.08</b>"],
       stem_word="Otomobilin", topic="Makine / taşıt · 84–87", mono=True)

sol_classify("s06", "B", "<b>84.25</b> · krikolar adıyla",
             dict(icon="car", name="Portatif hidrolik kriko", at="Kriko",
                  chips=[("ağır yük kaldırıcı", "kaldırıcısıdır"), ("otomobil için", "otomobiller")]),
             [("doc", "84.25 metni", "krikolar adıyla", "adıyla"),
              ("search", "Açıklama notu", "otomobil için portatif kriko", "açıklama"),
              ("x", "Bölüm XVII Not 2", "84.01–84.79 makineleri parça değil", "yedinci")],
             dict(code="84.25", title="Krikolar, ağır yük kaldırıcıları", at="Doğru"),
             [("82.05", "el aleti", False), ("84.25", "kriko", True), ("84.28", "kaldırma-taşıma", False),
              ("84.79", "kendine özgü", False), ("87.08", "taşıt parçası", False)],
             cand_at="Elle")

trap("s07", "Arabada kullanılır ≠ 87.08", ("cano", 430),
     "Araba için… <em>araba parçası!</em>",
     dict(code="87.08", title="Taşıt aksam, parçası", sub="arabayla kullanılıyor diye ✗", icon="x"),
     dict(code="84.25", title="Kriko", sub="84.01–84.79 makinesi ✓", icon="car"),
     "Makine mi, parça mı?",
     note=("dikkat", "Taşıtta kullanılan <b>pompa ve kompresörler</b> de Fasıl 84"),
     at=dict(tuzak="Tuzak", who="Cano", bub="parçasıdır", hayir="Hayır", wrong="şıkkını", right=("kriko", 2), note="dikkat", tag="Kısa"))

qscene("s08", 3,
       'Aşağıdakilerden hangisi tarife cetvelinde diğerlerinden <span class="neg">farklı<i></i></span> bir <mark>fasılda</mark> sınıflandırılır?',
       ["Hiçbir maddeyle karıştırılmamış, dökme hâldeki saf o-asetilsalisilik asit",
        "Bir dolgu maddesiyle karıştırılmış, dozlandırılmamış, dökme aspirin",
        "Dozlandırılmış, perakende satışa hazır aspirin tabletleri",
        "Tabii maden sularının buharlaştırılmasıyla elde edilen tıbbi tuzlar",
        "Dökme hâlde, tıbbi amaçla karıştırılmış şifalı bitkiler"],
       stem_word="Aşağıdakilerden", topic="Kimya / ilaç · 29–30", neg="farklı", small=True)

sol_statements("s09", "A", "Saf etken madde → <b>29.18</b> · diğerleri Fasıl 30",
               "Saf o-asetilsalisilik asit → Fasıl 30, ilaç",
               "Kimyaca belirli, izole <em>organik bileşik</em> → Fasıl 29 Not 1 → <em>2918.22</em>", "29.18",
               [("B", "Dolgu maddeli dökme aspirin", "30.03"), ("C", "Dozlandırılmış aspirin tableti", "30.04"),
                ("D", "Maden suyundan tıbbi tuzlar", "30.03 · açıklama notu"), ("E", "Tıbbi bitki karışımı", "30.03 · açıklama notu")],
               strike="Saf", fix="birinci", oth=["Dolgu", "dozlandırılmış", "maden", "bitki"])

trap("s10", "Bitki karışımı da ilaç", ("yardimci", 500),
     "Bitkiler <em>ilaç değildir!</em>",
     dict(code="E şıkkı", title="Bitki karışımı farklı", sub="bitki ilaç değil diye ✗", icon="x"),
     dict(code="30.03", title="Tıbbi bitki karışımı", sub="açıklama notunda adıyla ✓", icon="seed"),
     "Saf mı, karışım mı, doz mu?",
     note=("dikkat", "Saf madde dozlandırılıp tablet olunca → <b>30.04</b>"),
     who2=("baba", 470, "Saf mı, karışım mı, <i>doz mu?</i>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="ilaç", hayir="Hayır", wrong="şıkkını", right="Tedavi", note="dikkat",
             who2="Gümrükçü", tag=("Saf", 3)))

coach("s11", [("PARA ALIYOR MU?", ["ödeme var → 84.76", "ödeme yok → 84.19"], "lira"),
              ("TAŞIT PARÇASI?", ["kriko → 84.25", "87.08 değil"], "car"),
              ("SAF MI, KARIŞIM?", ["saf bileşik → 29.18", "karışım, doz → 30"], "flask")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("E", "Ödemesiz içecek makinesi", "84.19"), ("B", "Hidrolik kriko", "84.25"), ("A", "Saf etken madde", "29.18")], 17)
