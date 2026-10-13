import React from "react";
import { Video } from "@remotion/media";
import { Img, Sequence, interpolate, staticFile } from "remotion";
import { montserrat } from "../fonts";
import { BRAND, LED_DESIGN, TEACHERS, TeacherKey, clamp, easeOut, sec } from "../timeline";
import { Icon, LedBackground, LedBug, TeacherCard, appear } from "./parts";

// Everything that plays on the studio LED wall, on a 1280x750 design canvas.
// `t` is master-timeline seconds; word cues come from the voiceover alignment.

const H: React.CSSProperties = {
  position: "absolute",
  left: 0,
  right: 0,
  textAlign: "center",
  fontFamily: montserrat,
  color: BRAND.white,
  whiteSpace: "nowrap",
};

const rise = (t: number, at: number, dist = 40, dur = 0.4) => {
  const p = appear(t, at, dur);
  return { opacity: p, translate: `0px ${(1 - p) * dist}px` };
};

const countUp = (t: number, at: number, dur: number, to: number) =>
  Math.round(
    interpolate(t, [at, at + dur], [0, to], {
      ...clamp,
      easing: easeOut,
    }),
  );

const Stats: React.FC<{ t: number }> = ({ t }) => (
  <>
    <LedBackground />
    <LedBug />
    <div style={{ ...H, top: 150, fontSize: 30, fontWeight: 700, letterSpacing: 8, color: BRAND.orange, ...rise(t, 11.2) }}>
      2026 HAZIRLIK DÖNEMİ
    </div>
    <div style={{ position: "absolute", left: 640, top: 250, width: 3, height: 380, backgroundColor: "rgba(255,255,255,0.2)" }} />
    <div style={{ ...H, left: 0, right: 640, top: 250, ...rise(t, 11.42) }}>
      <div style={{ fontSize: 190, fontWeight: 900, color: BRAND.orange, lineHeight: 1 }}>
        {countUp(t, 11.42, 1.0, 1241)}
      </div>
      <div style={{ fontSize: 44, fontWeight: 800, marginTop: 16 }}>MESLEKTAŞIMIZ</div>
    </div>
    <div style={{ ...H, left: 640, right: 0, top: 250, ...rise(t, 13.36) }}>
      <div style={{ fontSize: 190, fontWeight: 900, lineHeight: 1 }}>
        +{countUp(t, 13.36, 0.8, 200)}
      </div>
      <div style={{ fontSize: 44, fontWeight: 800, marginTop: 16 }}>KOÇLUK ÖĞRENCİMİZ</div>
    </div>
  </>
);

const Hocalar: React.FC<{ t: number }> = ({ t }) => {
  const cards: { who: TeacherKey; at: number }[] = [
    { who: "baset", at: 18.9 },
    { who: "harun", at: 19.88 },
    { who: "erkan", at: 20.88 },
  ];
  return (
    <>
      <LedBackground />
      <LedBug />
      <div style={{ ...H, top: 112, fontSize: 28, fontWeight: 700, letterSpacing: 8, color: BRAND.orange, ...rise(t, 15.6) }}>
        FEDAKÂRLIKLA ÇALIŞAN
      </div>
      <div style={{ ...H, top: 150, fontSize: 66, fontWeight: 900, ...rise(t, 17.12) }}>
        KIYMETLİ HOCALARIMIZ
      </div>
      {cards.map((c, i) => (
        <TeacherCard key={c.who} who={c.who} t={t} at={c.at} slotsAt={17.6 + i * 0.12} x={90 + i * 380} y={250} w={340} h={470} />
      ))}
    </>
  );
};

const Ufuk: React.FC<{ t: number }> = ({ t }) => (
  <>
    <LedBackground />
    <LedBug />
    <TeacherCard who="ufuk" t={t} at={21.9} x={80} y={130} w={340} h={580} />
    <div style={{ position: "absolute", left: 470, top: 200, fontFamily: montserrat, color: BRAND.white }}>
      <div style={{ fontSize: 26, fontWeight: 700, letterSpacing: 3, color: BRAND.orange }}>
        EKRAN ARKASINDAKİ GİZLİ KAHRAMAN
      </div>
      <div style={{ fontSize: 76, fontWeight: 900, marginTop: 10, lineHeight: 1 }}>UFUK ÇETİNTAŞ</div>
      <div
        style={{
          display: "inline-block",
          marginTop: 24,
          padding: "10px 28px",
          borderRadius: 40,
          backgroundColor: BRAND.orange,
          fontSize: 34,
          fontWeight: 800,
          letterSpacing: 3,
        }}
      >
        GÜMRÜK KOÇU
      </div>
      <div style={{ display: "flex", alignItems: "center", gap: 18, marginTop: 56, ...rise(t, 27.64) }}>
        <Icon name="heart" size={56} />
        <div style={{ fontSize: 42, fontWeight: 800 }}>YÜREKTEN TEŞEKKÜRLER</div>
      </div>
    </div>
  </>
);

