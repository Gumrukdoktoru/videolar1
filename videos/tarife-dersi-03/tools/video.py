"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 3
META = "DERS · <b>TARİFE #3</b> · YATAK TAKIMI, DENİZ MEMELİLERİ, PATENLER"
TITLE = "Tarife Dersi 3 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · YATAK TAKIMI", ["s02", "s03", "s04"]), ("SORU 2 · DENİZ MEMELİSİ", ["s05", "s06", "s07"]),
    ("SORU 3 · PATENLİ BOT", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Kaz tüyü dolgulu yorgan hangi pozisyonda?", "Soru 2: Dondurulmuş fok eti hangi pozisyonda?",
      "Soru 3: Buz pateni takılı bot hangi pozisyonda?", "Koçun notu", "Cevap anahtarı"]
KW = [r"yatak takımı eşyası", r"doldurulmuş", r"dolgulu", r"uyku tulumlarını", r"Uyku tulumları", r"kaplanmış olsun olmasın", r"battaniyeleri",
      r"memeli", r"memelidir", r"Deniz memelilerinin", r"deniz memelisi", r"balık değil", r"balık değildir", r"yağları",
      r"paten takılmış botları", r"paten takılmış botlar", r"hariç tutar", r"Fasıl notu", r"Fasıl notları", r"spor eşyası", r"Oyuncak",
      r"A şıkkı", r"B şıkkı", r"C şıkkı", r"D şıkkı", r"E şıkkı", r"Dikkat:", r"Hayır!"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s03", T("s03", "Cevap"), "cevap"), ("s03", T("s03", "Bu"), "neutral"),
            ("s03", T("s03", "Belirleyici"), "dikkat"), ("s04", 0.0, "tuzak"), ("s04", T("s04", "Dikkat"), "dikkat"), ("s05", 0.0, "soru"),
            ("s06", T("s06", "Cevap"), "cevap"), ("s06", T("s06", "Fok"), "neutral"), ("s07", 0.0, "tuzak"), ("s07", T("s07", "dikkat"), "dikkat"),
            ("s08", 0.0, "soru"), ("s09", T("s09", "Cevap"), "cevap"), ("s09", T("s09", "Ama"), "uyari"), ("s09", T("s09", "Doksan"), "neutral"),
            ("s10", 0.0, "tuzak"), ("s11", 0.0, "neutral"), ("s11", T("s11", "Üç"), "dikkat"), ("s12", 0.0, "cevap")]

