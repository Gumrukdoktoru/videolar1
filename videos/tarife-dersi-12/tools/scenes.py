"""Tarife Dersi 12 (3 soru): pul biber 09.04 (07.12 değil), yalnız hücrelerden oluşan güneş paneli 85.41 (85.01 değil),
87.11 kapsamı (motorsuz skuter 95.03)."""
import kit
from kit import S, intro, qscene, sol_classify, sol_statements, trap, coach, answer_key

kit.NQ = 3

intro("s01", 12, "Pul biber, güneş paneli, iki tekerlek",
      [("flame", "Pul biber", "07.12 mi, 09.04 mü?", "pul"),
       ("chip", "Güneş paneli", "85.01 · 85.41", "güneş"),
       ("gear", "İki tekerlek", "87.11 · 95.03", "tekerlekli")], "ikincisine")

qscene("s02", 1,
       'Kurutulup pul hâlinde ezilmiş, başka hiçbir madde katılmamış <mark>kırmızı biber</mark>, yani pul biber, '
       'hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>07.09</b>", "<b>07.12</b>", "<b>09.04</b>", "<b>20.05</b>", "<b>21.03</b>"],
       stem_word="Kurutulup", topic="Sebze / baharat · 7–9", mono=True)

sol_classify("s03", "C", "<b>09.04</b> · kurutulmuş, ezilmiş biber",
             dict(icon="flame", name="Pul biber", at="Pul",
                  chips=[("kurutulmuş", "kurutulup"), ("ezilmiş", ("ezilmiş", 1))]),
             [("seed", "Capsicum cinsi", "kırmızı biber, kurutulmuş", "Kapsikum"),
              ("doc", "Fasıl 7 açıklama notu", "kuru Capsicum, Pimenta → dışarıda", "Yedinci"),
              ("check", "09.04 metni", "kuru, ezilmiş biberi adıyla sayar", "adıyla")],
             dict(code="09.04", title="Capsicum, Pimenta: kurutulmuş, ezilmiş", at="Doğru"),
             [("07.09", "taze sebze", False), ("07.12", "kuru sebze", False), ("09.04", "biber, baharat", True),
              ("20.05", "hazır sebze", False), ("21.03", "sos, çeşni", False)],
             cand_at="Taze")

trap("s04", "Kuru biber ≠ 07.12", ("cano", 430),
     "Biber sebzedir… <em>07.12!</em>",
     dict(code="07.12", title="Kurutulmuş sebze", sub="biber sebzedir diye ✗", icon="x"),
     dict(code="09.04", title="Kuru, ezilmiş biber", sub="baharat · Fasıl 9 ✓", icon="flame"),
     "Kuruysa baharat, tazeyse sebze!",
     note=("dikkat", "Biber <b>salçası</b>, biber <b>turşusu</b> gibi hazır ürünler → <b>Fasıl 20</b>"),
     at=dict(tuzak="Tuzak", who="Cano", bub="sebzedir", hayir="Hayır", wrong="şıkkını", right="baharat", note="dikkat", tag="Kısa"))

qscene("s05", 2,
       'Yalnızca birbirine bağlanmış <mark>güneş pillerinden</mark> oluşan; invertör, akü veya bir motoru doğrudan besleyen '
       'başka bir eleman içermeyen fotovoltaik güneş paneli hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>85.01</b>", "<b>85.04</b>", "<b>85.07</b>", "<b>85.41</b>", "<b>94.05</b>"],
       stem_word="Yalnızca", topic="Elektrik · Fasıl 85", mono=True)

sol_classify("s06", "D", "<b>85.41</b> · fotovoltaik hücreler, panel",
             dict(icon="chip", name="Fotovoltaik güneş paneli", at="Güneş",
                  chips=[("ışık → elektrik", "elektriğe"), ("modül / panel", "modül")]),
             [("bulb", "Fotovoltaik hücre", "ışığı doğrudan elektriğe çevirir", "fotovoltaik"),
              ("chip", "Yarı iletken cihaz", "panel hâlinde de → 85.41", "yarı"),
              ("doc", "85.01 açıklama notu", "akü, invertörlü → jeneratör", "açıklama")],
             dict(code="85.41", title="Fotovoltaik hücreler, modül, panel", at="Doğru"),
             [("85.01", "jeneratör", False), ("85.04", "konvertör", False), ("85.07", "akümülatör", False),
              ("85.41", "fotovoltaik hücre", True), ("94.05", "aydınlatma", False)],
             cand_at="Konvertörler")

