# 2026 Gümrük Sınavları — Hocalarımıza Teşekkür (9:16)

Can Yılmaz'ın stüdyoda, arkasındaki LED ekranda hocalarımızı göstererek teşekkür ettiği dikey (Reels/Shorts/TikTok) video.

**Çıktı:** [`cikti/hocalara-tesekkur-9x16.mp4`](cikti/hocalara-tesekkur-9x16.mp4) — 1080×1920, 30 fps, ≈ 59,7 sn, H.264 + AAC.

## Seslendirme (özet metin)

ElevenLabs **eleven_v4**, ses: **CAn Yılmaz2** (klon, duygu etiketleriyle):

> Büyük emeğin ve mücadelenin son günü! 2026 Gümrük Sınavları hazırlık maratonumuzun sonuna geldik. Aylar süren bu yorucu dönemi, birlik ve beraberlik içinde geride bırakıyoruz.
> 1241 meslektaşımız ve 200 koçluk öğrencimiz için, özel hayatlarından fedakârlık eden çok kıymetli hocalarımız… Baset Temiz, Harun Altınsoy ve Erkan Yavuz'a; günün her saatinde ekran arkasındaki gizli kahramanımız, Gümrük Koçu Ufuk Çetintaş'a… yürekten teşekkür ederiz!
> Ankara'da bizi yalnız bırakmayacak Hakan Uçak ve Ahmet Ercan İlgüz hocalarımıza da şimdiden teşekkürler.
> Bu süreci büyük bir azim ve kararlılıkla tamamlayan siz değerli meslektaşlarımıza şükranlarımızı sunuyoruz. Emeklerinizin karşılığını en güzel şekilde almanızı diliyoruz.
> Sadece ekran başında değil; Ankara'nın soğuğunda, o sınav kapısında da omuz omuza yanınızda olacağız.
> Yolunuz açık, başarınız daim olsun! 7/24 CAN'LI Eğitim Merkezi!

## Sahne akışı

| Zaman | Kamera / sahne | LED ekran / grafik |
| --- | --- | --- |
| 0–11 sn | Geniş plan, yavaş yaklaşma | HyperFrames kinetik başlık: "Büyük emeğin ve mücadelenin son günü!", "2026 Gümrük Sınavları — Tamamlandı", "Birlik ve beraberlik"; "CAN YILMAZ" alt bandı |
| 11–15 sn | Yakın plan | 1241 meslektaş / +200 koçluk öğrencisi sayaçları |
| 16–21 sn | Geniş → LED'e itme | "Kıymetli hocalarımız": Baset Temiz, Harun Altınsoy, Erkan Yavuz kartları (isim anında) |
| 21,5–27,7 sn | LED tam ekranı devralır | "Ekran arkasındaki gizli kahraman" — siluetten renge açılan Ufuk Çetintaş, "Gümrük Koçu" |
| 27,7–35 sn | Geniş | "Ankara'da bizi yalnız bırakmayacak": Hakan Uçak, Ahmet Ercan İlgüz |
| 35–41 sn | Duygusal yakın plan | Şükranlarımızla |
| 41–51 sn | Geniş | Emeklerinizin karşılığı → "Sadece ekran başında değil" → kar yağışı ile "Ankara'nın soğuğunda" → "Sınav kapısında" → tüm hocalar "Omuz omuza" |
| 51–53,7 sn | Yakın plan + konfeti | "Yolunuz açık, başarınız daim olsun!" |
| 53,7–59,7 sn | HyperFrames kapanış | 7/24 → CAN'LI → kep → Eğitim Merkezi logo açılışı |

Video boyunca (açılış başlığı hariç) kelime kelime vurgulanan altyazı vardır.

## Üretim hattı

1. **Ses** — ElevenLabs TTS (eleven_v4, "CAn Yılmaz2"), 4 denemeden en dinamik olanı; −16 LUFS'e normalize edildi. Kelime zamanlamaları → `remotion/public/altyazi.json`.
2. **Stüdyo** — Önce boş stüdyo zemini üretildi; ardından Can Yılmaz, kendi videolarından alınan yüz/gözlük/beden referanslarıyla (yalnızca karakter; videoların içeriği ve yazıları kullanılmadı) takım elbiseli olarak Nano Banana Pro ile (9:16, 2K) bu stüdyoya yerleştirildi (`remotion/public/media/studyo.jpg`).
3. **Konuşan sunucu** — OmniHuman 1.5 (1080p) ile 5 parça dudak senkronu (`media/sunucu-1..5.mp4`). Parçalar sesteki duraklamalardan bölündü; her parça sınırı bir kamera kesmesine veya tam ekran sahneye denk getirildi.
4. **Müzik** — ElevenLabs Music v2.5, enstrümantal, duygusal-motive edici (`media/muzik.mp3`).
5. **Hocalar** — ÖN pozlar kırpıldı, arka planlar `rembg` (isnet) ile temizlendi (`remotion/public/hocalar/`).
6. **Logo** — `logocanlı.png` renk katmanlarına ayrılıp `vtracer` ile vektörleştirildi; parçalar ayrı gruplar (`#wordmark #cap #badge7 #badge24 #tagline`), koyu zemin varyantı ile (`remotion/public/logo/`).
7. **HyperFrames** — `hyperframes/ekran-baslik` (LED ekran kinetik başlık, 1280×750) ve `hyperframes/kapanis-logo` (kapanış logo animasyonu, 1080×1920); render çıktıları `remotion/public/hf/`.
8. **Remotion** — `remotion/` ana kurgu: sanal stüdyo kamerası, LED ekrana gerçek zamanlı grafikler, tam ekran devralma, altyazı, kar/konfeti, ses miksajı.

## Çalıştırma

```bash
cd remotion
npm install
npx remotion studio                 # önizleme
npx remotion render TebrikVideo ../cikti/hocalara-tesekkur-9x16.mp4 --codec=h264 --crf=18
```

HyperFrames birimlerini yeniden üretmek için ilgili klasörde `npx hyperframes render . -o ./renders/video.mp4` çalıştırıp çıktıyı `remotion/public/hf/` altına kopyalayın.

## Not

Konuşan sunucu, gerçek Can Yılmaz'a benzemesi için kullanıcının onayladığı yeni stüdyo görseliyle yeniden üretildi (5 parça, OmniHuman 1.5, 1080p). Her parça nesne/hata açısından kare kare kontrol edildi.
