import React from "react";
import { Audio, Video } from "@remotion/media";
import { AbsoluteFill, Img, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { montserrat } from "./fonts";
import { Captions } from "./overlays/Captions";
import { AnlatimTarzi, Hocalar, Karsilastirma, KayitlarDoldu, Konum, Sahne, SekizinciKat, Siniflar } from "./overlays/Sahneler";
import { BRAND, DURATION_IN_FRAMES, INTRO, OUTRO_DURATION, OUTRO_START, appear, clamp, easeInOut, easeOut, sec } from "./timeline";
import { Icon } from "./ui";

// 9:16 promo: "CAN'LI 7/24 Eğitim Merkezi — Ankara kampı 08 Kasım'da başlıyor".
// Picture and voice: the client's own venue walkthrough (New Park Otel).
// Opening and closing stings: HyperFrames renders in public/hf/.
// Everything else is timed to the narration's word onsets.

const STAMP_AT = 56.88; // "dolmuştur"
const MUSIC_OFFSET = 2; // frames

// Short decaying camera shake when the "DOLDU" stamp lands.
const shakeAt = (t: number, at: number, amp: number) => {
  const d = t - at;
  if (d < 0 || d > 0.3) return { x: 0, y: 0 };
  const k = amp * (1 - d / 0.3);
  return { x: Math.sin(d * 110) * k, y: Math.cos(d * 95) * k * 0.7 };
};

const Footage: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  // The room settles in as the intro doors open, then a slow push-in.
  const settle = interpolate(t, [INTRO.revealStart, INTRO.end + 0.3], [1.1, 1.0], { ...clamp, easing: easeOut });
  const push = interpolate(t, [INTRO.end, OUTRO_START], [1.0, 1.06], clamp);
  const s = shakeAt(t, STAMP_AT, 16);
  return (
    <AbsoluteFill style={{ overflow: "hidden", backgroundColor: BRAND.navy }}>
      <AbsoluteFill style={{ scale: settle * push, translate: `${s.x}px ${s.y}px` }}>
        <Video src={staticFile("media/salon.mp4")} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      </AbsoluteFill>
      {/* Legibility: darker top for the info cards, darker bottom for captions. */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(7,11,31,0.55) 0%, rgba(7,11,31,0.18) 22%, rgba(7,11,31,0) 40%, rgba(0,0,0,0) 62%, rgba(0,0,0,0.6) 100%)",
        }}
      />
    </AbsoluteFill>
  );
};

// Brand bug and the camp date stay on screen through the walkthrough.
const Hud: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  // Local time: this layer's Sequence starts when the intro doors open.
  const p = appear(frame / fps, 0.05, 0.5);
  return (
    <AbsoluteFill style={{ opacity: p }}>
      <div
        style={{
          position: "absolute",
          left: 34,
          top: 40,
          padding: "14px 22px",
          borderRadius: 22,
          backgroundColor: "rgba(7,11,31,0.78)",
          boxShadow: "0 10px 30px rgba(0,0,0,0.35)",
          translate: `${(1 - p) * -40}px 0px`,
        }}
      >
        <Img src={staticFile("logo/logo-canli-dark.svg")} style={{ width: 190, display: "block" }} />
      </div>
      <div
        style={{
          position: "absolute",
          right: 34,
          top: 52,
          display: "flex",
          alignItems: "center",
          gap: 12,
          padding: "14px 24px",
          borderRadius: 999,
          backgroundColor: BRAND.orange,
          boxShadow: "0 10px 30px rgba(241,109,37,0.4)",
          fontFamily: montserrat,
          fontWeight: 900,
          fontSize: 34,
          letterSpacing: 2,
          color: BRAND.white,
          translate: `${(1 - p) * 40}px 0px`,
        }}
      >
        <Icon name="calendar" size={38} color={BRAND.white} stroke={9} /> 08 KASIM
      </div>
    </AbsoluteFill>
  );
};

// HyperFrames intro split into two doors that slide apart onto the room.
const IntroDoors: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const open = interpolate(t, [INTRO.revealStart, INTRO.end], [0, 1], { ...clamp, easing: easeInOut });
  const half = (side: "left" | "right") => (
    <AbsoluteFill
      style={{
        clipPath: side === "left" ? "inset(0 50% 0 0)" : "inset(0 0 0 50%)",
        translate: `${(side === "left" ? -1 : 1) * open * 560}px 0px`,
        boxShadow: "0 0 60px rgba(0,0,0,0.6)",
      }}
    >
      <Video src={staticFile("hf/giris.mp4")} muted style={{ width: "100%", height: "100%" }} />
    </AbsoluteFill>
  );
  return (
    <AbsoluteFill>
      {half("left")}
      {half("right")}
    </AbsoluteFill>
  );
};

