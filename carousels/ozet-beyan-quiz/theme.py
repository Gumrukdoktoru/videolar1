"""Radar / port-control visual system: sweep radar, HUD grid, port skyline, neon stamps, optic-form bubbles."""
import math

W, H = 1080, 1350
CYAN, AMBER, GREEN, RED, NAVY = "#2FE6D2", "#FFB020", "#2EE07A", "#FF4D6D", "#0B1A33"


def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def _sector(cx, cy, r, a1, a2):
    x1, y1 = _pt(cx, cy, r, a1)
    x2, y2 = _pt(cx, cy, r, a2)
    return f"M{cx:.1f} {cy:.1f} L{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f} Z"


def radar(cx, cy, R, sweep=-40, uid="r", blips=(), labels=True, op=1.0):
    """Radar scope: rings, crosshair, bearing ticks, fading sweep wedge, glowing blips."""
    dash = {2: ' stroke-dasharray="4 8"', 4: ' stroke-dasharray="4 8"'}
    rings = "".join(
        f'<circle cx="{cx}" cy="{cy}" r="{R * k / 5:.0f}" fill="none" stroke="{CYAN}" stroke-width="{2 if k == 5 else 1.2}" '
        f'opacity="{.42 if k == 5 else .2}"{dash.get(k, "")}/>'
        for k in range(1, 6))
    ticks = []
    for d in range(0, 360, 5):
        long = d % 30 == 0
        x1, y1 = _pt(cx, cy, R, d)
        x2, y2 = _pt(cx, cy, R - (22 if long else 10), d)
        ticks.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{CYAN}" stroke-width="{2 if long else 1}" opacity="{.55 if long else .3}"/>')
        if long and labels:
            tx, ty = _pt(cx, cy, R + 22, d)
            ticks.append(f'<text x="{tx:.1f}" y="{ty + 5:.1f}" text-anchor="middle" font-family="JetBrains Mono" font-size="13" fill="{CYAN}" opacity=".45">{(d + 90) % 360:03d}</text>')
    wedge = "".join(
        f'<path d="{_sector(cx, cy, R, sweep - 64 + i * 2, sweep - 62 + i * 2 + .4)}" fill="{CYAN}" opacity="{(i / 32) ** 2.2 * .34:.3f}"/>'
        for i in range(32))
    lx, ly = _pt(cx, cy, R, sweep)
    bl = []
    for (bx, by, rr, col, tag) in blips:
        bl.append(f'<circle cx="{bx}" cy="{by}" r="{rr * 2.6}" fill="{col}" opacity=".18" filter="url(#glow{uid})"/>'
                  f'<circle cx="{bx}" cy="{by}" r="{rr}" fill="{col}"/>'
                  f'<circle cx="{bx}" cy="{by}" r="{rr * 2.2}" fill="none" stroke="{col}" stroke-width="1.5" opacity=".55"/>')
        if tag:
            bl.append(f'<text x="{bx + rr * 2.6}" y="{by - rr * 1.6}" font-family="JetBrains Mono" font-weight="700" font-size="15" fill="{col}" opacity=".85">{tag}</text>')
    return f'''<g opacity="{op}">
  <circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#scope{uid})"/>
  {rings}
  <path d="M{cx - R} {cy} H{cx + R} M{cx} {cy - R} V{cy + R}" stroke="{CYAN}" stroke-width="1.2" opacity=".22"/>
  <path d="M{_pt(cx, cy, R, 45)[0]:.1f} {_pt(cx, cy, R, 45)[1]:.1f} L{_pt(cx, cy, R, 225)[0]:.1f} {_pt(cx, cy, R, 225)[1]:.1f} M{_pt(cx, cy, R, 135)[0]:.1f} {_pt(cx, cy, R, 135)[1]:.1f} L{_pt(cx, cy, R, 315)[0]:.1f} {_pt(cx, cy, R, 315)[1]:.1f}" stroke="{CYAN}" stroke-width="1" opacity=".1"/>
  {"".join(ticks)}
  {wedge}
  <line x1="{cx}" y1="{cy}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="{CYAN}" stroke-width="3" opacity=".85" filter="url(#glow{uid})"/>
  <line x1="{cx}" y1="{cy}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="#DFFFFB" stroke-width="1.4"/>
  <circle cx="{cx}" cy="{cy}" r="6" fill="{CYAN}"/>
  {"".join(bl)}
</g>'''


