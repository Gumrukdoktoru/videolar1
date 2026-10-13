import React from "react";
import { AbsoluteFill, Img, interpolate, random, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { montserrat } from "../fonts";
import { BRAND, clamp, easeInOut, easeOut } from "../timeline";
import { appear } from "../led/parts";

const useT = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return frame / fps;
};

// TV-style name strap for the presenter while the opening title plays.
export const LowerThird: React.FC = () => {
  const t = useT();
  const inP = interpolate(t, [1.0, 1.6], [0, 1], { ...clamp, easing: easeOut });
  const outP = interpolate(t, [6.2, 6.7], [0, 1], { ...clamp, easing: easeInOut });
  const wipe = inP * (1 - outP);
  return (
    <AbsoluteFill>
      <div
        style={{
          position: "absolute",
          left: 70,
          top: 1500,
          clipPath: `inset(0 ${100 - wipe * 100}% 0 0)`,
          fontFamily: montserrat,
        }}
      >
        <div style={{ display: "flex", alignItems: "stretch" }}>
          <div style={{ width: 14, backgroundColor: BRAND.orange }} />
          <div
            style={{
              padding: "14px 30px 10px 24px",
              backgroundColor: "rgba(7,11,31,0.86)",
              color: BRAND.white,
              fontSize: 68,
              fontWeight: 900,
              letterSpacing: 1,
            }}
          >
            CAN YILMAZ
          </div>
        </div>
        <div
          style={{
            display: "inline-block",
            marginLeft: 14,
            padding: "10px 24px",
            backgroundColor: BRAND.orange,
            color: BRAND.white,
            fontSize: 30,
            fontWeight: 800,
            letterSpacing: 3,
          }}
        >
          7/24 CAN&apos;LI EĞİTİM MERKEZİ
        </div>
      </div>
    </AbsoluteFill>
  );
};

const StatCard: React.FC<{ t: number; at: number; value: number; prefix?: string; label: string; x: number; accent: string }> = ({
  t,
  at,
  value,
  prefix = "",
  label,
  x,
  accent,
}) => {
  const p = appear(t, at - 0.15, 0.45);
  const out = interpolate(t, [14.85, 15.25], [0, 1], { ...clamp, easing: easeInOut });
  const n = Math.round(interpolate(t, [at, at + 0.9], [0, value], { ...clamp, easing: easeOut }));
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: 150,
        width: 440,
        height: 300,
        borderRadius: 28,
        backgroundColor: "rgba(7,11,31,0.72)",
        border: `3px solid ${accent}`,
        boxShadow: "0 20px 50px rgba(0,0,0,0.45)",
        backdropFilter: "blur(10px)",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: montserrat,
        color: BRAND.white,
        opacity: p * (1 - out),
        translate: `0px ${(1 - p) * 50 - out * 80}px`,
        scale: 0.9 + 0.1 * p,
      }}
    >
      <div style={{ fontSize: 150, fontWeight: 900, lineHeight: 1, color: accent }}>
        {prefix}
        {n}
      </div>
      <div style={{ fontSize: 38, fontWeight: 800, marginTop: 14, letterSpacing: 1 }}>{label}</div>
    </div>
  );
};

// Big numbers over the presenter close-up: "1241 meslektaşımız ve 200 koçluk öğrencimiz".
export const StatCards: React.FC = () => {
  const t = useT();
  return (
    <AbsoluteFill>
      <StatCard t={t} at={11.42} value={1241} label="MESLEKTAŞIMIZ" x={70} accent={BRAND.orange} />
      <StatCard t={t} at={13.36} value={200} prefix="+" label="KOÇLUK ÖĞRENCİMİZ" x={570} accent={BRAND.white} />
    </AbsoluteFill>
  );
};

// "Ankara'nın soğuğunda" — snow over the whole frame, with a cold grade.
export const Snow: React.FC<{ from: number; to: number }> = ({ from, to }) => {
  const t = useT();
  const { width, height } = useVideoConfig();
  const fade = Math.min(appear(t, from, 0.8), 1 - interpolate(t, [to - 0.4, to], [0, 1], clamp));
  if (fade <= 0) return null;
  const flakes = new Array(110).fill(0).map((_, i) => {
    const depth = random(`d${i}`);
    const size = 4 + depth * 12;
    const speed = 120 + depth * 260;
    const x0 = random(`x${i}`) * width;
    const y0 = random(`y${i}`) * (height + 200);
    const y = ((y0 + (t - from) * speed) % (height + 200)) - 100;
    const x = x0 + Math.sin(t * (0.8 + depth) + i) * (18 + depth * 30);
    return { x, y, size, depth, i };
  });
  const cold = interpolate(t, [from, from + 0.8, 50.6, 51.4], [0, 1, 1, 0.35], clamp);
  return (
    <AbsoluteFill style={{ opacity: fade }}>
      <AbsoluteFill style={{ backgroundColor: "rgba(120,170,255,0.14)", mixBlendMode: "screen", opacity: cold }} />
      {flakes.map((f) => (
        <div
          key={f.i}
          style={{
            position: "absolute",
            left: f.x,
            top: f.y,
            width: f.size,
            height: f.size,
            borderRadius: "50%",
            backgroundColor: "white",
            opacity: 0.35 + f.depth * 0.55,
            filter: f.depth > 0.8 ? "blur(2px)" : undefined,
          }}
        />
      ))}
    </AbsoluteFill>
  );
};

// Brand-colored confetti on "başarınız daim olsun!".
export const Confetti: React.FC<{ at: number }> = ({ at }) => {
  const t = useT();
  const { width, height } = useVideoConfig();
  const dt = t - at;
  if (dt < 0) return null;
  const colors = [BRAND.orange, BRAND.white, "#FFC24B", BRAND.orange];
  return (
    <AbsoluteFill style={{ opacity: interpolate(dt, [1.6, 2.2], [1, 0], clamp) }}>
      {new Array(70).fill(0).map((_, i) => {
        const side = i % 2 === 0 ? -1 : 1;
        const vx = side * -(260 + random(`vx${i}`) * 520);
        const vy = -(1300 + random(`vy${i}`) * 900);
        const x = (side < 0 ? 0 : width) + vx * dt;
        const y = height * 0.92 + vy * dt + 0.5 * 2600 * dt * dt;
        const rot = (random(`r${i}`) - 0.5) * 1440 * dt;
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: x,
              top: y,
              width: 14,
              height: 26,
              borderRadius: 3,
              backgroundColor: colors[i % colors.length],
              rotate: `${rot}deg`,
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

// Warm flash used to punch into the HyperFrames logo outro.
export const Flash: React.FC<{ at: number; dur?: number }> = ({ at, dur = 0.35 }) => {
  const t = useT();
  const o = interpolate(t, [at - dur / 2, at, at + dur / 2], [0, 1, 0], clamp);
  if (o <= 0) return null;
  return (
    <AbsoluteFill
      style={{
        opacity: o,
        background: "radial-gradient(circle at 50% 45%, #FFFFFF 0%, #FFD2A8 30%, rgba(241,109,37,0.9) 65%, rgba(241,109,37,0) 100%)",
        mixBlendMode: "screen",
      }}
    />
  );
};

export const Vignette: React.FC = () => (
  <AbsoluteFill
    style={{
      background: "radial-gradient(ellipse 85% 70% at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.45) 100%)",
    }}
  />
);

// Small corner logo used in the full-frame scene.
export const CornerLogo: React.FC<{ width?: number }> = ({ width = 210 }) => (
  <Img src={staticFile("logo/logo-canli-dark.svg")} style={{ position: "absolute", left: 60, top: 80, width }} />
);
