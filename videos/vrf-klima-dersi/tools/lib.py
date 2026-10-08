"""Shared building blocks for the VRF lesson compositions (scene wrapper, icons, timing lookup)."""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TIMING = json.load(open(ROOT / "timing.json"))
SCENES = {s["id"]: s for s in TIMING["scenes"]}


def _norm(w):
    return re.sub(r"[^\wçğıöşüİ']", "", w.lower().replace("i̇", "i"))


def T(sid, word, n=1, off=0.0):
    """Scene-local time of the n-th word in scene `sid` starting with `word`."""
    prefix = word.endswith("*")
    key = _norm(word.rstrip("*"))
    c = 0
    for x in SCENES[sid]["words"]:
        w = _norm(x["w"])
        if (w.startswith(key) if prefix else w == key):
            c += 1
            if c == n:
                return round(x["t"] + off, 2)
    raise KeyError(f"{sid}: word '{word}' #{n} not found")


def D(sid):
    return SCENES[sid]["dur"]


# ---------- icons (24x24 viewBox, stroke = currentColor) ----------
ICON = {
    "star": '<path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9z" fill="currentColor"/>',
    "eye": '<path d="M1.5 12S5.5 4.8 12 4.8 22.5 12 22.5 12 18.5 19.2 12 19.2 1.5 12 1.5 12z" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="12" cy="12" r="3.6" fill="currentColor"/>',
    "warn": '<path d="M12 2.5L23 21.5H1z" fill="currentColor"/><path d="M12 9v6" stroke="#2a0a0e" stroke-width="2.6" stroke-linecap="round"/><circle cx="12" cy="18.2" r="1.5" fill="#2a0a0e"/>',
    "trap": '<path d="M3 17h18M5 17l2-8 3 5 2-7 2 7 3-5 2 8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/><circle cx="12" cy="20.5" r="1.6" fill="currentColor"/>',
    "check": '<path d="M4 12.5l5 5L20 6.5" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>',
    "x": '<path d="M5 5l14 14M19 5L5 19" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"/>',
    "bulb": '<path d="M12 2.5a7 7 0 0 0-4 12.7V18h8v-2.8A7 7 0 0 0 12 2.5z" fill="currentColor"/><path d="M9 20.5h6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
    "doc": '<path d="M5 2.5h9l5 5v14H5z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M14 2.5v5h5M8 12h8M8 15.5h8M8 19h5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "building": '<path d="M3 21h18M5 21V9l7-5 7 5v12M9 21v-6h6v6M8 11h2M14 11h2" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>',
    "uni": '<path d="M2 9l10-5 10 5-10 5z" fill="currentColor"/><path d="M6 11v5c0 1.6 2.7 3 6 3s6-1.4 6-3v-5M21 9v6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
    "search": '<circle cx="10" cy="10" r="6.5" fill="none" stroke="currentColor" stroke-width="2.6"/><path d="M15 15l6 6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "valve": '<path d="M3 6l9 6-9 6zM21 6l-9 6 9 6z" fill="currentColor"/><path d="M12 12V3M8.5 3h7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
    "pipes": '<path d="M12 3v7M12 10L5 16M12 10l7 6M12 10v8M5 16v4M19 16v4M12 18v3" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><rect x="8" y="1" width="8" height="4" rx="1" fill="currentColor"/>',
    "gauge": '<path d="M3.5 17a9 9 0 1 1 17 0" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><path d="M12 15l5-6" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><circle cx="12" cy="15.5" r="2" fill="currentColor"/>',
    "net": '<circle cx="12" cy="4.5" r="2.5" fill="currentColor"/><circle cx="4.5" cy="19" r="2.5" fill="currentColor"/><circle cx="12" cy="19" r="2.5" fill="currentColor"/><circle cx="19.5" cy="19" r="2.5" fill="currentColor"/><path d="M12 7v9.5M12 10.5L4.5 16.5M12 10.5l7.5 6" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="2.5 2"/>',
    "arrow": '<path d="M4 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>',
    "shield": '<path d="M12 2.5l8 3v6c0 5-3.4 8.6-8 10-4.6-1.4-8-5-8-10v-6z" fill="currentColor"/><path d="M8 12l3 3 5-6" fill="none" stroke="#06221a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z" fill="currentColor"/><path d="M10 20.5a2.2 2.2 0 0 0 4 0" fill="none" stroke="currentColor" stroke-width="2.2"/>',
    "share": '<circle cx="18" cy="5" r="2.8" fill="currentColor"/><circle cx="6" cy="12" r="2.8" fill="currentColor"/><circle cx="18" cy="19" r="2.8" fill="currentColor"/><path d="M8.5 10.7l7-4.2M8.5 13.3l7 4.2" stroke="currentColor" stroke-width="2.2"/>',
    "question": '<circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M9 9.2a3 3 0 1 1 4.2 2.8c-.9.4-1.2 1-1.2 2" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><circle cx="12" cy="17.3" r="1.4" fill="currentColor"/>',
    "mail": '<rect x="2.5" y="5" width="19" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M3 6l9 7 9-7" fill="none" stroke="currentColor" stroke-width="2.2"/>',
    "flame": '<path d="M12 2.5c1 3.5 5.5 5.5 5.5 11a5.5 5.5 0 0 1-11 0c0-2.5 1.3-4 2.3-5 .2 1.8 1 2.8 2 3.2C10.5 8.5 11 5.5 12 2.5z" fill="currentColor"/>',
    "snow": '<path d="M12 2v20M3.3 7l17.4 10M20.7 7L3.3 17M9.5 3.5L12 6l2.5-2.5M9.5 20.5L12 18l2.5 2.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
}


