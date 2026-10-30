"""Shared building blocks for the lesson compositions (scene wrapper, icons, badges, timing lookup)."""
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
    "search": '<circle cx="10" cy="10" r="6.5" fill="none" stroke="currentColor" stroke-width="2.6"/><path d="M15 15l6 6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "arrow": '<path d="M4 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>',
    "shield": '<path d="M12 2.5l8 3v6c0 5-3.4 8.6-8 10-4.6-1.4-8-5-8-10v-6z" fill="currentColor"/><path d="M8 12l3 3 5-6" fill="none" stroke="#06221a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z" fill="currentColor"/><path d="M10 20.5a2.2 2.2 0 0 0 4 0" fill="none" stroke="currentColor" stroke-width="2.2"/>',
    "share": '<circle cx="18" cy="5" r="2.8" fill="currentColor"/><circle cx="6" cy="12" r="2.8" fill="currentColor"/><circle cx="18" cy="19" r="2.8" fill="currentColor"/><path d="M8.5 10.7l7-4.2M8.5 13.3l7 4.2" stroke="currentColor" stroke-width="2.2"/>',
    "question": '<circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M9 9.2a3 3 0 1 1 4.2 2.8c-.9.4-1.2 1-1.2 2" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><circle cx="12" cy="17.3" r="1.4" fill="currentColor"/>',
    "mail": '<rect x="2.5" y="5" width="19" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M3 6l9 7 9-7" fill="none" stroke="currentColor" stroke-width="2.2"/>',
    "cd": '<circle cx="12" cy="12" r="10" fill="currentColor" opacity=".25"/><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M6.5 9.5a6 6 0 0 1 3-3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>',
    "code": '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M13.5 4.5l-3 15" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    "calc": '<rect x="4" y="2.5" width="16" height="19" rx="2.5" fill="none" stroke="currentColor" stroke-width="2.2"/><rect x="7" y="5.5" width="10" height="4" rx="1" fill="currentColor"/><path d="M8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01M16 17h.01" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "chip": '<rect x="6" y="6" width="12" height="12" rx="1.5" fill="none" stroke="currentColor" stroke-width="2.2"/><rect x="9.5" y="9.5" width="5" height="5" fill="currentColor"/><path d="M9 2.5v3M15 2.5v3M9 18.5v3M15 18.5v3M2.5 9h3M2.5 15h3M18.5 9h3M18.5 15h3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "film": '<rect x="2.5" y="4" width="19" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M7 4v16M17 4v16M2.5 8.5H7M2.5 15.5H7M17 8.5h4.5M17 15.5h4.5" stroke="currentColor" stroke-width="2"/>',
    "music": '<path d="M9 18V5l11-2v13" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><circle cx="6.5" cy="18" r="2.8" fill="currentColor"/><circle cx="17.5" cy="16" r="2.8" fill="currentColor"/>',
    "export": '<path d="M4 15v5h16v-5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M12 15V3.5M7 8l5-5 5 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    "pause": '<rect x="5.5" y="4" width="4.5" height="16" rx="1.2" fill="currentColor"/><rect x="14" y="4" width="4.5" height="16" rx="1.2" fill="currentColor"/>',
    "pen": '<path d="M4 20l1.2-4.8L16 4.4a2 2 0 0 1 2.8 0l.8.8a2 2 0 0 1 0 2.8L8.8 18.8z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M14 6.5l3.5 3.5" stroke="currentColor" stroke-width="2.2"/>',
    "receipt": '<path d="M5 2.5h14v19l-2.3-1.6-2.4 1.6-2.3-1.6-2.3 1.6-2.4-1.6L5 21.5z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M8.5 8h7M8.5 11.5h7M8.5 15h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "clock": '<circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M12 6.5V12l3.8 2.6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    "scale": '<path d="M12 3.5v16.5M6.5 20.5h11M3.5 7h17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><circle cx="12" cy="3.6" r="1.6" fill="currentColor"/><path d="M3.5 7L1 13h5zM20.5 7L18 13h5z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M1 13a2.5 2.5 0 0 0 5 0zM18 13a2.5 2.5 0 0 0 5 0z" fill="currentColor"/>',
    "mask": '<path d="M2.5 3.5h11v6.5a5.5 5.5 0 0 1-11 0z" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/><path d="M5.6 7.6h.01M10.4 7.6h.01" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><path d="M5.6 11a3 3 0 0 0 4.8 0" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><path d="M15.5 8.5h6v5.5a5.5 5.5 0 0 1-9.4 3.9" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round" stroke-linecap="round"/><path d="M16.6 15.6a3 3 0 0 1 3.8 0" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/>',
    "gavel": '<path d="M14.2 2.4l7.4 7.4-3.2 3.2-7.4-7.4z" fill="currentColor"/><path d="M13.2 10.8L3.6 20.4" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M12.5 21.5h9" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
    "lira": '<path d="M8.5 3v17.5c5.2 0 9-3.4 9-8.5M5 11l9.5-4M5 15.2l9.5-4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    "gear": '<circle cx="12" cy="12" r="6.4" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="12" cy="12" r="2.4" fill="currentColor"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/>',
    "gem": '<path d="M6 3.5h12l3.5 5L12 21 2.5 8.5z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M2.5 8.5h19M9 3.5l-1.5 5L12 21l4.5-12.5L15 3.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>',
    "ship": '<path d="M2.5 14.5h19l-3 5.5h-13z" fill="currentColor"/><path d="M6 14.5V9h12v5.5M9.5 9V5h5v4" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
    "battery": '<rect x="2.5" y="7" width="17" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M21.5 10.3v3.4" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><path d="M6.5 9.8v4.4M10 9.8v4.4M13.5 9.8v4.4" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
    "flame": '<path d="M12 2.5c1 4 5.5 5.6 5.5 11a5.5 5.5 0 0 1-11 0c0-3 1.6-4.6 2.6-6 .3 2 1.2 3 2.2 3.4C10.6 8 11 5 12 2.5z" fill="currentColor"/>',
    "shoe": '<path d="M2.5 17.5V8.5h5l2 3.5c3 .8 7 1.5 9.5 2.6 1.4.6 2.5 1.6 2.5 2.9H2.5z" fill="currentColor"/><path d="M2.5 20.5h19" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
    "box": '<path d="M12 2.5l9 4.5v10l-9 4.5-9-4.5V7zM3 7l9 4.5L21 7M12 11.5v10" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/>',
    "globe": '<circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M2.5 12h19M12 2.5c3.4 3 3.4 16 0 19M12 2.5c-3.4 3-3.4 16 0 19" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "layers": '<path d="M12 3l9.5 5-9.5 5-9.5-5z" fill="currentColor"/><path d="M2.5 12.5l9.5 5 9.5-5M2.5 16.5l9.5 5 9.5-5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
    "ruler": '<rect x="2" y="7.5" width="20" height="9" rx="1.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M6 7.5v3.5M10 7.5v5M14 7.5v3.5M18 7.5v5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "sort": '<path d="M7 4v16M3.5 16.5L7 20l3.5-3.5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M13 6h8M13 11h6M13 16h4" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
    "percent": '<path d="M19 5L5 19" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><circle cx="7" cy="7" r="2.8" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="17" cy="17" r="2.8" fill="none" stroke="currentColor" stroke-width="2.4"/>',
    "bin": '<path d="M4 6.5h16M9.5 6.5V4h5v2.5M6 6.5l1.2 14h9.6L18 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M10 10v7.5M14 10v7.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "stamp": '<path d="M9 3.5h6v5.5l3 3H6l3-3z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><rect x="4" y="12" width="16" height="4.5" rx="1" fill="currentColor"/><path d="M4 20h16" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
    "bed": '<path d="M2.5 18.5V6M2.5 14h19v4.5M21.5 14v-2.5a3 3 0 0 0-3-3H10v5.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><circle cx="6.3" cy="10.8" r="2.2" fill="currentColor"/>',
    "fish": '<path d="M2.5 12c3-4.5 8-6 12-4.2 2 .9 3.4 2.4 4.3 4.2-.9 1.8-2.3 3.3-4.3 4.2-4 1.8-9 .3-12-4.2z" fill="currentColor"/><path d="M18.8 12l3-3.3v6.6z" fill="currentColor"/><circle cx="7.5" cy="11" r="1.2" fill="#071A45"/>',
    "skate": '<path d="M5 3.5h6l1 6.5 6.5 2.5c1.2.5 2 1.6 2 2.9V16H4.5z" fill="currentColor"/><path d="M3 19.5h17.5M7 16v3.5M16 16v3.5" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
    "bottle": '<path d="M9.5 2.5h5v3.5c0 1 1.5 2 2 3.5v11a1 1 0 0 1-1 1h-7a1 1 0 0 1-1-1v-11c.5-1.5 2-2.5 2-3.5z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><rect x="7.6" y="12" width="8.8" height="5" fill="currentColor"/>',
    "container": '<rect x="2.5" y="6" width="19" height="11.5" rx="1" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M6.5 8.5v6.5M10 8.5v6.5M13.5 8.5v6.5M17 8.5v6.5" stroke="currentColor" stroke-width="1.8"/><circle cx="6.5" cy="19.5" r="1.6" fill="currentColor"/><circle cx="17.5" cy="19.5" r="1.6" fill="currentColor"/>',
    "seed": '<path d="M12 2.5c4.6 3.4 6.6 7.4 6.6 11a6.6 6.6 0 0 1-13.2 0c0-3.6 2-7.6 6.6-11z" fill="currentColor"/><path d="M12 9v10" stroke="#071A45" stroke-width="1.8" stroke-linecap="round"/>',
    "radio": '<rect x="5" y="8" width="14" height="13.5" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M12 8V2.5M9 4.5a4.5 4.5 0 0 1 6 0" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="13" r="2.2" fill="currentColor"/><path d="M8.5 18h7" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "wheat": '<path d="M12 21.5V7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M12 7.5C9.6 7.1 8.2 5.4 8.2 3c2.4.4 3.8 2.1 3.8 4.5zM12 7.5c2.4-.4 3.8-2.1 3.8-4.5-2.4.4-3.8 2.1-3.8 4.5zM12 12.5c-2.4-.4-3.8-2.1-3.8-4.5 2.4.4 3.8 2.1 3.8 4.5zM12 12.5c2.4-.4 3.8-2.1 3.8-4.5-2.4.4-3.8 2.1-3.8 4.5zM12 17.5c-2.4-.4-3.8-2.1-3.8-4.5 2.4.4 3.8 2.1 3.8 4.5zM12 17.5c2.4-.4 3.8-2.1 3.8-4.5-2.4.4-3.8 2.1-3.8 4.5z" fill="currentColor"/>',
    "microwave": '<rect x="2" y="5" width="20" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><rect x="5" y="8" width="10" height="8" rx="1" fill="currentColor" opacity=".4"/><path d="M18.5 8.5v.01M18.5 12v.01M18.5 15.5v.01" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>',
    "flask": '<path d="M8.5 2.5h7M10 2.5v14a2 2 0 0 0 4 0v-14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M10 11.5h4v5a2 2 0 0 1-4 0z" fill="currentColor"/><path d="M5 21.5h14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "drop": '<path d="M12 2.5c3.8 4.6 6.5 8.2 6.5 11.7a6.5 6.5 0 0 1-13 0c0-3.5 2.7-7.1 6.5-11.7z" fill="currentColor"/><path d="M9 14.5a3 3 0 0 0 3 3" fill="none" stroke="#071A45" stroke-width="1.8" stroke-linecap="round"/>',
    "car": '<path d="M3 13l2-5.5A2 2 0 0 1 6.9 6h10.2a2 2 0 0 1 1.9 1.5L21 13v5h-2.5M5.5 18H3v-5h18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><circle cx="7.5" cy="18" r="2.2" fill="currentColor"/><circle cx="16.5" cy="18" r="2.2" fill="currentColor"/>',
    "truck": '<path d="M2.5 6h11v10h-11zM13.5 9.5h4l3.5 3.5v3h-7.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><circle cx="6.5" cy="17.5" r="2.2" fill="currentColor"/><circle cx="17" cy="17.5" r="2.2" fill="currentColor"/>',
    "cane": '<path d="M9.5 21.5V7.5a3.5 3.5 0 0 1 7 0v1.5" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/><path d="M8 16.5h3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "ring": '<circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="3.4"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="2 2"/>',
    "hover": '<path d="M4 12.5h16a2 2 0 0 1 0 4H4a2 2 0 0 1 0-4z" fill="currentColor"/><path d="M7 12.5V9a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v3.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M3 20h3M10.5 20h3M18 20h3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "case": '<rect x="3.5" y="4.5" width="17" height="15" rx="2.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M3.5 10h17" stroke="currentColor" stroke-width="2"/><path d="M7 14.5h10" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
    "bridge": '<path d="M2.5 8.5h12l6 3v5.5h-18z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M6 17v4M14 17v4" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><path d="M5.5 12.5h2M9.5 12.5h2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "salt": '<path d="M8 8h8l1.5 13.5h-11z" fill="currentColor"/><path d="M8.5 8V5.5a3.5 3.5 0 0 1 7 0V8" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10.5 4.5h.01M13.5 4.5h.01M12 6.2h.01" stroke="#071A45" stroke-width="1.6" stroke-linecap="round"/>',
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
function count(sel, at, from, to, dur, dec) {
  const els = q(sel), st = { v: from };
  const fmt = (v) => { const p = v.toFixed(dec || 0).split("."); return p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".") + (p[1] ? "," + p[1] : ""); };
  tl.fromTo(st, { v: from }, { v: to, duration: dur || 1, ease: "power2.out", onUpdate: () => els.forEach((e) => { e.textContent = fmt(st.v); }) }, at);
}
function pulse(sel, at, s) { tl.fromTo(q(sel), { scale: 1 }, { scale: s || 1.12, duration: 0.18, yoyo: true, repeat: 1, ease: "power2.out", transformOrigin: "50% 50%" }, at); }
function write(sel, at, dur) { tl.fromTo(q(sel), { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: dur || 0.8, ease: "power1.inOut" }, at); }
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
