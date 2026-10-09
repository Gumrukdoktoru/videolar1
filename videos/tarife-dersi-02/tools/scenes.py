"""Tarife Dersi 2: genel yorum kuralları, demir/çelikten ev eşyası (73.23), damga basan makineler (84.70)."""
from kit import S, intro, qscene, sol_statements, sol_classify, trap, coach, answer_key

intro("s01", 2, "Genel kurallar ve ilk sınıflandırmalar",
      [("layers", "Genel yorum kuralları", "başlık mı, not mu?", "genel"),
       ("bin", "Demir/çelikten ev eşyası", "Fasıl 73", "demir"),
       ("calc", "Büro makineleri", "Fasıl 84", "büro")], "ikincisine")

qscene("s02", 1,
       'Tarifenin yorumuna ilişkin <mark>genel kurallarla</mark> ilgili aşağıdaki ifadelerden hangisi <span class="neg">yanlıştır<i></i></span>?',
       ["Eksik veya bitirilmemiş eşya, sunulduğunda tamamlanmış eşyanın esas niteliğine sahipse tamamlanmış eşya gibi sınıflandırılır.",
        "Bölüm, fasıl ve tali fasıl başlıkları, eşyanın tarifedeki yerinin saptanmasında yasal dayanak oluşturur.",
        "Belli bir eşyaya göre yapılmış, uzun süreli kullanıma uygun mahfazalar eşyayla birlikte sunulduğunda onunla birlikte sınıflandırılır.",
        "İlk üç kurala göre sınıflandırılamayan eşya, en çok benzediği eşyanın pozisyonunda sınıflandırılır.",
        "Alt pozisyonlarda yalnızca aynı seviyedeki alt pozisyonlar karşılaştırılır."],
       stem_word="Tarifenin", topic="Genel yorum kuralları", neg="yanlıştır", small=True)

sol_statements("s03", "B", "Başlıklar sadece <em>gösterici</em> · yasal dayanak değil",
               "Başlıklar, eşyanın yerinin saptanmasında yasal dayanak oluşturur.",
               "Sınıflandırma <em>pozisyon metinlerine</em> ve <em>bölüm / fasıl notlarına</em> göre yapılır; başlıklar sadece yol gösterir.", "GYK 1",
               [("A", "Eksik / bitirilmemiş eşya, esas niteliği taşıyorsa tamamlanmış eşya gibi", "GYK 2(a)"),
                ("C", "Eşyaya özel, uzun süre kullanılan mahfaza eşyayla birlikte sınıflandırılır", "GYK 5(a)"),
                ("D", "Kurallarla yerleştirilemeyen eşya en çok benzediği eşyanın yerine", "GYK 4"),
                ("E", "Alt pozisyonda yalnızca aynı seviyedekiler karşılaştırılır", "GYK 6")],
               strike="başlıkları", fix="Sınıflandırma", oth=["A", "C", "D", "E"])

trap("s04", "Başlık yol gösterir, not karar verir", ("stajyer", 470),
     "Başlık “etler ve sakatat” diyor… bağırsak <em>Fasıl 2!</em>",
     dict(code="Fasıl 2", title="Etler ve yenilen sakatat", sub="başlığa bakıp karar vermek ✗", icon="doc"),
     dict(code="05.04", title="Hayvan bağırsakları", sub="Fasıl 2 notu bağırsağı hariç tutar ✓", icon="shield"),
     "Başlık yol gösterir, karar notla verilir!",
     note=("dikkat", "<em>GYK 4:</em> kıymete ya da ticari miktara değil, <em>en çok benzeyen</em> eşyaya bakılır."),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="bağırsağını", hayir="Hayır", wrong="başlığı", right="sıfır", note="dördüncü", tag="Başlık"))

qscene("s05", 2,
       '<mark>Paslanmaz çelikten</mark> mamul, iç kovası plastik olan, pedallı mutfak çöp kovası hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>39.24</b>", "<b>73.10</b>", "<b>73.26</b>", "<b>73.23</b>", "<b>94.03</b>"],
       stem_word="Paslanmaz", topic="Demir / çelikten eşya", mono=True)

