# CAN'LI 7/24 Eğitim Merkezi — Ankara Kampı Tanıtımı (9:16)

Ankara kampının 08 Kasım'da New Park Otel'de başladığını duyuran dikey (Reels/Shorts/TikTok) tanıtım videosu. Kurgunun omurgası, kullanıcının salonda çektiği kendi anlatımlı gezinti videosudur.

**Çıktı:** [`cikti/kamp-tanitim-9x16.mp4`](cikti/kamp-tanitim-9x16.mp4) — 1080×1920, 30 fps, 65 sn, H.264 + AAC, −14 LUFS.

## Anlatım (kullanıcının videosundan, olduğu gibi)

> Herkese merhaba arkadaşlar. 8 Kasım hazırlıklarımız şu an başlamış bulunmakta. New Park Otel'deyiz. New Park Otel'de Harun Altınsoy, Baset Temiz ve diğer hocalarımızın sahne alacağı ekran, kürsü burada olacak. Salonlarımız sekizinci katta ferah. Klasik Ankara otellerinin bodrum katındaki o rutubet ve nem kokusunun olduğu alanlardan değil, ferah atmosferiyle ders dinlemenize elverişli bir ortam. Zaten hocalarımızı biliyorsunuz, ekran okuyan hocalarımız değil, gümbür gümbür örnekli bir şekilde sınav odaklı ders anlatan eğitmenlerimiz. Gümrük müşaviri ve yardımcılığı sınıflarımız ayrı ayrı olacak. Yardımcılık sınıfı Begonya, gümrük müşavirliği sınıfımız burası, Lilyum sınıfı olacak. Tüm arkadaşlara başarılar diliyorum. Ankara kamp kayıtlarımız an itibariyle dolmuştur. Herkesin bilgilerine.

## Sahne akışı

Her grafik, anlatımdaki ilgili kelimenin söylendiği ana bağlıdır.

| Zaman | Görüntü |
| --- | --- |
| 0–4,9 sn | HyperFrames giriş: logo kurulur → "ANKARA KAMPI" → "8" denildiği anda **08 KASIM** → "HAZIRLIKLAR BAŞLADI"; ardından ekran iki kapı gibi açılıp salona geçer |
| 4,9–8 sn | 📍 NEW PARK OTEL · Ankara Kampı |
| 8–13 sn | Sahne alacak hocalarımız: Harun Altınsoy, Baset Temiz (+ diğer hocalarımız) |
| 13–16 sn | Sahne: ekran + kürsü burada olacak |
| 16–19 sn | Salonlarımız **8. KAT** — ferah |
| 19–32 sn | Klasik Ankara otelleri: bodrum kat / rutubet / nem kokusu → "DEĞİL!" → bizim salonlarımız: 8. katta, ferah atmosfer, derse elverişli |
| 33–41 sn | Hocalarımız: ~~ekran okuyan~~ DEĞİL → GÜMBÜR GÜMBÜR · örnekli · sınav odaklı |
| 41–51 sn | Sınıflarımız ayrı ayrı: Gümrük Müşavirliği → Lilyum Salonu (şu an buradayız), Müşavir Yardımcılığı → Begonya Salonu |
| 53–59 sn | Ankara kampı kayıtlarımız → **DOLDU** damgası |
| 59–65 sn | HyperFrames kapanış: logo, 08 KASIM'DA BAŞLIYOR, New Park Otel · 8. kat, KAYITLAR DOLDU |

Video boyunca kelime kelime vurgulanan altyazı ile sol üstte logo, sağ üstte "08 KASIM" rozeti bulunur.

## Üretim hattı

1. **Kaynak video** — Kullanıcının çektiği salon gezintisi (478×850, 60 fps): 30 fps'e çevrildi, hafif kontrast/renk düzeltmesi yapıldı (`remotion/public/media/salon.mp4`). Sesi aynen kullanıldı (`media/anlatim.m4a`).
2. **Altyazı** — ElevenLabs Scribe ile kelime zamanlamaları çıkarıldı; isimler ve yanlış duyulan kelimeler (Baset, rutubet, Yardımcılık, Lilyum) elle düzeltildi (`remotion/public/altyazi.json`).
3. **Müzik** — ElevenLabs Music v2.5, enerjik enstrümantal (`media/muzik.mp3`). İlk vuruşu "8 Kasım" anına denk getirildi; anlatım boyunca kısık, kapanışta yükselir.
4. **HyperFrames** — `hyperframes/giris` (açılış, 4,9 sn) ve `hyperframes/kapanis` (kapanış logo/tarih, 6 sn); render çıktıları `remotion/public/hf/`.
5. **Remotion** — `remotion/` ana kurgu: anlatıma bağlı bilgi kartları, kapı geçişi, damga anında kamera sarsıntısı ve flaş, altyazı, müzik ve efekt miksajı.

## Çalıştırma

```bash
cd remotion
npm install
npx remotion studio                 # önizleme
npx remotion render KampTanitim ../cikti/kamp-tanitim-9x16.mp4 --codec=h264 --crf=18
```

HyperFrames birimlerini yeniden üretmek için ilgili klasörde `npx hyperframes render . -o ./renders/video.mp4` çalıştırıp çıktıyı `remotion/public/hf/` altına kopyalayın (GSAP CDN'den yüklendiği için ağ erişimi gerekir).
