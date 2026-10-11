# Vergi Hesaplama Dersi 11 — Çevre katkı payı: hurdada binde beş, yakıtta yüzde bir (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** Ç firması ABD'den FOB teslim şekliyle aynı beyannamede iki kalem eşya ithal ediyor. 1. kalem kontrole tabi demir-çelik hurdası: FOB 600.000 $, navlun 45.000 $, sigorta 5.000 $; ayrıca Türkiye'deki boşaltma limanında 20.000 $ tahmil tahliye ödeniyor. 2. kalem kontrole tabi yakıt (petrol koku): FOB 80.000 $, navlun 18.000 $, sigorta 2.000 $. 1 $ = 40 TL. Ödenecek çevre katkı payı toplamı kaç TL?

A) 152.000 TL · **B) 170.000 TL** · C) 174.000 TL · D) 280.000 TL · E) 300.000 TL

**Cevap: B — 170.000 TL.**
- CIF: hurda 600.000 + 45.000 + 5.000 = 650.000 $ (Türkiye'deki tahmil tahliye girmez) · petrol koku 80.000 + 18.000 + 2.000 = 100.000 $
- Hurda ‰5: 650.000 × 0,005 = 3.250 $ · petrol koku %1: 100.000 × 0,01 = 1.000 $
- Toplam 4.250 $ × 40 = 170.000 TL

Çeldiriciler: A 152.000 (FOB üzerinden hesaplandı), C 174.000 (Türkiye'deki tahmil tahliye hurdanın matrahına katıldı), D 280.000 (oranlar ters uygulandı), E 300.000 (ikisine de %1 uygulandı).

## Video

- **Süre:** 4 dk 16 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 11 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Yardımcı — Ç firması adına (“Hurdaya da yüzde beş mi?”, “Her ithalatta ÇKP alınır mı?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** FOB teslim damgası, sayaçlı hesap satırları, çözüm defteri, “‰5 = %0,5” kartı, ödeme fişi, dört çeldirici analizi, “ÇKP kimden alınır?” kartı, CIF/FOB paneli, ÇKP’de 2 soru notu, 5 adımlı formül, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-11-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-11.mp4
```
