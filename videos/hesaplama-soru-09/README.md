# Vergi Hesaplama Dersi 9 — Tarım payı: bileşim kodu, T1 tutarı ve 100 kg net (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** B firması, Malezya menşeli ve Malezya'dan gelen gofret ithal ediyor; CIF kıymet 24.000 €, net ağırlık 6.000 kg, brüt ağırlık 6.300 kg. Bileşim tablosuna göre tarım payı kodu 7225: T1 tutarı 100 kg başına 40 €, T2 tutarı 25 €. GV %8, KDV %10, 1 € = 45 TL. Ödenecek GV + tarım payı + KDV toplamı kaç TL?

A) 277.290 TL · B) 311.040 TL · **C) 321.840 TL** · D) 327.780 TL · E) 331.344 TL

**Cevap: C — 321.840 TL.**
- Kıymet 24.000 € × 45 = 1.080.000 TL · GV %8 = 86.400 TL (tarım payı GV matrahına girmez)
- Tarım payı: AB dışı menşe → T1; 6.000 kg net ÷ 100 = 60 × 40 € = 2.400 € × 45 = 108.000 TL
- KDV: (1.080.000 + 86.400 + 108.000) × %10 = 127.440 → toplam 86.400 + 108.000 + 127.440 = 321.840 TL

Çeldiriciler: A 277.290 (AB menşeine ait T2 tutarı kullanıldı), B 311.040 (tarım payı KDV matrahına eklenmedi), D 327.780 (brüt ağırlık kullanıldı), E 331.344 (tarım payı GV matrahına da katıldı).

## Video

- **Süre:** 4 dk 39 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 9 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Cano — B firması adına (“Brüt ağırlığı mı alsak?”, “GV sıfırsa tarım payı da sıfır mı?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** bileşim kodu damgası, sayaçlı hesap satırları, çözüm defteri, bileşim kodu kartı, ödeme fişi, dört çeldirici analizi, “bileşim kodu nasıl bulunur?” kartı, AB menşeli eşya paneli, tarımda 3 soru notu, 5 adımlı formül, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-09-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-09.mp4
```
