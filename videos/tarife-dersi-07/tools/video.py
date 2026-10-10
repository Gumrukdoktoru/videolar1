"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 7
META = "DERS · <b>TARİFE #7</b> · YEM, EV ALETİ, KUVARS"
TITLE = "Tarife Dersi 7 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · FASIL 12", ["s02", "s03", "s04"]), ("SORU 2 · EV ALETLERİ", ["s05", "s06", "s07"]),
    ("SORU 3 · ERİTİLMİŞ KUVARS", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Hangisi 12. fasılda sınıflandırılır?", "Soru 2: Hangi ev aleti farklı fasılda?",
      "Soru 3: Eritilmiş kuvarstan deney tüpü hangi fasılda?", "Koçun notu", "Cevap anahtarı"]
KW = [r"yem bitkisi\w*", r"kaba yem", r"hububat\w*", r"adıyla", r"ekime mahsus", r"elektrotermik", r"Çamaşır kurutma",
      r"dokumaya elverişli", r"gazla çalışan", r"cam sayılır", r"camdır", r"eritildiyse", r"işlenmemiş",
      r"A şıkkı", r"B şıkkı", r"C şıkkı", r"D şıkkı", r"E şıkkı", r"dikkat:", r"Hayır!"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s03", T("s03", "Cevap"), "cevap"), ("s03", T("s03", "On"), "neutral"),
            ("s03", T("s03", "Diğer"), "dikkat"), ("s04", 0.0, "tuzak"), ("s04", T("s04", "dikkat"), "dikkat"), ("s05", 0.0, "soru"),
            ("s06", T("s06", "Cevap"), "cevap"), ("s06", T("s06", "Diğerleri"), "neutral"), ("s07", 0.0, "tuzak"),
            ("s07", T("s07", "dikkat"), "dikkat"), ("s08", 0.0, "soru"), ("s09", T("s09", "Cevap"), "cevap"),
            ("s09", T("s09", "Eşya"), "dikkat"), ("s09", T("s09", "Diğer", 2), "neutral"), ("s10", 0.0, "tuzak"),
            ("s10", T("s10", "dikkat"), "uyari"), ("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Yem bitkileri, ev aletleri ve eritilmiş kuvars",
    message="Fiğ kaba yemdir → 12.14 (D) · mikrodalga fırın 85.16, diğer ev aletleri Fasıl 84 (B) · eritilmiş kuvars her yerde camdır → Fasıl 70 (E).",
    intent="Ölçülen bilgi alanları: Fasıl 10 hububatı ile Fasıl 12 kaba yem ürünlerinin ayrımı, ev tipi cihazlarda Fasıl 84 (makineler) ile 85.16 (elektrotermik cihazlar) ayrımı ve Fasıl 70 Not 5 (eritilmiş kuvars ve eritilmiş silis tarifenin her yerinde cam sayılır).",
    team="Cano (kuş yemi de tohumdur diye kanarya otunu Fasıl 12’ye koyar → HAYIR, 10.08) · Stajyer (saç kurutma 85.16 diye çamaşır kurutma makinesini de oraya koyar → HAYIR, 84.51) ve Gümrükçü Baba (“ne kuruttuğuna bak”) · Yardımcı (kuvars mineraldir diye Fasıl 25 → HAYIR, eritilmiş kuvars camdır).",
    visuals="ürün kartı + 3 adımlı gerekçe + 5 aday pozisyon şeridi (doğru olan yeşil), yanlış şıkkın üstü çizilip DOĞRUSU kartı + diğer dört cihazın pozisyonları, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: 12.14 pozisyon metni (İsveç şalgamı, hayvan pancarı, kaba yem kökleri, kuru ot, yonca, korunga, üçgül, karalahana, acı bakla, fiğ ve benzeri kaba yem ürünleri), Fasıl 12 Not 3 (fiğ tohumları — Vicia faba hariç — ekime mahsus tohum sayılır, 12.09), 10.04 yulaf, 10.07 tane sorgum, 10.08 karabuğday ve kanarya otu tohumu; 84.15 klima, 84.18 buzdolabı, 84.22 bulaşık makinesi, 84.51 çamaşır kurutma makinesi, 85.16 mikrodalga fırınlar ve saç kurutma makineleri, 73.21 demir-çelikten elektriksiz ev tipi pişirme cihazları; Fasıl 70 Not 5 (eritilmiş kuvars ve diğer eritilmiş silis tarifenin her yerinde cam sayılır), 70.02 (işlenmemiş cam boru), 70.17 (laboratuvar cam eşyası), 25.06 doğal kuvars, 28.11 silisyum dioksit, 69.09 seramik laboratuvar eşyası, 71.03 yarı kıymetli taşlar.",
    yt_title="Fiğ Fasıl 12 mi? Mikrodalga Fırın 84 mü 85 mi? Eritilmiş Kuvars Cam mı? | Tarife Dersi #7 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin yedincisinde yine 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, Fasıl 12, 12.14, fiğ, kaba yem, hububat, Fasıl 10, 85.16, mikrodalga fırın, 84.51, ev aletleri, Fasıl 70, eritilmiş kuvars, 70.17, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Aşağıdakilerden hangisi tarife cetvelinin 12. faslında sınıflandırılır?",
             options=["Kuş yemi olarak kullanılan kanarya otu tohumu", "Karabuğday", "Yulaf",
                      "Hayvan yemi olarak kullanılan kurutulmuş fiğ otu", "Tane sorgum"],
             answer="D", why="Fiğ bir yem bitkisidir; 12.14 pozisyon metni yonca, korunga, fiğ ve benzeri kaba yem ürünlerini adıyla sayar. Diğer dördü hububattır ve Fasıl 10’da kalır: kanarya otu tohumu ve karabuğday 10.08, yulaf 10.04, tane sorgum 10.07. Fiğ tohumu da Fasıl 12 Not 3 gereği 12.09’dadır.",
             ref="12.14 pozisyon metni · Fasıl 12 Not 3", yt="Kuş yemi, karabuğday, fiğ: hangisi Fasıl 12’de? Hububat ile kaba yem ayrımı."),
        dict(stem="Aşağıdaki ev aletlerinden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
             options=["Ev tipi bulaşık yıkama makinesi", "Ev tipi mikrodalga fırın", "Ev tipi çamaşır kurutma makinesi",
                      "Duvar tipi split klima", "Ev tipi buzdolabı"], answer="B",
             why="Mikrodalga fırın elektrotermik ev cihazıdır ve 85.16’da adıyla sayılır. Klima 84.15, buzdolabı 84.18, bulaşık makinesi 84.22, çamaşır kurutma makinesi 84.51 ile Fasıl 84’tedir.",
             ref="85.16 ve Fasıl 84 pozisyon metinleri", yt="Mikrodalga, kurutma makinesi, klima: hangisi Fasıl 85’te? Saç kurutma ile çamaşır kurutma tuzağı."),
        dict(stem="Laboratuvarda kullanılmak üzere, eritilmiş kuvarstan yapılmış deney tüpü tarife cetvelinin hangi faslında sınıflandırılır?",
             options=["25", "28", "69", "71", "70"], answer="E",
             why="Fasıl 70 Not 5’e göre eritilmiş kuvars ve diğer eritilmiş silis tarifenin her yerinde cam sayılır; laboratuvar cam eşyası 70.17’dedir. İşlenmemiş eritilmiş kuvars boru da 70.02 ile Fasıl 70’tedir.",
             ref="Fasıl 70 Not 5 · 70.17", yt="Kuvars mineral mi, cam mı? Eritilmiş kuvarstan laboratuvar eşyası."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #7; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — 12. fasılda sınıflandırılan; 'sınıflandırılır' altı çizili; 5 ürün şıkkı; 3 sn geri sayım.",
        s03="CEVAP D; fiğ ürün kartı → yem bitkisi, pozisyon metni, kurutulmuş da olsa → 12.14; aday şeridi 10.08 · 10.08 · 10.04 · 12.14 ✓ · 10.07.",
        s04="TUZAK — Cano 'kuş yemi de tohum' diye A → HAYIR; Fasıl 12 ≠ 10.08 kartları; DİKKAT: fiğ tohumu 12.09.",
        s05="SORU 2/3 — farklı fasıldaki ev aleti; 'farklı bir fasılda' altı çizili; 5 cihaz şıkkı; 3 sn geri sayım.",
        s06="CEVAP B; mikrodalga → Fasıl 84 üstü çizilir, DOĞRUSU 85.16; diğer dört cihaz Fasıl 84 pozisyonlarıyla ✓.",
        s07="TUZAK — Stajyer çamaşır kurutmayı 85.16 sanar → HAYIR, 84.51; DİKKAT: gazlı ev tipi fırın 73.21; Gümrükçü Baba 'ne kuruttuğuna bak'.",
        s08="SORU 3/3 — eritilmiş kuvarstan deney tüpü hangi fasılda; 5 fasıl şıkkı; 3 sn geri sayım.",
        s09="CEVAP E; deney tüpü kartı → Fasıl 70 Not 5, laboratuvar eşyası → 70.17; aday şeridi 25 · 28 · 69 · 71 · 70 ✓.",
        s10="TUZAK — Yardımcı 'kuvars mineral' diye Fasıl 25 → HAYIR; Fasıl 25 ≠ Fasıl 70; DİKKAT: işlenmemiş boru 70.02.",
        s11="İPUCU · Koçun notu — zihin haritası: hububat ≠ yem · ev aletleri · eritilmiş kuvars.",
        s12="ÖNEMLİ · Cevap anahtarı D · B · E; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
