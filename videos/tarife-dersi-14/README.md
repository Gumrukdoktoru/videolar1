# Tarife Dersi 14 — Lokanta tipi semaver, kalem fener ve pozisyon sırası (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Bir lokantanın mutfağında kullanılmak üzere ithal edilen, tezgâh tipi, elektrikle ısıtılan büyük çay semaveri hangi tarife pozisyonunda sınıflandırılır?
**A) 84.19** · B) 85.14 · C) 85.16 · D) 85.43 · E) 94.03
**Doğru cevap: A.** 85.16 ev tipi elektrotermik cihazları kapsar; izahnamesi lokantalarda kullanılan tezgâh tipi kahve perkolatörlerini, çay ve süt semaverlerini ve normalde evlerde kullanılmayan diğer elektrotermik cihazları pozisyon dışında bırakır. Bunlar 84.19'da ısıtma ve pişirme cihazları arasındadır. Evde kullanılan küçük semaver 85.16'da kalır; restoran tipi mikrodalga fırın 85.14'tedir. (85.16 izahnamesi · 84.19)

**Soru 2.** Bir ucunda tükenmez kalem, diğer ucunda pille çalışan küçük bir LED el feneri bulunan kalem fener, perakende satışa sunuluyor. Eşyanın esas niteliğinin belirlenemediği kabul edilirse, hangi kurala göre hangi pozisyonda sınıflandırılır?
A) 85.13 · GYK 1 · B) 85.13 · GYK 3(b) · C) 96.08 · GYK 3(a) · **D) 96.08 · GYK 3(c)** · E) Ayrı ayrı · GYK 1
**Doğru cevap: D.** Kalem fener iki ayrı pozisyondaki eşyanın birleşimidir: tükenmez kalem 96.08, kendi pili olan portatif el feneri 85.13. GYK 3(a)'ya göre iki pozisyon da eşyanın yalnız bir kısmını tanımladığından eşit derecede özeldir; GYK 3(b) ile esas nitelik aranır ama belirlenemiyor; GYK 3(c) ile numara sırasına göre en son pozisyon, 96.08 seçilir. Eşya tek parça olduğundan ayrı ayrı sınıflandırılmaz. (GYK 3(a) · 3(b) · 3(c))

**Soru 3.** Aşağıdakilerden hangisinde eşyalar, tarife cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru sıralanmıştır?
A) Kolonya, yumurtalı erişte, plastik su şişesi, kâğıt alışveriş torbası · B) Yumurtalı erişte, kolonya, kâğıt alışveriş torbası, plastik su şişesi · C) Plastik su şişesi, kolonya, yumurtalı erişte, kâğıt alışveriş torbası · D) Yumurtalı erişte, plastik su şişesi, kolonya, kâğıt alışveriş torbası · **E) Yumurtalı erişte, kolonya, plastik su şişesi, kâğıt alışveriş torbası**
**Doğru cevap: E.** Yumurtalı erişte makarna olarak 19.02, kolonya tuvalet suyu olarak 33.03 (alkol içerse de Fasıl 22 değil), plastik su şişesi ambalaj eşyası olarak 39.23, kâğıt alışveriş torbası 48.19. Plastik (Fasıl 39) kâğıttan (Fasıl 48) önce gelir. (19.02 · 33.03 · 39.23 · 48.19)

Cevap dağılımı: A · D · E.

## Video

- **Süre:** 6 dk 01 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 14 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Cano (elektrikli ısıtıcı ev aletidir diye 85.16 → HAYIR, 84.19) · Yardımcı (ışık veren kısım daha önemli diye 85.13 → HAYIR, GYK 3(c), 96.08) ve Gümrükçü Baba (“önce 3(a), sonra 3(b), en son 3(c)”) · Stajyer (ambalajlar en sona kalır diye torbayı şişeden önce koyar → HAYIR) ve Gümrükçü Baba (“önce faslı bul, sonra sırala”).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), sıralama zinciri (4 eşya kartı) + dört yanlış sıralamanın ✗ gerekçesi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-14-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-14.mp4
```
