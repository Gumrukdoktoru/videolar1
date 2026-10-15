# Tarife Dersi 15 — Nevresim takımı, okey takımı ve bölüm yapısı (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Pamuklu dokuma kumaştan bir nevresim, bir çarşaf ve iki yastık kılıfından oluşan, perakende satış ambalajındaki nevresim takımı hangi tarife pozisyonunda sınıflandırılır?
A) 63.01 · **B) 63.02** · C) 63.04 · D) 63.08 · E) 94.04
**Doğru cevap: B.** Nevresim (yorgan kılıfı), çarşaf ve yastık kılıfları 63.02 izahnamesinde yatak çarşafı olarak adıyla sayılır. Takımdaki tüm parçalar aynı pozisyona girdiğinden takım kuralına gerek kalmaz; GYK 1 ile doğrudan 63.02. 63.08 halı, kilim, işlemeli masa örtüsü gibi eşyaların yapımına mahsus mensucat ve iplik takımlarıdır; içi doldurulmuş yorgan ve yastık 94.04'tedir. (63.02 izahnamesi · GYK 1)

**Soru 2.** Plastik taşlar ve ıstakalardan oluşan, perakende satılan okey takımı hangi tarife pozisyonunda sınıflandırılır?
A) 39.26 · B) 95.03 · **C) 95.04** · D) 95.05 · E) 95.06
**Doğru cevap: C.** Okey masa başında oynanan bir salon oyunudur. 95.04 video oyun konsollarından bilardoya kadar salon ve masa oyunlarını kapsar; tavla, satranç ve oyun kâğıtları da buradadır. Taşların plastikten olması sonucu değiştirmez; Fasıl 39 notları Fasıl 95 eşyasını hariç tutar. 95.03 oyuncaklar ve modeller içindir. (95.04 · Fasıl 39 notları)

**Soru 3.** Aşağıdaki seçeneklerin hangisinde sayılan eşyaların tümü tarife cetvelinin aynı bölümünde yer alır?
**A) Pusula, akort düdüğü, duvar saati** · B) Kontakt lens, optik olarak işlenmemiş gözlük camı, dürbün · C) Kol saati, deri saat kayışı, ahşap mücevher kutusu · D) Piyano, piyano taburesi, basılı nota · E) Metronom, gitar teli, gitar kılıfı
**Doğru cevap: A.** Pusula 90.14, akort düdüğü 92.09, duvar saati 91.05: üçü de Fasıl 90–92'den oluşan Bölüm XVIII'dedir. Diğer şıklarda en az bir yabancı var: optik olarak işlenmemiş gözlük camı 70.15 (Bölüm XIII); ahşap mücevher kutusu 44.20 (Bölüm IX); piyano taburesi 94.01 (Bölüm XX) ve basılı nota 49.04 (Bölüm X); ayrı gelen gitar kılıfı 42.02 (Bölüm VIII). Gitarla birlikte gelen, ona uygun kılıf ise GYK 5(a) ile gitarla sınıflandırılır. (Bölüm XVIII · 90.14 · 91.05 · 92.09)

Cevap dağılımı: B · C · A.

## Video

- **Süre:** 5 dk 34 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 15 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Yardımcı (takım kelimesini görünce 63.08 → HAYIR, 63.02) · Cano (oynanıyorsa oyuncaktır diye 95.03 → HAYIR, 95.04) · Stajyer (gitar kılıfını aksesuar sanıp 92.09 → HAYIR, 42.02) ve Gümrükçü Baba (“ayrı geldiyse kılıf, kendi yerine”).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), doğru ifade kartı + dört yanlış şıkkın düzeltmesi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-15-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-15.mp4
```