trap("s07", "Elektrik üretiyor ≠ 85.01", ("yardimci", 500),
     "Elektrik üretiyor… <em>jeneratör!</em>",
     dict(code="85.01", title="Fotovoltaik jeneratör", sub="elektrik üretiyor diye ✗", icon="battery"),
     dict(code="85.41", title="Tek başına panel", sub="yarı iletken cihaz ✓", icon="chip"),
     "Panelin yanında başka ne var?",
     note=("dikkat", "Fotovoltaik <b>LED aydınlatma cihazı</b> → <b>94.05</b>"),
     who2=("baba", 470, "Panelin yanında <i>ne var?</i>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="jeneratördür", hayir="Hayır", wrong="şıkkını", right="Tek", note="dikkat",
             who2="Gümrükçü", tag="Panelin"))

qscene("s08", 3,
       'Aşağıdakilerden hangisi <mark>87.11</mark> pozisyonunda <span class="neg">sınıflandırılmaz<i></i></span>?',
       ["Pedal çevrildiğinde devreye giren, yardımcı elektrik motorlu bisiklet",
        "Ayakla itilerek ilerleyen, yetişkinlerin de kullanabildiği motorsuz skuter",
        "Kendi kendini dengeleyen, tek kişilik, iki tekerlekli elektrikli nakil aracı",
        "Hem motoru hem pedalı bulunan mopet", "Motosiklete takılan yan sepet"],
       stem_word="Aşağıdakilerden", topic="Taşıtlar · Fasıl 87", neg="sınıflandırılmaz", small=True)

sol_statements("s09", "B", "Motorsuz skuter → <b>95.03</b> · 87.11 değil",
               "Ayakla itilen, motorsuz skuter → 87.11",
               "Motorsuz skuter yetişkin için olsa da <em>tekerlekli oyuncak</em> sayılır → <em>95.03</em>", "95.03",
               [("A", "Yardımcı elektrik motorlu bisiklet", "87.11"), ("C", "Kendini dengeleyen elektrikli araç", "87.11 · açıklama notu"),
                ("D", "Motoru ve pedalı olan mopet", "87.11"), ("E", "Motosiklet yan sepeti", "87.11")],
               strike="Motorsuz", fix="oyuncaklar", oth=["yardımcı", "kendi", "mopetler", "sepetleri"])

trap("s10", "Bisiklet ≠ hep 87.12", ("stajyer", 470),
     "Bisiklet bisiklettir… <em>87.12!</em>",
     dict(code="87.12", title="Motorsuz bisiklet", sub="bisiklet diye ✗", icon="x"),
     dict(code="87.11", title="Yardımcı motorlu bisiklet", sub="motor elektrikli olsa da ✓", icon="gear"),
     "Motor var mı?",
     note=("dikkat", "Çocuklar için <b>üç tekerlekli</b> bisiklet → <b>95.03</b>"),
     who2=("baba", 470, "Motor <i>var mı?</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="bisiklettir", hayir="Hayır", wrong="şıkkını", right="yardımcı", note="dikkat",
             who2="Gümrükçü", tag="Motor"))

coach("s11", [("KURU MU, TAZE Mİ?", ["kuru biber → 09.04", "taze biber → 07.09"], "flame"),
              ("JENERATÖR MÜ?", ["tek panel → 85.41", "akü, invertörlü → 85.01"], "chip"),
              ("MOTOR VAR MI?", ["motorlu bisiklet → 87.11", "motorsuz skuter → 95.03"], "gear")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("C", "Pul biber", "09.04"), ("D", "Güneş paneli", "85.41"), ("B", "Motorsuz skuter", "95.03")], 13)
