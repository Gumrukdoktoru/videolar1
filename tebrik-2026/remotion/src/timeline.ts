import { Easing } from "remotion";

export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;

export const sec = (s: number) => Math.round(s * FPS);

// The presenter is the user's own video, used as-is: only its room background
// was keyed out and the person placed (scaled, not altered) into the studio
// plate. One continuous take on the master timeline.
export const PRESENTER = "media/sunucu.mp4";
// Soundtrack: the audio of the same video (voice, music and effects in one).
export const SOUNDTRACK = "media/ses.m4a";

export const OUTRO_START = 53.73;
export const OUTRO_DURATION = 6;
export const DURATION_IN_FRAMES = sec(OUTRO_START) + sec(OUTRO_DURATION);

// The studio stage is a 1088x1920 frame. The LED wall in it (bezel included)
// sits at x 50..1040, y 62..642; the overlay bezel (9px) covers the plate bezel.
export const STAGE = { w: 1088, h: 1920 };
export const LED = { x: 50, y: 62, w: 990, h: 580 };
// LED content is designed on a 1280x750 canvas (same aspect as the wall).
export const LED_DESIGN = { w: 1280, h: 750 };

// Full-frame "screen takeover" for the Ufuk Çetintaş reveal.
export const TAKEOVER = { inStart: 21.45, inEnd: 21.85, outStart: 27.35, outEnd: 27.75 };

export const BRAND = {
  orange: "#F16D25",
  anthracite: "#414141",
  navy: "#070B1F",
  navy2: "#121A3D",
  white: "#FFFFFF",
};

export const easeOut = Easing.bezier(0.16, 1, 0.3, 1);
export const easeInOut = Easing.bezier(0.65, 0, 0.35, 1);
export const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

export const TEACHERS = {
  baset: { name: "BASET TEMİZ", img: "hocalar/baset-temiz.png", ratio: 308 / 532 },
  harun: { name: "HARUN ALTINSOY", img: "hocalar/harun-altinsoy.png", ratio: 305 / 503 },
  erkan: { name: "ERKAN YAVUZ", img: "hocalar/erkan-yavuz.png", ratio: 276 / 524 },
  ufuk: { name: "UFUK ÇETİNTAŞ", img: "hocalar/ufuk-cetintas.png", ratio: 252 / 443 },
  hakan: { name: "HAKAN UÇAK", img: "hocalar/hakan-ucak.png", ratio: 303 / 529 },
  ahmet: { name: "AHMET ERCAN İLGÜZ", img: "hocalar/ahmet-ercan-ilguz.png", ratio: 283 / 571 },
} as const;

export type TeacherKey = keyof typeof TEACHERS;
