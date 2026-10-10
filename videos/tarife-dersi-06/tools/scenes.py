"""Tarife Dersi 6: tarife cetvelinin yasal dayanağı, kod seviyeleri (8501.10), Fasıl 8 kapsamı (susam 12.07)."""
from kit import S, intro, qscene, sol_true, sol_ladder, sol_statements, trap, coach, answer_key

intro("s01", 6, "Yasal dayanak, kod seviyeleri, meyve faslı",
      [("gavel", "Yasal dayanak", "kim değiştirir?", "yasal"),
       ("sort", "Kod seviyeleri", "kaç hane, hangi sistem?", "kod"),
       ("seed", "Meyve faslı", "Fasıl 8 mi, 12 mi?", "meyve")], "altıncısına")

qscene("s02", 1,
       '<mark>Gümrük Giriş Tarife Cetveli</mark> ile ilgili aşağıdaki ifadelerden hangisi <span class="neg">doğrudur<i></i></span>?',
       ["Cetvel Brüksel Nomanklatürü esas alınarak düzenlenmiştir; pozisyonlarını değiştirmeye Cumhurbaşkanı yetkilidir.",
        "Cetvel Armonize Sistem Nomanklatürü esas alınarak düzenlenmiştir; pozisyonlarını değiştirmeye Ticaret Bakanlığı yetkilidir.",
        "Cetvel Dünya Gümrük Örgütü tarafından yayımlanır; ülkeler pozisyonlarını değiştiremez.",
        "Cetvel Armonize Sistem Nomanklatürü esas alınarak düzenlenmiştir; pozisyonlarını ve notlarını değiştirmeye Cumhurbaşkanı yetkilidir.",
        "Cetvelin ilk altı hanesi ulusal düzeyde belirlenir; Armonize Sistem yalnızca fasılları belirler."],
       stem_word="Gümrük", topic="Tarife cetveli · yasal dayanak", neg="doğrudur", small=True)

sol_true("s03", "D", "Armonize Sistem esas · yetki <em>Cumhurbaşkanında</em>",
         "Cetvel <em>Armonize Sistem Nomanklatürü</em> esas alınarak düzenlenmiştir; pozisyon, not ve genel kuralları "
         "genişletmeye, açmaya ve değiştirmeye <em>Cumhurbaşkanı</em> yetkilidir.", "TARİFE CETVELİ KANUNU",
         [("A", "<s>Brüksel Nomanklatürü</s> eski sistemdir; bugünkü dayanak <em>Armonize Sistem</em>."),
          ("B", "<s>Ticaret Bakanlığı</s> değil; değiştirme yetkisi <em>Cumhurbaşkanında</em>."),
          ("C", "<s>DGÖ yayımlamaz</s>; cetvel ulusaldır, her yıl <em>Cumhurbaşkanı kararıyla</em> yayımlanır."),
          ("E", "<s>Ulusal değil</s>; ilk 6 hane bütün Armonize Sistem ülkelerinde <em>ortaktır</em>.")],
         basis="Cumhurbaşkanı", oth=["Brüksel", "Ticaret", "yayımlamaz", "ilk"])

trap("s04", "Yayımlayan ≠ yetkili", ("cano", 430),
     "Cetveli bakanlık yayımlıyor… <em>B!</em>",
     dict(code="B", title="Ticaret Bakanlığı yetkili", sub="kanunda böyle yazmaz ✗", icon="building"),
     dict(code="D", title="Cumhurbaşkanı yetkili", sub="Kanun yetkiyi açıkça verir ✓", icon="gavel"),
     "Şıkkın iki yarısını da kontrol et!",
     note=("dikkat", "<em>Brüksel Nomanklatürü</em> = Armonize Sistemden önceki eski sistem; A şıkkının ilk yarısı tuzak"),
     at=dict(tuzak="Tuzak", who="Cano", bub="bakanlık", hayir="Hayır", wrong="şıkkını", right="Cumhurbaşkanına", note="dikkat", tag="tür"))

qscene("s05", 2,
       'Aşağıdaki kodlardan hangisi bir <mark>Armonize Sistem alt pozisyonudur</mark>?',
       ["<b>85.01</b>", "<b>8501.10</b>", "<b>85</b>", "<b>8501.10.10.00.00</b>", "<b>8501.10.10</b>"],
       stem_word="Aşağıdaki", topic="Tarife sistematiği · kod yapısı", mono=True)

