# Tarife Dersi 4 — Çakmak taşı, konteyner, alkolsüz içecek (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Çakmaklarda kullanılmak üzere küçük silindirler hâlinde hazırlanmış, ferroseryum alaşımından çakmak taşları hangi tarife pozisyonunda sınıflandırılır?
A) 96.13 · B) 28.46 · C) 72.02 · **D) 36.06** · E) 38.24
**Doğru cevap: D.** 96.13 çakmakları ve aksamını kapsar ama çakmak taşları ve fitilleri hariç tutar. Ferroseryum ve diğer piroforik alaşımlar her şekilde 36.06'dadır. Adındaki 'ferro' 72.02'ye götürmez. (96.13 ve 36.06 pozisyon metinleri)

**Soru 2.** Alüminyumdan yapılmış, kara ve hava yoluyla taşımaya göre özel olarak donatılmış, kancaları ve küçük tekerlekleri bulunan, bozulabilir gıdalar için yalıtımlı konteyner hangi tarife pozisyonunda sınıflandırılır?
**A) 86.09** · B) 76.11 · C) 76.12 · D) 84.18 · E) 87.16
**Doğru cevap: A.** 86.09 bir veya daha fazla taşıma şekline göre yapılmış ve donatılmış konteynerleri, yapıldığı maddeye bakmaksızın kapsar; izahname yalıtımlı konteynerleri sayar. Tank konteynerler ancak taşıta göre yapılıp bağlanıyorsa 86.09'dadır. (86.09 izahnamesi)

**Soru 3.** Hacmen %0,4 alkol içeren, maltlı alkolsüz bira hangi tarife pozisyonunda sınıflandırılır?
A) 22.03 · B) 22.06 · **C) 22.02** · D) 22.01 · E) 20.09
**Doğru cevap: C.** Fasıl 22 Not 3'e göre alkolsüz içecek, hacmen alkol derecesi %0,5'i geçmeyen içecektir (20 °C'de). %0,4 alkollü malt içeceği 22.02'de (2202.91 alkolsüz biralar); %0,5'in üstü 22.03. (Fasıl 22 Not 3, 2202.91)

Cevap dağılımı: D · A · C.

## Video

- **Süre:** 4 dk 53 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 4 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Cano (adında ferro var → 72.02 → HAYIR) · Yardımcı (alüminyum → 76.11 → HAYIR) · Stajyer (bira yazıyor → 22.03 → HAYIR) ve Gümrükçü Baba (“≤ %0,5 → 22.02, üstü → 22.03”).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** sınıflandırma yolu (ürün kartı → 3 adım → pozisyon) ve beş aday pozisyonun ✓/✗ şeridi, tuzak karşılaştırma kartları (≠), DİKKAT/UYARI kartları (çakmak aksamı kartuş 96.13 · ≤300 cm³ çakmak gazı 3606.10, tank konteyner şartı, 20 °C ölçüm), koçun notu zihin haritası, cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-04-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-04.mp4
```