DOC = dict(
    title="Yatak takımı, deniz memelileri, patenler",
    message="Dolgulu yorgan 94.04 (C) · fok eti 02.08 (A) · paten takılmış bot 95.06 (E).",
    intent="Ölçülen bilgi alanları: dolgulu yatak takımı eşyası (94.04), deniz memelilerinin eti (02.08) ve paten takılmış botlar (Fasıl 64 notu → 95.06).",
    team="Yardımcı (pamuklu yüz → 63.01 battaniye → HAYIR) · Cano (denizden çıkıyor → balık → HAYIR) · Stajyer (üstü deri → 64.03 → HAYIR) ve Gümrükçü Baba (“bıçak takılıysa 95.06; patensiz bot Fasıl 64”).",
    visuals="sınıflandırma yolu (ürün kartı → 3 adım → pozisyon) ve beş aday pozisyonun ✓/✗ şeridi, tuzak karşılaştırma kartları (≠), DİKKAT kartları (9404.30 uyku tulumları, 15.04 deniz memelisi yağları, 95.03 oyuncak ayakkabılar), koçun notu zihin haritası, cevap anahtarı",
    sources="94.04 pozisyon metni ve izahnamesi (yorganlar, yastıklar, 9404.30 uyku tulumları; kaplanmış olsun olmasın), 63.01 battaniyeler, 02.08 ve 0208.40 alt pozisyonu (balina, yunus, fok, deniz aslanı, deniz aygırı), 15.04 (balık ve deniz memelisi yağları), Fasıl 64 Not 1 (paten takılmış botlar hariç → Fasıl 95), 9506.70 (buz ve tekerlekli patenler, paten takılmış botlar dahil), Fasıl 64 genel açıklaması (patensiz paten ayakkabıları Fasıl 64).",
    yt_title="Dolgulu Yorgan (94.04), Fok Eti (02.08), Patenli Bot (95.06) | Tarife Dersi #3 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin üçüncüsünde yine 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, 94.04, yatak takımı, 02.08, deniz memelileri, 95.06, paten, Fasıl 64 notu, GTİP, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Dış yüzü pamuklu dokunmuş mensucattan, içi kaz tüyüyle doldurulmuş yorgan hangi tarife pozisyonunda sınıflandırılır?",
             options=["63.01", "63.02", "94.04", "52.08", "05.05"], answer="C",
             why="94.04 içi herhangi bir maddeyle doldurulmuş yatak takımı eşyasını (şilte, yorgan, yastık, uyku tulumu) kaplanmış olsun olmasın kapsar; dış yüzün pamuklu olması sonucu değiştirmez. Battaniyeler (63.01) dolgusuzdur.",
             ref="94.04 pozisyon metni", yt="Kaz tüyü dolgulu, dış yüzü pamuklu yorgan: 63.01 mi 94.04 mü? Uyku tulumları da aynı pozisyonda."),
        dict(stem="Dondurulmuş fok eti hangi tarife pozisyonunda sınıflandırılır?",
             options=["02.08", "03.03", "02.06", "16.02", "03.04"], answer="A",
             why="Fok deniz memelisidir, balık değildir. Fasıl 3 yalnız balık, kabuklu hayvan ve yumuşakçaları kapsar; deniz memelilerinin eti 02.08'de (0208.40: balina, yunus, fok, deniz aslanı, deniz aygırı). Yağları ise 15.04.",
             ref="0208.40 alt pozisyonu", yt="Dondurulmuş fok eti: balık mı, et mi? Deniz memelileri 02.08'de; yağları 15.04'te."),
        dict(stem="Altına buz pateni bıçağı sökülemeyecek şekilde tutturulmuş, üst kısmı deri, dış tabanı kauçuk bot hangi tarife pozisyonunda sınıflandırılır?",
             options=["64.03", "64.02", "95.03", "64.06", "95.06"], answer="E",
             why="Fasıl 64 Not 1 paten takılmış botları hariç tutar ve Fasıl 95'e gönderir; 9506.70 buz ve tekerlekli patenleri, paten takılmış botlar dahil kapsar. Patensiz paten botu Fasıl 64'te kalır; oyuncak karakterli ayakkabılar 95.03.",
             ref="Fasıl 64 Not 1, 9506.70", yt="Buz pateni bıçağı takılı deri bot: 64.03 mü 95.06 mı? Fasıl notu ayakkabı pozisyonlarının kapsamını sınırlar."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #3; 3 konu kartı; ekip tanıtımı.",
        s02="SORU 1/3 — kaz tüyü dolgulu yorgan; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s03="CEVAP C; ürün kartı → pozisyon metni / kaplama önemsiz / belirleyici → 94.04; 5 aday ✓/✗.",
        s04="TUZAK — Yardımcı 63.01 battaniye der → HAYIR; 63.01 ≠ 94.04; DİKKAT: uyku tulumları 9404.30.",
        s05="SORU 2/3 — dondurulmuş fok eti; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP A; Fasıl 3 değil → deniz memelisi → 0208.40 → 02.08; 5 aday ✓/✗.",
        s07="TUZAK — Cano 'denizden çıkıyor, balık' der → HAYIR; 03.03 ≠ 02.08; DİKKAT: yağları 15.04.",
        s08="SORU 3/3 — buz pateni bıçağı takılı deri bot; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s09="CEVAP E; ilk bakış 64.03 → Fasıl 64 Not 1 hariç → 9506.70 dahil → 95.06; 5 aday ✓/✗.",
        s10="TUZAK — Stajyer 64.03 der → Gümrükçü Baba 'bıçak takılıysa 95.06'; DİKKAT: oyuncak ayakkabılar 95.03.",
        s11="İPUCU · Koçun notu — zihin haritası: dolgu → 94.04 · türe bak · not belirler.",
        s12="ÖNEMLİ · Cevap anahtarı C · A · E; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
