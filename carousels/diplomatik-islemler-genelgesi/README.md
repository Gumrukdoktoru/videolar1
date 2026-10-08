# Diplomatik İşlemler Genelgesi (2026/11) — carousel

15 slaytlık 1080×1350 Instagram / LinkedIn carousel'i. Tema: diplomatik pasaport —
altın yaldızlı kapak, güvenlik baskılı (guilloche) vize sayfaları, damga rozetleri
(ÖNEMLİ · DİKKAT · UYARI · TUZAK), delikli sayfa numarası ve MRZ şeridi.

- `ozet.md` — slayt slayt özet (carousel metni)
- `png/` — paylaşıma hazır slaytlar (01–15)
- `diplomatik-islemler-carousel.pdf` — LinkedIn belge gönderisi için tek PDF
- `theme.py` (görsel sistem), `build.py` + `slides_more.py` (slaytlar), `render.js` (PNG/PDF)

```bash
python3 build.py && node render.js
```
