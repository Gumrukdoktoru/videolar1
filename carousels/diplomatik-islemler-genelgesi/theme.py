"""Passport / visa-page visual system: guilloche security print, stamps, wax seal, perforated numbers, MRZ."""
import math

W, H = 1080, 1350
NAVY, BURG, GOLD, TEAL, ROSE = "#10224F", "#7A1428", "#B8893B", "#0F7C7C", "#C9637A"


def _pts(fn, n, step):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in (fn(i * step) for i in range(n)))


def rosette(cx, cy, R, r, d, color, sw=1.1, op=0.5, turns=None, rot=0):
    """Hypotrochoid rosette as a polyline (guilloche)."""
    k = R - r
    turns = turns or r // math.gcd(int(R), int(r))
    n = int(1400 * turns ** 0.5)
    T = 2 * math.pi * turns
    a = math.radians(rot)

    def f(t):
        x = k * math.cos(t) + d * math.cos(k / r * t)
        y = k * math.sin(t) - d * math.sin(k / r * t)
        return cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)

    return f'<polyline points="{_pts(f, n + 1, T / n)}" fill="none" stroke="{color}" stroke-width="{sw}" opacity="{op}"/>'


def waves(y0, y1, lines, amp, freq, color_a, color_b, op=0.35, phase=0.0, sw=1.2):
    out = []
    for i in range(lines):
        y = y0 + (y1 - y0) * i / max(1, lines - 1)
        ph = phase + i * 0.22
        pts = " ".join(f"{x},{y + amp * math.sin(freq * x / W * 2 * math.pi + ph) + amp * 0.35 * math.sin(3.1 * freq * x / W * 2 * math.pi - ph):.1f}"
                       for x in range(-10, W + 20, 12))
        out.append(f'<polyline points="{pts}" fill="none" stroke="url(#wg)" stroke-width="{sw}" opacity="{op}"/>')
    return (f'<defs><linearGradient id="wg" x1="0" x2="1"><stop offset="0" stop-color="{color_a}"/>'
            f'<stop offset="1" stop-color="{color_b}"/></linearGradient></defs>' + "".join(out))


def visa_bg(seed):
    """Cream visa page with multicolour guilloche; seed varies placement per slide."""
    corners = [(980, 260), (100, 1080), (960, 1100), (120, 300)]
    cx, cy = corners[seed % 4]
    ph = seed * 0.9
    micro = ("DİPLOMATİK İŞLEMLER GENELGESİ · 2026/11 · " * 12)
    return f'''<svg class="bgsvg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" aria-hidden="true">
  <defs><linearGradient id="pg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D9EFEA"/><stop offset=".45" stop-color="#F8F1E2"/><stop offset="1" stop-color="#F3D9DE"/></linearGradient>
    <radialGradient id="pv" cx="50%" cy="50%" r="70%"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#3B1A10" stop-opacity=".16"/></radialGradient></defs>
  <rect width="{W}" height="{H}" fill="url(#pg)"/>
  {waves(110, 1250, 40, 26, 1.6, TEAL, ROSE, op=0.42, phase=ph, sw=1.4)}
  {rosette(cx, cy, 300, 76, 150, GOLD, op=0.42, sw=0.9)}
  {rosette(cx, cy, 300, 76, 95, TEAL, op=0.32, sw=0.8, rot=12)}
  {rosette(W - cx, H - cy, 200, 52, 100, ROSE, op=0.30, sw=0.8)}
  <rect width="{W}" height="{H}" fill="url(#pv)"/>
  <text x="40" y="1172" font-family="JetBrains Mono" font-size="9" letter-spacing="1.5" fill="{NAVY}" opacity=".35">{micro}</text>
</svg>'''


