---
workflow: general-video
flow: automation
storyboard: no
message: "CD içindeki yazılımda gümrük vergisi sadece taşıyıcı ortamdan (10 $), KDV yazılım dahil toplamdan alınır: 1 + 181,98 = 182,98 $ (A)."
destination: youtube
aspect: 1920x1080
language: tr
audience: gümrük müşavirliği / muavinliği sınavına hazırlananlar, gümrük öğrencileri (ders kanalı)
length: ~3 dk
angle: çıkmış soru çözümü / ders
---

## Intent

Gümrük Koçu ders kanalı için "Geçmiş Yıllar Vergi Hesaplama Soruları" derlemesinin 1. sorusunun
(CD üzerine kaydedilmiş yazılım ithalatı) anlatımlı çözümü. Kullanıcının ifadesiyle: "anlatımlı, görselli,
şekilli şemalı ve yazılı"; "oklar ve önemli-dikkat-uyarı-tuzak diye belirtmesini de yapacaksın";
"motion effectler kullanacaksın"; "seninde eklemen gereken farklı bir özellik varsa onu da ekleyebilirsin".

## Kaynak

- `Gumrukdoktoru/2027-GM-` deposu → `Hesaplamaçıkmış.pdf`: soru 1 (s. 480), cevap anahtarı 1-A (s. 499),
  çözüm (s. 500). Kapsam uyarısı ve ihracat notu aynı kitabın 69 ve 70. soru çözümlerinden (s. 512).

## Assets

- assets/img/koc-cutout.png — Gümrük Koçu (öğretmen) avatarı; anlatıcı/sunucu (VRF dersinden).
- assets/img/baba-crop.png — Gümrükçü Baba; tuzak sahnesinde konuşma balonlu kısa cameo.
- assets/img/logo-crop.png — Ufuk Çetintaş / Gümrük Eğitim Koçu logosu.
- ../../Müşavirbey — hâlâ boş dosya (2 bayt), kullanılamadı.

## Customizations

- Seslendirme: ElevenLabs **eleven_v4**, ses **Cem** (voice_id D1xRw7f8ZHedI7xJgfvz), flow Q74clmCvqLrwT14pnVLf.
- Avatar: hareketli kesik Gümrük Koçu görseli (konuşma ritmine bağlı nefes/sallanma + ses çubukları).
- Fatura görseli, matrah şeması, adım adım hesap makinesi/makbuz, oklar.
- Rozetler: ÖNEMLİ / DİKKAT / UYARI / TUZAK.
- Ek özellikler: "videoyu durdur" geri sayımı, şık eleme animasyonu, ilerleme çubuğu + bölüm etiketi,
  alt yazı (SRT), Koçun notu kartı, akılda kalıcı formül kartı.

## Notes

- Sayılar seslendirmede yazıyla (TTS güvenliği); alt yazıda rakama çevrilir.
- C ve D şıklarının nasıl türetildiği kaynakta yok; videoda yalnızca hesapla doğrulanan B ve E açıklanır.
