import { interpolate } from "remotion";
import { HEIGHT, LED, WIDTH, clamp, easeInOut } from "./timeline";

// A virtual studio camera over the 1088x1920 stage: the stage point (cx, cy)
// lands in the frame center, magnified by s.
export type Cam = { s: number; cx: number; cy: number };

export const WIDE: Cam = { s: 1, cx: 544, cy: 960 };
export const WIDE_PUSH: Cam = { s: 1.08, cx: 544, cy: 900 };
export const LED_FOCUS: Cam = { s: 1.09, cx: 545, cy: 880 };
export const PUSH_CAN: Cam = { s: 1.3, cx: 544, cy: 980 };
export const MED: Cam = { s: 1.42, cx: 544, cy: 1040 };
export const MED_DRIFT: Cam = { s: 1.47, cx: 544, cy: 1035 };
export const MED_TIGHT: Cam = { s: 1.6, cx: 544, cy: 1010 };

type Move = { from: number; to: number; a: Cam; b: Cam; linear?: boolean };

// Hard cuts happen where one move ends on a different framing than the next
// begins. Every lip-sync clip boundary (11.13, 21.88, 29.16, 41.30) sits on a
// cut or under the full-frame takeover, so the pose reset is never seen.
const MOVES: Move[] = [
  { from: 0, to: 11.13, a: WIDE, b: WIDE_PUSH },
  { from: 11.13, to: 15.0, a: MED, b: MED_DRIFT, linear: true },
  { from: 15.0, to: 16.2, a: MED_DRIFT, b: WIDE },
  { from: 16.2, to: 18.9, a: WIDE, b: WIDE },
  { from: 18.9, to: 21.85, a: WIDE, b: LED_FOCUS },
  { from: 21.85, to: 27.75, a: WIDE, b: WIDE },
  { from: 27.75, to: 29.16, a: WIDE, b: PUSH_CAN },
  { from: 29.16, to: 35.0, a: WIDE, b: WIDE_PUSH },
  { from: 35.0, to: 35.9, a: WIDE_PUSH, b: MED },
  { from: 35.9, to: 41.3, a: MED, b: MED_TIGHT, linear: true },
  { from: 41.3, to: 51.0, a: WIDE, b: WIDE_PUSH },
  { from: 51.0, to: 51.7, a: WIDE_PUSH, b: MED },
  { from: 51.7, to: 60, a: MED, b: MED_TIGHT, linear: true },
];

export const cameraAt = (t: number): Cam => {
  const m = MOVES.find((mv) => t >= mv.from && t < mv.to) ?? MOVES[MOVES.length - 1];
  const p = interpolate(t, [m.from, m.to], [0, 1], {
    ...clamp,
    easing: m.linear ? undefined : easeInOut,
  });
  return {
    s: m.a.s + (m.b.s - m.a.s) * p,
    cx: m.a.cx + (m.b.cx - m.a.cx) * p,
    cy: m.a.cy + (m.b.cy - m.a.cy) * p,
  };
};

export const stageTranslate = (c: Cam) =>
  `${WIDTH / 2 - c.cx * c.s}px ${HEIGHT / 2 - c.cy * c.s}px`;

// Where the LED wall lands in frame coordinates for a camera.
export const ledRectInFrame = (c: Cam) => ({
  x: WIDTH / 2 + (LED.x - c.cx) * c.s,
  y: HEIGHT / 2 + (LED.y - c.cy) * c.s,
  w: LED.w * c.s,
  h: LED.h * c.s,
});