def cover_bg():
    micro = ("DİPLOMATİK · GÜMRÜK · KURYE · TAKRİR · KARŞILIKLILIK · " * 10)
    return f'''<svg class="bgsvg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" aria-hidden="true">
  <defs>
    <radialGradient id="cg" cx="45%" cy="38%" r="80%"><stop offset="0" stop-color="#8A1A2F"/><stop offset=".55" stop-color="#5E0F1F"/><stop offset="1" stop-color="#2E0710"/></radialGradient>
    <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .22 0"/></filter>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#cg)"/>
  <rect width="{W}" height="{H}" filter="url(#grain)"/>
  {rosette(540, 450, 380, 76, 200, "#E9C77E", op=0.20, sw=0.8)}
  {rosette(540, 450, 380, 76, 130, "#E9C77E", op=0.14, sw=0.7, rot=9)}
  <rect x="44" y="44" width="{W - 88}" height="{H - 88}" rx="26" fill="none" stroke="#D9B46A" stroke-width="2.5" opacity=".7"/>
  <rect x="58" y="58" width="{W - 116}" height="{H - 116}" rx="20" fill="none" stroke="#D9B46A" stroke-width="1" opacity=".45"/>
  <text x="80" y="1300" font-family="JetBrains Mono" font-size="10" letter-spacing="2" fill="#E9C77E" opacity=".35">{micro}</text>
</svg>'''


STAMP_INK = {"gold": "#F3D58A", "onemli": "#B0122B", "dikkat": "#B45309", "uyari": "#B0122B", "tuzak": "#5B21B6", "bilgi": "#0E5E8A", "ok": "#0B7A55"}
STAMP_LBL = {"gold": "YENİ", "onemli": "ÖNEMLİ", "dikkat": "DİKKAT", "uyari": "UYARI", "tuzak": "TUZAK", "bilgi": "BİLGİ", "ok": "ONAY"}
_stamp_n = [0]


def stamp(kind, sub="05.10.2026", rot=-8, scale=1.0, label=None):
    """Rubber-stamp badge with distressed ink (SVG filter)."""
    _stamp_n[0] += 1
    fid = f"ink{_stamp_n[0]}"
    ink = STAMP_INK[kind]
    lab = label or STAMP_LBL[kind]
    w = int((52 + 30 * len(lab)) * scale)
    h = int(112 * scale)
    return f'''<svg class="stamp" width="{w + 20}" height="{h + 20}" viewBox="-10 -10 {w + 20} {h + 20}" style="transform:rotate({rot}deg)" aria-label="{lab}">
  <defs><filter id="{fid}"><feTurbulence type="fractalNoise" baseFrequency=".75" numOctaves="2" seed="{_stamp_n[0] * 3}" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.55" result="m"/>
    <feComposite in="SourceGraphic" in2="m" operator="in"/></filter></defs>
  <g filter="url(#{fid})" fill="none" stroke="{ink}">
    <rect x="2" y="2" width="{w - 4}" height="{h - 4}" rx="{14 * scale}" stroke-width="{6 * scale}"/>
    <rect x="{12 * scale}" y="{12 * scale}" width="{w - 24 * scale}" height="{h - 24 * scale}" rx="{8 * scale}" stroke-width="{2.2 * scale}"/>
    <text x="{w / 2}" y="{h * 0.56}" text-anchor="middle" fill="{ink}" stroke="none" font-family="Archivo Black" font-size="{44 * scale}" letter-spacing="{2 * scale}">{lab}</text>
    <text x="{w / 2}" y="{h * 0.82}" text-anchor="middle" fill="{ink}" stroke="none" font-family="JetBrains Mono" font-weight="700" font-size="{15 * scale}" letter-spacing="{3 * scale}">{sub}</text>
  </g></svg>'''


