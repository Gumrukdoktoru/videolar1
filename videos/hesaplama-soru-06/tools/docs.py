"""Write README.md, BRIEF.md, STORYBOARD.md and youtube-aciklama.txt from video.DOC + timing.json (tax-calculation lessons)."""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from video import NUM, DOC, YT, CHAPTERS  # noqa: E402

T = json.load(open(ROOT / "timing.json"))
SC = {s["id"]: s for s in T["scenes"]}
total = T["total"]
mm, ss = divmod(int(round(total)), 60)
name = f"hesaplama-soru-{NUM:02d}"


def ts(t):
    m, s = divmod(int(t), 60)
    return f"{m}:{s:02d}"


chap = [(YT[i], SC[ids[0]]["start"]) for i, (_, ids) in enumerate(CHAPTERS)]
ans = DOC["answer"]
opts = " · ".join((f"**{L}) {v}**" if L == ans else f"{L}) {v}") for L, v in DOC["options"])
ans_val = dict(DOC["options"])[ans]

readme = [f"# Vergi Hesaplama Dersi {NUM} — {DOC['title']} (Gümrük Koçu ders videosu)", "",
          "Sınav mantığına göre kurgulanmış **özgün** bir hesaplama sorusu ve anlatımlı çözümü. Soru kökü, sayılar ve çeldiriciler",
          "bize aittir; soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.", "",
          f"**Soru:** {DOC['question']}", "", opts, "", f"**Cevap: {ans} — {ans_val}.**"]
readme += [f"- {x}" for x in DOC["solution"]]
readme += ["", f"Çeldiriciler: {DOC['distractors']}", "", "## Video", "",
           f"- **Süre:** {mm} dk {ss:02d} sn · 1920×1080 · 30 fps",
           f"- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış \"Vergi Hesaplama Dersi {NUM} — Gümrük Koçu\")",
           "- **Sunucu:** Gümrük Koçu — kıpırdamayan, sabit görsel; duruma göre tepki görseline yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).",
           f"- **Konuklar:** {DOC['guests']}",
           "- **Rozetler:** ÖNEMLİ · DİKKAT · UYARI · TUZAK (+ SORU, İPUCU)",
           f"- **Ekstralar:** {DOC['extras']}; sayılar alt yazıda rakamla, soru ve şıklar okunurken anahtar kelime vurgusu yok.",
           "", "## Dosyalar", "", "| Dosya | Ne işe yarar |", "| --- | --- |",
           f"| `renders/{name}-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |",
           "| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |",
           "| `altyazi.srt` | Türkçe altyazı (sayılar rakamla) |",
           "| `narration/script.json` · `narration/display.json` | Seslendirme metni (sayılar TTS için yazıyla) · ek alt yazı eşlemeleri |",
           "| `tools/` | `hkit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py` (zamanlama + sayı → rakam), `build.py`, `docs.py` |",
           "", "## Yeniden üretmek", "", "```bash", "python3 tools/build_timing.py", "cd tools && python3 build.py && python3 docs.py && cd ..",
           "npx hyperframes check", f"npx hyperframes render -o renders/{name}.mp4", "```", ""]
(ROOT / "README.md").write_text("\n".join(readme))

brief = ["---", "workflow: general-video", "flow: automation", "storyboard: no",
         f'message: "{DOC["title"]} — cevap {ans}: {ans_val}."', "destination: youtube", "aspect: 1920x1080", "language: tr",
         "audience: gümrük müşavirliği / muavinliği sınavına hazırlananlar, gümrük öğrencileri (ders kanalı)",
         f"length: ~{total / 60:.1f} dk".replace(".", ","), "angle: örnek soru çözümü / vergi hesaplama ders serisi (her videoda 1 soru)", "---", "",
         "## Intent", "", f"Gümrük Koçu vergi hesaplama serisinin {NUM}. videosu. Konu: {DOC['title'].lower()}. Soru kökü, sayılar ve çeldiriciler",
         "bize ait; 5 şıklı; her yanlış şık belirli bir hesap hatasından türetildi. Videonun hiçbir yerinde sorunun bir sınavdan",
         "alındığı ima edilmez. Soru hazırlama ilkeleri: 2027-GM- reposundaki \"Soru Hazırlama Kurgusu ve Kuralları\" belgesi.", "",
         "## Assets", "", "- assets/img/koc-*.png — Gümrük Koçu (ana karakter) ve tepki görselleri.",
         "- assets/img/cano-cut.png, baba-crop.png, stajyer-cut.png, yardimci-cut.png — konuklar.", "- assets/img/logo-crop.png — logo.", "",
         "## Customizations", "", "- Seslendirme: ElevenLabs **eleven_v4**, ses **Cem** (voice_id D1xRw7f8ZHedI7xJgfvz).",
         "- Maskot titremez; tepki görselleri arasında yumuşak geçiş.", "", "## Notes", "", f"- Dayanak: {DOC['sources']}", ""]
(ROOT / "BRIEF.md").write_text("\n".join(brief))

sb = ["---", "mode: autonomous", f'message: "{DOC["title"]}"', "canvas: 1920x1080", f"duration: {total}s (sesten türetildi — timing.json)", "---", "",
      f"# Vergi hesaplama dersi {NUM} — sahne planı", ""]
for s in T["scenes"]:
    sb += [f"## {s['id']} · {s['title']}", f"- {s['start']:.1f}s → {s['start'] + s['dur']:.1f}s · src: compositions/{s['id']}.html",
           f"- {DOC['scenes'][s['id']]}", ""]
(ROOT / "STORYBOARD.md").write_text("\n".join(sb))

yt = ["BAŞLIK", DOC["yt_title"], "", "AÇIKLAMA", DOC["yt_intro"], "", f"Soru: {DOC['question']}", "",
      "Şıklar: " + " · ".join(f"{L}) {v}" for L, v in DOC["options"]), "", "BÖLÜMLER"] + [f"{ts(t)} {n}" for n, t in chap]
yt += ["", f"Cevap: {ans} — {ans_val}. Siz kaçta buldunuz? Yorumlara yazın!", "",
       "Videodaki soru eğitim amaçlı hazırlanmış özgün bir örnektir. Somut işlemlerde güncel mevzuat ve vergi oranları esas alınmalıdır.",
       "", "ETİKETLER", DOC["tags"], "", DOC["hashtags"], ""]
(ROOT / "youtube-aciklama.txt").write_text("\n".join(yt))
print("docs written", name)
