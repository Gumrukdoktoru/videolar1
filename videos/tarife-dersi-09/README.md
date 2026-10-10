# Tarife Dersi 9 — Özel amaçlı taşıtlar, silahlı bastonlar ve kauçuk contalar (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Aşağıdaki taşıt çiftlerinden hangisinde iki taşıt farklı tarife pozisyonlarında sınıflandırılır?
**A) Ambulans – İtfaiye aracı** · B) Cenaze arabası – Taksi · C) Golf arabası – Motorlu karavan · D) Beton mikser kamyonu – Vinçli kurtarıcı · E) Hapishane minibüsü – Binek otomobili
**Doğru cevap: A.** Ambulans insan taşımaya mahsus taşıt olarak 87.03’tedir; itfaiye aracı ise yangın söndürme hizmeti için donatılmış özel amaçlı taşıt olarak 87.05’tedir. Cenaze arabası, taksi, golf arabası, motorlu karavan, hapishane minibüsü ve binek otomobili 87.03’te; beton mikser ve vinçli kurtarıcı 87.05’tedir. (87.03 ve 87.05 açıklama notları)

**Soru 2.** İçine kurşun doldurularak ağırlaştırılmış, savunma amacıyla da kullanılabilen yürüyüş bastonu tarife cetvelinin hangi faslında sınıflandırılır?
A) 66 · B) 95 · C) 90 · **D) 93** · E) 44
**Doğru cevap: D.** Fasıl 66 Not 1, tüfekli, kılıçlı ve kurşunlu bastonları fasıl dışında bırakıp Fasıl 93’e gönderir. Ölçü gösteren bastonlar 90.17’de, spor sopaları 95.06’da, ahşap baston taslakları 44.04’tedir. (Fasıl 66 Not 1)

**Soru 3.** Bir otomobil motoruna ait, sertleştirilmemiş vulkanize kauçuktan yapılmış subap kapağı contası hangi tarife pozisyonunda sınıflandırılır?
A) 84.09 · B) 87.08 · **C) 40.16** · D) 84.84 · E) 40.17
**Doğru cevap: C.** Bölüm XVI Not 1, sertleştirilmemiş vulkanize kauçuktan teknik eşyayı bölüm dışında bırakıp 40.16’ya gönderir; bu yüzden conta motora ait olsa da 84.09’a ya da 87.08’e girmez. Sert kauçuk olmadığı için 40.17 de değildir. Farklı malzemeden contaların poşette takımı ise 84.84’tedir. (Bölüm XVI Not 1 · 40.16)

Cevap dağılımı: A · D · C.

## Video

- **Süre:** 5 dk 13 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 9 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Cano (golf arabası spor malzemesidir diye 95.06 → HAYIR, 87.03) · Stajyer (baston bastondur diye 66.02 → HAYIR, Fasıl 93) ve Gümrükçü Baba (“bastonun içinde ne var”) · Yardımcı (motordan söküldü diye 84.09 → HAYIR, 40.16).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** yanlış çiftin üstü çizilip DOĞRUSU kartı + diğer dört çiftin pozisyonları, ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (doğru olan yeşil), tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-09-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-09.mp4
```
