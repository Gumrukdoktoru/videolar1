import React from "react";
import { Img, interpolate, staticFile } from "remotion";
import { montserrat } from "../fonts";
import { BRAND, appear, backOut, clamp, easeInOut, leave } from "../timeline";
import { Beat, Icon, IconName, Kicker, Panel } from "../ui";

// Information beats over the venue walkthrough. Every cue time is the onset of
// the narration word it illustrates (master-time seconds).

const center: React.CSSProperties = { position: "absolute", left: 0, right: 0, display: "flex", justifyContent: "center" };

// "New Park Otel'deyiz."
export const Konum: React.FC = () => (
  <Beat name="Konum: New Park Otel" from={4.9} to={8.4}>
    {(t) => {
      const p = appear(t, 4.95, 0.55, backOut);
      const o = leave(t, 7.95, 0.3);
      return (
        <div style={{ ...center, top: 190, opacity: Math.min(1, p * 1.6) * (1 - o), translate: `0px ${(1 - p) * -40 - o * 40}px` }}>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 26,
              padding: "24px 48px 24px 26px",
              borderRadius: 999,
              backgroundColor: "rgba(7,11,31,0.84)",
              boxShadow: "0 20px 50px rgba(0,0,0,0.45), inset 0 0 0 2px rgba(255,255,255,0.12)",
              fontFamily: montserrat,
              color: BRAND.white,
              scale: 0.85 + 0.15 * p,
            }}
          >
            <div
              style={{
                width: 104,
                height: 104,
                borderRadius: 52,
                backgroundColor: BRAND.orange,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <Icon name="pin" size={64} color={BRAND.white} />
            </div>
            <div>
              <div style={{ fontWeight: 900, fontSize: 60, lineHeight: 1, letterSpacing: 1 }}>NEW PARK OTEL</div>
              <div style={{ fontWeight: 700, fontSize: 28, letterSpacing: 8, color: BRAND.orange, marginTop: 10 }}>
                ANKARA KAMPI
              </div>
            </div>
          </div>
        </div>
      );
    }}
  </Beat>
);

const TeacherCard: React.FC<{ t: number; at: number; x: number; name: string; img: string }> = ({ t, at, x, name, img }) => {
  const p = appear(t, at, 0.5);
  const sweep = interpolate(t, [at + 0.15, at + 0.9], [-60, 160], clamp);
  const w = 410;
  const h = 520;
  const plate = 74;
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: 270,
        width: w,
        height: h,
        borderRadius: 26,
        overflow: "hidden",
        opacity: p,
        translate: `0px ${(1 - p) * 70}px`,
        scale: 0.9 + 0.1 * p,
        background: "linear-gradient(180deg, rgba(241,109,37,0.5) 0%, rgba(30,36,80,0.95) 62%, rgba(10,14,34,1) 100%)",
        boxShadow: "0 22px 50px rgba(0,0,0,0.5), inset 0 0 0 2px rgba(255,255,255,0.16)",
      }}
    >
      <div
        style={{
          position: "absolute",
          left: "50%",
          bottom: plate - 10,
          width: w * 1.1,
          height: w * 0.9,
          translate: "-50% 30%",
          background: "radial-gradient(circle, rgba(241,109,37,0.6) 0%, rgba(241,109,37,0) 65%)",
        }}
      />
      <Img
        src={staticFile(img)}
        style={{
          position: "absolute",
          bottom: plate,
          left: "50%",
          height: h - plate - 14,
          translate: `-50% ${(1 - p) * 40}px`,
          filter: "drop-shadow(0 10px 20px rgba(0,0,0,0.5))",
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
          fontSize: 34,
          letterSpacing: 1,
          color: BRAND.white,
          whiteSpace: "nowrap",
        }}
      >
        {name}
      </div>
      <div
        style={{
          position: "absolute",
          top: 0,
          bottom: 0,
          width: "45%",
          left: `${sweep}%`,
          background: "linear-gradient(100deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.35) 50%, rgba(255,255,255,0) 100%)",
        }}
      />
    </div>
  );
};

