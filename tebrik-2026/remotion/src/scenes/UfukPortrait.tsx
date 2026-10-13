import React from "react";
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { montserrat } from "../fonts";
import { BRAND, TAKEOVER, TEACHERS, clamp, easeOut } from "../timeline";
import { LedBackground, appear } from "../led/parts";
import { CornerLogo } from "../overlays/Graphics";

// Full-frame portrait scene for "günün her saatinde ekran arkasındaki gizli
// kahramanımız, Gümrük Koçu Ufuk Çetintaş'a…". Local frame 0 = TAKEOVER.inStart.
export const UfukPortrait: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = TAKEOVER.inStart + frame / fps;
  const line = (at: number) => {
    const p = appear(t, at, 0.45);
    return { opacity: p, translate: `0px ${(1 - p) * 40}px` };
  };
  const reveal = interpolate(t, [25.64, 26.2], [0, 1], { ...clamp, easing: easeOut });
  const sweep = interpolate(t, [25.6, 26.4], [-40, 140], clamp);
  const clockAngle = interpolate(t, [22.1, 27.4], [0, 720], clamp);
  const monitorIn = appear(t, 21.9, 0.6);
  const dotOn = Math.floor(t * 2) % 2 === 0;
  return (
    <AbsoluteFill style={{ overflow: "hidden", backgroundColor: BRAND.navy }}>
      <LedBackground />
      <CornerLogo />
      <div style={{ position: "absolute", left: 0, right: 0, top: 210, textAlign: "center", fontFamily: montserrat, color: BRAND.white }}>
        <div style={{ fontSize: 40, fontWeight: 700, letterSpacing: 8, color: "rgba(255,255,255,0.8)", ...line(22.12) }}>GÜNÜN HER SAATİNDE</div>
        <div style={{ fontSize: 66, fontWeight: 900, marginTop: 14, ...line(23.36) }}>EKRAN ARKASINDAKİ</div>
        <div style={{ fontSize: 84, fontWeight: 900, color: BRAND.orange, ...line(24.32) }}>GİZLİ KAHRAMAN</div>
      </div>

      {/* Monitor with the hero inside */}
      <div
        style={{
          position: "absolute",
          left: 150,
          top: 520,
          width: 780,
          height: 860,
          borderRadius: 34,
          backgroundColor: "#0D1330",
          border: "10px solid #232B52",
          boxShadow: `0 30px 80px rgba(0,0,0,0.55), 0 0 ${60 + reveal * 60}px rgba(241,109,37,${0.25 + reveal * 0.35})`,
          overflow: "hidden",
          opacity: monitorIn,
          scale: 0.94 + 0.06 * monitorIn,
        }}
      >
        <div
          style={{
            position: "absolute",
            inset: 0,
            background: "radial-gradient(circle at 50% 75%, rgba(241,109,37,0.55) 0%, rgba(241,109,37,0) 60%)",
          }}
        />
        <div
          style={{
            position: "absolute",
            left: 26,
            top: 22,
            display: "flex",
            alignItems: "center",
            gap: 12,
            fontFamily: montserrat,
            fontWeight: 800,
            fontSize: 30,
            color: BRAND.white,
            letterSpacing: 2,
          }}
        >
          <div style={{ width: 20, height: 20, borderRadius: 10, backgroundColor: dotOn ? "#FF3B30" : "rgba(255,59,48,0.35)" }} />
          CANLI · 7/24
        </div>
        {/* 7/24 clock */}
        <div style={{ position: "absolute", right: 30, top: 18, width: 70, height: 70 }}>
          <div style={{ position: "absolute", inset: 0, borderRadius: 35, border: `5px solid ${BRAND.orange}` }} />
          <div
            style={{
              position: "absolute",
              left: 32,
              top: 12,
              width: 6,
              height: 25,
              borderRadius: 3,
              backgroundColor: BRAND.white,
              transformOrigin: "50% 100%",
              rotate: `${clockAngle}deg`,
            }}
          />
        </div>
        <Img
          src={staticFile(TEACHERS.ufuk.img)}
          style={{
            position: "absolute",
            bottom: 0,
            left: "50%",
            height: 740,
            translate: "-50% 0px",
            filter: `brightness(${reveal}) drop-shadow(0 0 ${18 - reveal * 10}px rgba(241,109,37,${0.95 - reveal * 0.5}))`,
          }}
        />
        <div
          style={{
            position: "absolute",
            top: 0,
            bottom: 0,
            width: "40%",
            left: `${sweep}%`,
            background: "linear-gradient(100deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.45) 50%, rgba(255,255,255,0) 100%)",
          }}
        />
      </div>

      <div style={{ position: "absolute", left: 0, right: 0, top: 1410, textAlign: "center", fontFamily: montserrat }}>
        <div
          style={{
            display: "inline-block",
            padding: "12px 36px",
            borderRadius: 50,
            backgroundColor: BRAND.orange,
            color: BRAND.white,
            fontSize: 44,
            fontWeight: 800,
            letterSpacing: 4,
            ...line(25.64),
          }}
        >
          GÜMRÜK KOÇU
        </div>
        <div style={{ fontSize: 96, fontWeight: 900, color: BRAND.white, marginTop: 18, ...line(26.32) }}>UFUK ÇETİNTAŞ</div>
      </div>
    </AbsoluteFill>
  );
};
