"""Tarife Dersi 11 (5 soru): Bölüm XII sıralaması (65.06 → 66.01 → 66.02 → 67.04), 73.07 boru bağlantı parçaları (hortum kelepçesi 73.26),
Fasıl 81 diğer adi metaller (kobalt 81.05), 84.28 teleferik/füniküler (vagon 86.05), manyetik torna aynası (85.05)."""
import kit
from kit import S, intro, qscene, sol_classify, sol_statements, sol_order, trap, coach, answer_key

kit.NQ = 5

intro("s01", 11, "Sıralama, boru, metal, füniküler, ayna",
      [("sort", "Sıralama", "65 · 66 · 67", "pozisyon"),
       ("ring", "Boru parçası", "73.07 mi?", "boru"),
       ("layers", "Adi metaller", "Fasıl 81", "adi"),
       ("gear", "Füniküler", "84.28 · 86.05", "teleferik"),
       ("chip", "Manyetik ayna", "84.66 · 85.05", "manyetik")], "birincisine")

qscene("s02", 1,
       'Aşağıdakilerden hangisinde eşyalar, tarife cetvelindeki <mark>pozisyon numaralarına göre küçükten büyüğe</mark> doğru sıralanmıştır?',
       ["Deri saplı kamçı, plastik baret, yağmur şemsiyesi, sentetik peruk",
        "Plastik baret, deri saplı kamçı, yağmur şemsiyesi, sentetik peruk",
        "Sentetik peruk, plastik baret, yağmur şemsiyesi, deri saplı kamçı",
        "Plastik baret, yağmur şemsiyesi, deri saplı kamçı, sentetik peruk",
        "Yağmur şemsiyesi, deri saplı kamçı, sentetik peruk, plastik baret"],
       stem_word="Aşağıdakilerden", topic="Sıralama · Bölüm XII", small=True)

sol_order("s03", "D", "<b>65.06</b> → <b>66.01</b> → <b>66.02</b> → <b>67.04</b>",
          [("65.06", "Plastik baret", "koruyucu başlık", "shield", "Plastik"),
           ("66.01", "Yağmur şemsiyesi", "şemsiyeler", "drop", "Yağmur"),
           ("66.02", "Deri saplı kamçı", "bastonlarla birlikte", "cane", "Kamçı"),
           ("67.04", "Sentetik peruk", "peruklar", "mask", "Sentetik")],
          [("A", "Kamçı → baret → şemsiye → peruk", "66.02, 65.06'dan önce olamaz"),
           ("B", "Baret → kamçı → şemsiye → peruk", "66.02, 66.01'den önce olamaz"),
           ("C", "Peruk → baret → şemsiye → kamçı", "67.04 en sonda olmalı"),
           ("E", "Şemsiye → kamçı → peruk → baret", "65.06 en başta olmalı")],
          at_wrong="Diğer")

trap("s04", "Deri sap ≠ Fasıl 42", ("cano", 430),
     "Sapı deri… <em>saraciye eşyası!</em>",
     dict(code="Fasıl 42", title="Saraciye eşyası", sub="sapı deri diye ✗", icon="case"),
     dict(code="66.02", title="Kamçı, baston", sub="malzemesi ne olursa olsun ✓", icon="cane"),
     "Malzemeye değil, eşyaya bak!",
     note=("dikkat", "Plastik baret <b>Fasıl 39</b>'a girmez · Fasıl 39 Not 2: Bölüm XII eşyası hariç → <b>65.06</b>"),
     at=dict(tuzak="Tuzak", who="Cano", bub="saraciye", hayir="Hayır", wrong="şıkkını", right="malzemesi", note="dikkat", tag="Kısa"))

qscene("s05", 2,
       'Demir veya çelikten yapılmış aşağıdaki eşyadan hangisi <mark>73.07</mark> pozisyonunda, yani boru bağlantı parçaları arasında '
       '<span class="neg">sınıflandırılmaz<i></i></span>?',
       ["Uç uca kaynak yapılacak dirsek", "Esnek hortumu sıkarak sabitleyen hortum kelepçesi", "Boruyu bir cihaza bağlayan flanş",
        "İki farklı çaptaki boruyu birleştiren redüksiyon", "Borunun açık ucunu kapatan kör tapa"],
       stem_word="Demir", topic="Demir-çelik · Fasıl 73", neg="sınıflandırılmaz")

