"""Tarife Dersi 15 (3 soru): nevresim takımı 63.02 (63.08 değil), okey takımı 95.04 (95.03 / 39.26 değil),
aynı bölümdeki eşyalar: pusula 90.14, akort düdüğü 92.09, duvar saati 91.05 → Bölüm XVIII."""
import kit
from kit import S, intro, qscene, sol_classify, sol_true, trap, coach, answer_key

kit.NQ = 3

intro("s01", 15, "Nevresim takımı, okey takımı, bölüm yapısı",
      [("bed", "Nevresim takımı", "63.02 · 63.08", "nevresim"),
       ("layers", "Okey takımı", "95.03 · 95.04", "okey"),
       ("music", "Bölüm yapısı", "Bölüm XVIII", "bölüm")], "beşincisine")

qscene("s02", 1,
       'Pamuklu dokuma kumaştan bir nevresim, bir çarşaf ve iki yastık kılıfından oluşan, <mark>perakende satış ambalajındaki</mark> '
       'nevresim takımı hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>63.01</b>", "<b>63.02</b>", "<b>63.04</b>", "<b>63.08</b>", "<b>94.04</b>"],
       stem_word="Pamuklu", topic="Mensucat · Fasıl 63", mono=True)

sol_classify("s03", "B", "<b>63.02</b> · yatak çarşafları",
             dict(icon="bed", name="Nevresim takımı", at="Nevresim",
                  chips=[("yorgan kılıfı", "yorgan"), ("çarşaf, yastık kılıfı", "çarşaf")]),
             [("doc", "63.02 açıklama notu", "yatak çarşafları adıyla", "adıyla"),
              ("layers", "Tüm parçalar 63.02", "takım kuralına gerek yok", "Takımdaki"),
              ("check", "GYK 1", "doğrudan 63.02", "birinci")],
             dict(code="63.02", title="Yatak çarşafları", at="Doğru"),
             [("63.01", "battaniye", False), ("63.02", "yatak çarşafı", True), ("63.04", "mefruşat", False),
              ("63.08", "halı yapım takımı", False), ("94.04", "yorgan", False)],
             cand_at="Yorganın")

