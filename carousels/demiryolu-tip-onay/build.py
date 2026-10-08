"""Fill slides.html placeholders -> carousel.html, then render.js exports PNG/PDF."""
import pathlib, re

D = pathlib.Path(__file__).resolve().parent
src = (D / "slides.html").read_text()
N = 8
W = 936  # content width

ARROW = '<svg width="34" height="34" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h14M13 6l6 6-6 6" fill="none" stroke="#1F45D6" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHECK = '<svg width="26" height="26" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
INFO = '<svg width="34" height="34" viewBox="0 0 24 24" aria-hidden="true" style="flex:none"><circle cx="12" cy="12" r="10" fill="#1F45D6"/><path d="M12 10.5v6" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><circle cx="12" cy="7.2" r="1.5" fill="#fff"/></svg>'
EYE = '<svg viewBox="0 0 24 24"><path d="M1.5 12S5.5 4.8 12 4.8 22.5 12 22.5 12 18.5 19.2 12 19.2 1.5 12 1.5 12z" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="12" cy="12" r="3.6" fill="currentColor"/></svg>'
STAR = '<svg viewBox="0 0 24 24"><path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9z" fill="currentColor"/></svg>'
SAVE = '<svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 3h12v18l-6-4-6 4z" fill="currentColor"/></svg>'
SHARE = '<svg width="26" height="26" viewBox="0 0 24 24"><path d="M3 11l18-8-8 18-2-8z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/></svg>'
BELL = '<svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z" fill="currentColor"/><path d="M10 20.5a2.2 2.2 0 0 0 4 0" fill="none" stroke="currentColor" stroke-width="2.2"/></svg>'

LOCO = ('<g transform="translate({x} 2)">'
        '<path d="M2 8 H92 Q118 8 128 30 L130 36 H2 Z" fill="#1F45D6" stroke="#0B1A44" stroke-width="2.5" stroke-linejoin="round"/>'
        '<path d="M12 14 h18 v9 h-18z M38 14 h18 v9 h-18z M64 14 h18 v9 h-18z" fill="#fff"/>'
        '<path d="M96 12 Q112 14 118 24 H96z" fill="#E4EAFD"/>'
        '<circle cx="22" cy="40" r="6" fill="#0B1A44"/><circle cx="40" cy="40" r="6" fill="#0B1A44"/>'
        '<circle cx="96" cy="40" r="6" fill="#0B1A44"/><circle cx="114" cy="40" r="6" fill="#0B1A44"/></g>')


def rail(n):
    w = 1008
    sleepers = "".join(f'<rect x="{x}" y="42" width="16" height="12" rx="2" fill="#0B1A44" opacity=".75"/>' for x in range(8, w, 34))
    tx = 30 + (n - 1) * (w - 200) / (N - 1)
    done = f'<path d="M0 49 H{tx + 10:.0f}" stroke="#1F45D6" stroke-width="5" opacity=".55"/>'
    stations = "".join(
        f'<circle cx="{30 + (i - 1) * (w - 200) / (N - 1) + 66:.0f}" cy="49" r="5" fill="{"#1F45D6" if i <= n else "#F6F4EE"}" stroke="#0B1A44" stroke-width="2"/>'
        for i in range(1, N + 1))
    return (f'<div class="rail"><svg width="{w}" height="56" viewBox="0 0 {w} 56" aria-hidden="true">{sleepers}'
            f'<path d="M0 46 H{w}" stroke="#0B1A44" stroke-width="3"/><path d="M0 52 H{w}" stroke="#0B1A44" stroke-width="2"/>'
            f'{done}{stations}{LOCO.format(x=round(tx))}</svg></div>')


def tb(n):
    last = n == N
    return ('<div class="lg"><img src="img/logo-crop.png" alt="Ufuk Çetintaş Gümrük Eğitim Koçu" /></div>'
            '<div class="ti"><small>KONU · RG 33394</small><b>Demiryolu Araçları Tip Onay Yönetmeliğinde Değişiklik</b></div>'
            f'<div class="pg"><small>SAYFA</small><b>{n:02d}/{N:02d}</b><span>{"kaydet ✓" if last else "kaydır →"}</span></div>')


def badge(kind):
    lab, ic = {"dikkat": ("DİKKAT", EYE), "onemli": ("ÖNEMLİ", STAR)}[kind]
    return f'<span class="badge b-{kind}">{ic}{lab}</span>'


html = src
for i in range(1, N + 1):
    html = html.replace(f"RAIL{i}\n", rail(i) + "\n")
    html = html.replace(f'<div class="tb TB{i}"></div>', f'<div class="tb">{tb(i)}</div>')
html = (html.replace("ARR34", ARROW).replace("ARROW", ARROW).replace("CHECK", CHECK).replace("INFO", INFO)
        .replace("BADGE_DIKKAT", badge("dikkat")).replace("BADGE_ONEMLI", badge("onemli"))
        .replace("SAVE", SAVE).replace("SHARE", SHARE).replace("BELL", BELL))
html = html.replace("SLEEPERS", "".join(f'<path d="M{x} 244 V 280"/>' for x in range(12, 936, 30)))

MAX = 1_804_582
px = lambda v: round(W * v / MAX)
vals = {"WOLD1": px(100_000), "WNEW1": px(1_804_582), "WOLD2": px(50_000), "WNEW2": px(902_283)}
for k, v in vals.items():
    html = html.replace(k + "px", f"{v}px")
html = html.replace("LOLD1px", f"{vals['WOLD1'] + 14}px").replace("LOLD2px", f"{vals['WOLD2'] + 14}px").replace("LNEW2px", f"{vals['WNEW2'] + 14}px")
ticks = [(0, "0"), (500_000, "500 bin"), (1_000_000, "1 milyon"), (1_500_000, "1,5 milyon")]
html = html.replace("AXIS", "".join(f'<span style="left:{px(v) + (24 if v == 0 else 0)}px">{t}</span>' for v, t in ticks))

left = re.findall(r"\b(RAIL\d|TB\d|ARROW|ARR34|CHECK|INFO|BADGE_\w+|SAVE|SHARE|BELL|SLEEPERS|AXIS|WOLD\d|WNEW\d|LOLD\d|LNEW\d)\b", html)
assert not left, left
(D / "carousel.html").write_text(html)
print("ok", vals)
