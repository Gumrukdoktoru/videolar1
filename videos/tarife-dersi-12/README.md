# Tarife Dersi 12 — Pul biber, güneş paneli ve iki tekerlekli taşıtlar (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Kurutulup pul hâlinde ezilmiş, başka hiçbir madde katılmamış kırmızı biber, yani pul biber, hangi tarife pozisyonunda sınıflandırılır?
A) 07.09 · B) 07.12 · **C) 09.04** · D) 20.05 · E) 21.03
**Doğru cevap: C.** Pul biber, Capsicum cinsi kırmızı biberin kurutulup ezilmiş hâlidir. Fasıl 7 açıklama notu Capsicum ve Pimenta cinsi biberlerin kurutulmuş, ezilmiş veya öğütülmüş meyvelerini fasıl dışında bırakır; 09.04 bunları adıyla sayar. Taze biber 07.09'dadır; 07.12 bu biberleri hariç tutar; salça, turşu gibi hazır ürünler Fasıl 20'ye gider. (Fasıl 7 açıklama notu · 09.04)

**Soru 2.** Yalnızca birbirine bağlanmış güneş pillerinden oluşan; invertör, akü veya bir motoru doğrudan besleyen başka bir eleman içermeyen fotovoltaik güneş paneli hangi tarife pozisyonunda sınıflandırılır?
A) 85.01 · B) 85.04 · C) 85.07 · **D) 85.41** · E) 94.05
**Doğru cevap: D.** Fotovoltaik hücreler modül veya panel hâlinde birleştirilmiş olsalar da yarı iletken cihaz olarak 85.41'dedir. 85.01 izahnamesi yalnız akü, invertör gibi cihazlarla birleştirilmiş ya da gücü doğrudan bir motora veren elemanlarla donatılmış panelleri fotovoltaik jeneratör sayar. Fotovoltaik LED aydınlatma cihazları 94.05'tedir. (85.41 · 85.01 izahnamesi)

**Soru 3.** Aşağıdakilerden hangisi 87.11 pozisyonunda sınıflandırılmaz?
A) Pedal çevrildiğinde devreye giren, yardımcı elektrik motorlu bisiklet · **B) Ayakla itilerek ilerleyen, yetişkinlerin de kullanabildiği motorsuz skuter** · C) Kendi kendini dengeleyen, tek kişilik, iki tekerlekli elektrikli nakil aracı · D) Hem motoru hem pedalı bulunan mopet · E) Motosiklete takılan yan sepet
**Doğru cevap: B.** 87.11 motosikletleri ve yardımcı motorlu bisikletleri kapsar; izahnameye göre mopetler, kendini dengeleyen iki tekerlekli elektrikli araçlar ve motosiklet sepetleri de buradadır. Motorsuz, ayakla itilen skuterler yetişkinler için tasarlanmış olsa bile 95.03'te tekerlekli oyuncaklar arasındadır. Yardımcı motoru olan bisiklet, motoru elektrikli olsa da 87.12'ye değil 87.11'e girer. (87.11 izahnamesi · 95.03)

Cevap dağılımı: C · D · B.

## Video

- **Süre:** 5 dk 29 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 12 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Cano (biber sebzedir diye 07.12 → HAYIR, 09.04) · Yardımcı (panel elektrik üretiyor diye 85.01 → HAYIR, 85.41) ve Gümrükçü Baba (“panelin yanında başka ne var?”) · Stajyer (bisiklet bisiklettir diye 87.12 → HAYIR, 87.11) ve Gümrükçü Baba (“motor var mı?”).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), yanlış ifade + DOĞRUSU kartı + dört doğru şık, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-12-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-12.mp4
```
