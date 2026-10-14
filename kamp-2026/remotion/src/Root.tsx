import React from "react";
import { Composition } from "remotion";
import { KampVideo } from "./KampVideo";
import { DURATION_IN_FRAMES, FPS, HEIGHT, WIDTH } from "./timeline";

export const RemotionRoot: React.FC = () => (
  <Composition
    id="KampTanitim"
    component={KampVideo}
    durationInFrames={DURATION_IN_FRAMES}
    fps={FPS}
    width={WIDTH}
    height={HEIGHT}
  />
);