def seal(size=150, text="2026/11", sub="GENELGE"):
    """Burgundy wax seal with an irregular rim."""
    r0 = size / 2 - 4
    pts = []
    for i in range(72):
        a = 2 * math.pi * i / 72
        rr = r0 * (0.93 + 0.05 * math.sin(7 * a) + 0.03 * math.sin(13 * a + 1.3) + 0.02 * math.cos(23 * a))
        pts.append(f"{size / 2 + rr * math.cos(a):.1f},{size / 2 + rr * math.sin(a):.1f}")
    c = size / 2
    return f'''<svg class="seal" width="{size}" height="{size}" viewBox="0 0 {size} {size}" aria-hidden="true">
  <defs><radialGradient id="sg{size}" cx="38%" cy="32%" r="75%"><stop offset="0" stop-color="#C23A4E"/><stop offset=".6" stop-color="#8E1B2E"/><stop offset="1" stop-color="#5A0E1C"/></radialGradient></defs>
  <polygon points="{' '.join(pts)}" fill="url(#sg{size})"/>
  <circle cx="{c}" cy="{c}" r="{r0 * 0.66}" fill="none" stroke="#5A0E1C" stroke-width="{size / 40}" opacity=".8"/>
  <circle cx="{c}" cy="{c}" r="{r0 * 0.66}" fill="none" stroke="#E7909C" stroke-width="{size / 90}" opacity=".5" transform="translate(-1 -1)"/>
  <text x="{c}" y="{c - size * 0.03}" text-anchor="middle" font-family="Archivo Black" font-size="{size * 0.15}" fill="#F6D7DC" opacity=".92">{text}</text>
  <text x="{c}" y="{c + size * 0.14}" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="{size * 0.075}" letter-spacing="1" fill="#F6D7DC" opacity=".8">{sub}</text>
</svg>'''


DOTS = {
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    "6": ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00010", "01100"],
}


def perf_number(num, cell=9, gap=16):
    s = f"{num:02d}"
    w = len(s) * (5 * cell + gap)
    circ = []
    for k, ch in enumerate(s):
        for ry, row in enumerate(DOTS[ch]):
            for rx, v in enumerate(row):
                if v == "1":
                    circ.append(f'<circle cx="{k * (5 * cell + gap) + rx * cell + cell / 2}" cy="{ry * cell + cell / 2}" r="{cell * 0.36}"/>')
    return f'<svg class="perf" width="{w}" height="{7 * cell}" viewBox="0 0 {w} {7 * cell}" aria-hidden="true"><g fill="#3B2F22" opacity=".55">{"".join(circ)}</g></svg>'


def mrz(page, total):
    l1 = "DN<GUMRUK<KOCU<<GENELGE<2026<11<<DIPLOMATIK"
    l2 = f"05102026<GGM<<SAYFA<{page:02d}<{total:02d}<<{'KAYDIR' if page < total else 'KAYDET'}"
    pad = lambda s: (s + "<" * 40)[:40]
    esc = lambda s: s.replace("<", "&lt;")
    return f'<div class="mrz"><div>{esc(pad(l1))}</div><div>{esc(pad(l2))}</div></div>'