// "Harun Altınsoy, Baset Temiz ve diğer hocalarımızın…"
export const Hocalar: React.FC = () => (
  <Beat name="Hocalar" from={8.2} to={13.0}>
    {(t) => {
      const o = leave(t, 12.55, 0.35);
      const k = appear(t, 8.22, 0.4);
      const more = appear(t, 10.66, 0.45, backOut);
      return (
        <div style={{ position: "absolute", inset: 0, opacity: 1 - o, translate: `0px ${-o * 60}px` }}>
          <div style={{ ...center, top: 175 }}>
            <Kicker text="SAHNE ALACAK HOCALARIMIZ" p={k} />
          </div>
          <TeacherCard t={t} at={8.32} x={110} name="HARUN ALTINSOY" img="hocalar/harun-altinsoy.png" />
          <TeacherCard t={t} at={9.34} x={560} name="BASET TEMİZ" img="hocalar/baset-temiz.png" />
          <div style={{ ...center, top: 820, opacity: Math.min(1, more * 1.5) }}>
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 14,
                padding: "16px 34px",
                borderRadius: 999,
                backgroundColor: "rgba(7,11,31,0.84)",
                boxShadow: "inset 0 0 0 3px rgba(241,109,37,0.9)",
                fontFamily: montserrat,
                fontWeight: 800,
                fontSize: 36,
                color: BRAND.white,
                scale: 0.8 + 0.2 * more,
              }}
            >
              <span style={{ color: BRAND.orange, fontSize: 46, lineHeight: 1 }}>+</span> DİĞER HOCALARIMIZ
            </div>
          </div>
        </div>
      );
    }}
  </Beat>
);

const Tile: React.FC<{ p: number; icon: IconName; label: string }> = ({ p, icon, label }) => (
  <div
    style={{
      width: 380,
      height: 270,
      borderRadius: 26,
      backgroundColor: "rgba(241,109,37,0.14)",
      boxShadow: "inset 0 0 0 3px rgba(241,109,37,0.85)",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      gap: 16,
      opacity: Math.min(1, p * 1.5),
      scale: 0.7 + 0.3 * p,
    }}
  >
    <Icon name={icon} size={120} />
    <div style={{ fontWeight: 900, fontSize: 56, letterSpacing: 2 }}>{label}</div>
  </div>
);

// "…sahne alacağı ekran, kürsü burada olacak."
export const Sahne: React.FC = () => (
  <Beat name="Sahne: ekran + kürsü" from={12.7} to={16.0}>
    {(t) => {
      const p = appear(t, 12.72, 0.4);
      const o = leave(t, 15.55, 0.3);
      const here = appear(t, 14.26, 0.4, backOut);
      return (
        <Panel x={90} y={190} w={900} h={560} style={{ opacity: p * (1 - o), translate: `0px ${(1 - p) * 40 - o * 50}px` }}>
          <div style={{ position: "absolute", left: 50, top: 44 }}>
            <Kicker text="SAHNE" p={p} />
          </div>
          <div style={{ position: "absolute", left: 50, right: 50, top: 120, display: "flex", justifyContent: "space-between" }}>
            <Tile p={appear(t, 12.78, 0.45, backOut)} icon="screen" label="EKRAN" />
            <Tile p={appear(t, 13.9, 0.45, backOut)} icon="podium" label="KÜRSÜ" />
          </div>
          <div
            style={{
              position: "absolute",
              left: 0,
              right: 0,
              top: 432,
              textAlign: "center",
              fontWeight: 900,
              fontSize: 54,
              color: BRAND.orange,
              letterSpacing: 3,
              opacity: here,
              scale: 0.85 + 0.15 * here,
            }}
          >
            BURADA OLACAK
          </div>
        </Panel>
      );
    }}
  </Beat>
);

