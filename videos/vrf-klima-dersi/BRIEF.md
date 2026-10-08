---
workflow: general-video
flow: automation
storyboard: no
message: "Multi-split mi VRF mi? Ticari ada değil, dört teknik kritere bakılır; eski BTB'ler bu kriterlerle yeniden değerlendirilecek."
destination: youtube
aspect: 1920x1080
language: tr
audience: gümrük müşavirleri, ithalatçılar, gümrük öğrencileri (ders kanalı)
length: ~3-4 dk
angle: how-to / ders
---

## Intent

Gümrük Koçu ders kanalı için, Gümrükler Genel Müdürlüğünün 01.10.2026 tarihli ve
E-17474625-162.01-00126963399 sayılı "VRF Klimalar" yazısını anlatan ders videosu.
Kullanıcının ifadesiyle: "anlatımlı, görselli, şekilli şemalı ve yazılı";
"oklar ve önemli-dikkat-uyarı-tuzak diye belirtmesini de yapacaksın"; "motion effectler kullanacaksın".

## Assets

- ../../Gümrükkoçu.png — Gümrük Koçu (öğretmen) avatarı; anlatıcı/sunucu. Arka planı sahte damalı, kesilmesi gerekiyor.
- ../../gmrükçü baba.jpg — Gümrükçü Baba karakteri; "tuzak" anında konuşma balonlu kısa cameo.
- ../../uçlogo.png — Ufuk Çetintaş / Gümrük Eğitim Koçu logosu; açılış ve kapanış.
- ../../Müşavirbey — boş dosya (2 bayt), kullanılamadı.

## Customizations

- Seslendirme: ElevenLabs **eleven_v4**, ses **Cem** (voice_id D1xRw7f8ZHedI7xJgfvz, İstanbul aksanı).
- Avatar: Gümrük Koçu görseli, Cem sesine dudak senkronlu (ElevenLabs üzerinden HeyGen Avatar 4); bütçe yetmezse hareketli kesik görsel.
- Şemalar, oklar, karşılaştırma tablosu, 4 kriter kontrol listesi.
- Uyarı rozetleri: ÖNEMLİ / DİKKAT / UYARI / TUZAK.
- Ek özellikler (Claude önerisi): ilerleme çubuğu + bölüm etiketi, alt yazı, mini quiz, "Koçun Tavsiyesi" kartı, özet kartı.

## Notes

- Kaynak metne sadık kal; GTİP numarası uydurma (yazıda yok).
- Kullanıcı ses ve avatarın HeyGen içindeki "ders kanalı öğretmen" görünümünü kastetmiş olabilir; HeyGen avatar kütüphanesine buradan erişim yok, repodaki Gümrükkoçu.png kullanıldı.