trap("s04", "“Takım” ≠ 63.08", ("yardimci", 500),
     "Takım yazıyor… <em>63.08!</em>",
     dict(code="63.08", title="Halı, kilim yapım takımı", sub="takım kelimesi diye ✗", icon="x"),
     dict(code="63.02", title="Hazır nevresim takımı", sub="yatak çarşafı ✓", icon="bed"),
     "Kelimeye değil, eşyaya bakın!",
     note=("dikkat", "İçi doldurulmuş <b>yorgan, yastık</b> → <b>94.04</b>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="takım", hayir="Hayır", wrong="şıkkını", right="Hazır", note="dikkat", tag="Kısa"))

qscene("s05", 2,
       'Plastik taşlar ve ıstakalardan oluşan, perakende satılan <mark>okey takımı</mark> hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>39.26</b>", "<b>95.03</b>", "<b>95.04</b>", "<b>95.05</b>", "<b>95.06</b>"],
       stem_word="Plastik", topic="Oyunlar · Fasıl 95", mono=True)

sol_classify("s06", "C", "<b>95.04</b> · salon ve masa oyunları",
             dict(icon="layers", name="Okey takımı", at="Okey",
                  chips=[("masa oyunu", "masa"), ("plastik taşlar", "plastikten")]),
             [("star", "Salon oyunu", "masa başında oynanır", "salon"),
              ("doc", "95.04 kapsamı", "konsol, bilardo, tavla, satranç", "kapsar"),
              ("x", "Fasıl 39 notu", "Fasıl 95 eşyası hariç", "notu")],
             dict(code="95.04", title="Salon ve masa oyunları", at="Doğru"),
             [("39.26", "plastik eşya", False), ("95.03", "oyuncak", False), ("95.04", "masa oyunu", True),
              ("95.05", "eğlence eşyası", False), ("95.06", "spor eşyası", False)],
             cand_at="Oyuncaklar")

trap("s07", "Oyun ≠ oyuncak", ("cano", 430),
     "Oynanıyorsa… <em>oyuncaktır!</em>",
     dict(code="95.03", title="Oyuncaklar, modeller", sub="oynanıyor diye ✗", icon="x"),
     dict(code="95.04", title="Okey, tavla, satranç", sub="masa oyunları ✓", icon="layers"),
     "Oyuncak mı, masa oyunu mu?",
     note=("dikkat", "Plastikten olsa da <b>Fasıl 95</b> eşyası <b>Fasıl 39</b>'a girmez"),
     at=dict(tuzak="Tuzak", who="Cano", bub="oyuncaktır", hayir="Hayır", wrong="şıkkını", right="masa", note="dikkat", tag="Kısa"))

qscene("s08", 3,
       'Aşağıdaki seçeneklerin hangisinde sayılan eşyaların <mark>tümü</mark> tarife cetvelinin <mark>aynı bölümünde</mark> yer alır?',
       ["Pusula, akort düdüğü, duvar saati", "Kontakt lens, optik olarak işlenmemiş gözlük camı, dürbün",
        "Kol saati, deri saat kayışı, ahşap mücevher kutusu", "Piyano, piyano taburesi, basılı nota",
        "Metronom, gitar teli, gitar kılıfı"],
       stem_word="Aşağıdaki", topic="Bölüm yapısı · XVIII")

sol_true("s09", "A", "Hepsi <b>Bölüm XVIII</b> · Fasıl 90–92",
         "Pusula <em>90.14</em> · akort düdüğü <em>92.09</em> · duvar saati <em>91.05</em> → hepsi <em>Bölüm XVIII</em>", "Fasıl 90–92",
         [("B", "İşlenmemiş gözlük camı → <em>70.15</em> · Bölüm XIII"),
          ("C", "Ahşap mücevher kutusu → <em>44.20</em> · Bölüm IX"),
          ("D", "Tabure <em>94.01</em> · XX, basılı nota <em>49.04</em> · X"),
          ("E", "Ayrı gelen gitar kılıfı → <em>42.02</em> · Bölüm VIII")],
         basis=("sekizinci", 1), oth=["gözlük", "Ahşap", "Piyano", "gitar"])

trap("s10", "Kılıf ≠ 92.09", ("stajyer", 470),
     "Gitarın aksesuarı… <em>92.09!</em>",
     dict(code="92.09", title="Müzik aleti aksesuarı", sub="gitarın aksesuarı diye ✗", icon="x"),
     dict(code="42.02", title="Müzik aleti mahfazası", sub="metinde adıyla · Bölüm VIII ✓", icon="case"),
     "Ayrı geldiyse kılıf, kendi yerine!",
     note=("dikkat", "Gitarla <b>birlikte</b> gelen, ona uygun kılıf → <b>GYK 5(a)</b>, gitarla"),
     who2=("baba", 470, "Ayrı geldiyse kılıf, <i>kendi yerine</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="aksesuarıdır", hayir="Hayır", wrong="şıkkını", right="mahfazaları", note="dikkat",
             who2="Gümrükçü", tag=("Ayrı", 2)))

coach("s11", [("EŞYAYA BAK", ["nevresim takımı → 63.02", "halı takımı → 63.08"], "bed"),
              ("İŞLEV BELİRLER", ["okey → 95.04", "oyuncak → 95.03"], "layers"),
              ("BÖLÜM XVIII", ["Fasıl 90 · 91 · 92", "ayrı kılıf → 42.02"], "music")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("B", "Nevresim takımı", "63.02"), ("C", "Okey takımı", "95.04"), ("A", "Pusula, akort, saat", "Bölüm XVIII")], 16)
