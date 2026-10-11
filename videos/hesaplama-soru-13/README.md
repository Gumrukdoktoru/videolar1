# Vergi Hesaplama Dersi 13 — Dampinge karşı vergi: menşe, net ağırlık ve KDV matrahı (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** D firması, Malezya'dan yüklenen ve menşe şahadetnamesine göre Çin menşeli polyester elyaf ithal ediyor; CIF kıymet 64.000 $, net 40.000 kg, brüt 41.500 kg. GV %4. Dampinge karşı vergi: Çin menşeli eşya için 0,30 $/kg, Malezya menşeli eşya için 0,45 $/kg. Tescilden sonra fabrikaya nakliye için 2.000 $ ödeniyor. KDV %20, 1 $ = 40 TL. Ödenecek GV + dampinge karşı vergi + KDV toplamı kaç TL?

**A) 1.210.880 TL** · B) 1.226.880 TL · C) 1.232.480 TL · D) 1.233.920 TL · E) 1.498.880 TL

**Cevap: A — 1.210.880 TL.**
- GV: 64.000 $ × %4 = 2.560 $ (damping GV matrahına girmez)
- Dampinge karşı vergi: menşe Çin → 40.000 kg net × 0,30 $ = 12.000 $
- KDV: (64.000 + 2.560 + 12.000) × %20 = 15.712 $ (tescil sonrası nakliye girmez) → toplam 30.272 $ × 40 = 1.210.880 TL

Çeldiriciler: B 1.226.880 (tescil sonrası nakliye KDV matrahına eklendi), C 1.232.480 (brüt ağırlık kullanıldı), D 1.233.920 (damping GV matrahına katıldı), E 1.498.880 (yükleme ülkesi Malezya'nın oranı uygulandı).

## Video

- **Süre:** 4 dk 51 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 13 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Yardımcı — D firması adına (“Malezya'dan geldi, Malezya oranı?”, “Malezya'dan geldiyse Malezya önlemi?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** menşe damgası, sayaçlı hesap satırları, çözüm defteri, menşe şahadetnamesi kartı, ödeme fişi, dört çeldirici analizi, “önlem hangi ülkeye?” kartı, önlem türleri paneli, “nereye bakılır?” notu, 5 adımlı formül, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-13-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-13.mp4
```