sol_classify("s06", "D", "<b>73.23</b> · demir/çelikten ev eşyası",
             dict(icon="bin", name="Paslanmaz çelik, pedallı mutfak çöp kovası", at="Önce",
                  chips=[("paslanmaz çelik gövde", "çelik"), ("plastik iç kova", "Plastik"), ("pedal mekanizması", "Pedal")]),
             [("box", "Asıl madde", "paslanmaz çelik → Fasıl 73", "maddesine"),
              ("star", "Esas nitelik", "plastik iç kova yalnız aksesuar", "aksesuar"),
              ("building", "Kullanım yeri", "ev ve mutfak işleri", "kullanım")],
             dict(code="73.23", title="Demir/çelikten sofra, mutfak ve ev eşyası", at="Yetmiş"),
             [("39.24", "plastikten ev eşyası", False), ("73.10", "depo, varil, kutu", False), ("73.26", "diğer demir/çelik eşya", False),
              ("73.23", "ev eşyası · çöp kutuları", True), ("94.03", "mobilyalar", False)],
             cand_at="izahname")

trap("s07", "Plastik iç kova ≠ plastik eşya", ("cano", 430),
     "İç kova plastik… o zaman <em>39.24!</em>",
     dict(code="39.24", title="Plastikten ev eşyası", sub="aksesuara bakıp karar ✗", icon="box"),
     dict(code="73.23", title="Çelikten ev eşyası", sub="esas nitelik çelikten ✓", icon="shield"),
     "Liste tahmin edilmez, izahnameye bakılır!",
     note=("dikkat", "<em>Atık kâğıt sepetleri</em> 73.23’e girmez → <b>73.25 / 73.26</b>"),
     at=dict(tuzak=0.3, who="Cano", bub="plastik", hayir="Hayır", wrong="pozisyon", right="esas", note="Atık", tag=("ev", 2)))

qscene("s08", 3,
       'Mektup ve kolilere <mark>posta pulu yerine geçen</mark> ücret damgasını basan, hesaplama tertibatı bulunan makineler hangi tarife pozisyonunda sınıflandırılır?',
       ["<b>84.43</b>", "<b>84.71</b>", "<b>84.72</b>", "<b>90.29</b>", "<b>84.70</b>"],
       stem_word="Mektup", topic="Makineler · Fasıl 84", mono=True)

sol_classify("s09", "E", "<b>84.70</b> · pozisyon metni adıyla sayıyor",
             dict(icon="stamp", name="Posta ücreti damga makinesi (hesaplama tertibatlı)", at="Seksen",
                  chips=[("damga basar", "damga"), ("bilet makineleri", "bilet"), ("yazar kasalar", "yazar")]),
             [("doc", "Pozisyon metni", "eşyayı adıyla sayıyor", "adıyla"),
              ("check", "GYK 1 yeterli", "metin açıkça kapsıyor", "birinci"),
              ("calc", "Ortak özellik", "toplama tertibatı (en az 2 rakam)", "toplama")],
             dict(code="84.70", title="Hesap mak., damga basan mak., yazar kasalar", at="kural"),
             [("84.43", "baskı makineleri", False), ("84.71", "otomatik bilgi işlem", False), ("84.72", "diğer büro makineleri", False),
              ("90.29", "sayaçlar", False), ("84.70", "damga basan makineler", True)],
             cand_at=("yazar", 2))

trap("s10", "Damga basmak ≠ baskı makinesi", ("yardimci", 500),
     "Damga basıyor… o zaman <em>84.43!</em>",
     dict(code="84.43", title="Baskı makineleri", sub="işe benzerlikten karar ✗", icon="doc"),
     dict(code="84.70", title="Damga basan makineler", sub="pozisyon metninde adıyla ✓", icon="stamp"),
     "Önce pozisyon metnini oku!",
     note=("uyari", "Sadece sayan düzenek <em>toplama tertibatı değildir</em> → sayaçlar <b>90.29</b>"),
     who2=("baba", 470, "Metin adıyla sayıyorsa <i>en özel tanım</i> odur!"),
     at=dict(tuzak=0.3, who="Yardımcımız", bub="damga", hayir="seçti", wrong="baskı", right="adıyla", note="sayaçlara", who2="Gümrükçü", tag="yer"))

coach("s11", [("BAŞLIK ≠ KARAR", ["Başlık yol gösterir", "Karar: metin + notlar"], "doc"),
              ("AKSESUAR", ["Başka maddeden aksesuar", "esas niteliği değiştirmez"], "box"),
              ("ADIYLA SAYILAN", ["Metin adıyla sayıyorsa", "önce oraya bak"], "search")],
      at_motto="kuralı", br=["Bir", "İki", "Üç"])

answer_key("s12", [("B", "Genel kurallar", "başlıklar sadece gösterici"), ("D", "Çelik çöp kovası", "73.23 · ev eşyası"),
                   ("E", "Damga basan makine", "84.70 · adıyla sayılır")], 3)