// "Salonlarımız sekizinci katta ferah."
export const SekizinciKat: React.FC = () => (
  <Beat name="8. kat" from={16.0} to={19.2}>
    {(t) => {
      const k = appear(t, 16.16, 0.4);
      const slam = appear(t, 16.82, 0.4, backOut);
      const ferah = appear(t, 17.64, 0.4, backOut);
      const o = leave(t, 18.85, 0.3);
      return (
        <div style={{ position: "absolute", inset: 0, opacity: 1 - o }}>
          <div
            style={{
              position: "absolute",
              left: 0,
              right: 0,
              top: 80,
              height: 820,
              background: "radial-gradient(ellipse 62% 50% at 50% 50%, rgba(7,11,31,0.78) 0%, rgba(7,11,31,0) 100%)",
              opacity: k,
            }}
          />
          <div style={{ ...center, top: 230 }}>
            <Kicker text="SALONLARIMIZ" p={k} size={34} />
          </div>
          <div
            style={{
              ...center,
              top: 290,
              fontFamily: montserrat,
              fontWeight: 900,
              fontSize: 215,
              lineHeight: 1,
              color: BRAND.white,
              opacity: Math.min(1, slam * 2),
              scale: 1.5 - 0.5 * slam,
              filter: `blur(${(1 - slam) * 10}px)`,
              textShadow: "0 18px 50px rgba(0,0,0,0.6)",
            }}
          >
            <span style={{ color: BRAND.orange }}>8.</span>&nbsp;KAT
          </div>
          <div style={{ ...center, top: 560, opacity: ferah }}>
            <div
              style={{
                padding: "14px 56px",
                borderRadius: 999,
                backgroundColor: BRAND.orange,
                fontFamily: montserrat,
                fontWeight: 900,
                fontSize: 64,
                letterSpacing: 10,
                color: BRAND.white,
                scale: 0.6 + 0.4 * ferah,
                boxShadow: "0 16px 40px rgba(241,109,37,0.45)",
              }}
            >
              FERAH
            </div>
          </div>
        </div>
      );
    }}
  </Beat>
);

const Row: React.FC<{ p: number; good: boolean; text: string; strike?: number }> = ({ p, good, text, strike = 0 }) => (
  <div
    style={{
      position: "relative",
      display: "flex",
      alignItems: "center",
      gap: 26,
      height: 96,
      opacity: p,
      translate: `${(1 - p) * -60}px 0px`,
    }}
  >
    <div
      style={{
        width: 72,
        height: 72,
        borderRadius: 36,
        backgroundColor: good ? BRAND.green : BRAND.red,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        flexShrink: 0,
      }}
    >
      <Icon name={good ? "check" : "cross"} size={44} color={BRAND.white} stroke={13} />
    </div>
    <div style={{ fontWeight: 800, fontSize: 50, letterSpacing: 1, whiteSpace: "nowrap" }}>{text}</div>
    {strike > 0 ? (
      <div
        style={{
          position: "absolute",
          left: 96,
          top: 44,
          height: 9,
          width: `${strike * 640}px`,
          borderRadius: 5,
          backgroundColor: BRAND.red,
          boxShadow: "0 0 14px rgba(232,67,46,0.7)",
        }}
      />
    ) : null}
  </div>
);

