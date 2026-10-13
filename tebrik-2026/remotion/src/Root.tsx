import React from "react";
import { Composition, Folder } from "remotion";
import { TebrikVideo } from "./TebrikVideo";
import { LowerThird, StatCards } from "./overlays/Graphics";
import { UfukPortrait } from "./scenes/UfukPortrait";
import { DURATION_IN_FRAMES, FPS, HEIGHT, TAKEOVER, WIDTH, sec } from "./timeline";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="TebrikVideo"
        component={TebrikVideo}
        durationInFrames={DURATION_IN_FRAMES}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
      />
      <Folder name="Sahneler">
        <Composition
          id="UfukPortrait"
          component={UfukPortrait}
          durationInFrames={sec(TAKEOVER.outEnd) - sec(TAKEOVER.inStart)}
          fps={FPS}
          width={WIDTH}
          height={HEIGHT}
        />
        <Composition id="LowerThird" component={LowerThird} durationInFrames={sec(7)} fps={FPS} width={WIDTH} height={HEIGHT} />
        <Composition id="StatCards" component={StatCards} durationInFrames={sec(16)} fps={FPS} width={WIDTH} height={HEIGHT} />
      </Folder>
    </>
  );
};