const Ankara: React.FC<{ t: number }> = ({ t }) => (
  <>
    <LedBackground />
    <LedBug />
    <div style={{ ...H, top: 92, display: "flex", justifyContent: "center", alignItems: "center", gap: 14, ...rise(t, 29.56) }}>
      <Icon name="pin" size={48} />
      <span style={{ fontSize: 34, fontWeight: 800, letterSpacing: 8, color: BRAND.orange }}>ANKARA&apos;DA</span>
    </div>
    <div style={{ ...H, top: 145, fontSize: 56, fontWeight: 900, ...rise(t, 29.97) }}>
      BİZİ YALNIZ BIRAKMAYACAK
    </div>
    <TeacherCard who="hakan" t={t} at={31.16} x={260} y={240} w={360} h={420} />
    <TeacherCard who="ahmet" t={t} at={32.08} x={660} y={240} w={360} h={420} />
    <div style={{ ...H, top: 680, fontSize: 38, fontWeight: 800, color: BRAND.orange, letterSpacing: 4, ...rise(t, 33.9, 20) }}>
      ŞİMDİDEN TEŞEKKÜRLER
    </div>
  </>
);

const Sukran: React.FC<{ t: number }> = ({ t }) => (
  <>
    <LedBackground />
    <LedBug />
    <div style={{ ...H, top: 140, fontSize: 40, fontWeight: 800, letterSpacing: 6, color: BRAND.orange, ...rise(t, 35.44) }}>
      AZİM VE KARARLILIKLA
    </div>
    <div style={{ ...H, top: 215, fontSize: 54, fontWeight: 900, ...rise(t, 38.56) }}>
      DEĞERLİ MESLEKTAŞLARIMIZA
    </div>
    <div style={{ ...H, top: 290, fontSize: 94, fontWeight: 900, color: BRAND.orange, ...rise(t, 39.92) }}>
      ŞÜKRANLARIMIZLA
    </div>
  </>
);

const Emek: React.FC<{ t: number }> = ({ t }) => {
  const stars = [
    [170, 160],
    [1100, 190],
    [230, 560],
    [1050, 600],
    [640, 690],
  ];
  return (
    <>
      <LedBackground />
      <LedBug />
      <div style={{ ...H, top: 110, display: "flex", justifyContent: "center", ...rise(t, 41.4) }}>
        <Icon name="cap" size={120} />
      </div>
      <div style={{ ...H, top: 262, fontSize: 54, fontWeight: 900, ...rise(t, 41.56) }}>EMEKLERİNİZİN KARŞILIĞINI</div>
      <div style={{ ...H, top: 342, fontSize: 88, fontWeight: 900, color: BRAND.orange, ...rise(t, 42.96) }}>
        EN GÜZEL ŞEKİLDE
      </div>
      <div style={{ ...H, top: 470, fontSize: 60, fontWeight: 900, ...rise(t, 43.84) }}>ALMANIZ DİLEĞİYLE</div>
      {stars.map(([x, y], i) => (
        <div
          key={i}
          style={{
            position: "absolute",
            left: x,
            top: y,
            fontSize: 44,
            color: BRAND.orange,
            opacity: appear(t, 42.2 + i * 0.25) * (0.55 + 0.45 * Math.sin(t * 5 + i)),
          }}
        >
          ✦
        </div>
      ))}
    </>
  );
};

const Ekran: React.FC<{ t: number }> = ({ t }) => {
  const strike = interpolate(t, [46.2, 46.55], [0, 1], { ...clamp, easing: easeOut });
  return (
    <>
      <LedBackground />
      <LedBug />
      <div style={{ ...H, top: 120, display: "flex", justifyContent: "center", ...rise(t, 45.12) }}>
        <div style={{ position: "relative" }}>
          <Icon name="laptop" size={170} color={BRAND.white} />
          <div
            style={{
              position: "absolute",
              left: 0,
              top: 82,
              height: 10,
              width: 170 * strike,
              borderRadius: 5,
              backgroundColor: BRAND.orange,
              rotate: "-20deg",
            }}
          />
        </div>
      </div>
      <div style={{ ...H, top: 330, fontSize: 70, fontWeight: 900, ...rise(t, 45.2) }}>SADECE EKRAN BAŞINDA</div>
      <div style={{ ...H, top: 430, fontSize: 130, fontWeight: 900, color: BRAND.orange, ...rise(t, 46.24) }}>DEĞİL!</div>
    </>
  );
};

const Soguk: React.FC<{ t: number }> = ({ t }) => (
  <>
    <LedBackground tint={1} glow="rgba(120,180,255,0.30)" />
    <LedBug />
    <div style={{ ...H, top: 110, display: "flex", justifyContent: "center", ...rise(t, 46.8) }}>
      <Icon name="snow" size={170} color="#D8ECFF" rotate={t * 25} />
    </div>
    <div style={{ ...H, top: 330, fontSize: 74, fontWeight: 900, ...rise(t, 46.8) }}>ANKARA&apos;NIN</div>
    <div
      style={{
        ...H,
        top: 420,
        fontSize: 132,
        fontWeight: 900,
        color: "#D8ECFF",
        textShadow: "0 0 30px rgba(140,200,255,0.8)",
        ...rise(t, 47.36),
      }}
    >
      SOĞUĞUNDA
    </div>
  </>
);

