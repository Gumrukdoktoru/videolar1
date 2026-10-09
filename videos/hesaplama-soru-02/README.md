# Vergi Hesaplama Dersi 2 — Kültür fonu, ceza ve uzlaşma (Gümrük Koçu ders videosu)

Kültür fonunun vergilendirmedeki yeri, GK md. 234 para cezası ve Gümrük Uzlaşma Yönetmeliği md. 6 üzerine kurgulanmış
**özgün** bir örnek soru ve anlatımlı çözümü. HyperFrames ile üretildi.

**Soru:** Sonradan kontrolde K firmasının 40.000 $ kıymetli ithalatında kültür fonunun hiç ödenmediği tespit ediliyor.
GV %0, ÖTV %10, KDV %20, kültür fonu %3; 1 $ = 30 TL. İdare kültür fonu için ilgili kuruma bildirimde bulunuyor, gümrük
vergileri için ek tahakkuk + ceza uyguluyor. Firma uzlaşabileceği tüm tutarlar için başvuruyor. Uzlaşmaya konu tutar?
**Cevap: D — 46.080 TL.** Kıymet 1.200.000 TL → kültür fonu 36.000 TL (kuruma bildirilir, uzlaşma dışı) · eksik ÖTV
36.000 × %10 = 3.600 · eksik KDV (36.000 + 3.600) × %20 = 7.920 → eksik vergi 11.520 · ceza 11.520 × 3 = 34.560 →
11.520 + 34.560 = 46.080 TL.
Çeldiriciler: A 11.520 (ceza unutuldu), B 36.000 (yalnız kültür fonu), C 43.200 (ÖTV, KDV matrahına eklenmedi:
10.800 + 32.400), E 82.080 (kültür fonu da uzlaşmaya katıldı).

- **Süre:** 4 dk 30 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 2 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş:
  normal · soru (düşünen) · dikkat (parmak yukarı) · uyarı (dur eli, ceza ve uzlaşma uyarısında) · cevap (başparmak) · tuzak (şaşkın)
- **Konuklar:** Cano — K firması temsilcisi (soruda "uzlaşabileceğimiz her tutar için başvuruyoruz", uyarıda
  "kültür fonunu da uzlaşalım mı?" → HAYIR!) · Gümrükçü Baba (tuzak sahnesinde doğru cevabı söyler)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** kültür fonunun 4 yönlü "girer / girmez" şeması (oklarla), sayaçlı hesaplar, çözüm defteri
  (kültür fonu satırı "UZLAŞMA DIŞI" damgalı), hesap makinesi (×3 ceza), uzlaşma makbuzu, dört çeldiricinin analizi,
  Uzlaşma Yön. md. 6 listesi, "önce sen bildir" karşılaştırması (GK 234/3: 34.560 → 3.456 TL), formül kartı,
  5 sn "videoyu durdur" geri sayımı, rakamlı alt yazı, YouTube bölümleri

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-02-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` | Seslendirme metni (sayılar TTS için yazıyla) |
| `tools/` | `build_timing.py` (zamanlama + alt yazı), `scenes_a/b.py` (sahneler), `build.py` (kompozisyon) |

## Yeniden üretmek

```bash
python3 tools/build_timing.py   # ses sürelerinden sahne zamanlaması + alt yazı
python3 tools/build.py          # compositions/*.html ve index.html
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-02.mp4
```
