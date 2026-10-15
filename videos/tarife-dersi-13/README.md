# Tarife Dersi 13 — Denizaltı periskobu, tansiyon aleti ve Türk müziği çalgıları (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Bir denizaltında kullanılmak üzere, denizaltıdan ayrı olarak ithal edilen periskop hangi tarife pozisyonunda sınıflandırılır?
A) 89.06 · B) 90.05 · **C) 90.13** · D) 90.15 · E) 93.05
**Doğru cevap: C.** Periskop optik bir alettir; ilk akla gelen 90.05 (dürbünler, teleskoplar) olsa da Fasıl 90 Not 4, denizaltı ve tanklar için periskopik teleskopları 90.05'in dışında bırakır. 9013.10 silahlar için teleskopik dürbünleri ve periskopları adıyla sayar. Denizaltının kendisi 89.06'dadır; Fasıl 90 veya Bölüm XVI makinelerine ait teleskoplar da 90.13'e gider. (Fasıl 90 Not 4 · 90.13)

**Soru 2.** Kola sarılan bir manşonla kan basıncını ölçen dijital tansiyon aleti hangi tarife pozisyonunda sınıflandırılır?
A) 85.43 · **B) 90.18** · C) 90.25 · D) 90.26 · E) 90.31
**Doğru cevap: B.** Tansiyon aleti bir basınç ölçer gibi görünse de tıpta teşhis için kullanılır. 90.18 izahnamesi kan basıncını ölçen sfigmomanometreleri ve tansiyometreleri stetoskoplarla birlikte adıyla sayar. 90.26 sıvı ve gazların akış, seviye ve basıncını ölçen cihazlar içindir; klinik termometre 90.25'tedir; elektronik olması 85.43'e götürmez. (90.18 izahnamesi · 90.26)

**Soru 3.** Aşağıdaki çalgılardan hangisi tarife cetvelinde diğerlerinden farklı bir pozisyonda sınıflandırılır?
A) Bağlama · B) Ud · C) Kanun · D) Kemençe · **E) Darbuka**
**Doğru cevap: E.** Bağlama, ud, kanun ve kemençe telli çalgılardır; mızrapla, parmakla ya da yayla çalınsalar da 92.02'de gitar, keman ve arp gibi diğer telli çalgılarla yer alırlar. Darbuka gerdirilmiş deriye elle vurularak çalınır; 92.06 izahnamesi darbukaları ve tefleri adıyla sayar. Ses kutusu olmayan, sesi elektrikle yükseltilen elektro gitar 92.07'dedir. (92.02 · 92.06 izahnamesi)

Cevap dağılımı: C · B · E.

## Video

- **Süre:** 5 dk 03 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 13 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Yardımcı (periskop da teleskoptur diye 90.05 → HAYIR, 90.13) · Stajyer (basınç ölçüyor diye 90.26 → HAYIR, 90.18) ve Gümrükçü Baba (“kimin basıncını ölçüyor?”) · Cano (kemençe yayla çalınıyor diye telli saymaz → HAYIR, 92.02).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** ürün kartı + 3 adımlı gerekçe + 5 aday şeridi (iki soruda), yanlış ifade + DOĞRUSU kartı + dört doğru şık, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, 3 soruluk cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-13-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-13.mp4
```
