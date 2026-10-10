# Vergi Hesaplama Dersi 5 — Gümrük kıymeti: komisyon, tasarım, çoğaltma hakkı ve montaj (Gümrük Koçu ders videosu)

Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler
bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

**Soru:** T firması Almanya'dan 50 dikiş makinesi ithal ediyor (tanesi FOB 1.200 €). TR'ye kadar navlun 2.500 €, sigorta 500 €. Satıcının acentesine 3.000 € satış komisyonu, kendi satın alma temsilcisine 1.500 € komisyon; İtalya'da hazırlanıp üreticiye bedelsiz verilen tasarım 4.000 €; TR'de çoğaltma hakkı 6.000 €; ithalattan sonra yapılacak, faturada ayrı gösterilen montaj 2.000 €. 1 € = 40 TL. Gümrük kıymeti kaç TL?

**A) 2.800.000 TL** · B) 2.860.000 TL · C) 2.880.000 TL · D) 3.040.000 TL · E) 3.180.000 TL

**Cevap: A — 2.800.000 TL.**
- Fiyat + nakliye: 60.000 + 2.500 + 500 = 63.000 €
- Ekle: satış komisyonu 3.000 € (GK 27/1-a), yurt dışı tasarım 4.000 € (GK 27/1-b) → 70.000 €
- Ekleme: satın alma komisyonu, TR'de çoğaltma hakkı, ayrı gösterilen montaj (GK 27/1-a, md. 28) · 70.000 × 40 = 2.800.000 TL

Çeldiriciler: B 2.860.000 (satın alma komisyonu eklendi), C 2.880.000 (ayrı gösterilen montaj eklendi), D 3.040.000 (TR'de çoğaltma hakkı eklendi), E 3.180.000 (ödenen her şey eklendi).

## Video

- **Süre:** 4 dk 43 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 5 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Yardımcı — T firması temsilcisi (“Ödediğimiz her şeyi ekleriz, değil mi?”, “Komisyon komisyondur, hepsini ekleyelim!” → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevap)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** ekle / ekleme sınıflandırma listesi (GK'YA EKLE · EKLENMEZ etiketleri), kanun kartları (GK 27/1-e, md. 30), sayaçlı hesap satırları, ödeme fişi, dört çeldirici analizi, komisyon türleri kartı, montaj paneli, “her ödemeye 3 soru” notu, 5 adımlı formül zinciri, 5 sn geri sayım; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-05-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |
| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-05.mp4
```
