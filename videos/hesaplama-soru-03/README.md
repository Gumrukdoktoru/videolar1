# Vergi Hesaplama Dersi 3 — Lisans ücreti, zamanaşımı, ceza ve peşin ödeme (Gümrük Koçu ders videosu)

Sonradan kontrolde ortaya çıkan, beyan edilmemiş lisans ücretleri üzerine kurgulanmış **özgün** bir örnek soru ve anlatımlı çözümü.
HyperFrames ile üretildi.

**Soru:** Haziran 2024'teki sonradan kontrolde M firmasının, ithal eşyasıyla ilgili ve satış koşulu olarak ödediği lisans ücretlerini
beyan etmediği anlaşılıyor. Ödeme ve ithalatlar her yıl mart ayında: 2021 → 8.000 $ (kur 8), 2022 → 15.000 $ (kur 15),
2023 → 20.000 $ (kur 20). GV %8, KDV %20. Firma ceza kararının tebliğinden itibaren 15 gün içinde vergi ve cezaları peşin ödüyor.
Ödenecek toplam tutar?
**Cevap: C — 601.250 TL.**
- Zamanaşımı (GK 197/2): 2021 ithalatının 3 yıllık süresi Mart 2024'te doldu → yalnız 2022 ve 2023.
- Kıymet farkı: 225.000 + 400.000 = 625.000 TL · GV %8 = 50.000 · KDV (625.000 + 50.000) × %20 = 135.000 → eksik vergi 185.000 TL.
- Ceza (GK 234/1-b): 185.000 × 3 = 555.000 · peşin ödeme (Kabahatler K. 17/6) ¾ → 416.250 TL.
- Toplam: 185.000 + 416.250 = 601.250 TL.

Çeldiriciler: A 185.000 (ceza unutuldu), B 568.750 (GV, KDV matrahına eklenmedi), D 662.818 (zamanaşımı unutuldu, 2021 katıldı),
E 740.000 (peşin ödeme indirimi unutuldu).

- **Süre:** 4 dk 46 sn · 1920×1080 · 30 fps
- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış "Vergi Hesaplama Dersi 3 — Gümrük Koçu")
- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş
  (soru · dikkat · uyarı · cevap · tuzak).
- **Konuklar:** Cano — M firması temsilcisi ("15 günde peşin ödeyelim!", "Vergiye de indirim var mı?" → HAYIR!) ·
  Gümrükçü Baba (tuzak sahnesinde doğru cevabı söyler)
- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)
- **Ekstralar:** kum saati animasyonu, 3 yıllık süre çubuklu **zamanaşımı çizelgesi** (kontrol çizgisi + "SÜRE DOLDU" damgası),
  sayaçlı hesaplar, çözüm defteri, hesap makinesi (×3), **¼'ü kesilen peşin ödeme çubuğu**, ödeme makbuzu, dört çeldirici analizi,
  GK 27/1-c iki şart kartı, "zamanaşımı nereden başlar?" seçenekleri, 5 adımlı formül zinciri, 5 sn geri sayım, rakamlı alt yazı, YouTube bölümleri

## Dosyalar

| Dosya | Ne işe yarar |
| --- | --- |
| `renders/hesaplama-soru-03-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |
| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |
| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |
| `narration/script.json` | Seslendirme metni (sayılar TTS için yazıyla) |
| `tools/` | `build_timing.py` (zamanlama + alt yazı), `scenes_a/b.py` (sahneler), `build.py` (kompozisyon) |

## Yeniden üretmek

```bash
python3 tools/build_timing.py
python3 tools/build.py
npx hyperframes check
npx hyperframes render -o renders/hesaplama-soru-03.mp4
```
