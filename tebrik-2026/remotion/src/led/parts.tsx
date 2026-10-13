import React from "react";
import { Img, interpolate, staticFile } from "remotion";
import { montserrat } from "../fonts";
import { BRAND, TEACHERS, TeacherKey, clamp, easeOut } from "../timeline";

export const appear = (t: number, at: number, dur = 0.4) =>
  interpolate(t, [at, at + dur], [0, 1], { ...clamp, easing: easeOut });

// Screen-wide look: deep navy, warm glow, faint LED pixel grid and scanlines.
export const LedBackground: React.FC<{ tint?: number; glow?: string }> = ({
  tint = 0,
  glow = "rgba(241,109,37,0.28)",
}) => (
  <>
    <div
      style={{
        position: "absolute",
        inset: 0,
        background: `radial-gradient(ellipse 70% 80% at 50% 60%, ${glow} 0%, rgba(241,109,37,0) 60%), linear-gradient(160deg, ${BRAND.navy2} 0%, ${BRAND.navy} 70%)`,
      }}
    />
    <div
      style={{
        position: "absolute",
        inset: 0,
        backgroundColor: "rgba(110,170,255,1)",
        opacity: tint * 0.22,
        mixBlendMode: "screen",
      }}
    />
    <div
      style={{
        position: "absolute",
        inset: 0,
        backgroundImage:
          "repeating-linear-gradient(0deg, rgba(255,255,255,0.035) 0px, rgba(255,255,255,0.035) 1px, transparent 1px, transparent 4px), repeating-linear-gradient(90deg, rgba(0,0,0,0.18) 0px, rgba(0,0,0,0.18) 1px, transparent 1px, transparent 4px)",
      }}
    />
  </>
);

// Channel bug that keeps the brand on the studio wall.
export const LedBug: React.FC = () => (
  <>
    <Img
      src={staticFile("logo/logo-canli-dark.svg")}
      style={{ position: "absolute", left: 36, top: 28, width: 150 }}
    />
    <div
      style={{
        position: "absolute",
        right: 40,
        top: 40,
        fontFamily: montserrat,
        fontWeight: 700,
        fontSize: 22,
        letterSpacing: 4,
        color: BRAND.orange,
      }}
    >
      2026 GÜMRÜK SINAVLARI
    </div>
  </>
);

export const TeacherCard: React.FC<{
  who: TeacherKey;
  t: number;
  at: number;
  x: number;
  y: number;
  w: number;
  h: number;
  slotsAt?: number;
  plate?: number;
}> = ({ who, t, at, x, y, w, h, slotsAt, plate = 64 }) => {
  const teacher = TEACHERS[who];
  const p = appear(t, at, 0.45);
  const slot = slotsAt === undefined ? 0 : appear(t, slotsAt, 0.3) * (1 - p);
  const sweep = interpolate(t, [at + 0.15, at + 0.85], [-60, 160], clamp);
  const imgH = h - plate - 6;
  const nameSize = Math.min(34, (w - 28) / (teacher.name.length * 0.68));
  return (
    <div style={{ position: "absolute", left: x, top: y, width: w, height: h }}>
      {slot > 0 ? (
        <div
          style={{
            position: "absolute",
            inset: 0,
            borderRadius: 18,
            border: "3px dashed rgba(255,255,255,0.35)",
            opacity: slot,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "rgba(255,255,255,0.4)",
            fontFamily: montserrat,
            fontWeight: 900,
            fontSize: 120,
          }}
        >
          ?
        </div>
      ) : null}
      <div
        style={{
          position: "absolute",
          inset: 0,
          borderRadius: 18,
          overflow: "hidden",
          opacity: p,
          translate: `0px ${(1 - p) * 60}px`,
          scale: 0.92 + 0.08 * p,
          background:
            "linear-gradient(180deg, rgba(241,109,37,0.42) 0%, rgba(30,36,80,0.92) 62%, rgba(10,14,34,1) 100%)",
          boxShadow: "0 18px 40px rgba(0,0,0,0.45), inset 0 0 0 2px rgba(255,255,255,0.14)",
        }}
      >
        <div
          style={{
            position: "absolute",
            left: "50%",
            bottom: plate - 4,
            width: w * 1.1,
            height: w * 0.9,
            translate: "-50% 30%",
            background: "radial-gradient(circle, rgba(241,109,37,0.55) 0%, rgba(241,109,37,0) 65%)",
          }}
        />
        <Img
          src={staticFile(teacher.img)}
          style={{
            position: "absolute",
            bottom: plate,
            left: "50%",
            height: imgH,
            translate: `-50% ${(1 - p) * 40}px`,
            filter: "drop-shadow(0 8px 18px rgba(0,0,0,0.5))",
          }}
        />
        <div
          style={{
            position: "absolute",
            left: 0,
            right: 0,
            bottom: 0,
            height: plate,
            backgroundColor: BRAND.orange,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontFamily: montserrat,
            fontWeight: 800,
            fontSize: nameSize,
            color: BRAND.white,
            letterSpacing: 1,
            whiteSpace: "nowrap",
          }}
        >
          {teacher.name}
        </div>
        <div
          style={{
            position: "absolute",
            top: 0,
            bottom: 0,
            width: "45%",
            left: `${sweep}%`,
            background:
              "linear-gradient(100deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.35) 50%, rgba(255,255,255,0) 100%)",
          }}
        />
      </div>
    </div>
  );
};

