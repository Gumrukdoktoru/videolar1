# Vergi Hesaplama Dersi 8 — Vergi zinciri: GV → TRT bandrol → ÖTV → KDV (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** M firması Çin'den 100 adet cep telefonu ithal ediyor; CIF kıymet 20.000 $, 1 $ = 40 TL. GV %5, TRT bandrol ücreti %10, ÖTV %20, KDV %20. Ödenecek GV + bandrol + ÖTV + KDV toplamı kaç TL?

A) 467.200 TL · B) 493.600 TL · C) 510.400 TL · D) 524.800 TL · **E) 530.560 TL**

**Cevap: E — 530.560 TL.**
- Kıymet 800.000 TL · GV %5 = 40.000 TL
- Bandrol: (800.000 + 40.000) × %10 = 84.000 · ÖTV: (840.000 + 84.000) × %20 = 184.800
- KDV: (924.000 + 184.800) × %20 = 221.760 → toplam 40.000 + 84.000 + 184.800 + 221.760 = 530.560 TL

Çeldiriciler: A 467.200 (GV hiç hesaplanmadı), B 493.600 (ÖTV KDV matrahına eklenmedi), C 510.400 (bandrol ÖTV matrahına eklenmedi), D 524.800 (GV bandrol matrahına eklenmedi).

## Video

- **Süre:** 4 dk 26 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 8 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Yardımcı — M firması adına (“Hepsini kıymetten hesaplasak?”, “Bandrolü ÖTV'den sonra mı hesaplasak?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** vergi sırası zinciri, sayaçlı hesap satırları, çözüm defteri, ödeme fişi, dört çeldirici analizi, “kim kimin matrahına girer?” kartı, KDV paneli, vergi merdiveni notu, 5 adımlı formül, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-08-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-08.mp4
```
