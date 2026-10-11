# Vergi Hesaplama Dersi 10 — ÖTV (III-A): bira ve şarapta nispi vergi mi, asgari maktu mu? (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** R firması aynı beyannameyle iki ürün ithal ediyor: 33 cl'lik 12.000 kutu bira (alkol %5, ÖTV'ye esas birim değer kutu başına 5 TL) ve 75 cl'lik 4.000 şişe şarap (alkol %13, şişe başına 60 TL). Nispi ÖTV oranı ikisinde de %63; asgari maktu vergi tutarı bira için 2,50 TL, şarap için 25 TL. Ödenecek toplam ÖTV kaç TL?

A) 112.800 TL · B) 124.500 TL · C) 189.000 TL · **D) 200.700 TL** · E) 313.500 TL

**Cevap: D — 200.700 TL.**
- Litre: bira 0,33 × 12.000 = 3.960 L · şarap 0,75 × 4.000 = 3.000 L
- Bira: nispi 60.000 × %63 = 37.800 · asgari maktu 3.960 × 5 × 2,50 = 49.500 → 49.500 TL (yüksek olan)
- Şarap: nispi 240.000 × %63 = 151.200 · asgari maktu 3.000 × 25 = 75.000 → 151.200 TL · toplam 49.500 + 151.200 = 200.700 TL

Çeldiriciler: A 112.800 (her üründe düşük olan alındı), B 124.500 (ikisinde de asgari maktu), C 189.000 (ikisinde de nispi; birada derece unutulursa da buraya düşülür), E 313.500 (nispi ile asgari maktu toplandı).

## Video

- **Süre:** 4 dk 41 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 10 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Stajyer — R firması adına (“Nispi ile maktuyu toplasak?”, “Formül hepsinde aynı değil mi?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** iki ürün kartı, sayaçlı hesap satırları, çözüm defteri (düşük olan üstü çizili), ödeme fişi, dört çeldirici analizi, “formül içkiye göre değişir” kartı, sigara paneli, “bu hangi içki?” notu, 5 adımlı formül, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-10-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-10.mp4
```
