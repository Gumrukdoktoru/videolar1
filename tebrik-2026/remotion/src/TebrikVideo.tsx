import React from "react";
import { Audio, Video } from "@remotion/media";
import { AbsoluteFill, Sequence, interpolate, staticFile } from "remotion";
import { Captions } from "./overlays/Captions";
import { Confetti, Flash, LowerThird, Snow, StatCards, Vignette } from "./overlays/Graphics";
import { Studio } from "./scenes/Studio";
import { DURATION_IN_FRAMES, OUTRO_DURATION, OUTRO_START, TAKEOVER, clamp, sec } from "./timeline";

// Master 9:16 film: "2026 Gümrük Sınavları — hocalarımıza teşekkür".
// Voice: ElevenLabs "CAn Yılmaz2" (eleven_v4). Presenter: OmniHuman 1.5 lip-sync.
// LED title + logo outro: HyperFrames renders in public/hf/.
// Overlay layers below read master-timeline seconds, so their Sequences start at 0.
const MUSIC_START = 2.5;

export const TebrikVideo: React.FC = () => {
  const sfx: { at: number; src: string; volume: number }[] = [
    { at: 0.0, src: "sfx/switch.wav", volume: 0.35 },
    { at: 11.2, src: "sfx/whoosh.wav", volume: 0.4 },
    { at: 13.2, src: "sfx/whoosh.wav", volume: 0.3 },
    { at: 18.9, src: "sfx/switch.wav", volume: 0.22 },
    { at: 19.88, src: "sfx/switch.wav", volume: 0.22 },
    { at: 20.88, src: "sfx/switch.wav", volume: 0.22 },
    { at: TAKEOVER.inStart, src: "sfx/whoosh.wav", volume: 0.45 },
    { at: 25.64, src: "sfx/ding.wav", volume: 0.18 },
    { at: TAKEOVER.outStart, src: "sfx/whoosh.wav", volume: 0.35 },
    { at: 31.16, src: "sfx/switch.wav", volume: 0.22 },
    { at: 32.08, src: "sfx/switch.wav", volume: 0.22 },
    { at: OUTRO_START - 0.08, src: "sfx/whip.wav", volume: 0.5 },
  ];
  const end = DURATION_IN_FRAMES;
  return (
    <AbsoluteFill style={{ backgroundColor: "black" }}>
      <Sequence name="Stüdyo" durationInFrames={sec(OUTRO_START)}>
        <Studio />
      </Sequence>
      <Sequence name="Alt bant" durationInFrames={sec(6.9)}>
        <LowerThird />
      </Sequence>
      <Sequence name="Rakamlar" durationInFrames={sec(15.4)}>
        <StatCards />
      </Sequence>
      <Sequence name="Kar" durationInFrames={sec(OUTRO_START)}>
        <Snow from={46.8} to={OUTRO_START} />
      </Sequence>
      <Sequence name="Konfeti" durationInFrames={sec(OUTRO_START)}>
        <Confetti at={52.72} />
      </Sequence>
      <Vignette />
      <Captions />
      <Sequence name="Kapanış logo (HyperFrames)" from={sec(OUTRO_START)} durationInFrames={sec(OUTRO_DURATION)}>
        <Video src={staticFile("hf/kapanis-logo.mp4")} muted />
      </Sequence>
      <Flash at={OUTRO_START} />

      <Audio name="Seslendirme" src={staticFile("media/seslendirme.wav")} />
      {/* Music enters after the cold-open line so its swell lands on "Yolunuz açık…". */}
      <Sequence name="Müzik" from={sec(MUSIC_START)} layout="none">
        <Audio
          src={staticFile("media/muzik.mp3")}
          volume={(f) =>
            interpolate(
              f + sec(MUSIC_START),
              [sec(MUSIC_START), sec(MUSIC_START) + 20, sec(56.2), sec(56.9), end - 20, end],
              [0, 0.13, 0.13, 0.5, 0.5, 0],
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
