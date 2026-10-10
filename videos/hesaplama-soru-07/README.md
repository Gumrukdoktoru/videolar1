# Vergi Hesaplama Dersi 7 — KKDF: fatura bedeli, alış kuru ve KDV matrahı (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** Z firması ABD'den kabul kredili ödemeyle ambalaj makinesi ithal ediyor. Fatura FOB 30.000 $; navlun 1.500 $, sigorta 500 $. GV %5, KKDF %6, KDV %20. TCMB döviz satış kuru 40 TL, döviz alış kuru 39,50 TL. İthalatta ödenecek KDV kaç TL?

A) 268.800 TL · **B) 283.020 TL** · C) 283.200 TL · D) 283.731 TL · E) 283.968 TL

**Cevap: B — 283.020 TL.**
- Kıymet: 32.000 $ × 40 (satış kuru) = 1.280.000 TL · GV %5 = 64.000 TL
- KKDF: fatura bedeli 30.000 $ × %6 = 1.800 $ × 39,50 (alış kuru) = 71.100 TL (GV matrahına girmez)
- KDV: (1.280.000 + 64.000 + 71.100) × %20 = 1.415.100 × %20 = 283.020 TL

Çeldiriciler: A 268.800 (KKDF KDV matrahına eklenmedi), C 283.200 (KKDF satış kuruyla çevrildi), D 283.731 (KKDF GV matrahına da katıldı), E 283.968 (KKDF CIF bedel üzerinden hesaplandı).

## Video

- **Süre:** 4 dk 34 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 7 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Cano — Z firması temsilcisi (“Tek kur yeter, değil mi?”, “Peşin ödedik, KKDF var mı?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** iki kur kartı (satış / alış), KKDF özet kural kartı, sayaçlı hesap satırları, çözüm defteri, KDV fişi, dört çeldirici analizi, “KKDF hangi ödemede?” kartı, “KKDF nereye girer?” paneli, “iki kur, iki iş” notu, 5 adımlı formül, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-07-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-07.mp4
```
