# Tarife Dersi 16 — Satış otomatları, araba krikosu ve aspirin (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Aşağıdakilerden hangisi 84.76 pozisyonunda sınıflandırılmaz?
A) Bozuk para veya kartla çalışan, soğutma tertibatlı kutu içecek satış otomatı · B) Para bozma makinesi · C) Jetonla çalışan tren bileti satış makinesi · D) Jetonla çalışan, kahve ve süt karıştırıcısı olan sıcak içecek otomatı · **E) Ödeme tertibatı olmayan, ofislerde kullanılan sıcak içecek verme makinesi**
**Doğru cevap: E.** 84.76 otomatik satış makinelerinin pozisyonudur; posta pulu, tren bileti, yiyecek ve içecek otomatları ve izahnameye göre para bozma makineleri de buradadır. Isıtma, soğutma ya da kahve-süt karıştırma tertibatı sonucu değiştirmez (8476.21). Ödemeyi kabul edecek tertibatı olmayan sıcak veya soğuk içecek verme makineleri ise izahnamede pozisyon dışında bırakılır: 84.19. (84.76 izahnamesi · 84.19)

**Soru 2.** Otomobilin lastiğini değiştirmek için kullanılan, elle çalıştırılan portatif hidrolik kriko hangi tarife pozisyonunda sınıflandırılır?
A) 82.05 · **B) 84.25** · C) 84.28 · D) 84.79 · E) 87.08
**Doğru cevap: B.** 84.25 krikoları adıyla sayar; izahnamesi otomobiller için portatif krikoları da bu pozisyona koyar. Bölüm XVII Not 2(e), 84.01–84.79 pozisyonlarına giren makineleri taşıt aksam ve parçası saymadığından 87.08'e girmez. 82.05 tarifenin başka yerinde yer almayan el aletleri içindir. (84.25 · Bölüm XVII Not 2(e))

**Soru 3.** Aşağıdakilerden hangisi tarife cetvelinde diğerlerinden farklı bir fasılda sınıflandırılır?
**A) Hiçbir maddeyle karıştırılmamış, dökme hâldeki saf o-asetilsalisilik asit** · B) Bir dolgu maddesiyle karıştırılmış, dozlandırılmamış, dökme aspirin · C) Dozlandırılmış, perakende satışa hazır aspirin tabletleri · D) Tabii maden sularının buharlaştırılmasıyla elde edilen tıbbi tuzlar · E) Dökme hâlde, tıbbi amaçla karıştırılmış şifalı bitkiler
**Doğru cevap: A.** Saf o-asetilsalisilik asit kimyaca belirli, izole bir organik bileşiktir; Fasıl 29 Not 1 ile Fasıl 29'da, 2918.22'de yer alır. Dolgu maddeli dökme aspirin, tıbbi bitki karışımları ve maden sularından elde edilen tıbbi tuzlar 30.03'te (izahnamede adıyla), dozlandırılmış aspirin tabletleri 30.04'tedir. (Fasıl 29 Not 1 · 2918.22 · 30.03 izahnamesi)

Cevap dağılımı: E · B · A.

## Video

- **Süre:** 5 dk 59 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 16 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Stajyer (soğutucusu var diye otomatı 84.18 sanır → HAYIR, 84.76) ve Gümrükçü Baba (“para alıyor mu?”) · Cano (kriko arabayla kullanılır diye 87.08 → HAYIR, 84.25) · Yardımcı (bitki karışımını ilaç saymaz → HAYIR, 30.03) ve Gümrükçü Baba (“saf mı, karışım mı, doz mu?”).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** yanlış ifade + DOĞRUSU kartı + dört doğru şık (iki soruda), ürün kartı + 3 adımlı gerekçe + 5 aday şeridi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-16-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-16.mp4
```
