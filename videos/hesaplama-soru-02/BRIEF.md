---
workflow: general-video
flow: automation
storyboard: no
message: "Kültür fonu kıymete girmez, vergiye (ÖTV/KDV) girer; cezaya ve uzlaşmaya girmez: 11.520 + 34.560 = 46.080 TL (D)."
destination: youtube
aspect: 1920x1080
language: tr
audience: gümrük müşavirliği / muavinliği sınavına hazırlananlar, gümrük öğrencileri (ders kanalı)
length: ~4,5 dk
angle: örnek soru çözümü / ders
---

## Intent

Gümrük Koçu ders kanalı için vergi hesaplama dersi #2: kültür fonu, eksik vergi, para cezası ve uzlaşma konusunda
**özgün**, sayıları ve kurgusu bize ait bir örnek soru ve anlatımlı çözümü. Kullanıcı notu: sınav sorularının aynısı
paylaşılmaz; tutarlar değiştirilerek özgün soru kurulur ve videonun hiçbir yerinde sorunun bir sınavdan alındığı ima
edilmez. "Anlatımlı, görselli, şekilli şemalı ve yazılı"; oklar ve ÖNEMLİ / DİKKAT / UYARI / TUZAK rozetleri; motion efektler.

## Assets

- assets/img/koc-cutout.png + koc-soru|dikkat|cevap|uyari|tuzak.png — Gümrük Koçu ve tepki görselleri (ders 1'den).
- assets/img/cano-cut.png — Cano (kullanıcının görseli; arka plan yerelde kaldırıldı) → K firması temsilcisi.
- assets/img/baba-crop.png — Gümrükçü Baba; tuzak sahnesinde doğru cevabı söyler.
- assets/img/logo-crop.png — Ufuk Çetintaş / Gümrük Eğitim Koçu logosu.

## Customizations

- Seslendirme: ElevenLabs **eleven_v4**, ses **Cem** (voice_id D1xRw7f8ZHedI7xJgfvz), akış h9VR5pyYkuDDtglwVmT1.
- Maskot titremez/kıpırdamaz: sabit görsel, durumlara göre tepki görseline yumuşak geçiş + küçük tepki rozeti.
- Kültür fonu yönlendirme şeması, sayaçlı hesaplar, çözüm defteri, hesap makinesi, uzlaşma makbuzu, çeldirici analizi,
  Uzlaşma Yön. md. 6 kartı, "önce sen bildir" karşılaştırması, formül kartı.

## Notes

- Dayanaklar (repo notlarından doğrulandı): GK md. 234/1 (vergi farkının üç katı), 234/3 (idare tespitinden önce
  bildirimde cezalar %10 nispetinde), Gümrük Uzlaşma Yönetmeliği md. 6/1, 6/3, 6/4.
- Sayılar seslendirmede yazıyla (TTS güvenliği); alt yazıda rakama çevrilir.
