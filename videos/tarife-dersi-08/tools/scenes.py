"""Tarife Dersi 8: 25.01 kapsamı (deniz suyu var, maden suyu 22.01), Armonize Sistemde olmayan notlar (ek notlar), bağlayıcı kaynaklar (AB BTB)."""
from kit import S, intro, qscene, sol_statements, trap, coach, answer_key

intro("s01", 8, "Tuz, cetvel notları, bağlayıcı kaynaklar",
      [("salt", "Tuz, deniz suyu", "25.01’in kapsamı", "tuz"),
       ("doc", "Cetvel notları", "hangisi AS’de yok?", "notlar"),
       ("gavel", "Bağlayıcılık", "AB BTB bağlar mı?", "bağlayıcı")], "sekizincisine")

qscene("s02", 1,
       'Aşağıdakilerden hangisi <mark>25.01</mark> pozisyonunda <span class="neg">sınıflandırılmaz<i></i></span>?',
       ["Gazlı doğal maden suyu", "Deniz suyu", "Saf sodyum klorür", "Denatüre tuz",
        "Topaklaşmayı önleyici madde katılmış sofra tuzu"],
       stem_word="Aşağıdakilerden", topic="Tuz · Fasıl 25", neg="sınıflandırılmaz")

sol_statements("s03", "A", "Maden suyu → <em>22.01</em> · 25.01 değil",
               "Gazlı doğal maden suyu → 25.01",
               "Maden suyu <em>içilecek sudur</em> → Fasıl 22, 22.01. 25.01 ise tuz, saf sodyum klorür ve deniz suyunu kapsar.", "22.01",
               [("B", "Deniz suyu", "25.01 · adıyla ✓"),
                ("C", "Saf sodyum klorür", "25.01 · adıyla ✓"),
                ("D", "Denatüre tuz", "25.01 · adıyla ✓"),
                ("E", "Katkılı sofra tuzu", "topaklaşma önleyici serbest ✓")],
               strike="Maden", fix="yirmi", oth=["deniz", "saf", "denatüre", "topaklaşmayı"])

trap("s04", "Deniz suyu ≠ 22.01", ("cano", 430),
     "Deniz suyu da su… <em>22.01!</em>",
     dict(code="22.01", title="Deniz suyu", sub="su diye Fasıl 22’ye ✗", icon="drop"),
     dict(code="25.01", title="Deniz suyu", sub="Fasıl 22 Not 1(b) · fasıl dışı ✓", icon="salt"),
     "Suyun adına değil, fasıl notuna bak!",
     note=("dikkat", "Damıtılmış ve iletken su → <b>28.53</b> · Fasıl 22 Not 1(c)"),
     at=dict(tuzak="Tuzak", who="Cano", bub="sudur", hayir="Hayır", wrong="şıkkını", right="birdedir", note="dikkat", tag="adına"))

qscene("s05", 2,
       'Türk Gümrük Tarife Cetvelinde yer alan aşağıdaki unsurlardan hangisi <mark>Armonize Sistem Nomanklatüründe</mark> '
       '<span class="neg">yer almaz<i></i></span>?',
       ["Bölüm notları", "Fasıl notları", "Ek notlar", "Alt pozisyon notları", "Tarifenin yorumuna ilişkin genel kurallar"],
       stem_word="Türk", topic="Tarife sistematiği · notlar", neg="almaz")

sol_statements("s06", "C", "Ek notlar → <em>KN + ulusal tarife</em>",
               "Ek notlar → Armonize Sistem",
               "Ek notlar <em>Kombine Nomanklatür</em> ve ulusal tarifeye aittir; 6 haneden sonraki ayrıntıyı yorumlar.", "KN + ULUSAL",
               [("A", "Bölüm notları", "AS · ortak ✓"),
                ("B", "Fasıl notları", "AS · ortak ✓"),
                ("D", "Alt pozisyon notları", "AS · 6 hane ✓"),
                ("E", "Genel yorum kuralları", "AS · GYK 1–6 ✓")],
               strike="Ek", fix="Kombine", oth=["Bölüm", "fasıl", "alt", "genel"])