ICON = {
    "car": '<path d="M3 14l2-5c.4-1 1.3-1.6 2.4-1.6h9.2c1.1 0 2 .6 2.4 1.6l2 5v4h-2.5M5.5 18H3v-4h18M7 18h10" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><circle cx="7" cy="18" r="2" fill="currentColor"/><circle cx="17" cy="18" r="2" fill="currentColor"/>',
    "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z M3 7l9 4 9-4 M12 11v10" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "bag": '<path d="M6.5 8.5 Q12 6 17.5 8.5 L20 20 Q12 22.5 4 20 Z" fill="currentColor" opacity=".18"/><path d="M6.5 8.5 Q12 6 17.5 8.5 L20 20 Q12 22.5 4 20 Z M9 7 C8 3.5 10.5 3 12 6.5 C13.5 3 16 3.5 15 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><circle cx="12" cy="13.5" r="2.6" fill="#8E1B2E"/>',
    "doc": '<path d="M5 2.5h9l5 5v14H5z M14 2.5v5h5 M8 12h8 M8 15.5h8 M8 19h5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>',
    "id": '<rect x="2.5" y="5" width="19" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.5" cy="11" r="2.4" fill="currentColor"/><path d="M5 16.5c.8-1.6 2-2.4 3.5-2.4s2.7.8 3.5 2.4 M14 10h5 M14 13.5h4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "flag": '<path d="M5 21V3 M5 4h12l-2.5 4L17 12H5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "scale": '<path d="M12 3v18 M6 21h12 M4 7h16 M7 7l-3 6h6z M17 7l-3 6h6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "plane": '<path d="M2.5 13.5l7-1.5L14 4.5c.5-.8 1.8-.6 2 .3l.2.7-2.3 7.3 5.8-1.2c1.4-.3 2.4 1.5 1.3 2.4L3.8 16.5z M6 19.5h12" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "ship": '<path d="M3 15l2 5h14l2-5z M6 15V9h12v6 M12 9V4 M9 6h6" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "moto": '<circle cx="5.5" cy="16.5" r="3.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="18.5" cy="16.5" r="3.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M5.5 16.5l4-6h5l4 6 M13 6h3l1.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "caravan": '<rect x="2.5" y="6" width="15" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M17.5 13H22 M5.5 9h4v3h-4z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8" cy="17.5" r="2" fill="currentColor"/>',
    "gear": '<circle cx="12" cy="12" r="3.2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "frame": '<rect x="3" y="4" width="18" height="14" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M6 15l4-5 3 3.5 2-2 3 3.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M9 21h6" stroke="currentColor" stroke-width="2"/>',
    "gift": '<rect x="3" y="9" width="18" height="12" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M2.5 9h19 M12 9v12 M12 9c-2-4-6-4-6-1.5S10 9 12 9c2 0 6 .5 6-1.5S14 5 12 9" fill="none" stroke="currentColor" stroke-width="2"/>',
    "column": '<path d="M3 21h18 M5 18h14 M4 8h16L12 3z M7 8v10 M12 8v10 M17 8v10" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "xray": '<rect x="3" y="3" width="18" height="18" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M7 7l10 10 M17 7L7 17" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
    "check": '<path d="M4 12.5l5 5L20 6.5" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "x": '<path d="M5 5l14 14M19 5L5 19" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "arrow": '<path d="M4 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>',
    "down": '<path d="M12 4v14M6 13l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>',
    "glass": '<path d="M7 3h10l-1 7a4 4 0 0 1-8 0z M12 14v6 M8 21h8" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "cig": '<rect x="2" y="11" width="16" height="4" rx="1" fill="none" stroke="currentColor" stroke-width="2"/><path d="M14 11v4 M20 11v4 M22 11v4 M20 8c0-2 2-2 2-4" fill="none" stroke="currentColor" stroke-width="2"/>',
    "seal": '<circle cx="12" cy="12" r="8" fill="currentColor"/><circle cx="12" cy="12" r="4.5" fill="none" stroke="#fff" stroke-width="1.6"/>',
    "globe": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18 M12 3c3 3 3 15 0 18 M12 3c-3 3-3 15 0 18" fill="none" stroke="currentColor" stroke-width="1.6"/>',
}


def ic(name, size=40, cls=""):
    return f'<svg class="ic {cls}" viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true">{ICON[name]}</svg>'


