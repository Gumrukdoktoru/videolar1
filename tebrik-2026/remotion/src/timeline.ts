import { Easing } from "remotion";

export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;

export const sec = (s: number) => Math.round(s * FPS);

// Presenter lip-sync clips (OmniHuman 1.5), cut from the voiceover at pauses.
// start/end are positions on the master timeline in seconds.
export const CHUNKS = [
  { src: "media/sunucu-1.mp4", start: 0, end: 11.13 },
  { src: "media/sunucu-2.mp4", start: 11.13, end: 21.88 },
  { src: "media/sunucu-3.mp4", start: 21.88, end: 29.16 },
  { src: "media/sunucu-4.mp4", start: 29.16, end: 41.3 },
  { src: "media/sunucu-5.mp4", start: 41.3, end: 53.9 },
] as const;

export const OUTRO_START = 53.73;
export const OUTRO_DURATION = 6;
export const DURATION_IN_FRAMES = sec(OUTRO_START) + sec(OUTRO_DURATION);

// The studio stage is the 1088x1920 lip-sync frame. The LED wall in it (bezel
// included) was measured at x 50..1040, y 62..642 and is stable in every clip.
export const STAGE = { w: 1088, h: 1920 };
export const LED = { x: 50, y: 62, w: 990, h: 580 };
// LED content is designed on a 1280x750 canvas (same aspect as the wall).
export const LED_DESIGN = { w: 1280, h: 750 };

// Full-frame "screen takeover" for the Ufuk Çetintaş reveal; it also covers the
// lip-sync clip boundary at 21.88 s.
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
