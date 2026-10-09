---
workflow: general-video
flow: automation
storyboard: no
message: "DVD'deki yazılımda gümrük vergisi yalnızca taşıyıcı ortamdan (50 $), KDV yazılım dahil toplamdan alınır: 5 + 511 = 516 $ (C)."
destination: youtube
aspect: 1920x1080
language: tr
audience: gümrük müşavirliği / muavinliği sınavına hazırlananlar, gümrük öğrencileri (ders kanalı)
length: ~4 dk
angle: örnek soru çözümü / ders
---

## Intent

Gümrük Koçu ders kanalı için vergi hesaplama dersi: Gümrük Yönetmeliği md. 54 konusunda **özgün**, sayıları ve
kurgusu bize ait bir örnek soru ve anlatımlı çözümü. Kullanıcı notu: sınav sorularının aynısı paylaşılmaz; sayılar
değiştirilerek özgün soru kurulur ve videonun hiçbir yerinde bu sorunun bir sınavdan alındığı ima edilmez.
"Anlatımlı, görselli, şekilli şemalı ve yazılı"; oklar ve ÖNEMLİ / DİKKAT / UYARI / TUZAK rozetleri; motion efektler.

## Assets

- assets/img/koc-cutout.png — Gümrük Koçu (normal duruş).
- assets/img/koc-soru|dikkat|cevap|uyari|tuzak.png — aynı maskotun tepki görselleri (ElevenLabs, Nano Banana 2;
  arka plan yerelde kaldırıldı, boy ve konum normal duruşla eşitlendi).
- assets/img/baba-crop.png — Gümrükçü Baba; tuzak sahnesinde doğru cevabı söyler.
- assets/img/logo-crop.png — Ufuk Çetintaş / Gümrük Eğitim Koçu logosu.

## Customizations

- Seslendirme: ElevenLabs **eleven_v4**, ses **Cem** (voice_id D1xRw7f8ZHedI7xJgfvz), akış XDgGZ25fxulTQbpL3tqz.
- Maskot titremez/kıpırdamaz: sabit görsel, durumlara göre tepki görseline yumuşak geçiş + küçük tepki rozeti.
- Fatura, matrah şeması, hesap makinesi, vergi makbuzu, dört çeldiricinin analizi, formül kartı.
- Ek: "videoyu durdur" geri sayımı, ilerleme çubuğu + bölüm etiketi, çözüm defteri, rakamlı alt yazı (SRT).

## Notes

- Sayılar seslendirmede yazıyla (TTS güvenliği); alt yazıda rakama çevrilir.
- Taşıyıcı olarak DVD seçildi (flash bellek yarı iletken içerdiği için md. 54/a kapsamında tartışmalı olabilir).
