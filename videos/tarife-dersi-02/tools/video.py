"""Per-video settings for build.py (chrome texts, chapters, caption keywords, mascot cues, YouTube chapters)."""
NUM = 2
META = "DERS · <b>TARİFE #2</b> · GENEL KURALLAR &amp; İLK SINIFLANDIRMALAR"
TITLE = "Tarife Dersi 2 — Gümrük Koçu"
CHAPTERS = [
    ("GİRİŞ", ["s01"]), ("SORU 1 · GENEL KURALLAR", ["s02", "s03", "s04"]), ("SORU 2 · EV EŞYASI", ["s05", "s06", "s07"]),
    ("SORU 3 · BÜRO MAKİNELERİ", ["s08", "s09", "s10"]), ("KOÇUN NOTU", ["s11"]), ("CEVAP ANAHTARI", ["s12"]),
]
YT = ["Giriş", "Soru 1: Genel yorum kuralları — hangisi yanlış?", "Soru 2: Çelikten çöp kovası hangi pozisyonda?",
      "Soru 3: Posta ücreti damga makinesi hangi pozisyonda?", "Koçun notu", "Cevap anahtarı"]
KW = [r"başlıkları", r"gösterici", r"yasal dayanak", r"pozisyon metinlerine", r"notlarına", r"esas niteliği", r"esas niteliğine",
      r"en çok benzeyen", r"aksesuar", r"paslanmaz çelik", r"çöp kutularını", r"Atık kâğıt sepetleri", r"izahname", r"izahnameye",
      r"adıyla", r"toplama tertibatı", r"toplama tertibatıdır", r"yazar kasalar", r"en özel tanım",
      r"A şıkkı", r"B şıkkı", r"C şıkkı", r"D şıkkı", r"E şıkkı", r"Dikkat!", r"Hayır!", r"yanlıştır"]


def cues(T):
    return [("s01", 0.2, "neutral"), ("s02", 0.0, "soru"), ("s03", T("s03", "Cevap"), "cevap"), ("s03", T("s03", "Diğer"), "neutral"),
            ("s04", 0.0, "tuzak"), ("s04", T("s04", "dördüncü"), "dikkat"), ("s05", 0.0, "soru"), ("s06", T("s06", "Cevap"), "cevap"),
            ("s06", T("s06", "Önce"), "neutral"), ("s07", 0.0, "tuzak"), ("s07", T("s07", "dikkat"), "dikkat"), ("s08", 0.0, "soru"),
            ("s09", T("s09", "Cevap"), "cevap"), ("s09", T("s09", "ortak"), "dikkat"), ("s10", 0.0, "tuzak"), ("s10", T("s10", "sayaçlara"), "uyari"),
            ("s11", 0.0, "neutral"), ("s11", T("s11", "Üç"), "dikkat"), ("s12", 0.0, "cevap")]