// "Klasik Ankara otellerinin bodrum katındaki o rutubet ve nem kokusunun olduğu
// alanlardan değil, ferah atmosferiyle ders dinlemenize elverişli bir ortam."
export const Karsilastirma: React.FC = () => (
  <Beat name="Bodrum değil, ferah" from={19.1} to={32.4}>
    {(t) => {
      const p1 = appear(t, 19.22, 0.45);
      const o1 = interpolate(t, [26.5, 26.85], [0, 1], { ...clamp, easing: easeInOut });
      const stamp = appear(t, 26.12, 0.25, backOut);
      const p2 = appear(t, 26.92, 0.45);
      const o2 = leave(t, 32.0, 0.3);
      return (
        <>
          {o1 < 1 ? (
            <Panel
              x={90}
              y={200}
              w={900}
              h={500}
              style={{ opacity: p1 * (1 - o1), translate: `${-o1 * 300}px ${(1 - p1) * 40}px`, rotate: `${-o1 * 6}deg` }}
            >
              <div style={{ position: "absolute", left: 50, top: 44 }}>
                <Kicker text="KLASİK ANKARA OTELLERİ" p={p1} color="rgba(255,255,255,0.75)" />
              </div>
              <div style={{ position: "absolute", left: 50, top: 130, display: "flex", flexDirection: "column", gap: 10 }}>
                <Row p={appear(t, 20.76, 0.4)} good={false} text="BODRUM KAT" strike={appear(t, 26.12, 0.3)} />
                <Row p={appear(t, 22.62, 0.4)} good={false} text="RUTUBET" strike={appear(t, 26.17, 0.3)} />
                <Row p={appear(t, 24.12, 0.4)} good={false} text="NEM KOKUSU" strike={appear(t, 26.22, 0.3)} />
              </div>
              <div
                style={{
                  position: "absolute",
                  right: 50,
                  top: 150,
                  padding: "10px 30px",
                  border: `8px solid ${BRAND.red}`,
                  borderRadius: 18,
                  fontWeight: 900,
                  fontSize: 84,
                  color: BRAND.red,
                  backgroundColor: "rgba(255,255,255,0.92)",
                  rotate: "-10deg",
                  opacity: stamp,
                  scale: 2 - stamp,
                }}
              >
                DEĞİL!
              </div>
            </Panel>
          ) : null}
          {t >= 26.92 ? (
            <Panel x={90} y={200} w={900} h={510} style={{ opacity: p2 * (1 - o2), translate: `${(1 - p2) * 300}px ${-o2 * 50}px` }}>
              <div style={{ position: "absolute", left: 50, top: 44 }}>
                <Kicker text="BİZİM SALONLARIMIZ" p={p2} />
              </div>
              <div style={{ position: "absolute", left: 50, top: 130, display: "flex", flexDirection: "column", gap: 24 }}>
                <Row p={appear(t, 27.0, 0.4)} good text="8. KATTA SALONLAR" />
                <Row p={appear(t, 27.94, 0.4)} good text="FERAH ATMOSFER" />
                <Row p={appear(t, 30.74, 0.4)} good text="DERSE ELVERİŞLİ" />
              </div>
            </Panel>
          ) : null}
        </>
      );
    }}
  </Beat>
);

// "Ekran okuyan hocalarımız değil, gümbür gümbür örnekli bir şekilde sınav odaklı…"
export const AnlatimTarzi: React.FC = () => (
  <Beat name="Ekran okuyan değil" from={32.6} to={41.0}>
    {(t) => {
      const k = appear(t, 32.98, 0.4);
      const line = appear(t, 34.0, 0.4);
      const strike = appear(t, 35.14, 0.25);
      const degil = appear(t, 35.14, 0.3, backOut);
      const g1 = appear(t, 36.02, 0.3, backOut);
      const g2 = appear(t, 36.44, 0.3, backOut);
      const shake = (at: number) => {
        const d = t - at;
        return d > 0 && d < 0.35 ? Math.sin(d * 90) * 10 * (1 - d / 0.35) : 0;
      };
      const c1 = appear(t, 36.98, 0.4, backOut);
      const c2 = appear(t, 38.08, 0.4, backOut);
      const o = leave(t, 40.6, 0.3);
      const chip = (p: number, text: string, filled: boolean) => (
        <div
          style={{
            padding: "16px 36px",
            borderRadius: 999,
            fontFamily: montserrat,
            fontWeight: 900,
            fontSize: 46,
            letterSpacing: 2,
            color: BRAND.white,
            backgroundColor: filled ? BRAND.orange : "rgba(7,11,31,0.85)",
            boxShadow: filled ? "0 14px 34px rgba(241,109,37,0.45)" : `inset 0 0 0 4px ${BRAND.orange}`,
            opacity: Math.min(1, p * 1.5),
            scale: 0.6 + 0.4 * p,
          }}
        >
          {text}
        </div>
      );
      return (
        <div style={{ position: "absolute", inset: 0, opacity: 1 - o, translate: `0px ${-o * 50}px` }}>
          <div
            style={{
              position: "absolute",
              left: 0,
              right: 0,
              top: 100,
              height: 860,
              background: "radial-gradient(ellipse 70% 52% at 50% 50%, rgba(7,11,31,0.8) 0%, rgba(7,11,31,0) 100%)",
              opacity: k,
            }}
          />
          <div style={{ ...center, top: 200 }}>
            <Kicker text="HOCALARIMIZ" p={k} size={34} />
          </div>
          <div style={{ ...center, top: 270, opacity: line, translate: `0px ${(1 - line) * 30}px` }}>
            <div style={{ position: "relative", fontFamily: montserrat, fontWeight: 900, fontSize: 96, color: "rgba(255,255,255,0.92)" }}>
              EKRAN OKUYAN
              <div
                style={{
                  position: "absolute",
                  left: -10,
                  top: 50,
                  height: 12,
                  width: `${strike * 104}%`,
                  borderRadius: 6,
                  backgroundColor: BRAND.red,
                  boxShadow: "0 0 18px rgba(232,67,46,0.8)",
                }}
              />
              <div
                style={{
                  position: "absolute",
                  right: -70,
                  top: -50,
                  padding: "4px 22px",
                  border: `6px solid ${BRAND.red}`,
                  borderRadius: 14,
                  backgroundColor: "rgba(255,255,255,0.94)",
                  color: BRAND.red,
                  fontSize: 56,
                  rotate: "12deg",
                  opacity: degil,
                  scale: 1.8 - 0.8 * degil,
                }}
              >
                DEĞİL
              </div>
            </div>
          </div>
          {[
            { p: g1, at: 36.02, top: 420 },
            { p: g2, at: 36.44, top: 570 },
          ].map((g) => (
            <div
              key={g.at}
              style={{
                ...center,
                top: g.top,
                fontFamily: montserrat,
                fontWeight: 900,
                fontSize: 150,
                lineHeight: 1,
                color: BRAND.orange,
                opacity: Math.min(1, g.p * 2),
                scale: 1.6 - 0.6 * g.p,
                translate: `${shake(g.at)}px 0px`,
                textShadow: "0 16px 40px rgba(0,0,0,0.55)",
              }}
            >
              GÜMBÜR
            </div>
          ))}
          <div style={{ ...center, top: 750, gap: 22 }}>
            {chip(c1, "ÖRNEKLİ", false)}
            {chip(c2, "SINAV ODAKLI", true)}
          </div>
        </div>
      );
    }}
  </Beat>
);

