---
mode: autonomous
message: "Kültür fonu kıymete girmez, vergiye girer; cezaya ve uzlaşmaya girmez → 46.080 TL (D)."
canvas: 1920x1080
duration: 270.374s (sesten türetildi — timing.json)
---

# Vergi hesaplama dersi 2 — sahne planı

Sahne HTML'leri `tools/build.py` ile üretilir; elle düzenleme yerine `tools/scenes_*.py` düzenlenip yeniden derlenir.

## s01 · Giriş
- 0.0s → 18.3s · src: compositions/s01.html
- Logo sting → VERGİ HESAPLAMA / DERS #2 → sallanan terazi + 'Kültür fonu & uzlaşma', TUZAK etiketi, 4 konu çipi, 'Hangi tutar uzlaşmaya girer?'. Maskot: normal.

## s02 · Soru
- 18.3s → 56.9s · src: compositions/s02.html
- Veriler: K firması (40.000 $, KÜLTÜR FONU ÖDENMEMİŞ damgası), iki yol (kurum bildirimi / ek tahakkuk + ceza), oranlar GV %0 · ÖTV %10 · KDV %20 · KF %3 · kur 30 TL, Cano (K firması) balonu, İSTENEN şeridi. Maskot: soru.

## s03 · Şıklar
- 56.9s → 80.2s · src: compositions/s03.html
- Şıklar A–E (11.520 · 36.000 · 43.200 · 46.080 · 82.080 TL); 'Videoyu durdur' kartı + 5 sn geri sayım. Maskot: soru.

## s04 · Anahtar kural
- 80.2s → 105.0s · src: compositions/s04.html
- ÖNEMLİ rozeti; KÜLTÜR FONU jetonundan dört ok: gümrük kıymeti ✗ · ÖTV+KDV matrahı ✓ · uzlaşma ✗ · 3 kat ceza ✗; özellik 1 ve 2 etiketleri. Maskot: dikkat.

## s05 · Adım 1
- 105.0s → 125.4s · src: compositions/s05.html
- Adım 1: 40.000 $ × 30 = 1.200.000 TL (sayaç), GV %0 → 0 TL, eksik KF 1.200.000 × %3 = 36.000 TL, 'ilgili kuruma bildirilir · UZLAŞMA DIŞI'; defterde üstü çizili KF satırı. Maskot: normal.

## s06 · Adım 2
- 125.4s → 153.2s · src: compositions/s06.html
- Adım 2: DİKKAT rozeti; KF → ÖTV & KDV matrahına girer; 36.000 × %10 = 3.600 · 36.000 + 3.600 = 39.600 · 39.600 × %20 = 7.920 → eksik vergi 11.520 TL; defter. Maskot: dikkat.

## s07 · Adım 3
- 153.2s → 166.8s · src: compositions/s07.html
- Adım 3: GK md. 234/1 özet şeridi (3 katı para cezası · kültür fonuna uygulanmaz), ×3 rozeti, hesap makinesi 11.520 × 3 = 34.560; defter. Maskot: uyarı.

## s08 · Sonuç
- 166.8s → 179.9s · src: compositions/s08.html
- Uzlaşma makbuzu: eksik vergi 11.520 + ceza 34.560, kültür fonu 36.000 üstü çizili; toplam 46.080 TL; D şıkkı yeşil, CEVAP: D damgası + konfeti. Maskot: cevap.

## s09 · Tuzaklar
- 179.9s → 206.6s · src: compositions/s09.html
- TUZAK rozeti; A/B/C/E çeldirici kartları (hatanın nedeni + hesap); Gümrükçü Baba 'Doğrusu D: 46.080 TL!'. Maskot: tuzak.

## s10 · Uyarı
- 206.6s → 228.5s · src: compositions/s10.html
- UYARI rozeti; Gümrük Uzlaşma Yön. md. 6 listesi (matraha girip gümrükçe tahsil edilmeyen yükler · tahsilat aşaması · kaçakçılık); Cano 'Kültür fonunu da uzlaşalım mı?' → HAYIR!; uzlaşmaya girebilen tutar şeridi. Maskot: uyarı.

## s11 · Koçun notu
- 228.5s → 249.8s · src: compositions/s11.html
- İPUCU rozeti; 'idare tespit ederse 34.560' ↔ 'firma önce bildirirse (GK 234/3) %10 → 3.456 TL'; kültür fonu formül kartı (kıymete ✗ · vergiye ✓ · cezaya ✗ · uzlaşmaya ✗). Maskot: normal → dikkat.

## s12 · Kapanış
- 249.8s → 270.4s · src: compositions/s12.html
- Özet: eksik vergi 11.520 + ceza 34.560 → D 46.080 TL, 'kültür fonu 36.000 TL uzlaşma dışı' notu, abone/paylaş, logo + veda. Maskot: normal → cevap.
