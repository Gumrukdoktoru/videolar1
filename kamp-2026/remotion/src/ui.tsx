import React from "react";
import { Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { montserrat } from "./fonts";
import { BRAND, sec } from "./timeline";

// A named slot on the master timeline. Children get master-time seconds, so
// every cue can be written with the narration's word timings directly.
export const Beat: React.FC<{
  name: string;
  from: number;
  to: number;
  children: (t: number) => React.ReactNode;
}> = ({ name, from, to, children }) => (
  <Sequence name={name} from={sec(from)} durationInFrames={sec(to) - sec(from)}>
    <BeatBody from={from}>{children}</BeatBody>
  </Sequence>
);

const BeatBody: React.FC<{ from: number; children: (t: number) => React.ReactNode }> = ({ from, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return <>{children(from + frame / fps)}</>;
};

// Frosted navy card used by every information beat.
export const Panel: React.FC<{
  x: number;
  y: number;
  w: number;
  h?: number;
  style?: React.CSSProperties;
  children?: React.ReactNode;
}> = ({ x, y, w, h, style, children }) => (
  <div
    style={{
      position: "absolute",
      left: x,
      top: y,
      width: w,
      height: h,
      borderRadius: 30,
      backgroundColor: "rgba(7,11,31,0.80)",
      backdropFilter: "blur(14px)",
      boxShadow: "0 24px 60px rgba(0,0,0,0.45), inset 0 0 0 2px rgba(255,255,255,0.10)",
      fontFamily: montserrat,
      color: BRAND.white,
      overflow: "hidden",
      ...style,
    }}
  >
    {children}
  </div>
);

// Small spaced heading with an orange bar.
export const Kicker: React.FC<{ text: string; p: number; color?: string; size?: number }> = ({
  text,
  p,
  color = BRAND.orange,
  size = 30,
}) => (
  <div style={{ display: "flex", alignItems: "center", gap: 16, opacity: p }}>
    <div style={{ width: 70 * p, height: 8, borderRadius: 4, backgroundColor: color }} />
    <div
      style={{
        fontFamily: montserrat,
        fontWeight: 800,
        fontSize: size,
        letterSpacing: 6 - 3 * p,
        color,
        whiteSpace: "nowrap",
      }}
    >
      {text}
    </div>
  </div>
);

export type IconName =
  | "pin"
  | "check"
  | "cross"
  | "screen"
  | "podium"
  | "flower"
  | "calendar"
  | "users"
  | "bolt";

export const Icon: React.FC<{ name: IconName; size: number; color?: string; stroke?: number }> = ({
  name,
  size,
  color = BRAND.orange,
  stroke = 7,
}) => {
  const c = {
    fill: "none",
    stroke: color,
    strokeWidth: stroke,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
  };
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" style={{ flexShrink: 0 }}>
      {name === "pin" ? (
        <>
          <path d="M50 94 C30 68 18 54 18 38 A32 32 0 0 1 82 38 C82 54 70 68 50 94 Z" fill={color} />
          <circle cx="50" cy="38" r="12" fill={BRAND.navy} />
        </>
      ) : null}
      {name === "check" ? <polyline points="16,54 40,78 86,26" {...c} /> : null}
      {name === "cross" ? (
        <>
          <line x1="22" y1="22" x2="78" y2="78" {...c} />
          <line x1="78" y1="22" x2="22" y2="78" {...c} />
        </>
      ) : null}
      {name === "screen" ? (
        <>
          <rect x="8" y="16" width="84" height="54" rx="6" {...c} />
          <line x1="50" y1="70" x2="50" y2="84" {...c} />
          <line x1="30" y1="86" x2="70" y2="86" {...c} />
        </>
      ) : null}
      {name === "podium" ? (
        <>
          <path d="M22 30 H78 L70 92 H30 Z" {...c} />
          <line x1="14" y1="30" x2="86" y2="30" {...c} />
          <path d="M50 30 V14 M42 12 H58" {...c} />
        </>
      ) : null}
      {name === "flower" ? (
        <g {...c}>
          {[0, 72, 144, 216, 288].map((a) => (
            <ellipse key={a} cx="50" cy="28" rx="12" ry="20" transform={`rotate(${a} 50 50)`} />
          ))}
          <circle cx="50" cy="50" r="8" fill={color} />
        </g>
      ) : null}
      {name === "calendar" ? (
        <>
          <rect x="12" y="20" width="76" height="68" rx="8" {...c} />
          <line x1="12" y1="40" x2="88" y2="40" {...c} />
          <line x1="32" y1="10" x2="32" y2="28" {...c} />
          <line x1="68" y1="10" x2="68" y2="28" {...c} />
        </>
      ) : null}
      {name === "users" ? (
        <g {...c}>
          <circle cx="36" cy="34" r="14" />
          <path d="M10 86 C10 64 22 56 36 56 C50 56 62 64 62 86" />
          <circle cx="70" cy="30" r="11" />
          <path d="M66 52 C80 52 90 60 90 80" />
        </g>
      ) : null}
      {name === "bolt" ? <path d="M58 6 L22 56 H48 L40 94 L78 40 H52 Z" fill={color} /> : null}
    </svg>
  );
};
