---
mode: autonomous
message: "GV taşıyıcıdan, KDV yazılım dahil toplamdan: 5 + 511 = 516 $ (C)."
canvas: 1920x1080
duration: 236.68s (sesten türetildi — timing.json)
---

# Vergi hesaplama dersi 1 — sahne planı

Sahne HTML'leri `tools/build.py` ile üretilir; elle düzenleme yerine `tools/scenes_*.py` düzenlenip yeniden derlenir.

## s01 · Giriş
- 0.0s → 17.6s · src: compositions/s01.html
- Logo sting → VERGİ HESAPLAMA / DERS #1 → dönen DVD + kod rozeti, 'GV = ? KDV = ?' → kâğıt-kalem çipi. Maskot: normal.

## s02 · Soru
- 17.6s → 48.5s · src: compositions/s02.html
- Veriler: (B) şirketi ve eşya kartları, fatura (DVD 50 $ / yazılım 2.500 $, '2 AYRI KALEM'), GV %10 · KDV %20, İSTENEN şeridi. Maskot: soru (düşünen).

## s03 · Şıklar
- 48.5s → 70.7s · src: compositions/s03.html
- Şıklar A–E (16 · 511 · 516 · 765 · 816); 'Videoyu durdur' kartı + 5 sn geri sayım. Maskot: soru.

## s04 · Anahtar kural
- 70.7s → 96.9s · src: compositions/s04.html
- ÖNEMLİ rozeti, GY md. 54 özet kartı, DVD → GÜMRÜK KIYMETİ 50 $ ✓ / Yazılım → GİRMEZ ✗, DİKKAT: ayrı gösterilme şartı. Maskot: dikkat.

## s05 · Adım 1
- 96.9s → 107.8s · src: compositions/s05.html
- Adım 1: GV matrahı 50 $, yazılımın üstü çizilir, 50 × %10 = 5 $, çözüm defterine 1. satır. Maskot: normal.

## s06 · Adım 2
- 107.8s → 127.2s · src: compositions/s06.html
- DİKKAT: yazılım → gümrük kıymeti ✗ / KDV matrahı ✓; 50 + 5 + 2.500 = 2.555 $; deftere 2. satır. Maskot: dikkat.

## s07 · Adım 3
- 127.2s → 134.9s · src: compositions/s07.html
- Hesap makinesi: 2.555 × 0,20 = 511; deftere 3. satır. Maskot: normal.

## s08 · Sonuç
- 134.9s → 146.5s · src: compositions/s08.html
- Vergi makbuzu (toplam 516), şıklarda C yeşil ✓, 'CEVAP: C' damgası + konfeti. Maskot: cevap (başparmak).

## s09 · Tuzaklar
- 146.5s → 175.9s · src: compositions/s09.html
- TUZAK: dört kart — A 16 (yazılım KDV'den de çıkarıldı), B 511 (GV unutuldu), D 765, E 816 (yazılım GV'ye katıldı); Gümrükçü Baba doğrusunu söyler. Maskot: tuzak (şaşkın).

## s10 · Uyarı
- 175.9s → 200.7s · src: compositions/s10.html
- UYARI: 'taşıyıcı ortam' ve 'veri/komut' kapsam dışı listeleri; DVD + film → film bedeli dahil (40 $ + 3.000 $ = 3.040 $). Maskot: uyarı (dur eli).

## s11 · Koçun notu
- 200.7s → 217.7s · src: compositions/s11.html
- İPUCU · Koçun notu: ihracatta da gümrük kıymeti = taşıyıcı; formül kartı GV ← taşıyıcı, KDV ← taşıyıcı + GV + yazılım. Maskot: normal → dikkat.

## s12 · Kapanış
- 217.7s → 236.7s · src: compositions/s12.html
- Özet satırları, C · 516 USD rozeti, ABONE OL / PAYLAŞ, logo kapanışı. Maskot: cevap.

