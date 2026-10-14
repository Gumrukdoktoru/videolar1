# 2026 Gümrük Sınavları — Hocalarımıza Teşekkür (9:16)

Can Yılmaz'ın stüdyoda, arkasındaki LED ekranda hocalarımızı göstererek teşekkür ettiği dikey (Reels/Shorts/TikTok) video.

**Çıktı:** [`cikti/hocalara-tesekkur-9x16.mp4`](cikti/hocalara-tesekkur-9x16.mp4) — 1080×1920, 30 fps, ≈ 59,7 sn, H.264 + AAC.

## Seslendirme (özet metin)

Videonun sesi, kullanıcının gönderdiği videonun kendi sesidir (seslendirme + müzik + efektler, olduğu gibi). Metin:

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

1. **Sunucu ve ses** — Kullanıcının gönderdiği video **olduğu gibi** kullanıldı; karakter yapay zekâ ile üretilmedi veya değiştirilmedi. Videonun 9:16 bölümü kırpıldı, yalnızca arkasındaki oda kaldırıldı:
   - Kamera sabit olduğu için örnek karelerdeki kaba insan maskelerinden (`u2net_human_seg`) temiz bir arka plan tabakası çıkarıldı.
   - Her kare bu tabakayla farkı alınarak piksel hassasiyetinde ayrıldı; kenarlardaki oda rengi temizlendi.
   - Kişi yalnızca ölçeklenerek (1,25×) stüdyo zeminine yerleştirildi; ayak altına temas gölgesi ve zemin yansıması eklendi (`remotion/public/media/sunucu.mp4`).
   - Ses, aynı videodan alındı (`media/ses.m4a`); görüntüyle birebir senkron.
2. **Stüdyo** — Boş stüdyo zemini (LED ekranlı), Nano Banana Pro ile 9:16 üretildi.
3. **Altyazı** — Kelime zamanlamaları → `remotion/public/altyazi.json`.
4. **Hocalar** — ÖN pozlar kırpıldı, arka planlar `rembg` (isnet) ile temizlendi (`remotion/public/hocalar/`).
5. **Logo** — `logocanlı.png` renk katmanlarına ayrılıp `vtracer` ile vektörleştirildi; parçalar ayrı gruplar (`#wordmark #cap #badge7 #badge24 #tagline`), koyu zemin varyantı ile (`remotion/public/logo/`).
6. **HyperFrames** — `hyperframes/ekran-baslik` (LED ekran kinetik başlık, 1280×750) ve `hyperframes/kapanis-logo` (kapanış logo animasyonu, 1080×1920); render çıktıları `remotion/public/hf/`.
7. **Remotion** — `remotion/` ana kurgu: sanal stüdyo kamerası, LED ekrana gerçek zamanlı grafikler, tam ekran devralma, altyazı, kar/konfeti.

## Çalıştırma

```bash
cd remotion
npm install
npx remotion studio                 # önizleme
npx remotion render TebrikVideo ../cikti/hocalara-tesekkur-9x16.mp4 --codec=h264 --crf=18
```

HyperFrames birimlerini yeniden üretmek için ilgili klasörde `npx hyperframes render . -o ./renders/video.mp4` çalıştırıp çıktıyı `remotion/public/hf/` altına kopyalayın.

## Not

Sunucu, kullanıcının kendi videosundaki kişidir; yüz, kıyafet, el ve dudak hareketleri kaynak videodakiyle aynıdır. Kaynak videonun sesi, kurgunun zamanlamasıyla aynı olduğundan (yalnızca 40 ms kaydırıldı) tüm LED sahneleri, altyazılar ve geçişler korunmuştur.
