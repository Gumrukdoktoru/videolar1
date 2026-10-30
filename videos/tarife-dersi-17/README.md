# Tarife Dersi 17 — Sülfonlanmış hint yağı, porselen salon bebeği ve pozisyon sırası (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Sülfürik asitle muamele edilerek sülfonlanmış hint yağı, yani Türk kırmızısı yağı, hangi tarife pozisyonunda sınıflandırılır?
A) 15.15 · B) 15.16 · C) 15.18 · **D) 34.02** · E) 38.23
**Doğru cevap: D.** Hint yağı bitkisel sabit yağ olarak 15.15'tedir. Fasıl 15 Not 1 sülfonatlı sıvı yağları fasıl dışında bırakır; 15.18 izahnamesi de sülfonlanmış yağları (sülfürik asitle muamele edilmiş sıvı yağlar) adıyla 34.02'ye gönderir. 15.18 metnindeki 'kükürtlenmiş' yağlar sülfonlanmış yağlarla aynı şey değildir. (Fasıl 15 Not 1 · 15.18 izahnamesi · 34.02)

**Soru 2.** Çocukların oynaması için değil, süs amacıyla yapılmış, giydirilmiş porselen salon bebeği hangi tarife pozisyonunda sınıflandırılır?
A) 69.11 · B) 69.13 · **C) 95.03** · D) 96.18 · E) 97.03
**Doğru cevap: C.** 95.03 izahnamesi yalnız çocukların eğlenmesine mahsus bebekleri değil, salon bebekleri ve maskot bebekler gibi dekoratif amaçlı yapma bebekleri de kapsar ve bebeklerin seramikten yapılabileceğini belirtir. Fasıl 69 Not 2(k) Fasıl 95 eşyasını hariç tutar. Seramikten bir hayvan biblosu 69.13'e, vitrin mankeni 96.18'e gider. (95.03 izahnamesi · Fasıl 69 Not 2(k))

**Soru 3.** Aşağıdakilerden hangisinde eşyalar, tarife cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru sıralanmıştır?
A) Bambu yemek çubuğu, şekerli kondanse süt, ayakla çalışan bisiklet pompası, para sayma makinesi · **B) Şekerli kondanse süt, bambu yemek çubuğu, ayakla çalışan bisiklet pompası, para sayma makinesi** · C) Şekerli kondanse süt, bambu yemek çubuğu, para sayma makinesi, ayakla çalışan bisiklet pompası · D) Şekerli kondanse süt, ayakla çalışan bisiklet pompası, bambu yemek çubuğu, para sayma makinesi · E) Para sayma makinesi, şekerli kondanse süt, bambu yemek çubuğu, ayakla çalışan bisiklet pompası
**Doğru cevap: B.** Şekerli kondanse süt 04.02, bambudan Çin usulü yemek çubukları 44.19 (4419.12), ayakla çalışan bisiklet pompası el veya ayakla çalışan hava pompası olarak 84.14 (8414.20), para sayma makinesi 84.72. Bölüm XVII Not 2(e) 84.01–84.79 makinelerini taşıt parçası saymadığından pompa 87.14'e girmez; para sayma makinesi 84.70 (hesap makineleri) değil 84.72'dir. (04.02 · 4419.12 · 8414.20 · 84.72)

Cevap dağılımı: D · C · B.

## Video

- **Süre:** 5 dk 56 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 17 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Yardımcı (15.18 metninde kükürtlenmiş yazıyor diye 15.18 → HAYIR, 34.02) · Cano (çocuk oynamıyor diye süs eşyası 69.13 → HAYIR, 95.03) · Stajyer (bisiklet pompasını 87.14 sanıp sona koyar → HAYIR, 84.14) ve Gümrükçü Baba (“makineyse önce 84'e bak”).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), sıralama zinciri (4 eşya kartı) + dört yanlış sıralamanın ✗ gerekçesi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-17-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-17.mp4
```
