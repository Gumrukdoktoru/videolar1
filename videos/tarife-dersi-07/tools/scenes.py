"""Tarife Dersi 7: Fasıl 12 kaba yem (fiğ 12.14), ev aletleri 84 / 85 (mikrodalga 85.16), eritilmiş kuvars = cam (70.17)."""
from kit import S, intro, qscene, sol_classify, sol_statements, trap, coach, answer_key

intro("s01", 7, "Yem bitkileri, ev aletleri, eritilmiş kuvars",
      [("wheat", "Yem bitkileri", "Fasıl 10 mu, 12 mi?", "yem"),
       ("microwave", "Ev aletleri", "84 mü, 85 mi?", "ev"),
       ("flask", "Eritilmiş kuvars", "mineral mi, cam mı?", "eritilmiş")], "yedincisine")

qscene("s02", 1,
       'Aşağıdakilerden hangisi tarife cetvelinin <mark>12. faslında</mark> <span class="neg">sınıflandırılır<i></i></span>?',
       ["Kuş yemi olarak kullanılan kanarya otu tohumu", "Karabuğday", "Yulaf",
        "Hayvan yemi olarak kullanılan kurutulmuş fiğ otu", "Tane sorgum"],
       stem_word="Aşağıdakilerden", topic="Bitkisel ürünler · Fasıl 12", neg="sınıflandırılır")

sol_classify("s03", "D", "<b>12.14</b> · fiğ, yonca ve benzeri kaba yem",
             dict(icon="wheat", name="Kurutulmuş fiğ otu (hayvan yemi)", at="Fiğ",
                  chips=[("hayvan yemi", "hayvan"), ("kurutulmuş ot", "kurutulmuş")]),
             [("seed", "Yem bitkisi", "tane olarak yenmez", "yenmez"),
              ("doc", "Pozisyon metni", "yonca, korunga, fiğ… adıyla", "adıyla"),
              ("check", "Kurutulmuş da olsa", "sonuç değişmez", "değiştirmez")],
             dict(code="12.14", title="Kaba yem ürünleri", at="Diğer"),
             [("10.08", "kanarya otu · kuş yemi", False), ("10.08", "karabuğday", False), ("10.04", "yulaf", False),
              ("12.14", "fiğ · kaba yem", True), ("10.07", "tane sorgum", False)],
             cand_at="hububattır")

trap("s04", "Kuş yemi ≠ Fasıl 12", ("cano", 430),
     "Kuş yemi de tohum… <em>Fasıl 12!</em>",
     dict(code="Fasıl 12", title="Kanarya otu tohumu", sub="tohum diye 12’ye ✗", icon="seed"),
     dict(code="10.08", title="Kanarya otu · hububat", sub="kuş yemi olsa da Fasıl 10 ✓", icon="wheat"),
     "Önce bitkiyi tanı: hububat mı, yem mi?",
     note=("dikkat", "Fiğ tohumu da Fasıl 12’de → <b>12.09</b> · Fasıl 12 Not 3: ekime mahsus tohum"),
     at=dict(tuzak="Tuzak", who="Cano", bub="tohumdur", hayir="Hayır", wrong="şıkkını", right="hububattır", note="dikkat", tag="bitkiyi"))

qscene("s05", 2,
       'Aşağıdaki <mark>ev aletlerinden</mark> hangisi diğerlerinden <span class="neg">farklı bir fasılda<i></i></span> sınıflandırılır?',
       ["Ev tipi bulaşık yıkama makinesi", "Ev tipi mikrodalga fırın", "Ev tipi çamaşır kurutma makinesi",
        "Duvar tipi split klima", "Ev tipi buzdolabı"],
       stem_word="Aşağıdaki", topic="Makineler · Fasıl 84–85", neg="farklı")

sol_statements("s06", "B", "Mikrodalga fırın → <em>85.16</em> · elektrotermik",
               "Mikrodalga fırın → Fasıl 84",
               "Mikrodalga fırın <em>elektrotermik</em> ev cihazıdır → Fasıl 85, 85.16. Diğer dördü makine → Fasıl 84.", "85.16",
               [("A", "Ev tipi bulaşık makinesi", "84.22 ✓"),
                ("C", "Çamaşır kurutma makinesi", "84.51 ✓"),
                ("D", "Split klima", "84.15 ✓"),
                ("E", "Ev tipi buzdolabı", "84.18 ✓")],
               strike="Mikrodalga", fix="elektrotermik", oth=["bulaşık", "kurutma", "Klima", "buzdolabı"])

