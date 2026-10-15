"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 15
META = "DERS · <b>TARİFE #15</b> · 3 SORU · FASIL 63 · 95 · BÖLÜM XVIII"
TITLE = "Tarife Dersi 15 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · NEVRESİM TAKIMI", ["s02", "s03", "s04"]), ("SORU 2 · OKEY TAKIMI", ["s05", "s06", "s07"]),
    ("SORU 3 · BÖLÜM YAPISI", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Nevresim takımı 63.02 mi, 63.08 mi?", "Soru 2: Okey takımı oyuncak mı, masa oyunu mu?",
      "Soru 3: Hangi şıktaki eşyaların tümü aynı bölümde?", "Koçun notu", "Cevap anahtarı"]
KW = ["yatak çarşafları", "adıyla", "takım kuralına gerek yoktur", "Kelimeye değil", "eşyaya bakın",
      "salon oyunudur", "masa oyunları", "Oyuncak mı", "masa oyunu mu",
      "on sekizinci bölümdedir", "en az bir yabancı", "Müzik aleti mahfazaları", "Ayrı geldiyse",
      "A şıkkı", "B şıkkı", "C şıkkı", "D şıkkı", "E şıkkı", "dikkat:", "Hayır!"]


def cues(T):
    out = [("s01", 0.2, "neutral")]
    for q, s, t in (("s02", "s03", "s04"), ("s05", "s06", "s07"), ("s08", "s09", "s10")):
        out += [(q, 0.0, "soru"), (s, T(s, "Cevap"), "cevap"), (s, T(s, "Cevap") + 3.0, "neutral"), (t, 0.0, "tuzak"), (t, T(t, "dikkat"), "dikkat")]
    return out + [("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Nevresim takımı, okey takımı ve bölüm yapısı",
    message="Nevresim takımı 63.02, 63.08 değil (B) · okey takımı 95.04, 95.03 ya da 39.26 değil (C) · pusula 90.14, akort düdüğü 92.09, duvar saati 91.05: hepsi Bölüm XVIII (A).",
    intent="Bu derste 3 soru var. Ölçülen bilgi alanları: 63.02 izahnamesinin nevresim (yorgan kılıfı), çarşaf ve yastık kılıflarını yatak çarşafı olarak adıyla sayması; tüm parçaları aynı pozisyona giren takımda GYK 1 ile doğrudan sınıflandırma, 63.08'in halı, kilim, işlemeli masa örtüsü yapım takımlarıyla sınırlı olması, dolgulu yorgan ve yastık 94.04; okeyin salon ve masa oyunu olarak 95.04'te yer alması, 95.03 oyuncaklar, Fasıl 39 notunun Fasıl 95 eşyasını hariç tutması; Bölüm XVIII'in Fasıl 90–92'den oluşması (pusula 90.14, saat 91.05, akort düdüğü, metronom, tel 92.09), işlenmemiş gözlük camı 70.15 (XIII), ahşap mücevher kutusu 44.20 (IX), müzik aleti mahfazası 42.02 (VIII), tabure 94.01 (XX), basılı nota 49.04 (X); aletiyle birlikte gelen kılıfta GYK 5(a).",
    team="Yardımcı (takım kelimesini görünce 63.08 → HAYIR, 63.02) · Cano (oynanıyorsa oyuncaktır diye 95.03 → HAYIR, 95.04) · Stajyer (gitar kılıfını aksesuar sanıp 92.09 → HAYIR, 42.02) ve Gümrükçü Baba (“ayrı geldiyse kılıf, kendi yerine”).",
    visuals="ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), doğru ifade kartı + dört yanlış şıkkın düzeltmesi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: 63.02 izahnamesi (yatak çarşafları: çarşaflar, yastık kılıfları, yorgan kılıfları), 63.01, 63.04, 63.08 (halı, kilim, işlemeli masa örtüsü vb. yapımına mahsus mensucat ve iplikten takımlar), 94.04; GYK 1; 95.04 (salon ve masa oyunları; tavla, satranç, oyun kâğıtları, video oyun konsolları, bilardo), 95.03, 95.05, 95.06, 39.26, Fasıl 39 notları (Fasıl 95 eşyası hariç); Bölüm XVIII (Fasıl 90, 91, 92): 90.01, 90.05, 90.14 (pusulalar), 91.01–91.02, 91.05 (duvar saatleri), 91.13, 92.01, 92.09 (aksam ve aksesuarlar, teller, metronomlar, akort düdükleri); 70.15 (Bölüm XIII), 44.20 izahnamesi (ahşap mücevher kutuları, Bölüm IX), 42.02 (müzik aletleri mahfazaları, Bölüm VIII), 94.01 (Bölüm XX), 49.04 (Bölüm X); GYK 5(a).",
    yt_title="Nevresim Takımı 63.02 mi 63.08 mi? · Okey Takımı 95.04 · Bölüm XVIII Sorusu | Tarife Dersi #15 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin on beşincisinde 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, nevresim takımı, 63.02, 63.08, yatak çarşafı, okey, 95.04, 95.03, masa oyunları, Bölüm XVIII, pusula, 90.14, akort düdüğü, 92.09, duvar saati, 91.05, gitar kılıfı, 42.02, 44.20, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Pamuklu dokuma kumaştan bir nevresim, bir çarşaf ve iki yastık kılıfından oluşan, perakende satış ambalajındaki nevresim takımı hangi tarife pozisyonunda sınıflandırılır?",
             options=["63.01", "63.02", "63.04", "63.08", "94.04"], answer="B",
             why="Nevresim (yorgan kılıfı), çarşaf ve yastık kılıfları 63.02 izahnamesinde yatak çarşafı olarak adıyla sayılır. Takımdaki tüm parçalar aynı pozisyona girdiğinden takım kuralına gerek kalmaz; GYK 1 ile doğrudan 63.02. 63.08 halı, kilim, işlemeli masa örtüsü gibi eşyaların yapımına mahsus mensucat ve iplik takımlarıdır; içi doldurulmuş yorgan ve yastık 94.04'tedir.",
             ref="63.02 izahnamesi · GYK 1", yt="Nevresim takımı: takım kuralı mı, 63.02 mi?"),
        dict(stem="Plastik taşlar ve ıstakalardan oluşan, perakende satılan okey takımı hangi tarife pozisyonunda sınıflandırılır?",
             options=["39.26", "95.03", "95.04", "95.05", "95.06"], answer="C",
             why="Okey masa başında oynanan bir salon oyunudur. 95.04 video oyun konsollarından bilardoya kadar salon ve masa oyunlarını kapsar; tavla, satranç ve oyun kâğıtları da buradadır. Taşların plastikten olması sonucu değiştirmez; Fasıl 39 notları Fasıl 95 eşyasını hariç tutar. 95.03 oyuncaklar ve modeller içindir.",
             ref="95.04 · Fasıl 39 notları", yt="Okey takımı: oyuncak mı, masa oyunu mu?"),
        dict(stem="Aşağıdaki seçeneklerin hangisinde sayılan eşyaların tümü tarife cetvelinin aynı bölümünde yer alır?",
             options=["Pusula, akort düdüğü, duvar saati", "Kontakt lens, optik olarak işlenmemiş gözlük camı, dürbün",
                      "Kol saati, deri saat kayışı, ahşap mücevher kutusu", "Piyano, piyano taburesi, basılı nota", "Metronom, gitar teli, gitar kılıfı"],
             answer="A", why="Pusula 90.14, akort düdüğü 92.09, duvar saati 91.05: üçü de Fasıl 90–92'den oluşan Bölüm XVIII'dedir. Diğer şıklarda en az bir yabancı var: optik olarak işlenmemiş gözlük camı 70.15 (Bölüm XIII); ahşap mücevher kutusu 44.20 (Bölüm IX); piyano taburesi 94.01 (Bölüm XX) ve basılı nota 49.04 (Bölüm X); ayrı gelen gitar kılıfı 42.02 (Bölüm VIII). Gitarla birlikte gelen, ona uygun kılıf ise GYK 5(a) ile gitarla sınıflandırılır.",
             ref="Bölüm XVIII · 90.14 · 91.05 · 92.09", yt="Pusula, akort düdüğü, duvar saati: aynı bölüm sorusu."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #15; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — nevresim takımı; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s03="CEVAP B; nevresim takımı kartı → 63.02 notu, tüm parçalar 63.02, GYK 1 → 63.02; aday şeridi.",
        s04="TUZAK — Yardımcı takım kelimesini görünce 63.08 → HAYIR, 63.02; DİKKAT: dolgulu yorgan, yastık 94.04.",
        s05="SORU 2/3 — okey takımı; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP C; okey kartı → salon oyunu, 95.04 kapsamı, Fasıl 39 notu → 95.04; aday şeridi.",
        s07="TUZAK — Cano oynanıyorsa oyuncaktır diye 95.03 → HAYIR, 95.04; DİKKAT: Fasıl 95 eşyası Fasıl 39'a girmez.",
        s08="SORU 3/3 — eşyaların tümü aynı bölümde; 5 üçlü şık; 3 sn geri sayım.",
        s09="CEVAP A; doğru ifade kartı (90.14 · 92.09 · 91.05 → Bölüm XVIII) + dört yanlış şıkkın düzeltmesi (70.15, 44.20, 94.01 / 49.04, 42.02).",
        s10="TUZAK — Stajyer ayrı gelen gitar kılıfını 92.09 sanır → HAYIR, 42.02; DİKKAT: gitarla birlikte gelen kılıf GYK 5(a); Gümrükçü Baba 'ayrı geldiyse kılıf, kendi yerine'.",
        s11="İPUCU · Koçun notu — zihin haritası: eşyaya bak · işlev belirler · Bölüm XVIII.",
        s12="ÖNEMLİ · Cevap anahtarı B · C · A; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
