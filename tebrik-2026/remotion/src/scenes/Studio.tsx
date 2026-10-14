import React from "react";
import { Video } from "@remotion/media";
import { AbsoluteFill, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { cameraAt, ledRectInFrame, stageTranslate } from "../camera";
import { LedContent } from "../led/LedContent";
import { BRAND, HEIGHT, LED, LED_DESIGN, PRESENTER, STAGE, TAKEOVER, WIDTH, clamp, easeInOut, sec } from "../timeline";
import { UfukPortrait } from "./UfukPortrait";

// The studio: the presenter take on a virtual camera, with our own graphics on the
// LED wall (so they stay sharp and on cue), plus the full-frame screen takeover.
export const Studio: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const cam = cameraAt(t);
  // Shallow depth of field: the wall softens when the camera is tight on Can.
  const ledBlur = interpolate(cam.s, [1.12, 1.5, 1.72], [0, 6, 9], clamp);

  return (
    <AbsoluteFill style={{ backgroundColor: "#05070F", overflow: "hidden" }}>
      <div
        style={{
          position: "absolute",
          left: 0,
          top: 0,
          width: STAGE.w,
          height: STAGE.h,
          transformOrigin: "0 0",
          translate: stageTranslate(cam),
          scale: cam.s,
        }}
      >
        <Video name="Sunucu" src={staticFile(PRESENTER)} muted style={{ width: STAGE.w, height: STAGE.h }} />
        <div
          style={{
            position: "absolute",
            left: LED.x,
            top: LED.y,
            width: LED.w,
            height: LED.h,
            borderRadius: 6,
            overflow: "hidden",
            boxShadow: "0 0 70px rgba(241,109,37,0.18), 0 0 0 9px #262C3D",
            filter: ledBlur > 0.05 ? `blur(${ledBlur}px)` : undefined,
          }}
        >
          <div style={{ position: "absolute", left: 0, top: 0, transformOrigin: "0 0", scale: LED.w / LED_DESIGN.w }}>
            <LedContent t={t} />
          </div>
          <div
            style={{
              position: "absolute",
              inset: 0,
              background: "linear-gradient(115deg, rgba(255,255,255,0.07) 0%, rgba(255,255,255,0) 35%, rgba(255,255,255,0) 70%, rgba(255,255,255,0.04) 100%)",
            }}
          />
        </div>
      </div>
      <Takeover t={t} />
    </AbsoluteFill>
  );
};

// The LED panel grows to fill the frame for the Ufuk Çetintaş reveal, then
// shrinks back into the wall.
const Takeover: React.FC<{ t: number }> = ({ t }) => {
  if (t < TAKEOVER.inStart || t >= TAKEOVER.outEnd) return null;
  const p =
    t < TAKEOVER.outStart
      ? interpolate(t, [TAKEOVER.inStart, TAKEOVER.inEnd], [0, 1], { ...clamp, easing: easeInOut })
      : interpolate(t, [TAKEOVER.outStart, TAKEOVER.outEnd], [1, 0], { ...clamp, easing: easeInOut });
  const led = ledRectInFrame(cameraAt(t));
  const x = led.x * (1 - p);
  const y = led.y * (1 - p);
  const w = led.w + (WIDTH - led.w) * p;
  const h = led.h + (HEIGHT - led.h) * p;
  const ledOpacity =
    t < TAKEOVER.outStart
      ? interpolate(t, [TAKEOVER.inStart + 0.2, TAKEOVER.inEnd], [1, 0], clamp)
      : interpolate(t, [TAKEOVER.outStart + 0.1, TAKEOVER.outEnd - 0.1], [0, 1], clamp);
  const portraitOpacity =
    t < TAKEOVER.outStart
      ? interpolate(t, [TAKEOVER.inStart + 0.1, TAKEOVER.inEnd - 0.05], [0, 1], clamp)
      : interpolate(t, [TAKEOVER.outStart, TAKEOVER.outStart + 0.25], [1, 0], clamp);
  const ledScale = w / LED_DESIGN.w;
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        width: w,
        height: h,
        overflow: "hidden",
        borderRadius: 6 * (1 - p),
        backgroundColor: BRAND.navy,
        boxShadow: `0 0 ${80 * p}px rgba(0,0,0,0.6)`,
      }}
    >
      <div
        style={{
          position: "absolute",
          left: 0,
          top: (h - LED_DESIGN.h * ledScale) / 2,
          transformOrigin: "0 0",
          scale: ledScale,
          opacity: ledOpacity,
        }}
      >
        <LedContent t={t} withTitle={false} />
      </div>
      <div
        style={{
          position: "absolute",
          left: 0,
          top: 0,
          width: WIDTH,
          height: HEIGHT,
          transformOrigin: "0 0",
          scale: w / WIDTH,
          opacity: portraitOpacity,
        }}
      >
        <Sequence name="Ufuk Çetintaş (tam ekran)" from={sec(TAKEOVER.inStart)} durationInFrames={sec(TAKEOVER.outEnd) - sec(TAKEOVER.inStart)}>
          <UfukPortrait />
        </Sequence>
      </div>
    </div>
  );
};
