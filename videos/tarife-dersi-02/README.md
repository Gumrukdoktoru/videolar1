# Tarife Dersi 2 — Genel kurallar ve ilk sınıflandırmalar (Gümrük Koçu ders videosu)

Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve
çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.

## Sorular

**Soru 1.** Tarifenin yorumuna ilişkin genel kurallarla ilgili aşağıdaki ifadelerden hangisi yanlıştır?
A) Eksik veya bitirilmemiş eşya, sunulduğunda tamamlanmış eşyanın esas niteliğine sahipse tamamlanmış eşya gibi sınıflandırılır. · **B) Bölüm, fasıl ve tali fasıl başlıkları, eşyanın tarifedeki yerinin saptanmasında yasal dayanak oluşturur.** · C) Belli bir eşyaya göre yapılmış, uzun süreli kullanıma uygun mahfazalar eşyayla birlikte sunulduğunda onunla birlikte sınıflandırılır. · D) İlk üç kurala göre sınıflandırılamayan eşya, en çok benzediği eşyanın pozisyonunda sınıflandırılır. · E) Alt pozisyonlarda yalnızca aynı seviyedeki alt pozisyonlar karşılaştırılır.
**Doğru cevap: B.** Başlıklar sadece gösterici niteliktedir; sınıflandırma pozisyon metinlerine ve bölüm/fasıl notlarına göre yapılır. A: GYK 2(a), C: GYK 5(a), D: GYK 4, E: GYK 6. (GYK 1)

**Soru 2.** Paslanmaz çelikten mamul, iç kovası plastik olan, pedallı mutfak çöp kovası hangi tarife pozisyonunda sınıflandırılır?
A) 39.24 · B) 73.10 · C) 73.26 · **D) 73.23** · E) 94.03
**Doğru cevap: D.** Esas nitelik paslanmaz çelikten; plastik iç kova aksesuar. 73.23 demir/çelikten sofra, mutfak ve ev eşyasını kapsar; izahname çöp kutularını sayar. Atık kâğıt sepetleri ise 73.25/73.26. (73.23 izahnamesi)

**Soru 3.** Mektup ve kolilere posta pulu yerine geçen ücret damgasını basan, hesaplama tertibatı bulunan makineler hangi tarife pozisyonunda sınıflandırılır?
A) 84.43 · B) 84.71 · C) 84.72 · D) 90.29 · **E) 84.70**
**Doğru cevap: E.** 84.70 pozisyon metni posta pulu yerine damga basan makineleri adıyla sayar; ortak özellik toplama tertibatıdır (yazar kasalar hariç). Sadece sayan sayaçlar 90.29. (84.70 pozisyon metni)

Cevap dağılımı: B · D · E.

## Video

- **Süre:** 5 dk 21 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Tarife Dersi 2 — Gümrük Koçu")
- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).
- **Ekip:** Stajyer (bağırsağı başlığa bakıp Fasıl 2'ye koyar → HAYIR) · Cano (plastik iç kova → 39.24 → HAYIR) · Yardımcı (damga basıyor → 84.43) ve Gümrükçü Baba (“metin adıyla sayıyorsa en özel tanım odur”).
- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ
- **Görseller:** yanlış ifade üstü çizilip DOĞRUSU kartı + diğer dört ifadenin kural etiketleri (GYK 2(a), 5(a), 4, 6), sınıflandırma yolu (ürün kartı → 3 adım → pozisyon), beş aday pozisyonun ✓/✗ şeridi, tuzak karşılaştırma kartları (≠), koçun notu zihin haritası, cevap anahtarı; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/tarife-dersi-02-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |
| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |
| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
cd tools && python3 build.py && python3 docs.py && cd ..
npx hyperframes check
npx hyperframes render -o renders/tarife-dersi-02.mp4
```