trap("s07", "Kurutma ≠ 85.16", ("stajyer", 470),
     "Saç kurutma 85.16… <em>çamaşır da!</em>",
     dict(code="85.16", title="Çamaşır kurutma makinesi", sub="saç kurutma gibi sandı ✗", icon="flame"),
     dict(code="84.51", title="Çamaşır kurutma makinesi", sub="mensucat makinesi · Fasıl 84 ✓", icon="gear"),
     "Ne kuruttuğuna bak: saç mı, çamaşır mı?",
     note=("dikkat", "Demir-çelikten gazlı, elektriksiz ev tipi fırın ve ocak → <b>73.21</b>"),
     who2=("baba", 470, "Saç kurutma <i>85.16</i> · çamaşır kurutma <i>84.51</i>"),
     at=dict(tuzak="Tuzak", who="Stajyerimiz", bub="saç", hayir="Hayır", wrong="şıkkını", right="elverişli", note="dikkat",
             who2="Gümrükçü", tag="kuruttuğuna"))

qscene("s08", 3,
       'Laboratuvarda kullanılmak üzere, <mark>eritilmiş kuvarstan</mark> yapılmış deney tüpü tarife cetvelinin hangi faslında sınıflandırılır?',
       ["<b>Fasıl 25</b>", "<b>Fasıl 28</b>", "<b>Fasıl 69</b>", "<b>Fasıl 71</b>", "<b>Fasıl 70</b>"],
       stem_word="Laboratuvarda", topic="Cam ve cam eşya · Fasıl 70", mono=True)

sol_classify("s09", "E", "<b>Fasıl 70</b> · eritilmiş kuvars camdır (70.17)",
             dict(icon="flask", name="Eritilmiş kuvarstan laboratuvar deney tüpü", at="Yetmişinci",
                  chips=[("eritilmiş kuvars", "eritilmiş"), ("laboratuvar eşyası", "laboratuvar")]),
             [("doc", "Fasıl 70 Not 5", "eritilmiş kuvars = cam", "beşinci"),
              ("search", "Eşya ne?", "laboratuvar deney tüpü", "tüpüdür"),
              ("check", "Pozisyon", "laboratuvar cam eşyası", "nedenle")],
             dict(code="70.17", title="Laboratuvar cam eşyası · Fasıl 70", at="pozisyonunda"),
             [("25", "doğal kuvars · 25.06", False), ("28", "silisyum dioksit", False), ("69", "seramik eşya", False),
              ("71", "yarı kıymetli taş", False), ("70", "cam · 70.17", True)],
             cand_at="Diğer")

trap("s10", "Kuvars ≠ Fasıl 25", ("yardimci", 500),
     "Kuvars bir mineral… <em>Fasıl 25!</em>",
     dict(code="Fasıl 25", title="Doğal kuvars", sub="eritilmişi değil ✗", icon="gem"),
     dict(code="Fasıl 70", title="Eritilmiş kuvars = cam", sub="Fasıl 70 Not 5 · her yerde ✓", icon="flask"),
     "Kuvars eritildiyse cam faslına bak!",
     note=("dikkat", "Eritilmiş kuvarstan <em>işlenmemiş</em> boru → <b>70.02</b>"),
     at=dict(tuzak="Tuzak", who="Yardımcımız", bub="mineraldir", hayir="Hayır", wrong="şıkkını", right="camdır", note="dikkat", tag="eritildiyse"))

coach("s11", [("HUBUBAT ≠ YEM", ["hububat → Fasıl 10", "fiğ, yonca → 12.14"], "wheat"),
              ("EV ALETLERİ", ["mikrodalga → 85.16", "çamaşır kurutma → 84.51"], "microwave"),
              ("ERİTİLMİŞ KUVARS", ["her yerde cam", "lab. eşyası → 70.17"], "flask")],
      at_motto="kuralı", br=["Bir", "İki", ("Üç", 2)])

answer_key("s12", [("D", "Kurutulmuş fiğ otu", "12.14 · kaba yem"), ("B", "Mikrodalga fırın", "85.16 · elektrotermik"),
                   ("E", "Kuvars deney tüpü", "Fasıl 70 · 70.17")], 8)
