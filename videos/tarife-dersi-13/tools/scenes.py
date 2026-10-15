"""Tarife Dersi 13 (3 soru): denizaltı periskobu 90.13 (Fasıl 90 Not 4, 90.05 değil), dijital tansiyon aleti 90.18 (90.26 değil),
farklı pozisyondaki çalgı: darbuka 92.06 (bağlama, ud, kanun, kemençe 92.02)."""
import kit
from kit import S, intro, qscene, sol_classify, sol_statements, trap, coach, answer_key

kit.NQ = 3

intro("s01", 13, "Periskop, tansiyon aleti, Türk çalgıları",
      [("eye", "Periskop", "90.05 mi, 90.13 mü?", "periskop"),
       ("scale", "Tansiyon aleti", "90.18 · 90.26", "tansiyon"),
       ("music", "Türk çalgıları", "92.02 · 92.06", "Türk")], "üçüncüsüne")

qscene("s02", 1,
       'Bir <mark>denizaltında</mark> kullanılmak üzere, denizaltıdan ayrı olarak ithal edilen <mark>periskop</mark> '
       'hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>89.06</b>", "<b>90.05</b>", "<b>90.13</b>", "<b>90.15</b>", "<b>93.05</b>"],
       stem_word="Bir", topic="Optik aletler · Fasıl 90", mono=True)

sol_classify("s03", "C", "<b>90.13</b> · Fasıl 90 Not 4",
             dict(icon="eye", name="Denizaltı periskobu", at="Periskop",
                  chips=[("optik alet", "optik"), ("denizaltı için", "denizaltı")]),
             [("search", "Akla gelen: 90.05", "dürbünler, teleskoplar", "dürbün"),
              ("doc", "Fasıl 90 Not 4", "denizaltı, tank periskobu → 90.05 dışı", "dördüncü"),
              ("check", "9013.10 metni", "silah dürbünü, periskop adıyla", "adıyla")],
             dict(code="90.13", title="Silah dürbünleri, periskoplar", at="Doğru"),
             [("89.06", "denizaltı", False), ("90.05", "dürbün, teleskop", False), ("90.13", "periskop", True),
              ("90.15", "ölçme, gözlem", False), ("93.05", "silah aksamı", False)],
             cand_at="Denizaltının")

trap("s04", "Periskop ≠ 90.05", ("yardimci", 500),
     "Periskop da teleskop… <em>90.05!</em>",
     dict(code="90.05", title="Dürbün, teleskop", sub="teleskoptur diye ✗", icon="x"),
     dict(code="90.13", title="Denizaltı, tank periskobu", sub="Fasıl 90 Not 4 ✓", icon="eye"),
     "Önce fasıl notunu okuyun!",
     note=("dikkat", "Fasıl 90 ya da <b>Bölüm XVI</b> makinelerine ait teleskoplar → <b>90.13</b>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="teleskoptur", hayir="Hayır", wrong="şıkkını", right="tanklar", note="dikkat", tag="Kısa"))

qscene("s05", 2,
       'Kola sarılan bir manşonla <mark>kan basıncını</mark> ölçen dijital tansiyon aleti hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>85.43</b>", "<b>90.18</b>", "<b>90.25</b>", "<b>90.26</b>", "<b>90.31</b>"],
       stem_word="Kola", topic="Ölçme / tıp · Fasıl 90", mono=True)

sol_classify("s06", "B", "<b>90.18</b> · tansiyometreler adıyla",
             dict(icon="drop", name="Dijital tansiyon aleti", at="Tansiyon",
                  chips=[("tıbbi teşhis", "teşhis"), ("kan basıncı", "kan")]),
             [("scale", "Basınç ölçer mi?", "görünüş yanıltır", "basınç"),
              ("doc", "90.18 açıklama notu", "sfigmomanometre, tansiyometre adıyla", "sfigmomanometreleri"),
              ("x", "90.26 değil", "sıvı, gaz basıncı: manometre", "manometreler")],
             dict(code="90.18", title="Tıp aletleri: tansiyometreler", at="Doğru"),
             [("85.43", "elektrikli cihaz", False), ("90.18", "tıbbi alet", True), ("90.25", "termometre", False),
              ("90.26", "manometre", False), ("90.31", "diğer ölçme", False)],
             cand_at="Elektronik")

trap("s07", "Basınç ölçer ≠ 90.26", ("stajyer", 470),
     "Basınç ölçüyor… <em>90.26!</em>",
     dict(code="90.26", title="Manometre", sub="basınç ölçüyor diye ✗", icon="gear"),
     dict(code="90.18", title="Tansiyon aleti", sub="tıbbi alet · adıyla ✓", icon="drop"),
     "Kimin basıncını ölçüyor?",
     note=("dikkat", "Ateş ölçen <b>klinik termometre</b> → <b>90.25</b>"),
     who2=("baba", 470, "Kimin basıncını <i>ölçüyor?</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="ölçüyor", hayir="Hayır", wrong="şıkkını", right="tıbbi", note="dikkat",
             who2="Gümrükçü", tag="Kimin"))

qscene("s08", 3,
       'Aşağıdaki <mark>çalgılardan</mark> hangisi tarife cetvelinde diğerlerinden <span class="neg">farklı<i></i></span> bir pozisyonda sınıflandırılır?',
       ["Bağlama", "Ud", "Kanun", "Kemençe", "Darbuka"],
       stem_word="Aşağıdaki", topic="Müzik aletleri · Fasıl 92", neg="farklı")

sol_statements("s09", "E", "Darbuka → <b>92.06</b> · diğerleri 92.02",
               "Darbuka → 92.02, telli çalgılarla",
               "Darbuka gerdirilmiş deriye <em>elle vurularak</em> çalınır → <em>92.06</em>, adıyla", "92.06",
               [("A", "Bağlama", "92.02 · telli"), ("B", "Ud", "92.02 · telli"),
                ("C", "Kanun", "92.02 · telli"), ("D", "Kemençe", "92.02 · yaylı, telli")],
               strike="Darbuka", fix="darbukaları", oth=["Bağlama", "ud", "kanun", "kemençe"])

trap("s10", "Yaylı da telli", ("cano", 430),
     "Yayla çalınıyor… <em>telli değil!</em>",
     dict(code="D şıkkı", title="Kemençe farklı", sub="yaylı, telli sayılmaz diye ✗", icon="x"),
     dict(code="92.02", title="Kemençe de telli", sub="keman gibi yaylı çalgı ✓", icon="music"),
     "Tel mi titriyor, deri mi?",
     note=("dikkat", "Ses kutusu olmayan <b>elektro gitar</b> → <b>92.07</b>"),
     at=dict(tuzak="Tuzak", who="Cano", bub="yayla", hayir="Hayır", wrong="şıkkını", right="keman", note="dikkat", tag="Kısa"))

coach("s11", [("FASIL NOTU", ["periskop → 90.13", "dürbün → 90.05"], "doc"),
              ("NEYİ ÖLÇÜYOR?", ["kan basıncı → 90.18", "gaz basıncı → 90.26"], "scale"),
              ("SESİN KAYNAĞI", ["tel → 92.02", "deri → 92.06"], "music")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("C", "Periskop", "90.13"), ("B", "Tansiyon aleti", "90.18"), ("E", "Darbuka", "92.06")], 14)