sol_ladder("s06", "B", "<b>8501.10</b> · Armonize Sistem alt pozisyonu",
           [("85", 2, "Fasıl", "elektrikli makine ve cihazlar", False, "faslı"),
            ("85.01", 4, "Pozisyon", "Armonize Sistem", False, ("pozisyonu", 1)),
            ("8501.10", 6, "Alt pozisyon", "Armonize Sistem · bütün AS ülkelerinde ortak", True, ("alt", 1)),
            ("8501.10.10", 8, "Kombine Nomanklatür", "Avrupa Birliği", False, "Kombine"),
            ("8501.10.10.00.00", 12, "GTİP", "Gümrük Tarife İstatistik Pozisyonu", False, "İstatistik")],
           note_html="İlk <em>6 hane</em> bütün Armonize Sistem ülkelerinde <em>aynıdır</em>", note_at="ortaktır")

trap("s07", "En uzun kod ≠ AS düzeyi", ("stajyer", 470),
     "En uzun kod en ayrıntılısı… <em>12 hane!</em>",
     dict(code="12 hane", title="8501.10.10.00.00", sub="ulusal istatistik pozisyonu ✗", icon="layers"),
     dict(code="6 hane", title="8501.10", sub="Armonize Sistem 6 hanede biter ✓", icon="globe"),
     "Sistemin adını gör, hanesini say!",
     note=("dikkat", "7.–8. hane → <b>Kombine Nomanklatür</b> · sonrası → ulusal açılım"),
     who2=("baba", 470, "Hangi sistem? <i>O sistemin hanesini say!</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="uzun", hayir="Hayır", wrong="kodu", right="biter", note="Yedinci",
             who2="Gümrükçü", tag="sayısını"))

qscene("s08", 3,
       'Aşağıdakilerden hangisi tarife cetvelinin <mark>8. faslında</mark> <span style="white-space:nowrap"><span class="neg">sınıflandırılmaz<i></i></span>?</span>',
       ["Susam tohumu", "Kabuğu soyulmuş badem", "Taze avokado", "Kurutulmuş kayısı", "Kaju cevizi"],
       stem_word="Aşağıdakilerden", topic="Bitkisel ürünler · Fasıl 8", neg="sınıflandırılmaz")

sol_statements("s09", "A", "Susam → <em>12.07</em> · yağlı tohum",
               "Susam tohumu → Fasıl 8",
               "Susam bir <em>yağlı tohumdur</em> → Fasıl 12, 12.07. Fasıl 8 yalnızca yenilen meyveleri ve sert kabuklu meyveleri kapsar.", "12.07",
               [("B", "Kabuğu soyulmuş badem", "08.02 · sert kabuklu ✓"),
                ("C", "Taze avokado", "08.04 · taze meyve ✓"),
                ("D", "Kurutulmuş kayısı", "08.13 · kurutulmuş ✓"),
                ("E", "Kaju cevizi", "08.01 · sert kabuklu ✓")],
               strike="Susam", fix="yağlı", oth=["Badem", "avokado", "kayısı", "kaju"])

trap("s10", "Çerez gibi yenir ≠ meyve", ("yardimci", 500),
     "Çerez gibi yeniyor… <em>Fasıl 8!</em>",
     dict(code="Fasıl 8", title="Yenilen meyveler", sub="susam meyve değil ✗", icon="box"),
     dict(code="12.07", title="Yağlı tohumlar · susam", sub="Fasıl 12 ✓", icon="seed"),
     "Meyve mi, yağlı tohum mu? Önce onu sor!",
     note=("dikkat", "Yer fıstığı → <b>12.02</b> · kavrulmuş ya da hazırlanmışsa → <b>Fasıl 20</b>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="çerez", hayir="Hayır", wrong="koydu", right="yağlı", note="dikkat", tag="Kavrulmuş"))

coach("s11", [("YASAL DAYANAK", ["Armonize Sistem esas", "yetki: Cumhurbaşkanı"], "gavel"),
              ("KOD MERDİVENİ", ["2 · 4 · 6 · 8 · 12 hane", "AS düzeyi = ilk 6 hane"], "sort"),
              ("YAĞLI TOHUMLAR", ["susam, yer fıstığı → Fasıl 12", "meyve faslı değil"], "seed")],
      at_motto="kuralı", br=["Bir", "İki", "Üç"])

answer_key("s12", [("D", "Yasal dayanak", "AS esas · Cumhurbaşkanı yetkili"), ("B", "Kod seviyesi", "8501.10 · AS alt pozisyonu"),
                   ("A", "Susam tohumu", "12.07 · Fasıl 12")], 7)
