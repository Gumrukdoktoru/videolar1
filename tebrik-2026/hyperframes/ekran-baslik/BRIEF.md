---
workflow: motion-graphics
flow: automation
storyboard: no
message: "2026 Gümrük sınavları hazırlık maratonu tamamlandı — bu dönemi birlik ve beraberlik içinde geride bırakıyoruz."
destination: studio-led-wall
aspect: 1280x750
language: tr
length: 11.13s
audience: "7/24 CAN'LI Eğitim Merkezi öğrencileri ve hocaları (gümrük sınavı adayları)"
angle: kinetic-type
---

## Intent

Content that plays INSIDE the large LED video wall of a TV studio set, behind a
presenter. The Remotion master composites this MP4 onto the wall and carries the
presenter's voice; every typographic beat here lands on the spoken word onsets
(from `remotion/public/altyazi.json`). Tone: celebratory, proud, warm — a
"marathon complete" congratulation from the brand.

## Assets

- assets/logo-canli-dark.svg — brand logo (white + orange, viewBox 3000×1320), small channel bug top-left from ~0.4 s, ≈220 px wide.
- assets/fonts/montserrat-{600,800,900}.woff2 — Montserrat static instances (latin + latin-ext, Turkish İ Ş Ğ Ü Ö Ç), embedded via local @font-face for deterministic renders.

## Customizations

- Canvas 1280×750 (exact LED aspect), 30 fps, exactly 11.13 s, opaque MP4.
- Screen power-on (0.00–0.40): horizontal light line expands to full frame.
- Scene 1 "BÜYÜK EMEĞİN / VE MÜCADELENİN / SON GÜNÜ!" — per-word mask-rise on onsets, "SON GÜNÜ!" orange with scale punch.
- Scene 2 "2026" (orange) + "GÜMRÜK SINAVLARI / HAZIRLIK MARATONU", race/progress track 0→100 % (4.5–6.0 s) with finish flag, "TAMAMLANDI" stamp (white on orange pill + check) slams at ~5.9 s.
- Scene 3 "AYLAR SÜREN YORUCU BİR DÖNEM" (small, white 70 %), hero "BİRLİK VE / BERABERLİK" with orange underline sweep + "İÇİNDE", final "GERİDE BIRAKIYORUZ" in orange; final frame holds 10.6–11.13 (no fade-out).
- LED-screen look: navy gradient #070B1F → #121A3D, subtle orange radial glow, very faint pixel-grid / scanline texture.

## Notes

- Brand palette: orange #F16D25, anthracite #414141, white #FFFFFF.
- 60 px safe margin for all text; headline font-size ≥ 90 px, supporting ≥ 44 px (shown ~990 px wide on a phone-format video).
- No narration/audio in this file. User pre-approved design and render (no approval gate).
