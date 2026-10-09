"""Whisper dropped the option readout in s03; rebuild its word timings from silence-detected phrase spans."""
import json, pathlib, shutil

N = pathlib.Path(__file__).resolve().parent.parent / "narration" / "tx"
# (start, end, phrase) — spans from `ffmpeg -af silencedetect=noise=-35dB:d=0.12` on narration/s03.mp3
SEG = [
    (0.06, 0.99, "Şıklarımız şöyle."),
    (1.53, 2.10, "A şıkkı,"), (2.44, 4.39, "yüz seksen iki virgül doksan sekiz."),
    (4.80, 5.49, "B şıkkı,"), (5.72, 7.71, "yüz seksen bir virgül doksan sekiz."),
    (8.17, 8.90, "C şıkkı,"), (9.17, 11.34, "yüz doksan sekiz virgül doksan sekiz."),
    (11.80, 12.50, "D şıkkı,"), (12.81, 15.13, "iki yüz doksan dokuz virgül doksan sekiz."),
    (15.62, 16.26, "E şıkkı,"), (16.54, 18.30, "iki yüz seksen iki virgül seksen."),
    (19.51, 21.83, "Videoyu durdurun ve önce kendiniz çözün."),
]
if not (N / "s03-whisper.json").exists():
    shutil.copy(N / "s03.json", N / "s03-whisper.json")
out = []
for st, en, phrase in SEG:
    ws = phrase.split()
    tot = sum(len(w) for w in ws)
    t = st
    for w in ws:
        d = (en - st) * len(w) / tot
        out.append({"text": " " + w, "start": round(t, 3), "end": round(t + d, 3)})
        t += d
json.dump(out, open(N / "s03.json", "w"), ensure_ascii=False)
print("s03 words", len(out))
