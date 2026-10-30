"""Tarife Dersi 17 (3 soru): sülfonlanmış hint yağı 34.02 (15.18 açıklama notu), porselen salon bebeği 95.03 (Fasıl 69 Not 2),
pozisyon sırası 04.02 → 44.19 → 84.14 → 84.72 (bisiklet pompası 87.14 değil)."""
import kit
from kit import S, intro, qscene, sol_classify, sol_order, trap, coach, answer_key

kit.NQ = 3

intro("s01", 17, "Hint yağı, porselen bebek, pozisyon sırası",
      [("drop", "Hint yağı", "15.18 · 34.02", "hint"),
       ("gem", "Porselen bebek", "69.13 · 95.03", "porselen"),
       ("sort", "Pozisyon sırası", "04 · 44 · 84", "pozisyon")], "yedincisine")

qscene("s02", 1,
       'Sülfürik asitle muamele edilerek <mark>sülfonlanmış</mark> hint yağı, yani Türk kırmızısı yağı, hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>15.15</b>", "<b>15.16</b>", "<b>15.18</b>", "<b>34.02</b>", "<b>38.23</b>"],
       stem_word="Sülfürik", topic="Yağlar / kimya · 15–34", mono=True)

sol_classify("s03", "D", "<b>34.02</b> · yüzey aktif organik madde",
             dict(icon="drop", name="Sülfonlanmış hint yağı", at="Hint",
                  chips=[("sülfürik asitle", "sülfürik"), ("yüzey aktif", "yüzey")]),
             [("drop", "Hint yağı", "sabit yağ → 15.15", "bitkisel"),
              ("doc", "Fasıl 15 Not 1", "sülfonatlı yağlar hariç", "birinci"),
              ("check", "15.18 açıklama notu", "sülfonlanmış yağlar → 34.02", "adıyla")],
             dict(code="34.02", title="Yüzey aktif organik maddeler", at="Doğru"),
             [("15.15", "sabit yağ", False), ("15.16", "hidrojenize yağ", False), ("15.18", "işlem görmüş yağ", False),
              ("34.02", "yüzey aktif madde", True), ("38.23", "yağ asidi", False)],
             cand_at="Sülfonlama")

