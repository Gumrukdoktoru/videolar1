# Vergi Hesaplama Dersi 12 — Kısmi muafiyetle geçici ithalat: vergilerin aylık %3'ü (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** V firması, Çin'den kiraladığı bir mobil vinci kısmi muafiyet suretiyle geçici ithalat rejimine tabi tutuyor. Tescil tarihinde gümrük kıymeti 150.000 $, 1 $ = 40 TL; GV %5, İGV %10, KDV %20. Vinç rejimde 7 ay 12 gün kaldıktan sonra yeniden ihraç ediliyor. Rejim süresince ödenmesi gereken ithalat vergileri toplamı kaç TL?

A) 216.000 TL · B) 478.800 TL · C) 504.000 TL · D) 506.160 TL · **E) 547.200 TL**

**Cevap: E — 547.200 TL.**
- Kıymet 150.000 $ × 40 = 6.000.000 TL · GV %5 = 300.000 · İGV %10 = 600.000
- KDV: (6.000.000 + 300.000 + 600.000) × %20 = 1.380.000 → vergiler toplamı 2.280.000 TL
- Aylık: 2.280.000 × %3 = 68.400 TL · 7 ay 12 gün = 8 ay (ay kesri tam ay) → 68.400 × 8 = 547.200 TL

Çeldiriciler: A 216.000 (KDV hesaba katılmadı), B 478.800 (12 gün atılıp 7 ay sayıldı), C 504.000 (KDV matrahına GV ve İGV eklenmedi), D 506.160 (gün kesri oranlanıp 7,4 ay sayıldı).

## Video

- **Süre:** 4 dk 16 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 12 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Cano — V firması adına (“Kıymetin yüzde üçü değil mi?”, “Oran düşerse tutar da düşer mi?” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** kısmi muafiyet damgası, sayaçlı hesap satırları ve toplam, GK md. 130 kartı, çözüm defteri, ödeme fişi, dört çeldirici analizi, sonradan serbest dolaşım kartı, tescil tarihi paneli, “üç şeyi karıştırma” notu, 5 adımlı formül, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-12-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-12.mp4
```