def icon(name, size=40, cls=""):
    return f'<svg class="ico {cls}" viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true">{ICON[name]}</svg>'


BADGE = {
    "onemli": ("ÖNEMLİ", "star"),
    "dikkat": ("DİKKAT", "eye"),
    "uyari": ("UYARI", "warn"),
    "tuzak": ("TUZAK", "trap"),
    "ipucu": ("İPUCU", "bulb"),
    "soru": ("SORU", "question"),
}


def badge(kind, extra_id="", big=False):
    label, ic = BADGE[kind]
    idattr = f' id="{extra_id}"' if extra_id else ""
    size = "badge-big" if big else ""
    return f'<div{idattr} class="badge b-{kind} {size}"><span class="bi">{icon(ic, 44 if big else 34)}</span><span class="bt">{label}</span></div>'


# ---------- HVAC drawing pieces (SVG fragments in user units) ----------
def odu(x, y, cls="odu", w=170, h=120, label=""):
    """Outdoor unit: box + fan; fan group carries class fan for rotation."""
    cx, cy, r = 62, h / 2, 40
    blades = "".join(
        f'<path d="M{cx} {cy} Q {cx + 30} {cy - 14} {cx + 34} {cy - 2} Q {cx + 18} {cy + 6} {cx} {cy}z" transform="rotate({a} {cx} {cy})" fill="#9CC0FF"/>'
        for a in (0, 120, 240)
    )
    grille = "".join(f'<line x1="{118 + i * 11}" y1="20" x2="{118 + i * 11}" y2="{h - 20}" stroke="#5B7FD6" stroke-width="3"/>' for i in range(4))
    lab = f'<text x="{w / 2}" y="{h + 34}" class="svgl" text-anchor="middle">{label}</text>' if label else ""
    return (
        f'<g transform="translate({x} {y})"><g class="{cls}">'
        f'<rect width="{w}" height="{h}" rx="14" fill="#17295E" stroke="#8FB2FF" stroke-width="4"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0E1C46" stroke="#8FB2FF" stroke-width="3"/>'
        f'<g class="fan" data-cx="{cx}" data-cy="{cy}">{blades}</g>'
        f'<circle cx="{cx}" cy="{cy}" r="6" fill="#DCE7FF"/>{grille}{lab}</g></g>'
    )


def idu(x, y, cls="idu", w=170, h=54, label="", tag=""):
    """Indoor wall unit."""
    lab = f'<text x="{w / 2}" y="{h + 34}" class="svgl" text-anchor="middle">{label}</text>' if label else ""
    tg = f'<text x="{w / 2}" y="{-14}" class="svgt" text-anchor="middle">{tag}</text>' if tag else ""
    return (
        f'<g transform="translate({x} {y})"><g class="{cls}">'
        f'<rect width="{w}" height="{h}" rx="16" fill="#EAF0FF" stroke="#8FB2FF" stroke-width="3"/>'
        f'<path d="M14 {h - 14} H {w - 14}" stroke="#93A6D6" stroke-width="4" stroke-linecap="round"/>'
        f'<circle cx="{w - 20}" cy="16" r="5" class="led" fill="#2ED47A"/>{tg}{lab}</g></g>'
    )


def valve(x, y, cls="valve", s=1.0):
    return (
        f'<g transform="translate({x} {y}) scale({s})"><g class="{cls}">'
        f'<path d="M-18 -13 L0 0 L-18 13z M18 -13 L0 0 L18 13z" fill="#FFC53D" stroke="#3a2a00" stroke-width="2"/>'
        f'<path d="M0 0 V-22 M-9 -22 H9" stroke="#FFC53D" stroke-width="4" stroke-linecap="round"/></g></g>'
    )


