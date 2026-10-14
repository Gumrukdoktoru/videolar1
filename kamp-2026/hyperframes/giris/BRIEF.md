---
workflow: motion-graphics
flow: automation
storyboard: no
mode: autonomous
message: "Opening title sting: the 7/24 CAN'LI Eğitim Merkezi logo assembles, 'ANKARA KAMPI' tracks in, '08 KASIM' punches in on the spoken date, then 'HAZIRLIKLAR BAŞLADI' stamps in; everything clears to a clean background for the master's split-door reveal."
aspect: 1080x1920
destination: 9:16 vertical promo for the Ankara camp (cut in by the Remotion master as its FIRST shot, full-frame, opaque)
language: tr
length: 4.90s (exact, 147 frames @ 30 fps)
narration: no (the client's own narration lives in the Remotion master, not in this file)
export: mp4 (opaque, H.264)
---

# Giriş sting — CAN'LI 7/24 Eğitim Merkezi · Ankara Kampı

**Category:** `logo-reveal` + `kinetic-type` (form categories, no search; user-supplied vector logo).

**Approved by the user upfront** (design + render). No questions; render once checks and proof snapshots pass.

Client: CAN'LI 7/24 Eğitim Merkezi (Turkish customs-exam prep school). Promo for the Ankara camp
starting 8 November ("08 KASIM") at New Park Otel, Ankara. The master's soundtrack is the client's
narration (venue walkthrough); this sting covers the first 4.9 s, and this file's t=0 = master t=0.

## Voice sync (master timeline, word onsets)

| words                        | time        |
| ---------------------------- | ----------- |
| Herkese merhaba arkadaşlar.  | 0.62–1.90   |
| 8                            | 2.06        |
| Kasım                        | 2.38–2.58   |
| hazırlıklarımız              | 2.60–3.28   |
| şu an                        | 3.34–3.66   |
| başlamış                     | 3.80        |
| bulunmakta.                  | 4.32–4.80   |

## Beats

- 0.00–1.20 brand logo assembles near the top third (reuse of the `kapanis-logo` choreography, same SVG
  groups `#badge7 #badge24 #wordmark #cap #tagline`): badges 7 / 24 pop, CAN'LI rises letter by letter,
  graduation cap drops onto the A, tagline "Eğitim Merkezi" wipes in.
- ~1.00–1.60 "ANKARA KAMPI" kinetic label: tracking-in + orange underline draw.
- 2.06 hero hit "08" (huge, heavy, orange): scale overshoot + short glow flash, impact frame exactly at 2.06 s;
  "KASIM" (white) lands on the spoken "Kasım" at 2.38.
- 2.60–3.90 "HAZIRLIKLAR" reveals over "hazırlıklarımız", then "BAŞLADI" stamps in at 3.80 (stamp frame + ring).
- 4.20–4.45 every text/logo element exits fast (up and out + blur).
- 4.45–4.90 background-only frames (no text, no logo) for the master's split-door reveal.

## Constraints

- Keep y = 1380..1720 px free of important content (master overlays word captions there).
- ~90 px side safe margins.
- Literal Turkish uppercase strings (KASIM, BAŞLADI, HAZIRLIKLAR, ANKARA KAMPI); never CSS text-transform.

## Look

Colors: orange #F16D25, anthracite #414141, navy #070B1F, navy2 #121A3D, white #FFFFFF. Deep navy gradient
with warm orange radial glow, subtle LED pixel grid / scanline texture, gentle glow breathing; premium
TV-broadcast feel. Logo: `assets/logo-canli-dark.svg` (dark-background variant), inlined.
Font: Montserrat variable (100–900), local `assets/fonts/Montserrat-latin.woff2` + `Montserrat-latin-ext.woff2`,
two @font-face rules split by unicode-range. No network fonts.

## Delivery

`renders/video.mp4` (1080x1920, 30 fps, 147 frames = 4.90 s) → copied to
`/home/user/videolar1/kamp-2026/remotion/public/hf/giris.mp4`.
