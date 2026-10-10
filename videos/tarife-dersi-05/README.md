# Tarife Dersi 5 — Mineral mumlar, telsiz kumanda, deri eşya (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Petrolden elde edilen, mikrokristal bünyeli petrol mumu hangi tarife pozisyonunda sınıflandırılır?
A) 34.04 · **B) 27.12** · C) 15.21 · D) 27.10 · E) 33.04
**Doğru cevap: B.** 27.12 vazelin, parafin, mikrokristal bünyeli petrol mumu ve diğer mineral mumları adıyla sayar (renklendirilmiş olsun olmasın). 34.04 suni ve müstahzar mumlar içindir; cilt bakımı için perakende vazelin 33.04. (27.12 pozisyon metni)

**Soru 2.** Radyo frekansıyla çalışan ve bir kule vincinin hareketlerini uzaktan kontrol etmeye yarayan telsiz kumanda cihazı hangi tarife pozisyonunda sınıflandırılır?
A) 85.43 · B) 84.31 · C) 85.37 · D) 85.17 · **E) 85.26**
**Doğru cevap: E.** 85.26 uzaktan kumanda etmeye mahsus telsiz kontrol cihazlarını kapsar (8526.92). Bölüm XVI Not 2(a) gereği kendi pozisyonu olan aksam, ait olduğu makineye bakılmadan kendi pozisyonunda sınıflandırılır. TV kızılötesi kumandaları 85.43. (85.26, Bölüm XVI Not 2(a))

**Soru 3.** Aşağıdakilerden hangisi 42.02 pozisyonunda sınıflandırılmaz?
A) Dış yüzü dokumaya elverişli maddeden sırt çantası · B) Alüminyumdan yapılmış, tekerlekli valiz · **C) Tabii deriden bel kemeri** · D) Vulkanize liften evrak çantası · E) Plastik madde yaprağından tuvalet çantası
**Doğru cevap: C.** 42.02'nin birinci grubu (bavul, valiz, evrak/okul çantası, gözlük kılıfı…) her maddeden olabilir; ikinci grubu (seyahat, sırt, tuvalet çantaları, cüzdan, mücevher kutusu…) yalnızca deri, plastik yaprak, tekstil, vulkanize lif veya kartondan. Deri bel kemeri giyim aksesuarıdır: 42.03 (4203.30). Ahşap mücevher kutusu 44.20. (42.02 pozisyon metni, 4203.30)

Cevap dağılımı: B · E · C.

## Video

- **Süre:** 4 dk 54 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 5 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Stajyer (mum → 34.04 → HAYIR) · Yardımcı (vinç aksamı 84.31 → HAYIR) ve Gümrükçü Baba (“TV'nin kızılötesi kumandası 85.43”) · Cano (deriyse 42.02 → HAYIR).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** sınıflandırma yolu (ürün kartı → 3 adım → pozisyon), beş aday pozisyonun ✓/✗ şeridi, 'hangisi sınıflandırılmaz' çözümünde üstü çizilen şık + DOĞRUSU kartı + diğer şıkların grup etiketleri, tuzak karşılaştırma kartları (≠), DİKKAT kartları (perakende vazelin 33.04, TV kızılötesi kumanda 85.43, ahşap mücevher kutusu 44.20), koçun notu zihin haritası, cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-05-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-05.mp4
```
