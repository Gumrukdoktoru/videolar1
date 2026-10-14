import { Easing, interpolate } from "remotion";

export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;

export const sec = (s: number) => Math.round(s * FPS);

// Master timeline = the client's venue walkthrough (narration starts at 0.62 s).
// The HyperFrames intro covers its first seconds and opens like two doors;
// the HyperFrames outro takes over right after "Herkesin bilgilerine."
export const INTRO = { revealStart: 4.45, end: 4.9 };
export const OUTRO_START = 59.0;
export const OUTRO_DURATION = 6;
export const DURATION_IN_FRAMES = sec(OUTRO_START + OUTRO_DURATION);

export const BRAND = {
  orange: "#F16D25",
  red: "#E8432E",
  anthracite: "#414141",
  navy: "#070B1F",
  navy2: "#121A3D",
  white: "#FFFFFF",
  green: "#38C172",
};

export const easeOut = Easing.bezier(0.16, 1, 0.3, 1);
export const easeIn = Easing.bezier(0.7, 0, 0.84, 0);
export const easeInOut = Easing.bezier(0.65, 0, 0.35, 1);
export const backOut = Easing.bezier(0.34, 1.56, 0.64, 1);
export const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

// 0 → 1 entrance starting at `at` (seconds, master time).
export const appear = (t: number, at: number, dur = 0.4, easing = easeOut) =>
  interpolate(t, [at, at + dur], [0, 1], { ...clamp, easing });

// 0 → 1 exit starting at `at`.
export const leave = (t: number, at: number, dur = 0.3) =>
  interpolate(t, [at, at + dur], [0, 1], { ...clamp, easing: easeIn });
