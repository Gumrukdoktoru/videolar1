# Tarife Dersi 10 — Hava yastıklı taşıtlar, kıymetli metalden eşya ve yolcu biniş köprüleri (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Hava yastığı üzerinde hareket eden taşıtların sınıflandırılmasıyla ilgili aşağıdaki ifadelerden hangisi doğrudur?
A) Hava yastıklı taşıtların tamamı, hava taşıtlarıyla birlikte 88. fasılda sınıflandırılır. · **B) Kılavuz bir hat üzerinde gitmek üzere tasarlanmış hava trenleri 86. fasılda sınıflandırılır.** · C) Hem karada hem suda gidebilen hava yastıklı taşıtlar 89. fasılda sınıflandırılır. · D) Yalnız su üzerinde giden, kıyıya çıkabilen hava yastıklı taşıtlar 87. fasılda sınıflandırılır. · E) Hava yastıklı taşıtlar, benzedikleri taşıta bakılmaksızın 84. fasılda makine olarak sınıflandırılır.
**Doğru cevap: B.** Bölüm XVII Not 5’e göre hava yastıklı taşıtlar en çok benzedikleri taşıtlarla sınıflandırılır: kılavuz hat üzerinde gidenler (hava trenleri) Fasıl 86, karada veya hem karada hem suda gidenler Fasıl 87, su üzerinde gidenler kıyıya çıkabilse de Fasıl 89. Hiçbiri Fasıl 84’te makine sayılmaz. (Bölüm XVII Not 5)

**Soru 2.** Gümüşten yapılmış, cepte taşınan türden sigara tabakası hangi tarife pozisyonunda sınıflandırılır?
**A) 71.13** · B) 71.14 · C) 71.17 · D) 42.02 · E) 96.14
**Doğru cevap: A.** Fasıl 71 Not 9’a göre mücevherci eşyası; küçük süs eşyası ile cepte, el çantasında veya üstte taşınan kişisel eşyayı (sigara tabakası, pudralık, tespih) kapsar. Gümüşten olduğu için 71.13’tedir. Masada duran gümüş sigara kutusu ve kül tablası kuyumcu eşyası olarak 71.14’tedir; adi metalden sigara tabakası taklit mücevher sayılmaz. (Fasıl 71 Not 9, 10 ve 11)

**Soru 3.** Bir yolcu limanında, kruvaziyer gemilere biniş için kullanılan, teleskopik hareketli bir tünelden oluşan yolcu biniş köprüsü hangi tarife pozisyonunda sınıflandırılır?
A) 84.26 · B) 73.08 · C) 84.28 · **D) 84.79** · E) 89.07
**Doğru cevap: D.** Yolcu biniş köprüsü kendine özgü işlevi olan, başka pozisyonda belirtilmeyen bir makinedir: 84.79. Armonize Sistem havalimanında kullanılanlar için 8479.71, diğerleri için 8479.79 alt pozisyonlarını açar. 73.08 sabit çelik köprüler gibi inşaat aksamı içindir; yürüyen merdiven ve yürüyen yollar 84.28’dedir. (84.79 · 8479.71 / 8479.79)

Cevap dağılımı: B · A · D.

## Video

- **Süre:** 5 dk 49 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 10 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Cano (kıyıya çıkabiliyor diye su üstü hava yastıklı tekneyi Fasıl 87 sanır → HAYIR, Fasıl 89) · Stajyer (sigara gereci kuyumcu eşyası diye 71.14 → HAYIR, 71.13) ve Gümrükçü Baba (“cepte mi, masada mı?”) · Yardımcı (adı köprü diye 73.08 → HAYIR, 84.79) ve Gümrükçü Baba (“adına değil, işlevine bak”).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** doğru ifade kartı + dört yanlış ifadenin ✗ ve düzeltmeleri, ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (doğru olan yeşil), tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-10-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-10.mp4
```
