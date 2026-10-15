"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 13
META = "DERS · <b>TARİFE #13</b> · 3 SORU · FASIL 90 · 92"
TITLE = "Tarife Dersi 13 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · PERİSKOP", ["s02", "s03", "s04"]), ("SORU 2 · TANSİYON ALETİ", ["s05", "s06", "s07"]),
    ("SORU 3 · TÜRK ÇALGILARI", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Denizaltı periskobu 90.05 mi, 90.13 mü?", "Soru 2: Tansiyon aleti 90.18 mi, 90.26 mı?",
      "Soru 3: Bağlama, ud, kanun, kemençe, darbuka — hangisi farklı?", "Koçun notu", "Cevap anahtarı"]
KW = ["optik alettir", "dördüncü notu", "Fasıl notu açık", "adıyla", "fasıl notunu",
      "teşhis için", "sfigmomanometreleri", "tansiyometreleri", "manometreler", "tıbbi bir alettir", "Kimin basıncını",
      "telli çalgılardır", "vurmalı bir çalgıdır", "yaylı çalgıları", "Tel mi titriyor",
      "A şıkkı", "B şıkkı", "C şıkkı", "D şıkkı", "E şıkkı", "dikkat:", "Hayır!"]


def cues(T):
    out = [("s01", 0.2, "neutral")]
    for q, s, t in (("s02", "s03", "s04"), ("s05", "s06", "s07"), ("s08", "s09", "s10")):
        out += [(q, 0.0, "soru"), (s, T(s, "Cevap"), "cevap"), (s, T(s, "Cevap") + 3.0, "neutral"), (t, 0.0, "tuzak"), (t, T(t, "dikkat"), "dikkat")]
    return out + [("s11", 0.0, "neutral"), ("s11", T("s11", "Üç", 2), "dikkat"), ("s12", 0.0, "cevap")]