trap("s04", "Kükürtlenmiş ≠ sülfonlanmış", ("yardimci", 500),
     "Metinde kükürtlenmiş… <em>15.18!</em>",
     dict(code="15.18", title="Kükürtlenmiş yağlar", sub="metinde yazıyor diye ✗", icon="x"),
     dict(code="34.02", title="Sülfonlanmış yağ", sub="15.18 notunda hariç ✓", icon="drop"),
     "Sülfonlandıysa artık yağ değil!",
     note=("dikkat", "İşlem görmemiş saf hint yağı → <b>15.15</b>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="kükürtlenmiş", hayir="Hayır", wrong="şıkkını", right="Sülfonlanmış", note="dikkat", tag="Kısa"))

qscene("s05", 2,
       'Çocukların oynaması için değil, <mark>süs amacıyla</mark> yapılmış, giydirilmiş porselen salon bebeği hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>69.11</b>", "<b>69.13</b>", "<b>95.03</b>", "<b>96.18</b>", "<b>97.03</b>"],
       stem_word="Çocukların", topic="Seramik / oyuncak · 69–95", mono=True)

sol_classify("s06", "C", "<b>95.03</b> · salon bebekleri adıyla",
             dict(icon="gem", name="Porselen salon bebeği", at="Porselenden",
                  chips=[("süs amaçlı", "süs"), ("seramik", "seramikten")]),
             [("search", "Akla gelen: 69.13", "seramik süs eşyası", "ilk"),
              ("doc", "95.03 açıklama notu", "salon, maskot bebekler adıyla", "salon"),
              ("x", "Fasıl 69 Not 2", "Fasıl 95 eşyası hariç", "ikinci")],
             dict(code="95.03", title="Oyuncaklar, yapma bebekler", at="Doğru"),
             [("69.11", "porselen sofra", False), ("69.13", "seramik süs", False), ("95.03", "yapma bebek", True),
              ("96.18", "vitrin mankeni", False), ("97.03", "heykel eseri", False)],
             cand_at="Vitrin")

trap("s07", "Süs bebeği ≠ 69.13", ("cano", 430),
     "Çocuk oynamıyor… <em>süs eşyası!</em>",
     dict(code="69.13", title="Seramik süs eşyası", sub="çocuk oynamıyor diye ✗", icon="x"),
     dict(code="95.03", title="Salon bebeği", sub="dekoratif bebekler de ✓", icon="gem"),
     "Bebekse 95, biblosa 69!",
     note=("dikkat", "Seramikten <b>hayvan biblosu</b> → <b>69.13</b>"),
     at=dict(tuzak="Tuzak", who="Cano", bub="oynamıyor", hayir="Hayır", wrong="şıkkını", right="dekoratif", note="dikkat", tag="Kısa"))

qscene("s08", 3,
       'Aşağıdakilerden hangisinde eşyalar, tarife cetvelindeki <mark>pozisyon numaralarına göre küçükten büyüğe</mark> doğru sıralanmıştır?',
       ["Bambu yemek çubuğu, şekerli kondanse süt, ayakla çalışan bisiklet pompası, para sayma makinesi",
        "Şekerli kondanse süt, bambu yemek çubuğu, ayakla çalışan bisiklet pompası, para sayma makinesi",
        "Şekerli kondanse süt, bambu yemek çubuğu, para sayma makinesi, ayakla çalışan bisiklet pompası",
        "Şekerli kondanse süt, ayakla çalışan bisiklet pompası, bambu yemek çubuğu, para sayma makinesi",
        "Para sayma makinesi, şekerli kondanse süt, bambu yemek çubuğu, ayakla çalışan bisiklet pompası"],
       stem_word="Aşağıdakilerden", topic="Sıralama · Fasıl 04–84", small=True)

sol_order("s09", "B", "<b>04.02</b> → <b>44.19</b> → <b>84.14</b> → <b>84.72</b>",
          [("04.02", "Şekerli kondanse süt", "konsantre süt", "drop", "Şekerli"),
           ("44.19", "Bambu yemek çubuğu", "Çin usulü çubuklar", "layers", "Bambudan"),
           ("84.14", "Bisiklet pompası", "hava pompası", "gear", "Ayakla"),
           ("84.72", "Para sayma makinesi", "büro makinesi", "calc", "Para")],
          [("A", "Çubuk → süt → pompa → para sayma", "44.19, 04.02'den önce olamaz"),
           ("C", "Süt → çubuk → para sayma → pompa", "84.72, 84.14'ten önce olamaz"),
           ("D", "Süt → pompa → çubuk → para sayma", "84.14, 44.19'dan önce olamaz"),
           ("E", "Para sayma → süt → çubuk → pompa", "84.72 en başta olamaz")],
          at_wrong="Diğer")

trap("s10", "Pompa ≠ 87.14", ("stajyer", 470),
     "Bisiklet aksesuarı… <em>87.14!</em>",
     dict(code="87.14", title="Bisiklet aksesuarı", sub="bisiklet için diye ✗", icon="x"),
     dict(code="84.14", title="El, ayak hava pompası", sub="Bölüm XVII Not 2 ✓", icon="gear"),
     "Makineyse önce 84!",
     note=("dikkat", "Para sayma makinesi <b>84.70</b> değil → <b>84.72</b>"),
     who2=("baba", 470, "Makineyse önce <i>84'e bak</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="aksesuarıdır", hayir="Hayır", wrong="şıkkını", right="yedinci", note="dikkat",
             who2="Gümrükçü", tag="Makineyse"))

coach("s11", [("SÜLFONLAMA", ["hint yağı → 15.15", "sülfonlanmış → 34.02"], "drop"),
              ("BEBEK = 95.03", ["salon bebeği → 95.03", "biblo → 69.13"], "gem"),
              ("MAKİNE → 84", ["pompa → 84.14", "87.14 değil"], "gear")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("D", "Sülfonlanmış hint yağı", "34.02"), ("C", "Porselen salon bebeği", "95.03"), ("B", "Pozisyon sırası", "04.02 → 84.72")], 18)
