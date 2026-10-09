# Tarife Dersi 3 — Yatak takımı, deniz memelileri, patenler (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Dış yüzü pamuklu dokunmuş mensucattan, içi kaz tüyüyle doldurulmuş yorgan hangi tarife pozisyonunda sınıflandırılır?
A) 63.01 · B) 63.02 · **C) 94.04** · D) 52.08 · E) 05.05
**Doğru cevap: C.** 94.04 içi herhangi bir maddeyle doldurulmuş yatak takımı eşyasını (şilte, yorgan, yastık, uyku tulumu) kaplanmış olsun olmasın kapsar; dış yüzün pamuklu olması sonucu değiştirmez. Battaniyeler (63.01) dolgusuzdur. (94.04 pozisyon metni)

**Soru 2.** Dondurulmuş fok eti hangi tarife pozisyonunda sınıflandırılır?
**A) 02.08** · B) 03.03 · C) 02.06 · D) 16.02 · E) 03.04
**Doğru cevap: A.** Fok deniz memelisidir, balık değildir. Fasıl 3 yalnız balık, kabuklu hayvan ve yumuşakçaları kapsar; deniz memelilerinin eti 02.08'de (0208.40: balina, yunus, fok, deniz aslanı, deniz aygırı). Yağları ise 15.04. (0208.40 alt pozisyonu)

**Soru 3.** Altına buz pateni bıçağı sökülemeyecek şekilde tutturulmuş, üst kısmı deri, dış tabanı kauçuk bot hangi tarife pozisyonunda sınıflandırılır?
A) 64.03 · B) 64.02 · C) 95.03 · D) 64.06 · **E) 95.06**
**Doğru cevap: E.** Fasıl 64 Not 1 paten takılmış botları hariç tutar ve Fasıl 95'e gönderir; 9506.70 buz ve tekerlekli patenleri, paten takılmış botlar dahil kapsar. Patensiz paten botu Fasıl 64'te kalır; oyuncak karakterli ayakkabılar 95.03. (Fasıl 64 Not 1, 9506.70)

Cevap dağılımı: C · A · E.

## Video

- **Süre:** 4 dk 42 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 3 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Yardımcı (pamuklu yüz → 63.01 battaniye → HAYIR) · Cano (denizden çıkıyor → balık → HAYIR) · Stajyer (üstü deri → 64.03 → HAYIR) ve Gümrükçü Baba (“bıçak takılıysa 95.06; patensiz bot Fasıl 64”).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** sınıflandırma yolu (ürün kartı → 3 adım → pozisyon) ve beş aday pozisyonun ✓/✗ şeridi, tuzak karşılaştırma kartları (≠), DİKKAT kartları (9404.30 uyku tulumları, 15.04 deniz memelisi yağları, 95.03 oyuncak ayakkabılar), koçun notu zihin haritası, cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-03-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-03.mp4
```