const Kapi: React.FC<{ t: number }> = ({ t }) => (
  <>
    <LedBackground />
    <LedBug />
    <div style={{ ...H, top: 110, display: "flex", justifyContent: "center", ...rise(t, 48.2) }}>
      <Icon name="door" size={180} />
    </div>
    <div style={{ ...H, top: 340, fontSize: 70, fontWeight: 900, ...rise(t, 48.32) }}>O SINAV</div>
    <div style={{ ...H, top: 430, fontSize: 132, fontWeight: 900, color: BRAND.orange, ...rise(t, 48.72) }}>
      KAPISINDA
    </div>
  </>
);

const Omuz: React.FC<{ t: number }> = ({ t }) => {
  const team: TeacherKey[] = ["hakan", "harun", "baset", "erkan", "ufuk", "ahmet"];
  const head = 1 - appear(t, 51.0, 0.35);
  return (
    <>
      <LedBackground />
      <LedBug />
      <div style={{ ...H, top: 96, opacity: head }}>
        <div style={{ fontSize: 100, fontWeight: 900, color: BRAND.orange, ...rise(t, 49.44) }}>OMUZ OMUZA</div>
        <div style={{ fontSize: 56, fontWeight: 900, marginTop: 4, ...rise(t, 50.0) }}>YANINIZDAYIZ</div>
      </div>
      <div style={{ ...H, top: 110, opacity: 1 - head }}>
        <div style={{ fontSize: 66, fontWeight: 900 }}>YOLUNUZ AÇIK,</div>
        <div style={{ fontSize: 66, fontWeight: 900, color: BRAND.orange }}>BAŞARINIZ DAİM OLSUN!</div>
      </div>
      {team.map((who, i) => {
        const p = appear(t, 49.5 + i * 0.09, 0.45);
        return (
          <Img
            key={who}
            src={staticFile(TEACHERS[who].img)}
            style={{
              position: "absolute",
              bottom: 0,
              left: 70 + i * 190,
              height: who === "ufuk" ? 360 : 410,
              opacity: p,
              translate: `0px ${(1 - p) * 80}px`,
              filter: "drop-shadow(0 6px 14px rgba(0,0,0,0.6))",
            }}
          />
        );
      })}
    </>
  );
};

const SCENES: { id: string; from: number; to: number; fadeIn?: boolean; fadeOut?: boolean; C: React.FC<{ t: number }> }[] = [
  { id: "stats", from: 11.13, to: 16.3, fadeIn: false, C: Stats },
  { id: "hocalar", from: 16.0, to: 21.95, C: Hocalar },
  { id: "ufuk", from: 21.9, to: 29.16, fadeIn: false, fadeOut: false, C: Ufuk },
  { id: "ankara", from: 29.16, to: 35.45, fadeIn: false, C: Ankara },
  { id: "sukran", from: 35.2, to: 41.3, fadeOut: false, C: Sukran },
  { id: "emek", from: 41.3, to: 45.1, fadeIn: false, C: Emek },
  { id: "ekran", from: 44.95, to: 46.9, C: Ekran },
  { id: "soguk", from: 46.75, to: 48.45, C: Soguk },
  { id: "kapi", from: 48.3, to: 49.55, C: Kapi },
  { id: "omuz", from: 49.4, to: 60, fadeOut: false, C: Omuz },
];

export const LedContent: React.FC<{ t: number; withTitle?: boolean }> = ({ t, withTitle = true }) => {
  return (
    <div
      style={{
        position: "absolute",
        left: 0,
        top: 0,
        width: LED_DESIGN.w,
        height: LED_DESIGN.h,
        overflow: "hidden",
        backgroundColor: BRAND.navy,
      }}
    >
      {withTitle ? (
        <Sequence name="LED title (HyperFrames)" durationInFrames={sec(11.13) + 1} layout="none">
          <Video
            src={staticFile("hf/ekran-baslik.mp4")}
            muted
            style={{ position: "absolute", left: 0, top: 0, width: LED_DESIGN.w, height: LED_DESIGN.h }}
          />
        </Sequence>
      ) : null}
      {SCENES.filter((s) => t >= s.from - 0.01 && t < s.to + 0.01).map((s) => {
        const fin = s.fadeIn === false ? 1 : appear(t, s.from, 0.3);
        const fout = s.fadeOut === false ? 1 : 1 - interpolate(t, [s.to - 0.3, s.to], [0, 1], clamp);
        return (
          <div key={s.id} style={{ position: "absolute", inset: 0, opacity: Math.min(fin, fout) }}>
            <s.C t={t} />
          </div>
        );
      })}
    </div>
  );
};