sol_statements("s06", "B", "Hortum kelepçesi → <b>73.26</b> · 73.07 değil",
               "Esnek hortumu sıkarak sabitleyen hortum kelepçesi → 73.07",
               "Kelepçe boruyla <em>birleşmez</em>; esnek hortumu sıkıp sabitler → <em>73.26</em> (demir-çelikten diğer eşya)", "73.26",
               [("A", "Uç uca kaynak dirsek", "73.07 · birleştirir"), ("C", "Cihaza bağlayan flanş", "73.07 · bağlar"),
                ("D", "Redüksiyon", "73.07 · çapları birleştirir"), ("E", "Kör tapa", "73.07 · ucu kapatır")],
               strike="Hortum", fix="yüzden", oth=["Dirsek", "flanş", "redüksiyon", "kör"])

trap("s07", "Kör tapa da 73.07", ("stajyer", 470),
     "Bağlamıyor… <em>73.07 değil!</em>",
     dict(code="73.26", title="Kör tapa", sub="iki boruyu bağlamıyor diye ✗", icon="x"),
     dict(code="73.07", title="Kör tapa", sub="borunun açık ucunu kapatır ✓", icon="ring"),
     "Parça boruyla bütünleşiyor mu?",
     note=("dikkat", "Boruyu duvara tutturan <b>kanca ve destekler</b> 73.07'de <em>değil</em>"),
     who2=("baba", 470, "Boruyla <i>bütünleşiyor</i> mu?"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="bağlamıyor", hayir="Hayır", wrong="şıkkını", right="kapatan", note="dikkat",
             who2="Gümrükçü", tag="bütünleşiyor"))

qscene("s08", 3,
       'Aşağıdaki adi metallerden hangisi için Armonize Sistemde <span class="neg">ayrı bir fasıl açılmamıştır<i></i></span>; '
       'bu metal ve ondan eşya <mark>81. fasılda</mark>, diğer adi metaller arasında yer alır?',
       ["Nikel", "Kurşun", "Çinko", "Kalay", "Kobalt"],
       stem_word="Aşağıdaki", topic="Adi metaller · Bölüm XV", neg="açılmamıştır")

sol_classify("s09", "E", "<b>Kobalt</b> → Fasıl 81 · <b>81.05</b>",
             dict(icon="layers", name="Kobalt ve kobalttan eşya", at="On",
                  chips=[("adi metal", "adi"), ("ayrı faslı yok", "hepsi")]),
             [("doc", "Kendi faslı olanlar", "74 · 75 · 76 · 78 · 79 · 80", "bakır"),
              ("search", "Diğer adi metaller", "tek fasılda toplanır", "Diğer"),
              ("check", "Fasıl 81", "W · Mo · Mg · Co · Ti …", "tungsten")],
             dict(code="81.05", title="Kobalt ve kobalttan eşya", at=("Kobalt", 2)),
             [("Fasıl 75", "nikel", False), ("Fasıl 78", "kurşun", False), ("Fasıl 79", "çinko", False),
              ("Fasıl 80", "kalay", False), ("81.05", "kobalt", True)],
             cand_at="pozisyonunda")

trap("s10", "Nikel ≠ Fasıl 81", ("yardimci", 500),
     "Kobaltın da <em>faslı vardır!</em>",
     dict(code="Fasıl 75", title="Nikel", sub="kendi faslı var ✗", icon="x"),
     dict(code="Fasıl 81", title="Kobalt", sub="81.05 · diğer adi metaller ✓", icon="layers"),
     "Altı metalin faslı var, gerisi 81!",
     note=("dikkat", "<b>Fasıl 77</b> boş · ileride kullanılmak üzere ayrılmış"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="kobaltın", hayir="Hayır", wrong="Nikelin", right=("kobalt", 2), note="dikkat", tag="Kısa"))

qscene("s11", 4,
       'Aşağıdakilerden hangisi <mark>84.28</mark> pozisyonunda <span class="neg">sınıflandırılmaz<i></i></span>?',
       ["Füniküler hattında kullanılan, kendinden hareketli olmayan yolcu vagonu", "Kayak merkezinde kullanılan telesiyej",
        "Kayakçıları yamaç boyunca çeken teleski", "Füniküler hattının çekiş mekanizması ve bucurgatı",
        "Alışveriş merkezinde kullanılan yürüyen merdiven"],
       stem_word="Aşağıdakilerden", topic="Kaldırma-taşıma · Fasıl 84", neg="sınıflandırılmaz", small=True)

