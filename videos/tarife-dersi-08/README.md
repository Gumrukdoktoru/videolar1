# Tarife Dersi 8 — Tuz ve deniz suyu, cetvel notları ve bağlayıcı kaynaklar (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Aşağıdakilerden hangisi 25.01 pozisyonunda sınıflandırılmaz?
**A) Gazlı doğal maden suyu** · B) Deniz suyu · C) Saf sodyum klorür · D) Denatüre tuz · E) Topaklaşmayı önleyici madde katılmış sofra tuzu
**Doğru cevap: A.** Maden suları ve gazlı sular 22.01’dedir. 25.01 pozisyon metni sofra tuzu ve denatüre tuz dahil tuzu, saf sodyum klorürü ve deniz suyunu adıyla sayar; topaklaşmayı önleyici madde katılmasına da izin verir. Deniz suyu Fasıl 22 Not 1(b) ile Fasıl 22 dışındadır; damıtılmış su ise Not 1(c) ile 28.53’tedir. (25.01 pozisyon metni · Fasıl 22 Not 1)

**Soru 2.** Türk Gümrük Tarife Cetvelinde yer alan aşağıdaki unsurlardan hangisi Armonize Sistem Nomanklatüründe yer almaz?
A) Bölüm notları · B) Fasıl notları · **C) Ek notlar** · D) Alt pozisyon notları · E) Tarifenin yorumuna ilişkin genel kurallar
**Doğru cevap: C.** Bölüm, fasıl ve alt pozisyon notları ile genel yorum kuralları Armonize Sistemin parçasıdır ve bütün üye ülkelerde ortaktır. Ek notlar ise Kombine Nomanklatüre ve ulusal tarifeye aittir; 6 haneden sonraki ayrıntıyı yorumlar. (Armonize Sistem Nomanklatürü · Kombine Nomanklatür)

**Soru 3.** Türkiye’de tarife sınıflandırması yapılırken aşağıdakilerden hangisi bağlayıcı bir kaynak değildir?
A) Türk Gümrük Tarife Cetveli · B) Tarifenin yorumuna ilişkin genel kurallar · C) Gümrük Genel Tebliği ile yayımlanan Gümrük Tarife Cetveli İzahnamesi · D) Gümrük Genel Tebliği ile yayımlanan tarife sınıflandırma kararları · **E) AB Bağlayıcı Tarife Bilgisi veri tabanındaki kararlar**
**Doğru cevap: E.** Gümrükler Genel Müdürlüğünün 2020 tarihli yazısına göre AB BTB’leri ülkemiz mevzuatında yalnızca yardımcı bir referans kaynaktır; resmî bağlayıcılığı yoktur. Tarife cetveli ve genel yorum kuralları cetvelin kendisidir; izahname ve sınıflandırma kararları Gümrük Genel Tebliği olarak yayımlanır. (GGM yazısı, 23.03.2020 · Gümrük Genel Tebliğleri)

Cevap dağılımı: A · C · E.

## Video

- **Süre:** 5 dk 01 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 8 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Cano (deniz suyu da sudur diye Fasıl 22 → HAYIR, 25.01) · Stajyer (alt pozisyonu ulusal açılım sanır → HAYIR, 6 haneli alt pozisyon Armonize Sistemin) ve Gümrükçü Baba (“notun hangi haneyi yorumladığına bak”) · Yardımcı (AB BTB’sine dayanarak sınıflandırır → HAYIR, yardımcı referans).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** yanlış şıkkın üstü çizilip DOĞRUSU kartı + diğer dört şıkkın ✓ ve dayanakları, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-08-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-08.mp4
```
