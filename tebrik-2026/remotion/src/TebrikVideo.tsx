import React from "react";
import { Audio, Video } from "@remotion/media";
import { AbsoluteFill, Sequence, staticFile } from "remotion";
import { Captions } from "./overlays/Captions";
import { Confetti, Flash, LowerThird, Snow, StatCards, Vignette } from "./overlays/Graphics";
import { Studio } from "./scenes/Studio";
import { OUTRO_DURATION, OUTRO_START, SOUNDTRACK, sec } from "./timeline";

// Master 9:16 film: "2026 Gümrük Sınavları — hocalarımıza teşekkür".
// Presenter and soundtrack: the user's own video (background keyed out).
// LED title + logo outro: HyperFrames renders in public/hf/.
// Overlay layers below read master-timeline seconds, so their Sequences start at 0.
export const TebrikVideo: React.FC = () => {
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

      {/* Voice, music and effects come mixed in the user's video. */}
      <Audio name="Ses (kullanıcı videosu)" src={staticFile(SOUNDTRACK)} />
    </AbsoluteFill>
  );
};
