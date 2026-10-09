# Çıkmış Hesaplama Sorusu 1 — CD'deki yazılım (Gümrük Koçu ders videosu)

"Geçmiş Yıllar Vergi Hesaplama Soruları" derlemesinin 1. sorusunun (CD üzerine kaydedilmiş yazılım ithalatı)
HyperFrames ile üretilmiş anlatımlı çözümü. Kaynak: `Gumrukdoktoru/2027-GM-` → `Hesaplamaçıkmış.pdf`
(soru s. 480, cevap anahtarı 1-A s. 499, çözüm s. 500; kapsam uyarısı ve ihracat notu 69-70. soru çözümleri, s. 512).

**Cevap: A — 182,98 USD.**
GV matrahı yalnızca taşıyıcı ortam (10 $) → GV 1 $ · KDV matrahı 10 + 1 + 1.000 = 1.011 $ → KDV 181,98 $.

- **Süre:** 3 dk 56 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne, sahne başına ayrı kayıt, `narration/`;
  ElevenLabs akışı: "Çıkmış Hesaplama Soru 1 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu (öğretmen görseli), konuşmaya göre hareket eden gövde + ses çubukları
- **Konuk:** Gümrükçü Baba (tuzak sahnesinde konuşma balonuyla)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** fatura görseli, "videoyu durdur" 5 sn geri sayımı, 4 adımlı ilerleme şeridi, sahneler arası
  dolan "çözüm defteri", hesap makinesi animasyonu, vergi makbuzu, çeldirici analizi (B ve E şıklarının
  nasıl kurulduğu + doğrusu), akılda kalıcı formül kartı, rakamlı alt yazı, YouTube bölümleri

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-01-web.mp4` | Bitmiş video (repoda). Ana render (CRF 16) boyut nedeniyle repoya eklenmez; aşağıdaki komutla yeniden üretilir |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` | Seslendirme metni (sayılar TTS için yazıyla) |
| `tools/` | `build_timing.py` (zamanlama + alt yazı), `fix_tx.py` (3. sahne şık okuması için kelime zamanları), `scenes_a/b.py`, `build.py` |

## Yeniden üretmek

```bash
python3 tools/fix_tx.py         # Whisper'ın atladığı şık okumasını sessizlik aralıklarından yeniden kurar
python3 tools/build_timing.py   # ses sürelerinden sahne zamanlaması + alt yazı
python3 tools/build.py          # compositions/*.html ve index.html
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-01.mp4
```

Not: C (198,98) ve D (299,98) şıklarının nasıl türetildiği kaynakta açıklanmadığı için videoda yalnızca
hesapla doğrulanabilen B ve E çeldiricileri analiz edildi.