def pouch(w=300):
    """Diplomatic pouch illustration with wax seal and tag."""
    return f'''<svg class="pouch" width="{w}" height="{w * 1.05:.0f}" viewBox="0 0 300 315" aria-hidden="true">
  <path d="M60 70 Q150 40 240 70 L262 270 Q150 300 38 270 Z" fill="#2F3F6E" stroke="#10224F" stroke-width="5" stroke-linejoin="round"/>
  <path d="M60 70 Q150 40 240 70 L236 100 Q150 76 64 100 Z" fill="#22305A"/>
  <path d="M84 98 Q150 80 216 98" stroke="#C9A55A" stroke-width="5" fill="none" stroke-dasharray="10 8"/>
  <path d="M150 62 C 120 20, 95 30, 108 52 M150 62 C 180 20, 205 30, 192 52" stroke="#C9A55A" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path d="M70 120 L52 260 M230 120 L248 260" stroke="#3C4E85" stroke-width="3" opacity=".7"/>
  <g transform="translate(150 70)"><path d="M0 0 L-6 70 L6 70 Z" fill="#C9A55A"/></g>
  <circle cx="150" cy="150" r="34" fill="#8E1B2E" stroke="#5A0E1C" stroke-width="4"/>
  <circle cx="150" cy="150" r="20" fill="none" stroke="#E7909C" stroke-width="2.5" opacity=".7"/>
  <rect x="96" y="208" width="108" height="48" rx="6" fill="#F4EFE3" stroke="#10224F" stroke-width="3" transform="rotate(-6 150 232)"/>
  <text x="150" y="238" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="16" fill="#10224F" transform="rotate(-6 150 232)">DİPLOMATİK</text>
</svg>'''


def emblem(size=420, top="GENELGE", num="2026/11"):
    """Gold-foil passport-style emblem: rings, rosette core, globe, laurels, arc text."""
    c = size / 2
    leaves = []
    for side in (-1, 1):
        for i in range(9):
            a = math.radians(115 + i * 15) if side < 0 else math.radians(65 - i * 15)
            rr = c * 0.80
            x, y = c + rr * math.cos(a), c + rr * math.sin(a) * 1.0
            rot = math.degrees(a) + (90 if side < 0 else -90) + side * 25
            leaves.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{size*0.018:.1f}" ry="{size*0.045:.1f}" transform="rotate({rot:.1f} {x:.1f} {y:.1f})"/>')
    return f'''<svg class="emblem" width="{size}" height="{size}" viewBox="0 0 {size} {size}" aria-hidden="true">
  <defs><linearGradient id="gf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FBE7B5"/><stop offset=".45" stop-color="#E2B865"/><stop offset="1" stop-color="#A9772A"/></linearGradient>
    <path id="arcT" d="M {c - c*0.62} {c} A {c*0.62} {c*0.62} 0 0 1 {c + c*0.62} {c}"/></defs>
  <g fill="none" stroke="url(#gf)">
    <circle cx="{c}" cy="{c}" r="{c*0.97}" stroke-width="3"/>
    <circle cx="{c}" cy="{c}" r="{c*0.92}" stroke-width="1.2"/>
    <circle cx="{c}" cy="{c}" r="{c*0.70}" stroke-width="3"/>
    <circle cx="{c}" cy="{c}" r="{c*0.46}" stroke-width="2"/>
    {rosette(c, c, c*0.44, c*0.44/4.1, c*0.20, "#E9C77E", op=0.85, sw=0.8).replace('stroke="#E9C77E"', 'stroke="url(#gf)"')}
    <circle cx="{c}" cy="{c}" r="{c*0.20}" stroke-width="2.5"/>
    <path d="M{c - c*0.2} {c} H{c + c*0.2} M{c} {c - c*0.2} C {c + c*0.1} {c - c*0.1}, {c + c*0.1} {c + c*0.1}, {c} {c + c*0.2} M{c} {c - c*0.2} C {c - c*0.1} {c - c*0.1}, {c - c*0.1} {c + c*0.1}, {c} {c + c*0.2}" stroke-width="2"/>
  </g>
  <g fill="url(#gf)" opacity=".95">{"".join(leaves)}</g>
  <text font-family="Marcellus" font-size="{size*0.075}" letter-spacing="{size*0.02}" fill="url(#gf)" text-anchor="middle"><textPath href="#arcT" startOffset="50%">{top}</textPath></text>
  <text x="{c}" y="{c + c*0.62}" text-anchor="middle" font-family="Archivo Black" font-size="{size*0.10}" fill="url(#gf)">{num}</text>
</svg>'''