const ClassCard: React.FC<{
  t: number;
  top: number;
  titleAt: number;
  title: string;
  salonAt: number;
  salon: string;
  hereAt?: number;
}> = ({ t, top, titleAt, title, salonAt, salon, hereAt }) => {
  const p = appear(t, titleAt, 0.45);
  const s = appear(t, salonAt, 0.5);
  const here = hereAt === undefined ? 0 : appear(t, hereAt, 0.35, backOut);
  return (
    <Panel x={90} y={top} w={900} h={280} style={{ opacity: p, translate: `${(1 - p) * 80}px 0px` }}>
      <div style={{ position: "absolute", left: 46, top: 40, display: "flex", alignItems: "center", gap: 18 }}>
        <Icon name="users" size={54} />
        <div style={{ fontWeight: 800, fontSize: 40, letterSpacing: 1 }}>{title}</div>
      </div>
      <div
        style={{
          position: "absolute",
          left: 46,
          top: 112,
          display: "flex",
          alignItems: "center",
          gap: 20,
          whiteSpace: "nowrap",
          clipPath: `inset(0 ${(1 - s) * 100}% 0 0)`,
        }}
      >
        <Icon name="flower" size={80} stroke={6} />
        <div style={{ fontWeight: 900, fontSize: 60, color: BRAND.orange, letterSpacing: 2 }}>{salon}</div>
      </div>
      {s < 0.05 ? (
        <div style={{ position: "absolute", left: 46, top: 150, width: 320, height: 10, borderRadius: 5, backgroundColor: "rgba(255,255,255,0.18)" }} />
      ) : null}
      {here > 0 ? (
        <div
          style={{
            position: "absolute",
            right: 26,
            bottom: 22,
            display: "flex",
            alignItems: "center",
            gap: 8,
            padding: "8px 20px 8px 12px",
            borderRadius: 999,
            backgroundColor: BRAND.orange,
            fontWeight: 800,
            fontSize: 24,
            letterSpacing: 2,
            opacity: here,
            scale: 0.6 + 0.4 * here,
          }}
        >
          <Icon name="pin" size={34} color={BRAND.white} /> ŞU AN BURADAYIZ
        </div>
      ) : null}
    </Panel>
  );
};