const Outro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  // The sting carries its own flash tail on its first frames; keep the cut quick.
  const p = interpolate(t, [0, 0.4], [0, 1], { ...clamp, easing: easeOut });
  return (
    <AbsoluteFill style={{ opacity: Math.min(1, p * 4), scale: 1.06 - 0.06 * p }}>
      <Video src={staticFile("hf/kapanis.mp4")} muted />
    </AbsoluteFill>
  );
};

const Flash: React.FC<{ at: number; peak?: number }> = ({ at, peak = 0.9 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const o = interpolate(frame / fps, [at - 0.05, at, at + 0.3], [0, peak, 0], clamp);
  if (o <= 0) return null;
  return <AbsoluteFill style={{ backgroundColor: "white", opacity: o }} />;
};

export const KampVideo: React.FC = () => {
  const end = DURATION_IN_FRAMES;
  const sfx: { at: number; src: string; volume: number }[] = [
    { at: 2.0, src: "sfx/whip.wav", volume: 0.3 },
    { at: INTRO.revealStart, src: "sfx/whoosh.wav", volume: 0.45 },
    { at: 4.95, src: "sfx/switch.wav", volume: 0.22 },
    { at: 8.32, src: "sfx/switch.wav", volume: 0.2 },
    { at: 9.34, src: "sfx/switch.wav", volume: 0.2 },
    { at: 12.78, src: "sfx/switch.wav", volume: 0.18 },
    { at: 13.9, src: "sfx/switch.wav", volume: 0.18 },
    { at: 16.78, src: "sfx/whip.wav", volume: 0.28 },
    { at: 20.76, src: "sfx/switch.wav", volume: 0.16 },
    { at: 22.62, src: "sfx/switch.wav", volume: 0.16 },
    { at: 24.12, src: "sfx/switch.wav", volume: 0.16 },
    { at: 26.12, src: "sfx/shutter-modern.wav", volume: 0.3 },
    { at: 26.92, src: "sfx/whoosh.wav", volume: 0.3 },
    { at: 35.14, src: "sfx/shutter-modern.wav", volume: 0.3 },
    { at: 36.0, src: "sfx/whip.wav", volume: 0.25 },
    { at: 46.12, src: "sfx/ding.wav", volume: 0.14 },
    { at: 49.3, src: "sfx/ding.wav", volume: 0.14 },
    { at: STAMP_AT - 0.03, src: "sfx/shutter-modern.wav", volume: 0.5 },
    { at: OUTRO_START - 0.1, src: "sfx/whoosh.wav", volume: 0.45 },
  ];
  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.navy }}>
      <Sequence name="Salon (müşteri videosu)" durationInFrames={sec(OUTRO_START)}>
        <Footage />
      </Sequence>
      <Konum />
      <Hocalar />
      <Sahne />
      <SekizinciKat />
      <Karsilastirma />
      <AnlatimTarzi />
      <Siniflar />
      <KayitlarDoldu />
      <Sequence name="Logo + tarih" from={sec(INTRO.end)} durationInFrames={sec(OUTRO_START) - sec(INTRO.end)}>
        <Hud />
      </Sequence>
      <Sequence name="Giriş (HyperFrames)" durationInFrames={sec(INTRO.end)}>
        <IntroDoors />
      </Sequence>
      <Captions />
      <Sequence name="Kapanış (HyperFrames)" from={sec(OUTRO_START)} durationInFrames={sec(OUTRO_DURATION)}>
        <Outro />
      </Sequence>
      <Flash at={STAMP_AT} peak={0.35} />
      <Flash at={OUTRO_START} peak={0.45} />

      <Audio name="Anlatım (müşteri videosu)" src={staticFile("media/anlatim.m4a")} />
      {/* ElevenLabs Music v2.5 take whose first hit (1.99 s) is nudged onto "8 Kasım" (2.06 s). */}
      <Sequence name="Müzik" from={MUSIC_OFFSET} layout="none">
        <Audio
          src={staticFile("media/muzik.mp3")}
          volume={(f) =>
            interpolate(
              f + MUSIC_OFFSET,
              [0, sec(0.5), sec(0.9), sec(OUTRO_START - 0.3), sec(OUTRO_START + 0.4), end - sec(0.8), end],
              [0.5, 0.5, 0.13, 0.13, 0.85, 0.85, 0],
              clamp,
            )
          }
        />
      </Sequence>
      {sfx.map((s, i) => (
        <Sequence key={i} name="SFX" from={Math.max(0, sec(s.at))} durationInFrames={sec(1.5)} layout="none">
          <Audio src={staticFile(s.src)} volume={s.volume} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