// Small inline icons (stroke style), sized by the parent.
export const Icon: React.FC<{
  name: "pin" | "snow" | "door" | "laptop" | "cap" | "heart" | "check";
  size: number;
  color?: string;
  stroke?: number;
  rotate?: number;
}> = ({ name, size, color = BRAND.orange, stroke = 5, rotate = 0 }) => {
  const common = {
    fill: "none",
    stroke: color,
    strokeWidth: stroke,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
  };
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" style={{ rotate: `${rotate}deg` }}>
      {name === "pin" ? (
        <>
          <path d="M50 92 C30 66 20 52 20 38 A30 30 0 0 1 80 38 C80 52 70 66 50 92 Z" {...common} />
          <circle cx="50" cy="38" r="11" {...common} />
        </>
      ) : null}
      {name === "snow" ? (
        <g {...common}>
          {[0, 60, 120].map((a) => (
            <g key={a} transform={`rotate(${a} 50 50)`}>
              <line x1="50" y1="8" x2="50" y2="92" />
              <polyline points="38,18 50,28 62,18" />
              <polyline points="38,82 50,72 62,82" />
            </g>
          ))}
        </g>
      ) : null}
      {name === "door" ? (
        <>
          <path d="M24 92 V12 H76 V92" {...common} />
          <path d="M24 92 L60 82 V20 L24 12" {...common} fill={color} fillOpacity={0.25} />
          <circle cx="52" cy="54" r="3.5" fill={color} />
          <line x1="12" y1="92" x2="88" y2="92" {...common} />
        </>
      ) : null}
      {name === "laptop" ? (
        <>
          <rect x="18" y="22" width="64" height="42" rx="4" {...common} />
          <path d="M8 76 H92 L84 64 H16 Z" {...common} />
        </>
      ) : null}
      {name === "cap" ? (
        <>
          <path d="M50 18 L94 38 L50 58 L6 38 Z" {...common} fill={color} fillOpacity={0.25} />
          <path d="M24 48 V70 C24 78 76 78 76 70 V48" {...common} />
          <path d="M88 41 V66" {...common} />
          <circle cx="88" cy="70" r="4" fill={color} />
        </>
      ) : null}
      {name === "heart" ? (
        <path
          d="M50 86 C20 64 8 48 8 32 C8 18 20 8 32 8 C40 8 46 12 50 20 C54 12 60 8 68 8 C80 8 92 18 92 32 C92 48 80 64 50 86 Z"
          fill={color}
          stroke="none"
        />
      ) : null}
      {name === "check" ? <polyline points="18,52 40,74 82,28" {...common} /> : null}
    </svg>
  );
};
