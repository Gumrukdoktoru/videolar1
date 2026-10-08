# VRF Klimalar — Gümrük Koçu ders videosu

Gümrükler Genel Müdürlüğünün 01.10.2026 tarihli, E-17474625-162.01-00126963399 sayılı
"VRF Klimalar" yazısını anlatan, HyperFrames (HeyGen) ile üretilmiş ders videosu.

- **Süre:** 4 dk 18 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (İstanbul aksanı). 15 sahne, sahne başına ayrı kayıt (`narration/`)
- **Sunucu:** Gümrük Koçu (repodaki `Gümrükkoçu.png`, arka planı temizlenmiş), konuşmaya göre hareket eden gövde + ses çubukları
- **Konuk karakter:** Gümrükçü Baba ("ÖNEMLİ" sahnesinde konuşma balonuyla)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** ilerleme çubuğu + bölüm etiketi, kelimeye senkron alt yazı, mini quiz (3-2-1 geri sayım),
  Koçun Tavsiyesi kartı, özet/abone kartı, ses efektleri

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/vrf-klima-dersi.mp4` | Bitmiş video |
| `youtube-bolumler.txt` | YouTube açıklamasına yapıştırılacak bölüm zaman damgaları |
| `altyazi.srt` | YouTube'a ayrı yüklenebilecek Türkçe altyazı |
| `narration/script.json` | Seslendirme metni (sahne sahne) |
| `index.html`, `compositions/` | HyperFrames kompozisyonu (üretilmiş dosyalar) |
| `tools/` | Sahneleri üreten betikler (`scenes_a/b/c.py`, `build.py`, `build_timing.py`) |

## Yeniden üretmek

```bash
python3 tools/build_timing.py   # ses sürelerinden sahne zamanlaması + alt yazı
python3 tools/build.py          # compositions/*.html ve index.html
npx hyperframes check           # kalite kontrolü
npx hyperframes render --fps 30 -o renders/vrf-klima-dersi.mp4
```

## Dudak senkronlu avatar (isteğe bağlı yükseltme)

Şu anki sunucu hareketli ama dudak senkronu yok. İki yol var:

1. **ElevenLabs → HeyGen Avatar 4:** Akışta (`VRF Klima Dersi — Gümrük Koçu`) yeşil perdeli görsel
   (`assets/img/koc-avatar-green.png`) ve 1. sahnenin sesi bağlı bir HeyGen Avatar 4 düğümü hazır.
   Tahmini maliyet ~12.100 kredi / 20 sn (tüm video ≈ 145.000 kredi) olduğu için onay olmadan çalıştırılmadı.
2. **HeyGen hesabınızdaki "Gümrük Koçu" (öğretmen görünümü) avatarı:** Ortama bir HeyGen API anahtarı
   eklenirse aynı Cem seslendirmesiyle o avatar üretilip sunucu kartına yerleştirilebilir.