DOC = dict(
    title="Denizaltı periskobu, tansiyon aleti ve Türk müziği çalgıları",
    message="Denizaltı periskobu 90.13, 90.05 değil (C) · dijital tansiyon aleti 90.18, 90.26 değil (B) · darbuka 92.06, bağlama, ud, kanun ve kemençe 92.02 (E).",
    intent="Bu derste 3 soru var. Ölçülen bilgi alanları: Fasıl 90 Not 4'ün denizaltı ve tanklar için periskopik teleskopları 90.05 dışında bırakıp 90.13'e göndermesi (denizaltı 89.06; Fasıl 90 ve Bölüm XVI makinelerine ait teleskoplar 90.13); 90.18 izahnamesinin sfigmomanometreleri ve tansiyometreleri adıyla sayması, 90.26'nın sıvı ve gaz basıncını ölçen manometrelerle sınırlı olması (klinik termometre 90.25, elektronik olması 85.43'e götürmez); 92.02 telli çalgılar (mızraplı, parmakla ya da yayla çalınan) ile 92.06 vurmalı çalgılar (darbukalar ve tefler adıyla), ses kutusu olmayan elektro gitar 92.07.",
    team="Yardımcı (periskop da teleskoptur diye 90.05 → HAYIR, 90.13) · Stajyer (basınç ölçüyor diye 90.26 → HAYIR, 90.18) ve Gümrükçü Baba (“kimin basıncını ölçüyor?”) · Cano (kemençe yayla çalınıyor diye telli saymaz → HAYIR, 92.02).",
    visuals="ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), yanlış ifade + DOĞRUSU kartı + dört doğru şık, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı",
    sources="Gümrük Tarife Cetveli ve İzahnamesi: Fasıl 90 Not 4 (denizaltı ve tanklar için periskopik teleskoplar ile bu fasıl veya Bölüm XVI makinelerine ait teleskoplar 90.05'e girmez, 90.13), 89.06, 90.05, 9013.10 (silahlar için teleskopik dürbünler; periskoplar), 90.15, 93.05; 90.18 izahnamesi (sfigmomanometreler, tansiyometreler, stetoskoplar), 90.25 (klinik termometreler), 90.26 (sıvı ve gazların akış, seviye, basınç ölçümü; manometreler), 90.31, 85.43; 92.02 (keman, gitar, arp gibi telli diğer çalgılar), 92.06 izahnamesi (darbukalar ve tefler), 92.07 (sesi elektrikle üretilen veya yükseltilen çalgılar).",
    yt_title="Periskop 90.05 mi 90.13 mü? · Tansiyon Aleti 90.18 mi 90.26 mı? · Darbuka Hangi Pozisyonda? | Tarife Dersi #13 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin on üçüncüsünde 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, tarife sınıflandırma, periskop, 90.13, 90.05, Fasıl 90 notları, tansiyon aleti, 90.18, 90.26, manometre, 90.25, darbuka, 92.06, bağlama, ud, kanun, kemençe, 92.02, 92.07, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Bir denizaltında kullanılmak üzere, denizaltıdan ayrı olarak ithal edilen periskop hangi tarife pozisyonunda sınıflandırılır?",
             options=["89.06", "90.05", "90.13", "90.15", "93.05"], answer="C",
             why="Periskop optik bir alettir; ilk akla gelen 90.05 (dürbünler, teleskoplar) olsa da Fasıl 90 Not 4, denizaltı ve tanklar için periskopik teleskopları 90.05'in dışında bırakır. 9013.10 silahlar için teleskopik dürbünleri ve periskopları adıyla sayar. Denizaltının kendisi 89.06'dadır; Fasıl 90 veya Bölüm XVI makinelerine ait teleskoplar da 90.13'e gider.",
             ref="Fasıl 90 Not 4 · 90.13", yt="Denizaltı periskobu: teleskop mu, 90.13 mü?"),
        dict(stem="Kola sarılan bir manşonla kan basıncını ölçen dijital tansiyon aleti hangi tarife pozisyonunda sınıflandırılır?",
             options=["85.43", "90.18", "90.25", "90.26", "90.31"], answer="B",
             why="Tansiyon aleti bir basınç ölçer gibi görünse de tıpta teşhis için kullanılır. 90.18 izahnamesi kan basıncını ölçen sfigmomanometreleri ve tansiyometreleri stetoskoplarla birlikte adıyla sayar. 90.26 sıvı ve gazların akış, seviye ve basıncını ölçen cihazlar içindir; klinik termometre 90.25'tedir; elektronik olması 85.43'e götürmez.",
             ref="90.18 izahnamesi · 90.26", yt="Tansiyon aleti: manometre mi, tıp aleti mi?"),
        dict(stem="Aşağıdaki çalgılardan hangisi tarife cetvelinde diğerlerinden farklı bir pozisyonda sınıflandırılır?",
             options=["Bağlama", "Ud", "Kanun", "Kemençe", "Darbuka"], answer="E",
             why="Bağlama, ud, kanun ve kemençe telli çalgılardır; mızrapla, parmakla ya da yayla çalınsalar da 92.02'de gitar, keman ve arp gibi diğer telli çalgılarla yer alırlar. Darbuka gerdirilmiş deriye elle vurularak çalınır; 92.06 izahnamesi darbukaları ve tefleri adıyla sayar. Ses kutusu olmayan, sesi elektrikle yükseltilen elektro gitar 92.07'dedir.",
             ref="92.02 · 92.06 izahnamesi", yt="Bağlama, ud, kanun, kemençe, darbuka: hangisi farklı pozisyonda?"),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #13; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — denizaltı periskobu; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s03="CEVAP C; periskop kartı → akla gelen 90.05, Fasıl 90 Not 4, 9013.10 metni → 90.13; aday şeridi.",
        s04="TUZAK — Yardımcı periskobu teleskop sanır, 90.05 → HAYIR, 90.13; DİKKAT: Fasıl 90 / Bölüm XVI makinelerinin teleskopları 90.13.",
        s05="SORU 2/3 — dijital tansiyon aleti; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP B; tansiyon aleti kartı → basınç ölçer mi, 90.18 notu, 90.26 değil → 90.18; aday şeridi.",
        s07="TUZAK — Stajyer basınç ölçüyor diye 90.26 → HAYIR, 90.18; DİKKAT: klinik termometre 90.25; Gümrükçü Baba 'kimin basıncını ölçüyor?'.",
        s08="SORU 3/3 — 'farklı' altı çizili; bağlama, ud, kanun, kemençe, darbuka; 3 sn geri sayım.",
        s09="CEVAP E; 'darbuka → 92.02' üstü çizili → DOĞRUSU 92.06; dört telli çalgı 92.02.",
        s10="TUZAK — Cano kemençeyi yaylı diye farklı sanır → HAYIR, 92.02; DİKKAT: elektro gitar 92.07.",
        s11="İPUCU · Koçun notu — zihin haritası: fasıl notu · neyi ölçüyor · sesin kaynağı.",
        s12="ÖNEMLİ · Cevap anahtarı C · B · E; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
