---
mode: autonomous
message: "GV taşıyıcı ortamdan, KDV yazılım dahil toplamdan: 1 + 181,98 = 182,98 $ (A)."
canvas: 1920x1080
duration: 235.53s (sesten türetildi — timing.json)
---

# Çıkmış hesaplama sorusu 1 — sahne planı

Sahne HTML'leri `tools/build.py` ile üretilir; elle düzenleme yerine `tools/scenes_*.py` düzenlenip yeniden derlenir.

## s01 · Giriş
- 0.0s → 16.9s · src: compositions/s01.html
- Logo sting → VERGİ HESAPLAMA / SORU #1 → dönen CD + kod rozeti, 'GV = ? KDV = ?' → kâğıt-kalem çipi.

## s02 · Soru
- 16.9s → 46.5s · src: compositions/s02.html
- Veriler: ithalatçı ve eşya kartları, fatura (CD 10 $ / yazılım 1.000 $ vurgulu, '2 AYRI KALEM' etiketi), GV %10 · KDV %18 karoları, İSTENEN şeridi.

## s03 · Şıklar
- 46.5s → 74.8s · src: compositions/s03.html
- Şıklar A–E sırayla kayar; 'Videoyu durdur' kartı + 5 sn geri sayım halkası.

## s04 · Anahtar kural
- 74.8s → 100.5s · src: compositions/s04.html
- ÖNEMLİ rozeti, GY md. 54 özet kartı (vurgu çizgisi), CD → GÜMRÜK KIYMETİ ✓ / Yazılım → GİRMEZ ✗ okları, DİKKAT: ayrı gösterilme şartı.

## s05 · Adım 1
- 100.5s → 111.2s · src: compositions/s05.html
- Adım şeridi (1/4), GV matrahı 10 $, yazılımın üstü çizilir, 10 × %10 = 1 $ sayacı, çözüm defterine 1. satır.

## s06 · Adım 2
- 111.2s → 129.3s · src: compositions/s06.html
- DİKKAT rozeti, 'Yazılım → gümrük kıymeti ✗ / KDV matrahı ✓', alt alta toplama 10 + 1 + 1.000 = 1.011 $, deftere 2. satır.

## s07 · Adım 3
- 129.3s → 137.7s · src: compositions/s07.html
- Hesap makinesi: tuş basımları, 1.011 × 0,18 = 181,98, deftere 3. satır.

## s08 · Sonuç
- 137.7s → 151.7s · src: compositions/s08.html
- Vergi makbuzu (toplam sayacı 182,98), şıklarda A yeşil ✓ diğerleri sönük, 'CEVAP: A' damgası + konfeti.

## s09 · Tuzaklar
- 151.7s → 174.6s · src: compositions/s09.html
- TUZAK rozeti; B (GV unutuldu) ve E (yazılım GV'ye katıldı, GV KDV'ye eklenmedi) kartları + 'Doğrusu' satırları; Gümrükçü Baba balonu.

## s10 · Uyarı
- 174.6s → 198.7s · src: compositions/s10.html
- UYARI rozeti; 'taşıyıcı ortam' ve 'veri/komut' kapsam dışı listeleri; CD + film → film bedeli dahil (soru 70 örneği).

## s11 · Koçun notu
- 198.7s → 215.6s · src: compositions/s11.html
- İPUCU · Koçun notu: ihracat yönü (soru 69) = 10 $; formül kartı GV ← CD, KDV ← CD + GV + yazılım.

## s12 · Kapanış
- 215.6s → 235.5s · src: compositions/s12.html
- Özet satırları, A · 182,98 USD rozeti, ABONE OL / PAYLAŞ, logo kapanışı.