// "Gümrük müşaviri ve yardımcılığı sınıflarımız ayrı ayrı olacak. Yardımcılık
// sınıfı Begonya, gümrük müşavirliği sınıfımız burası, Lilyum sınıfı olacak."
export const Siniflar: React.FC = () => (
  <Beat name="Ayrı sınıflar" from={41.4} to={51.0}>
    {(t) => {
      const k = appear(t, 41.56, 0.4);
      const ayri = appear(t, 43.62, 0.4, backOut);
      const o = leave(t, 50.6, 0.3);
      return (
        <div style={{ position: "absolute", inset: 0, opacity: 1 - o, translate: `0px ${-o * 50}px` }}>
          <div style={{ ...center, top: 175, alignItems: "center", gap: 20 }}>
            <Kicker text="SINIFLARIMIZ" p={k} size={34} />
            <div
              style={{
                padding: "8px 26px",
                borderRadius: 999,
                backgroundColor: BRAND.orange,
                fontFamily: montserrat,
                fontWeight: 900,
                fontSize: 34,
                letterSpacing: 3,
                color: BRAND.white,
                opacity: ayri,
                scale: 0.6 + 0.4 * ayri,
              }}
            >
              AYRI AYRI
            </div>
          </div>
          <ClassCard t={t} top={250} titleAt={41.56} title="GÜMRÜK MÜŞAVİRLİĞİ" salonAt={49.3} salon="LİLYUM SALONU" hereAt={48.8} />
          <ClassCard t={t} top={560} titleAt={42.56} title="MÜŞAVİR YARDIMCILIĞI" salonAt={46.12} salon="BEGONYA SALONU" />
        </div>
      );
    }}
  </Beat>
);

// "Ankara kamp kayıtlarımız an itibariyle dolmuştur. Herkesin bilgilerine."
export const KayitlarDoldu: React.FC = () => (
  <Beat name="Kayıtlar doldu" from={53.4} to={59.2}>
    {(t) => {
      const k = appear(t, 53.5, 0.4);
      const big = appear(t, 54.46, 0.45);
      const stamp = appear(t, 56.88, 0.22, backOut);
      const info = appear(t, 57.6, 0.4);
      return (
        <div style={{ position: "absolute", inset: 0 }}>
          <div
            style={{
              position: "absolute",
              left: 0,
              right: 0,
              top: 90,
              height: 880,
              background: "radial-gradient(ellipse 70% 50% at 50% 50%, rgba(7,11,31,0.82) 0%, rgba(7,11,31,0) 100%)",
              opacity: k,
            }}
          />
          <div style={{ ...center, top: 220 }}>
            <Kicker text="ANKARA KAMPI" p={k} size={36} />
          </div>
          <div
            style={{
              ...center,
              top: 290,
              fontFamily: montserrat,
              fontWeight: 900,
              fontSize: 112,
              color: BRAND.white,
              opacity: big,
              translate: `0px ${(1 - big) * 40}px`,
              textShadow: "0 14px 40px rgba(0,0,0,0.6)",
            }}
          >
            KAYITLARIMIZ
          </div>
          <div style={{ ...center, top: 440 }}>
            <div
              style={{
                padding: "10px 60px",
                border: `14px solid ${BRAND.red}`,
                borderRadius: 26,
                backgroundColor: "rgba(255,255,255,0.95)",
                fontFamily: montserrat,
                fontWeight: 900,
                fontSize: 170,
                lineHeight: 1.05,
                letterSpacing: 6,
                color: BRAND.red,
                rotate: "-8deg",
                opacity: Math.min(1, stamp * 3),
                scale: 2.2 - 1.2 * stamp,
                boxShadow: "0 24px 60px rgba(0,0,0,0.5)",
              }}
            >
              DOLDU
            </div>
          </div>
          <div style={{ ...center, top: 760, opacity: info, translate: `0px ${(1 - info) * 30}px` }}>
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 16,
                padding: "16px 36px",
                borderRadius: 999,
                backgroundColor: "rgba(7,11,31,0.86)",
                boxShadow: "inset 0 0 0 3px rgba(241,109,37,0.9)",
                fontFamily: montserrat,
                fontWeight: 800,
                fontSize: 38,
                color: BRAND.white,
              }}
            >
              <Icon name="calendar" size={46} /> 08 KASIM · NEW PARK OTEL
            </div>
          </div>
        </div>
      );
    }}
  </Beat>
);
