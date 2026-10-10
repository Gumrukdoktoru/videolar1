# Vergi Hesaplama Dersi 6 — Demuraj ve liman giderleri: kıymete mi, KDV matrahına mı? (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** Y firması Güney Kore'den 100 ton çelik sac ithal ediyor; fiyat tonu 600 $ CFR (navlun dahil), sigorta 400 $. Yükleme limanında bekleme nedeniyle 1.600 $ demuraj; Mersin Limanı'nda boşaltmada 2.000 $ demuraj ve 1.000 $ tahmil–tahliye ödeniyor. GV %10, KDV %20. Ödenecek GV + KDV toplamı kaç $?

A) 19.200 $ · B) 19.840 $ · C) 19.928 $ · **D) 20.440 $** · E) 20.800 $

**Cevap: D — 20.440 $.**
- Kıymet: 60.000 + 400 + 1.600 (yükleme limanı demurajı) = 62.000 $ · GV %10 = 6.200 $
- Mersin'deki demuraj 2.000 $ ve tahmil–tahliye 1.000 $ kıymete girmez, KDV matrahına girer
- KDV: (62.000 + 6.200 + 3.000) × %20 = 14.240 $ → toplam 6.200 + 14.240 = 20.440 $

Çeldiriciler: A 19.200 (GV, KDV matrahına eklenmedi), B 19.840 (yurt içi giderler KDV matrahına eklenmedi), C 19.928 (yükleme limanı demurajı unutuldu), E 20.800 (varış giderleri kıymete eklendi).

## Video

- **Süre:** 4 dk 42 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 6 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Stajyer — Y firması adına (“Demuraj demurajdır, hepsi kıymete!” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** “hangi gider nereye?” sınıflandırma listesi (FİYATTA · GK'YA EKLE · YALNIZ KDV MATRAHI), Genelge 2009/32 kartı, sayaçlı hesap satırları, çözüm defteri, ödeme fişi, dört çeldirici analizi, demuraj yer kartı, ardiye paneli, “çizgi: giriş yeri” notu, 5 adımlı formül, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-06-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-06.mp4
```
