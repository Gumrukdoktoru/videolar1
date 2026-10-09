# Tarife Dersi 1 — Tarife cetvelinin sistematiği (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Türk Gümrük Tarife Cetvelinde adi metaller ve adi metallerden eşya hangi bölüm ve fasıllarda yer almaktadır?
A) On dördüncü bölüm, 71. fasıl · B) On altıncı bölüm, 84-85. fasıllar · **C) On beşinci bölüm, 72-83. fasıllar** ·
D) On üçüncü bölüm, 68-70. fasıllar · E) On yedinci bölüm, 86-89. fasıllar
**Doğru cevap: C.** Adi metaller XV. bölümde, 72–83. fasıllardadır; 77. fasıl Armonize Sistemde ileride kullanılmak üzere
saklı tutulur. Tuzaklar: 84–85 makinelerdir (işlevine göre sınıflandırılır); 71. fasıl kıymetli metallerdir.
(Tarife cetveli, Bölüm XV)

**Soru 2.** Armonize Sistem ve tarife cetvelinin sınıflandırma mantığı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?
A) AS, merkezi Brüksel'de bulunan Dünya Gümrük Örgütü bünyesinde hazırlanmıştır. · B) Kodun ilk altı hanesi, sisteme taraf
tüm ülkelerde aynı şekilde uygulanır. · C) Sınıflandırma genel olarak canlıdan cansıza, ham maddeden mamul eşyaya doğru bir
sıra izler. · D) 84-96. fasıllardaki eşya, genel olarak işlevine göre sınıflandırılır. · **E) İlk bakışta iki pozisyona
girebilen eşya, vergi oranı yüksek olan pozisyonda sınıflandırılır.**
**Doğru cevap: E.** Tarifede vergi oranına göre sınıflandırma yoktur. İki pozisyona girebilen eşyada 3 numaralı genel kural
sırayla uygulanır: (a) en özel tanım, (b) esas nitelik, (c) numara sırasına göre en son pozisyon. Gizli tuzak: AS'yi Dünya
Ticaret Örgütü değil, Dünya Gümrük Örgütü hazırlar. Ek bilgi: 12 haneli kodda 1–6 AS, 7–8 AB Kombine Nomanklatürü,
9–10 milli alt açılım, 11–12 istatistik. (Tarifenin yorumuna ilişkin genel kurallar, Kural 3)

**Soru 3.** Türk Gümrük Tarife Cetvelinde kullanılan ölçü birimi kısaltmaları ile anlamlarına ilişkin aşağıdaki
eşleştirmelerden hangisi yanlıştır?
**A) ct/l – Karat** · B) p/st – Adet · C) ce/el – Hücre adedi · D) p/a – Çift · E) TJ – Terajul (brüt kalori değeri)
**Doğru cevap: A.** Karatın kısaltması c/k'dir; ct/l ton başına taşıma kapasitesini gösterir. p/a çift, p/st adettir.
1 karat = 0,2 gram. (Tarife cetveli, kısaltmalar ve semboller)

Cevap dağılımı: C · E · A.

## Video

- **Süre:** 5 dk 43 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 1 — Gümrük Koçu").
  Kısaltmalar TTS için harf harf yazıldı ("ce te bölü le"); okunuş ElevenLabs Scribe ile doğrulandı, alt yazıda kısaltma
  olarak görünür (ct/l, c/k, p/a, p/st, ce/el, TJ, DGÖ, DTÖ).
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Stajyer (p/a'yı adet sanar → HAYIR) · Yardımcı (metalden yapılmış diye makineleri seçer → YANLIŞ) ·
  Cano ("Dünya Ticaret Örgütü!" → HAYIR) · Gümrükçü Baba ("DGÖ gümrük, DTÖ ticaret!").
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** 21 bölüm şeridi ve XV. bölümün 72–83 fasıl ızgarası (77 SAKLI), madde/işlev ayrım çubuğu
  (çelik vida 73.18 · torna tezgâhı 84.58), kıymetli ≠ adi metal kartları, genel kural 3 basamakları, DGÖ/DTÖ kartları,
  12 haneli kod çözümlemesi (8501.10.10.00.00), ölçü birimi kartları, benzer kısaltma çiftleri, koçun notu zihin haritası,
  cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz (ipucu vermemek için).

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-01-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla, kısaltmalar yazılı) |
| `narration/script.json` | Seslendirme metni |
| `tools/` | `build_timing.py` (zamanlama + alt yazı), `scenes_a/b.py` (sahneler), `build.py` (kompozisyon) |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-01.mp4
```