trap("s07", "Alt pozisyon ≠ ulusal", ("stajyer", 470),
     "Alt pozisyon… <em>ulusal açılım!</em>",
     dict(code="D", title="Alt pozisyon notları", sub="ulusal sandı ✗", icon="sort"),
     dict(code="AS", title="6 haneli alt pozisyon", sub="Armonize Sistemin parçası ✓", icon="globe"),
     "Not hangi haneyi yorumluyor?",
     note=("dikkat", "Ek notlar 8 ve daha fazla haneyi yorumlar → ülkeden ülkeye değişebilir"),
     who2=("baba", 470, "Hangi haneyi yorumluyor? <i>6 mı, 8 mi?</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="ulusal", hayir="Hayır", wrong="şıkkını", right="Sistemindir", note="dikkat",
             who2="Gümrükçü", tag="haneyi"))

qscene("s08", 3,
       'Türkiye’de tarife sınıflandırması yapılırken aşağıdakilerden hangisi <mark>bağlayıcı</mark> bir kaynak '
       '<span class="neg">değildir<i></i></span>?',
       ["Türk Gümrük Tarife Cetveli", "Tarifenin yorumuna ilişkin genel kurallar",
        "Gümrük Genel Tebliği ile yayımlanan Gümrük Tarife Cetveli İzahnamesi",
        "Gümrük Genel Tebliği ile yayımlanan tarife sınıflandırma kararları",
        "AB Bağlayıcı Tarife Bilgisi veri tabanındaki kararlar"],
       stem_word="Türkiye'de", topic="Tarife mevzuatı · kaynaklar", neg="değildir", small=True)

sol_statements("s09", "E", "AB BTB → <em>yardımcı referans</em> · bağlayıcı değil",
               "AB BTB veri tabanı → bağlayıcı kaynak",
               "AB BTB’leri ülkemizde yalnızca <em>yardımcı referans</em>; resmî bağlayıcılığı yok (GGM yazısı, 2020).", "REFERANS",
               [("A", "Türk Gümrük Tarife Cetveli", "cetvelin kendisi ✓"),
                ("B", "Genel yorum kuralları", "cetvelin parçası ✓"),
                ("C", "Gümrük Tarife Cetveli İzahnamesi", "Gümrük Genel Tebliği ✓"),
                ("D", "Tarife sınıflandırma kararları", "Gümrük Genel Tebliği ✓")],
               strike="Avrupa", fix="yardımcı", oth=[("Tarife", 2), ("genel", 2), "izahname", "sınıflandırma"])

trap("s10", "AB BTB ≠ bağlayıcı", ("yardimci", 500),
     "AB’de BTB var… <em>aynısını yazalım!</em>",
     dict(code="AB BTB", title="Tek dayanak", sub="bağlayıcı sandı ✗", icon="globe"),
     dict(code="GGM 2020", title="Yardımcı referans", sub="resmî bağlayıcılığı yok ✓", icon="doc"),
     "AB BTB’si yol gösterir, karar vermez!",
     note=("dikkat", "Türkiye’de verilen <b>BTB</b> → gümrük idaresini hak sahibine karşı bağlar"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="bulunca", hayir="Hayır", wrong="dayandırdı", right="farklı", note="dikkat", tag="gösterir"))

coach("s11", [("25.01", ["tuz · saf NaCl · deniz suyu", "maden suyu → 22.01"], "salt"),
              ("NOTLAR", ["bölüm, fasıl, alt poz. → AS", "ek notlar → KN + ulusal"], "doc"),
              ("BAĞLAYICILIK", ["cetvel, GYK, izahname ✓", "AB BTB → referans"], "gavel")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("A", "Gazlı maden suyu", "22.01 · 25.01 değil"), ("C", "Ek notlar", "KN + ulusal tarife"),
                   ("E", "AB BTB veri tabanı", "yardımcı referans")], 9)