DOC = dict(
    title="Genel kurallar ve ilk sınıflandırmalar",
    message="Başlık gösterici (B) · çelik çöp kovası 73.23 (D) · damga basan makine 84.70 (E).",
    intent="Ölçülen bilgi alanları: tarifenin yorumuna ilişkin genel kurallar, demir/çelikten ev eşyası (73.23) ve hesaplama tertibatlı büro makineleri (84.70).",
    team="Stajyer (bağırsağı başlığa bakıp Fasıl 2'ye koyar → HAYIR) · Cano (plastik iç kova → 39.24 → HAYIR) · Yardımcı (damga basıyor → 84.43) ve Gümrükçü Baba (“metin adıyla sayıyorsa en özel tanım odur”).",
    visuals="yanlış ifade üstü çizilip DOĞRUSU kartı + diğer dört ifadenin kural etiketleri (GYK 2(a), 5(a), 4, 6), sınıflandırma yolu (ürün kartı → 3 adım → pozisyon), beş aday pozisyonun ✓/✗ şeridi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı",
    sources="Tarifenin Yorumu ile İlgili Genel Kurallar 2017 (Kural 1 açıklama notu: başlıklar sadece gösterici; Kural 2(a) eksik bisiklet örneği), Fasıl 2 notu (bağırsaklar 05.04), 73.23 izahnamesi (çöp kutuları; atık kâğıt sepetleri hariç → 73.25/73.26), 84.70 pozisyon metni ve izahnamesi (posta pulu yerine damga basan makineler; toplama tertibatı; sayaçlar 90.29), 39.24, 73.10 pozisyon metinleri.",
    yt_title="Genel Yorum Kuralları, Çelik Ev Eşyası (73.23) ve Damga Makinesi (84.70) | Tarife Dersi #2 · 3 Soru | Gümrük Koçu",
    yt_intro="Tarife derslerinin ikincisinde yine 3 soru çözüyoruz. Her soruda 3 saniye düşünme süreniz var; sonra cevabı, gerekçesini ve tuzak şıkları adım adım anlatıyoruz.",
    tags="gümrük tarifesi, genel yorum kuralları, GYK, tarife sınıflandırma, 73.23, 84.70, izahname, GTİP, gümrük müşavirliği sınavı, gümrük müşavir yardımcılığı, tarife soruları, Gümrük Koçu",
    hashtags="#gümrük #tarife #GTİP #GümrükKoçu",
    questions=[
        dict(stem="Tarifenin yorumuna ilişkin genel kurallarla ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
             options=["Eksik veya bitirilmemiş eşya, sunulduğunda tamamlanmış eşyanın esas niteliğine sahipse tamamlanmış eşya gibi sınıflandırılır.",
                      "Bölüm, fasıl ve tali fasıl başlıkları, eşyanın tarifedeki yerinin saptanmasında yasal dayanak oluşturur.",
                      "Belli bir eşyaya göre yapılmış, uzun süreli kullanıma uygun mahfazalar eşyayla birlikte sunulduğunda onunla birlikte sınıflandırılır.",
                      "İlk üç kurala göre sınıflandırılamayan eşya, en çok benzediği eşyanın pozisyonunda sınıflandırılır.",
                      "Alt pozisyonlarda yalnızca aynı seviyedeki alt pozisyonlar karşılaştırılır."],
             answer="B", why="Başlıklar sadece gösterici niteliktedir; sınıflandırma pozisyon metinlerine ve bölüm/fasıl notlarına göre yapılır. A: GYK 2(a), C: GYK 5(a), D: GYK 4, E: GYK 6.",
             ref="GYK 1", yt="Genel yorum kuralları: hangi ifade yanlış? Başlık gösterici, karar metin ve notla; GYK 4'te kıymete değil benzerliğe bakılır."),
        dict(stem="Paslanmaz çelikten mamul, iç kovası plastik olan, pedallı mutfak çöp kovası hangi tarife pozisyonunda sınıflandırılır?",
             options=["39.24", "73.10", "73.26", "73.23", "94.03"], answer="D",
             why="Esas nitelik paslanmaz çelikten; plastik iç kova aksesuar. 73.23 demir/çelikten sofra, mutfak ve ev eşyasını kapsar; izahname çöp kutularını sayar. Atık kâğıt sepetleri ise 73.25/73.26.",
             ref="73.23 izahnamesi", yt="Paslanmaz çelik, iç kovası plastik çöp kovası: 39.24 mü 73.23 mü? Esas nitelik ve izahname listesi."),
        dict(stem="Mektup ve kolilere posta pulu yerine geçen ücret damgasını basan, hesaplama tertibatı bulunan makineler hangi tarife pozisyonunda sınıflandırılır?",
             options=["84.43", "84.71", "84.72", "90.29", "84.70"], answer="E",
             why="84.70 pozisyon metni posta pulu yerine damga basan makineleri adıyla sayar; ortak özellik toplama tertibatıdır (yazar kasalar hariç). Sadece sayan sayaçlar 90.29.",
             ref="84.70 pozisyon metni", yt="Posta ücreti damga makinesi: 84.43 baskı makinesi mi, 84.70 mi? Pozisyon metni adıyla sayıyorsa önce oraya bakın."),
    ],
    scenes=dict(
        s01="Logo sting → TARİFE DERSİ #2; 3 konu kartı; ekip tanıtımı (Stajyer, Yardımcı, Gümrükçü Baba, Cano).",
        s02="SORU 1/3 — genel kurallar, 'yanlıştır' altı çizili + DİKKAT · yanlışı bul!; 5 uzun şık; 3 sn geri sayım.",
        s03="CEVAP B; B ifadesi üstü çizilir, DOĞRUSU kartı (GYK 1); diğer dört ifade kural etiketleriyle ✓ (GYK 2(a), 5(a), 4, 6).",
        s04="TUZAK — Stajyer bağırsağı Fasıl 2'ye koyar → HAYIR; Fasıl 2 ≠ 05.04 kartları; DİKKAT: GYK 4 en çok benzeyen eşya.",
        s05="SORU 2/3 — paslanmaz çelik çöp kovası; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s06="CEVAP D; ürün kartı (çelik gövde, plastik iç kova, pedal) → asıl madde / esas nitelik / kullanım → 73.23; 5 aday ✓/✗.",
        s07="TUZAK — Cano plastik iç kova diye 39.24 → HAYIR; DİKKAT: atık kâğıt sepetleri 73.25 / 73.26.",
        s08="SORU 3/3 — posta pulu yerine damga basan makine; 5 pozisyon şıkkı; 3 sn geri sayım.",
        s09="CEVAP E; pozisyon metni adıyla sayar → GYK 1 yeter → ortak özellik toplama tertibatı → 84.70; 5 aday ✓/✗.",
        s10="TUZAK — Yardımcı 84.43 der → Gümrükçü Baba 'metin adıyla sayıyorsa en özel tanım'; UYARI: sayaçlar 90.29.",
        s11="İPUCU · Koçun notu — zihin haritası: başlık ≠ karar · aksesuar · adıyla sayılan.",
        s12="ÖNEMLİ · Cevap anahtarı B · D · E; skor kutucukları; yorum/abone/paylaş; sıradaki ders; ekip.",
    ),
)