def skyline(y0=1150, uid="s"):
    """Port silhouette: ship, container stacks, STS gantry cranes — radar-scanned look."""
    out = []
    # water line + reflections
    out.append(f'<rect x="0" y="{y0 + 150}" width="{W}" height="{H - y0 - 150}" fill="#04101F"/>')
    for i in range(7):
        y = y0 + 158 + i * 7
        out.append(f'<line x1="{(i * 137) % 300}" y1="{y}" x2="{W}" y2="{y}" stroke="{CYAN}" stroke-width="1" opacity="{.10 - i * .012:.3f}" stroke-dasharray="{18 + i * 6} {10 + i * 4}"/>')
    # ship hull at left
    out.append(f'<path d="M20 {y0 + 112} L330 {y0 + 112} L306 {y0 + 152} L44 {y0 + 152} Z" fill="#0A1A33" stroke="{CYAN}" stroke-width="1.3" stroke-opacity=".35"/>')
    out.append(f'<rect x="48" y="{y0 + 62}" width="54" height="50" fill="#0A1A33" stroke="{CYAN}" stroke-width="1.2" stroke-opacity=".35"/>')
    out.append(f'<rect x="58" y="{y0 + 70}" width="34" height="8" fill="{CYAN}" opacity=".25"/>')
    cols = ["#123A5C", "#163055", "#0F2C4A", "#1A3C5E", "#5A3A16", "#123A5C"]
    k = 0
    for cx in range(112, 300, 46):
        for lvl in range(2 + (cx // 46) % 2):
            out.append(f'<rect x="{cx}" y="{y0 + 88 - lvl * 24}" width="44" height="22" fill="{cols[k % 6]}" stroke="{CYAN}" stroke-width=".8" stroke-opacity=".3"/>')
            k += 1
    # yard stacks
    for bx in (420, 640, 860):
        for c in range(4):
            for lvl in range(1 + (bx + c * 7) % 3):
                out.append(f'<rect x="{bx + c * 48}" y="{y0 + 128 - lvl * 22}" width="46" height="20" fill="{cols[(k + c) % 6]}" stroke="{CYAN}" stroke-width=".8" stroke-opacity=".28"/>')
                k += 1
    # gantry cranes
    for gx in (380, 600, 820):
        g = (f'<g stroke="{CYAN}" stroke-opacity=".45" stroke-width="2" fill="none">'
             f'<path d="M{gx} {y0 + 150} L{gx + 10} {y0 + 10} M{gx + 70} {y0 + 150} L{gx + 60} {y0 + 10} M{gx + 5} {y0 + 80} H{gx + 65} M{gx} {y0 + 150} L{gx + 65} {y0 + 80} M{gx + 70} {y0 + 150} L{gx + 5} {y0 + 80}"/>'
             f'<path d="M{gx - 120} {y0 + 10} H{gx + 120} M{gx + 35} {y0 - 40} L{gx - 110} {y0 + 10} M{gx + 35} {y0 - 40} L{gx + 115} {y0 + 10} M{gx + 35} {y0 - 40} V{y0 + 10}" stroke-width="1.6"/>'
             f'<line x1="{gx - 70}" y1="{y0 + 10}" x2="{gx - 70}" y2="{y0 + 60}" stroke-width="1" stroke-dasharray="3 3"/></g>'
             f'<rect x="{gx - 82}" y="{y0 + 60}" width="24" height="12" fill="{AMBER}" opacity=".55"/>'
             f'<circle cx="{gx + 35}" cy="{y0 - 42}" r="3.5" fill="{RED}"/>'
             f'<circle cx="{gx + 35}" cy="{y0 - 42}" r="9" fill="{RED}" opacity=".25" filter="url(#glow{uid})"/>')
        out.append(g)
    return "".join(out)


def radar_bg(uid, cx=820, cy=300, R=560, sweep=-40, blips=(), port=True, tint="#0E2B4A"):
    gx = cx / W * 100
    gy = cy / H * 100
    micro = ("ÖZET BEYAN · GÜMRÜK GÖZETİMİ · GK 35/A · 35/B · 35/C · 36 · 47 · 152 · GY 67 · 74 · ") * 6
    return f'''<svg class="bgsvg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" aria-hidden="true">
  <defs>
    <radialGradient id="bg{uid}" cx="{gx:.1f}%" cy="{gy:.1f}%" r="95%"><stop offset="0" stop-color="{tint}"/><stop offset=".55" stop-color="#081528"/><stop offset="1" stop-color="#040A16"/></radialGradient>
    <radialGradient id="scope{uid}"><stop offset="0" stop-color="{CYAN}" stop-opacity=".10"/><stop offset=".7" stop-color="{CYAN}" stop-opacity=".03"/><stop offset="1" stop-color="{CYAN}" stop-opacity=".07"/></radialGradient>
    <pattern id="grid{uid}" width="54" height="54" patternUnits="userSpaceOnUse"><path d="M54 0H0V54" fill="none" stroke="{CYAN}" stroke-width="1" opacity=".07"/></pattern>
    <pattern id="scan{uid}" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#000" opacity=".22"/></pattern>
    <filter id="glow{uid}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
    <filter id="grain{uid}"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="{len(uid) * 7}"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .05 0"/></filter>
    <linearGradient id="fade{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#040A16" stop-opacity="0"/><stop offset="1" stop-color="#040A16" stop-opacity=".9"/></linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg{uid})"/>
  <rect width="{W}" height="{H}" fill="url(#grid{uid})"/>
  {radar(cx, cy, R, sweep, uid, blips)}
  {skyline(1110, uid) if port else ""}
  <rect y="1180" width="{W}" height="170" fill="url(#fade{uid})"/>
  <rect width="{W}" height="{H}" fill="url(#scan{uid})"/>
  <rect width="{W}" height="{H}" filter="url(#grain{uid})"/>
  <text x="34" y="{H - 14}" font-family="JetBrains Mono" font-size="10" letter-spacing="2" fill="{CYAN}" opacity=".28">{micro}</text>
</svg>'''


STAMP_INK = {"tuzak": AMBER, "dikkat": "#FF8A3D", "onemli": RED, "uyari": RED, "ok": GREEN, "bilgi": CYAN, "yanlis": RED}
STAMP_LBL = {"tuzak": "TUZAK", "dikkat": "DİKKAT", "onemli": "ÖNEMLİ", "uyari": "UYARI", "ok": "DOĞRU", "bilgi": "BİLGİ", "yanlis": "YANLIŞ"}
_n = [0]


def stamp(kind, sub="", rot=-8, scale=1.0, label=None):
    """Distressed rubber stamp in neon ink."""
    _n[0] += 1
    fid = f"ink{_n[0]}"
    ink = STAMP_INK[kind]
    lab = label or STAMP_LBL[kind]
    w = int((52 + 31 * len(lab)) * scale)
    h = int((112 if sub else 86) * scale)
    subt = (f'<text x="{w / 2}" y="{h * 0.82}" text-anchor="middle" fill="{ink}" stroke="none" font-family="JetBrains Mono" '
            f'font-weight="700" font-size="{19 * scale}" letter-spacing="{2 * scale}">{sub}</text>') if sub else ""
    ty = h * (0.56 if sub else 0.66)
    return f'''<svg class="stamp" width="{w + 20}" height="{h + 20}" viewBox="-10 -10 {w + 20} {h + 20}" style="transform:rotate({rot}deg)" aria-label="{lab}">
  <defs><filter id="{fid}"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="{_n[0] * 5}" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.88" result="m"/>
    <feComposite in="SourceGraphic" in2="m" operator="in"/></filter></defs>
  <g filter="url(#{fid})" fill="none" stroke="{ink}">
    <rect x="2" y="2" width="{w - 4}" height="{h - 4}" rx="{12 * scale}" stroke-width="{5.5 * scale}"/>
    <rect x="{11 * scale}" y="{11 * scale}" width="{w - 22 * scale}" height="{h - 22 * scale}" rx="{7 * scale}" stroke-width="{2 * scale}"/>
    <text x="{w / 2}" y="{ty}" text-anchor="middle" fill="{ink}" stroke="none" font-family="Unbounded" font-weight="900" font-size="{40 * scale}" letter-spacing="{2 * scale}">{lab}</text>
    {subt}
  </g></svg>'''


ICON = {
    "ship": '<path d="M3 15l2 5h14l2-5z M6 15V9h12v6 M12 9V4 M9 6h6" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "bulk": '<path d="M2.5 15l2 5h15l2-5z M5 15c1.5-4.5 4-7 7-7s5.5 2.5 7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M8 15c1-2.5 2.5-4 4-4s3 1.5 4 4z" fill="currentColor" opacity=".45"/>',
    "train": '<rect x="5" y="2.5" width="14" height="14" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M5 10h14 M8.5 20.5l-2 1.5 M15.5 20.5l2 1.5 M9 16.5l-1 4 M15 16.5l1 4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="8.5" cy="13.3" r="1.2" fill="currentColor"/><circle cx="15.5" cy="13.3" r="1.2" fill="currentColor"/>',
    "plane": '<path d="M2.5 13.5l7-1.5L14 4.5c.5-.8 1.8-.6 2 .3l.2.7-2.3 7.3 5.8-1.2c1.4-.3 2.4 1.5 1.3 2.4L3.8 16.5z M6 19.5h12" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "gate": '<path d="M3 21V9l4.5-4 4.5 4v12 M12 21V9l4.5-4L21 9v12 M3 13h18 M3 17.5h18" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "route": '<path d="M3 17c4 0 4.5-10 9-10s5 10 9 10" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="2.5 3" stroke-linecap="round"/><path d="M17.5 14l3.5 3-3.5 3" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
    "clock": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7v5l3.5 2.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
    "doc": '<path d="M5 2.5h9l5 5v14H5z M14 2.5v5h5 M8 12h8 M8 15.5h8 M8 19h5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>',
    "eye": '<path d="M2 12s3.8-7 10-7 10 7 10 7-3.8 7-10 7S2 12 2 12z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="3.2" fill="currentColor"/>',
    "lock": '<rect x="4.5" y="10.5" width="15" height="10.5" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 10.5V7a4 4 0 0 1 8 0v3.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="15.5" r="1.6" fill="currentColor"/>',
    "key": '<circle cx="7.5" cy="8" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10.5 11l9.5 9.5 M15.5 16l2.2-2.2 M18 18.5l2.2-2.2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "search": '<circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M15.5 15.5L21 21" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>',
    "alert": '<path d="M12 3L2 20.5h20z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M12 9.5v5" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><circle cx="12" cy="17.5" r="1.4" fill="currentColor"/>',
    "unload": '<path d="M3 3.5h18 M12 3.5v5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M12 8.5c-1.6 0-1.6 2.4 0 2.4" fill="none" stroke="currentColor" stroke-width="2"/><rect x="5.5" y="12" width="13" height="8.5" rx="1" fill="none" stroke="currentColor" stroke-width="2"/><path d="M9.5 12v8.5 M14.5 12v8.5" stroke="currentColor" stroke-width="1.4"/>',
    "swap": '<path d="M4 8h14l-3.5-3.5 M20 16H6l3.5 3.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
    "fire": '<path d="M12 21.5c-4 0-6.8-2.6-6.8-6.3 0-3.6 2.8-5.6 3.6-9.7 2.3 1.4 3.4 3.6 3.2 5.8 1.2-.8 1.8-2.2 1.7-3.6 2.8 2 4.1 4.8 4.1 7.5 0 3.7-2.8 6.3-5.8 6.3z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "export": '<path d="M3 7.5l7-3.5 7 3.5v8l-7 3.5-7-3.5z M3 7.5l7 3.5 7-3.5 M10 11v8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M15 12.5h7 M19 9.5l3 3-3 3" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
    "warehouse": '<path d="M2.5 21V9.5L12 4l9.5 5.5V21 M6.5 21v-8h11v8 M6.5 17h11" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "comment": '<path d="M4 4.5h16a1.5 1.5 0 0 1 1.5 1.5v10a1.5 1.5 0 0 1-1.5 1.5H10l-5 4v-4H4A1.5 1.5 0 0 1 2.5 16V6A1.5 1.5 0 0 1 4 4.5z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M7 9.5h10 M7 13h6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "bookmark": '<path d="M6 3h12v18l-6-4.5L6 21z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
    "share": '<path d="M21.5 3L10 14.5 M21.5 3l-7 18.5-4.5-7-7-4.5z" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round" stroke-linecap="round"/>',
    "follow": '<circle cx="9" cy="8" r="4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M2 21c.8-4 3.6-6 7-6s6.2 2 7 6 M19 8v6 M16 11h6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "check": '<path d="M4 12.5l5 5L20 6.5" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "x": '<path d="M5.5 5.5l13 13M18.5 5.5l-13 13" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "arrow": '<path d="M4 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>',
    "radar": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.5" fill="none" stroke="currentColor" stroke-width="1.6" opacity=".7"/><path d="M12 12L18.4 5.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><circle cx="16" cy="14.5" r="1.6" fill="currentColor"/>',
    "scale": '<path d="M12 3v18 M6 21h12 M4 7h16 M7 7l-3 6h6z M17 7l-3 6h6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "pen": '<path d="M4 20l1-4.5L16.5 4a2 2 0 0 1 2.8 0l.7.7a2 2 0 0 1 0 2.8L8.5 19z M14 6.5l3.5 3.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "chip": '<rect x="5" y="5" width="14" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><rect x="9" y="9" width="6" height="6" fill="currentColor" opacity=".5"/><path d="M9 2v3 M15 2v3 M9 19v3 M15 19v3 M2 9h3 M2 15h3 M19 9h3 M19 15h3" stroke="currentColor" stroke-width="1.8"/>',
    "door": '<path d="M5 21V3.5h10V21 M3 21h18 M15 5.5l4 1.5V21" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><circle cx="12" cy="12.5" r="1.3" fill="currentColor"/>',
}


def ic(name, size=40, cls=""):
    return f'<svg class="ic {cls}" viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true">{ICON[name]}</svg>'
