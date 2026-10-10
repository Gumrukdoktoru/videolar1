# Tarife Dersi 6 — Yasal dayanak, kod seviyeleri ve meyve faslı (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Gümrük Giriş Tarife Cetveli ile ilgili aşağıdaki ifadelerden hangisi doğrudur?
A) Cetvel Brüksel Nomanklatürü esas alınarak düzenlenmiştir; pozisyonlarını değiştirmeye Cumhurbaşkanı yetkilidir. · B) Cetvel Armonize Sistem Nomanklatürü esas alınarak düzenlenmiştir; pozisyonlarını değiştirmeye Ticaret Bakanlığı yetkilidir. · C) Cetvel Dünya Gümrük Örgütü tarafından yayımlanır; ülkeler pozisyonlarını değiştiremez. · **D) Cetvel Armonize Sistem Nomanklatürü esas alınarak düzenlenmiştir; pozisyonlarını ve notlarını değiştirmeye Cumhurbaşkanı yetkilidir.** · E) Cetvelin ilk altı hanesi ulusal düzeyde belirlenir; Armonize Sistem yalnızca fasılları belirler.
**Doğru cevap: D.** Kanuna göre cetvel Armonize Sistem Nomanklatürü esas alınarak düzenlenmiştir; pozisyon, not ve genel kuralları genişletmeye, açmaya ve değiştirmeye Cumhurbaşkanı yetkilidir. A: Brüksel Nomanklatürü eski sistem; B: yetki bakanlıkta değil; C: cetvel ulusaldır, DGÖ yayımlamaz; E: ilk 6 hane bütün AS ülkelerinde ortaktır. (Gümrük Giriş Tarife Cetveli Hakkında Kanun)

**Soru 2.** Aşağıdaki kodlardan hangisi bir Armonize Sistem alt pozisyonudur?
A) 85.01 · **B) 8501.10** · C) 85 · D) 8501.10.10.00.00 · E) 8501.10.10
**Doğru cevap: B.** İlk 2 hane fasıl, 4 hane pozisyon, 6 hane Armonize Sistem alt pozisyonu (bütün AS ülkelerinde ortak); 8 hane AB Kombine Nomanklatürü, 12 hane GTİP. (TGTC kod yapısı)

**Soru 3.** Aşağıdakilerden hangisi tarife cetvelinin 8. faslında sınıflandırılmaz?
**A) Susam tohumu** · B) Kabuğu soyulmuş badem · C) Taze avokado · D) Kurutulmuş kayısı · E) Kaju cevizi
**Doğru cevap: A.** Fasıl 8 yenilen meyveleri ve sert kabuklu meyveleri kapsar (badem 08.02, avokado 08.04, kaju 08.01, kurutulmuş kayısı 08.13). Susam yağlı tohumdur: Fasıl 12, 12.07. Yer fıstığı 12.02; kavrulmuşsa Fasıl 20. (Fasıl 12 notu · 12.07)

Cevap dağılımı: D · B · A.

## Video

- **Süre:** 5 dk 19 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 6 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Cano (cetveli bakanlık yayımlıyor diye B → HAYIR) · Stajyer (en uzun kod en ayrıntılı diye 12 hane → HAYIR) ve Gümrükçü Baba (“hangi sistem geçiyorsa o sistemin hanesini say”) · Yardımcı (çerez gibi yenir diye susamı Fasıl 8'e koyar → HAYIR).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** doğru ifade kartı + dört yanlış ifadenin ✗ ve düzeltmeleri, 2 → 4 → 6 → 8 → 12 hane kod merdiveni (doğru basamak yeşil), yanlış şıkkın üstü çizilip DOĞRUSU kartı + diğer dört ürünün pozisyonları, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-06-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-06.mp4
```
