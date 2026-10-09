# Vergi Hesaplama Dersi 1 — DVD'deki yazılım (Gümrük Koçu ders videosu)

Gümrük Yönetmeliği md. 54 (veri/komut yüklü taşıyıcılar) üzerine kurgulanmış özgün bir örnek soru ve anlatımlı
çözümü. HyperFrames ile üretildi.

**Soru:** (B) şirketi DVD'ye kaydedilmiş muhasebe yazılımı ithal ediyor. Faturada DVD 50 $, yazılım 2.500 $;
GV %10, KDV %20. GV + KDV toplamı?
**Cevap: C — 516 $.** GV matrahı yalnızca taşıyıcı (50 $) → GV 5 $ · KDV matrahı 50 + 5 + 2.500 = 2.555 $ → KDV 511 $.
Diğer şıkların her biri belirli bir hatadan gelir: A 16 (yazılım KDV'den de çıkarıldı), B 511 (GV unutuldu),
D 765 (yazılım GV'ye katıldı, GV KDV matrahına eklenmedi), E 816 (yazılım GV'ye katıldı).

- **Süre:** 3 dk 57 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 1 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel. Duruma göre tepki görseline geçer (yumuşak geçiş):
  normal · soru (düşünen) · dikkat (parmak yukarı) · cevap (başparmak) · uyarı (dur eli) · tuzak (şaşkın).
  Tepki görselleri, kullanıcının kendi maskot görselinden ElevenLabs'ta (Nano Banana 2) üretildi: `assets/img/koc-*.png`
- **Konuk:** Gümrükçü Baba (tuzak sahnesinde doğru cevabı söyler)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** fatura görseli, 5 sn "videoyu durdur" geri sayımı, 4 adımlı ilerleme şeridi, çözüm defteri,
  hesap makinesi, vergi makbuzu, dört çeldiricinin tek tek analizi, formül kartı, rakamlı alt yazı, YouTube bölümleri

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-01-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` | Seslendirme metni (sayılar TTS için yazıyla) |
| `tools/` | `build_timing.py` (zamanlama + alt yazı), `scenes_a/b.py` (sahneler), `build.py` (kompozisyon) |

## Yeniden üretmek

```bash
python3 tools/build_timing.py   # ses sürelerinden sahne zamanlaması + alt yazı
python3 tools/build.py          # compositions/*.html ve index.html
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-01.mp4
```