SCENE_HELPERS = r"""
const SID = "__SID__";
const R = document.getElementById(SID);
const q = (s) => R.querySelectorAll(s);
const tl = gsap.timeline({ paused: true });
function draw(sel, at, dur, ease) {
  q(sel).forEach((p) => { p.setAttribute("pathLength", "1"); p.style.strokeDasharray = "1 1"; p.style.strokeDashoffset = "1"; });
  tl.fromTo(q(sel), { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: dur || 0.8, ease: ease || "power2.inOut", stagger: 0.12 }, at);
}
function pop(sel, at, stagger, ease) {
  tl.fromTo(q(sel), { scale: 0.2, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.5, ease: ease || "back.out(2.2)", stagger: stagger || 0 }, at);
}
function rise(sel, at, stagger, dy) {
  tl.fromTo(q(sel), { y: dy == null ? 46 : dy, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "power3.out", stagger: stagger || 0 }, at);
}
function slideX(sel, at, dx, stagger) {
  tl.fromTo(q(sel), { x: dx, opacity: 0 }, { x: 0, opacity: 1, duration: 0.65, ease: "expo.out", stagger: stagger || 0 }, at);
}
function fadeIn(sel, at, dur) { tl.fromTo(q(sel), { opacity: 0 }, { opacity: 1, duration: dur || 0.4, ease: "power1.out" }, at); }
function fadeTo(sel, at, v, dur) { tl.to(q(sel), { opacity: v, duration: dur || 0.4, ease: "power1.inOut" }, at); }
function slam(sel, at) {
  tl.fromTo(q(sel), { scale: 2.6, opacity: 0, rotation: -8, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, rotation: 0, duration: 0.42, ease: "expo.in" }, at);
  tl.fromTo(q(sel), { x: -6 }, { x: 0, duration: 0.3, ease: "elastic.out(1.2,0.3)" }, at + 0.42);
}
function flow(sel, from, to, speed) {
  q(sel).forEach((p, i) => {
    const sp = Array.isArray(speed) ? speed[i % speed.length] : speed || 60;
    tl.fromTo(p, { strokeDashoffset: 0 }, { strokeDashoffset: -sp * (to - from), duration: to - from, ease: "none" }, from);
  });
}
function spinFans(from, to, rps) {
  q(".fan").forEach((f, i) => {
    const cx = f.dataset.cx, cy = f.dataset.cy, st = { d: i * 37 };
    tl.fromTo(st, { d: i * 37 }, { d: i * 37 + 360 * (rps || 1.2) * (to - from), duration: to - from, ease: "none",
      onUpdate: () => f.setAttribute("transform", `rotate(${st.d} ${cx} ${cy})`) }, from);
  });
}
function breathe(sel, from, to, amp, period) {
  const n = Math.max(0, Math.floor((to - from) / (period || 2.4)) - 1);
  tl.fromTo(q(sel), { scale: 1, transformOrigin: "50% 50%" }, { scale: 1 + (amp || 0.04), duration: (period || 2.4) / 2, ease: "sine.inOut", yoyo: true, repeat: n * 2 + 1 }, from);
}
function strike(sel, at, dur) { tl.fromTo(q(sel), { scaleX: 0 }, { scaleX: 1, duration: dur || 0.45, ease: "power2.out" }, at); }
function exitAll(at) { tl.to(q(".stage"), { opacity: 0, y: -24, duration: 0.35, ease: "power2.in" }, at); }
"""


def scene(sid, body, css, js, keys, exit=True):
    dur = D(sid)
    helpers = SCENE_HELPERS.replace("__SID__", sid)
    helpers += f"\nconst D = {dur};\nconst K = {json.dumps(keys)};\n"
    return f"""<!doctype html>
<html lang="tr">
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>
        #{sid} {{ position: absolute; inset: 0; overflow: hidden; }}
        #{sid} .stage {{ position: absolute; inset: 0; }}
{css}
      </style>
      <div id="{sid}" data-composition-id="{sid}" data-width="1920" data-height="1080" data-duration="{dur}">
        <div class="stage">
{body}
        </div>
      </div>
      <script>
(() => {{
{helpers}
{js}
{f"exitAll({round(dur - 0.42, 2)});" if exit else ""}
window.__timelines["{sid}"] = tl;
}})();
      </script>
    </template>
  </body>
</html>
"""
