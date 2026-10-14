import React, { useCallback, useEffect, useMemo, useState } from "react";
import { createTikTokStyleCaptions } from "@remotion/captions";
import type { Caption, TikTokPage } from "@remotion/captions";
import { AbsoluteFill, Sequence, interpolate, staticFile, useCurrentFrame, useDelayRender, useVideoConfig } from "remotion";
import { montserrat } from "../fonts";
import { BRAND, OUTRO_START, clamp, easeOut } from "../timeline";

// Word-by-word captions of the client's narration (Scribe timings, names and
// mis-heard words corrected by hand in altyazi.json).
const SWITCH_CAPTIONS_EVERY_MS = 1300;

const CaptionPage: React.FC<{ page: TikTokPage }> = ({ page }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const absoluteMs = page.startMs + (frame / fps) * 1000;
  const enter = interpolate(frame, [0, 5], [0, 1], { ...clamp, easing: easeOut });
  return (
    <AbsoluteFill style={{ justifyContent: "flex-start", alignItems: "center" }}>
      <div
        style={{
          position: "absolute",
          top: 1450,
          width: 960,
          textAlign: "center",
          fontFamily: montserrat,
          fontWeight: 800,
          fontSize: 64,
          lineHeight: 1.18,
          whiteSpace: "pre-wrap",
          color: BRAND.white,
          WebkitTextStroke: "12px rgba(0,0,0,0.92)",
          paintOrder: "stroke fill",
          textShadow: "0 6px 18px rgba(0,0,0,0.55)",
          opacity: enter,
          translate: `0px ${(1 - enter) * 18}px`,
        }}
      >
        {page.tokens.map((token, i) => {
          const active = token.fromMs <= absoluteMs && token.toMs > absoluteMs;
          // Keep the leading space outside the scaled word so the pop never eats it.
          const lead = token.text.match(/^\s*/)?.[0] ?? "";
          return (
            <React.Fragment key={`${token.fromMs}-${i}`}>
              {lead}
              <span
                style={{
                  color: active ? BRAND.orange : BRAND.white,
                  display: "inline-block",
                  padding: "0 4px",
                  scale: active ? 1.06 : 1,
                  whiteSpace: "pre",
                }}
              >
                {token.text.slice(lead.length)}
              </span>
            </React.Fragment>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

export const Captions: React.FC = () => {
  const { fps } = useVideoConfig();
  const [captions, setCaptions] = useState<Caption[] | null>(null);
  const { delayRender, continueRender, cancelRender } = useDelayRender();
  const [handle] = useState(() => delayRender("Loading captions"));

  const fetchCaptions = useCallback(async () => {
    try {
      const res = await fetch(staticFile("altyazi.json"));
      setCaptions((await res.json()) as Caption[]);
      continueRender(handle);
    } catch (e) {
      cancelRender(e);
    }
  }, [continueRender, cancelRender, handle]);

  useEffect(() => {
    fetchCaptions();
  }, [fetchCaptions]);

  const pages = useMemo(() => {
    if (!captions) return [];
    return createTikTokStyleCaptions({
      captions,
      combineTokensWithinMilliseconds: SWITCH_CAPTIONS_EVERY_MS,
    }).pages;
  }, [captions]);

  const lastFrame = Math.round(OUTRO_START * fps);
  return (
    <AbsoluteFill>
      {pages.map((page, index) => {
        const next = pages[index + 1] ?? null;
        const startFrame = Math.round((page.startMs / 1000) * fps);
        const endFrame = Math.min(
          next ? Math.round((next.startMs / 1000) * fps) : Infinity,
          startFrame + Math.round((SWITCH_CAPTIONS_EVERY_MS / 1000) * fps) + 15,
          lastFrame,
        );
        if (endFrame - startFrame <= 0) return null;
        return (
          <Sequence key={index} name="Altyazı" from={startFrame} durationInFrames={endFrame - startFrame}>
            <CaptionPage page={page} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
