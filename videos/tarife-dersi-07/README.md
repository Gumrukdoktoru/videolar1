# Tarife Dersi 7 — Yem bitkileri, ev aletleri ve eritilmiş kuvars (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Aşağıdakilerden hangisi tarife cetvelinin 12. faslında sınıflandırılır?
A) Kuş yemi olarak kullanılan kanarya otu tohumu · B) Karabuğday · C) Yulaf · **D) Hayvan yemi olarak kullanılan kurutulmuş fiğ otu** · E) Tane sorgum
**Doğru cevap: D.** Fiğ bir yem bitkisidir; 12.14 pozisyon metni yonca, korunga, fiğ ve benzeri kaba yem ürünlerini adıyla sayar. Diğer dördü hububattır ve Fasıl 10’da kalır: kanarya otu tohumu ve karabuğday 10.08, yulaf 10.04, tane sorgum 10.07. Fiğ tohumu da Fasıl 12 Not 3 gereği 12.09’dadır. (12.14 pozisyon metni · Fasıl 12 Not 3)

**Soru 2.** Aşağıdaki ev aletlerinden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?
A) Ev tipi bulaşık yıkama makinesi · **B) Ev tipi mikrodalga fırın** · C) Ev tipi çamaşır kurutma makinesi · D) Duvar tipi split klima · E) Ev tipi buzdolabı
**Doğru cevap: B.** Mikrodalga fırın elektrotermik ev cihazıdır ve 85.16’da adıyla sayılır. Klima 84.15, buzdolabı 84.18, bulaşık makinesi 84.22, çamaşır kurutma makinesi 84.51 ile Fasıl 84’tedir. (85.16 ve Fasıl 84 pozisyon metinleri)

**Soru 3.** Laboratuvarda kullanılmak üzere, eritilmiş kuvarstan yapılmış deney tüpü tarife cetvelinin hangi faslında sınıflandırılır?
A) 25 · B) 28 · C) 69 · D) 71 · **E) 70**
**Doğru cevap: E.** Fasıl 70 Not 5’e göre eritilmiş kuvars ve diğer eritilmiş silis tarifenin her yerinde cam sayılır; laboratuvar cam eşyası 70.17’dedir. İşlenmemiş eritilmiş kuvars boru da 70.02 ile Fasıl 70’tedir. (Fasıl 70 Not 5 · 70.17)

Cevap dağılımı: D · B · E.

## Video

- **Süre:** 5 dk 05 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 7 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Cano (kuş yemi de tohumdur diye kanarya otunu Fasıl 12’ye koyar → HAYIR, 10.08) · Stajyer (saç kurutma 85.16 diye çamaşır kurutma makinesini de oraya koyar → HAYIR, 84.51) ve Gümrükçü Baba (“ne kuruttuğuna bak”) · Yardımcı (kuvars mineraldir diye Fasıl 25 → HAYIR, eritilmiş kuvars camdır).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** ürün kartı + 3 adımlı gerekçe + 5 aday pozisyon şeridi (doğru olan yeşil), yanlış şıkkın üstü çizilip DOĞRUSU kartı + diğer dört cihazın pozisyonları, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-07-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-07.mp4
```