sol_statements("s12", "A", "Füniküler vagonu → <b>86.05</b> · 84.28 değil",
               "Füniküler hattında kullanılan yolcu vagonu → 84.28",
               "Fünikülerde yalnız <em>çekiş mekanizması ve bucurgat</em> 84.28'de; vagonlar → <em>86.05</em>", "86.05",
               [("B", "Telesiyej", "8428.60"), ("C", "Teleski", "8428.60"),
                ("D", "Füniküler çekiş mekanizması, bucurgat", "8428.60"), ("E", "Yürüyen merdiven", "8428.40")],
               strike="Ama", fix="vagonlar", oth=["telesiyejler", "teleskiler", "fünikülerlerin", "yürüyen"])

trap("s13", "Kayak merkezi ≠ spor eşyası", ("stajyer", 470),
     "Kayak merkezi… <em>spor eşyası!</em>",
     dict(code="95.06", title="Spor malzemesi", sub="kayak merkezi diye ✗", icon="skate"),
     dict(code="84.28", title="Telesiyej, teleski", sub="insan taşıyan makine ✓", icon="gear"),
     "Vagon taşıttır, çekiş makinedir!",
     note=("dikkat", "Füniküler <b>rayları ve teçhizatı</b> → <b>73.02</b> ya da <b>86.08</b>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="spor", hayir="Hayır", wrong="şıkkını", right="Telesiyej", note="dikkat", tag="Kısa"))

qscene("s14", 5,
       'Bir torna tezgâhında iş parçasını <mark>mıknatıs gücüyle</mark> tutmaya yarayan elektromanyetik torna aynası, tezgâhtan ayrı olarak '
       'ithal ediliyor. Bu eşya hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>84.58</b>", "<b>84.66</b>", "<b>85.05</b>", "<b>85.36</b>", "<b>85.43</b>"],
       stem_word="Bir", topic="Makine / elektrik · 84–85", mono=True)

sol_classify("s15", "C", "<b>85.05</b> · elektromanyetik aynalar adıyla",
             dict(icon="chip", name="Elektromanyetik torna aynası (ayrı)", at="pozisyon",
                  chips=[("mıknatısla tutar", "mıknatıslı"), ("tezgâhtan ayrı", "tezgâhların")]),
             [("doc", "85.05 metni", "elektromanyetik aynalar adıyla", "adıyla"),
              ("search", "84.66 mı?", "mekanik iş tutucular, aynalar", "tutucularını"),
              ("check", "Açıklama notu", "elektrikli aksam → Fasıl 85", "açıklama")],
             dict(code="85.05", title="Elektromıknatıslar, manyetik aynalar", at="Doğru"),
             [("84.58", "torna tezgâhı", False), ("84.66", "mekanik ayna", False), ("85.05", "manyetik ayna", True),
              ("85.36", "anahtar, röle", False), ("85.43", "diğer el. cihaz", False)],
             cand_at="gönderir")

trap("s16", "Tezgâh aksesuarı ≠ 84.66", ("yardimci", 500),
     "Tezgâh aksesuarı… <em>84.66!</em>",
     dict(code="84.66", title="Mekanik ayna", sub="tezgâh aksesuarı diye ✗", icon="gear"),
     dict(code="85.05", title="Elektromanyetik ayna", sub="mıknatısla tutar ✓", icon="chip"),
     "Mıknatısla mı tutuyor?",
     note=("dikkat", "Elektromanyetik <b>kavrama, kaplin ve fren</b> → <b>85.05</b>"),
     who2=("baba", 470, "Mıknatısla mı <i>tutuyor?</i>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="aksesuarıdır", hayir="Hayır", wrong="Mekanik", right="elektromanyetik", note="dikkat",
             who2="Gümrükçü", tag="Mıknatısla"))

coach("s17", [("EŞYAYA BAK", ["baret 65 · kamçı 66", "peruk 67"], "search"),
              ("NOTU OKU", ["kobalt → 81.05", "kelepçe → 73.26"], "doc"),
              ("İŞLEVE BAK", ["vagon → 86.05", "manyetik ayna → 85.05"], "gear")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s18", [("D", "Pozisyon sırası", "65.06 → 67.04"), ("B", "Hortum kelepçesi", "73.26"), ("E", "Kobalt", "81.05"),
                   ("A", "Füniküler vagonu", "86.05"), ("C", "Manyetik ayna", "85.05")], 12)
