# Vergi Hesaplama Dersi 4 — İlave gümrük vergisi: nispi tutar ve en az / en çok sınırı (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** K firması, Çin menşeli 4.000 kg plastik mutfak eşyası ithal ediyor. CIF kıymet 16.000 $. GV %10; İGV %30, ancak kg başına en az 1,5 $, en çok 2,5 $; KDV %20. Ödenecek GV + İGV + KDV toplamı kaç $?

A) 10.880 $ · B) 11.120 $ · **C) 12.320 $** · D) 17.120 $ · E) 18.080 $

**Cevap: C — 12.320 $.**
- GV: 16.000 × %10 = 1.600 $ · İGV nispi: 16.000 × %30 = 4.800 $
- En az: 4.000 × 1,5 = 6.000 $ · en çok: 4.000 × 2,5 = 10.000 $ → nispi en azın altında → İGV = 6.000 $
- KDV: (16.000 + 1.600 + 6.000) × %20 = 4.720 $ → toplam 1.600 + 6.000 + 4.720 = 12.320 $

Çeldiriciler: A 10.880 (min karşılaştırması yapılmadı, nispi yazıldı), B 11.120 (İGV KDV matrahına eklenmedi), D 17.120 (en çok tutar uygulandı), E 18.080 (nispi + en az toplandı).

## Video

- **Süre:** 4 dk 25 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 4 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Cano — K firması temsilcisi (“Yüzde otuz yeter, değil mi?”, “Nispi ile en azı toplayalım mı?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** min–max koridor çubukları (EN AZ / NİSPİ / EN ÇOK, uygulanan tutar vurgusu), sayaçlı hesap satırları, çözüm defteri, ödeme fişi, dört çeldirici analizi, min–max kural kartı, brüt/net ağırlık uyarısı, 5 adımlı formül zinciri, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-04-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-04.mp4
```
