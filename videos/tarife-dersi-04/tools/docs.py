"""Write README.md, BRIEF.md, STORYBOARD.md and youtube-aciklama.txt from video.DOC + timing.json."""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from video import NUM, DOC, YT, CHAPTERS  # noqa: E402

T = json.load(open(ROOT / "timing.json"))
SC = {s["id"]: s for s in T["scenes"]}
total = T["total"]
mm, ss = divmod(int(round(total)), 60)
name = f"tarife-dersi-{NUM:02d}"


def ts(t):
    m, s = divmod(int(t), 60)
    return f"{m}:{s:02d}"


chap = [(YT[i], SC[ids[0]]["start"]) for i, (_, ids) in enumerate(CHAPTERS)]
qs = DOC["questions"]
key = " · ".join(q["answer"] for q in qs)

readme = [f"# Tarife Dersi {NUM} — {DOC['title']} (Gümrük Koçu ders videosu)", "",
          "Tarife konusunun sınav mantığına göre kurgulanmış **3 özgün soru** ve anlatımlı çözümleri. Soru kökleri, şıklar ve",
          "çeldiriciler bize aittir; hiçbir soru bir sınavdan aynen alınmamıştır. HyperFrames ile üretildi.", "", "## Sorular", ""]
for i, q in enumerate(qs, 1):
    opts = " · ".join((f"**{L}) {o}**" if L == q["answer"] else f"{L}) {o}") for L, o in zip("ABCDE", q["options"]))
    readme += [f"**Soru {i}.** {q['stem']}", opts, f"**Doğru cevap: {q['answer']}.** {q['why']} ({q['ref']})", ""]
readme += [f"Cevap dağılımı: {key}.", "", "## Video", "",
           f"- **Süre:** {mm} dk {ss:02d} sn · 1920×1080 · 30 fps",
           f"- **Seslendirme:** ElevenLabs **Eleven v4**, ses: **Cem** (12 sahne; akış \"Tarife Dersi {NUM} — Gümrük Koçu\")",
           "- **Ana karakter:** Gümrük Koçu — sabit görsel, titremez; tepki görsellerine yumuşak geçiş (soru · dikkat · uyarı · cevap · tuzak).",
           f"- **Ekip:** {DOC['team']}",
           "- **Rozetler:** SORU · DİKKAT · UYARI · TUZAK · İPUCU · ÖNEMLİ",
           f"- **Görseller:** {DOC['visuals']}; her soruda 3 saniyelik geri sayım. Soru okunurken alt yazıda anahtar kelime vurgusu yapılmaz.",
           "", "## Dosyalar", "", "| Dosya | Ne işe yarar |", "| --- | --- |",
           f"| `renders/{name}-web.mp4` | Bitmiş video (repoda). Ana render boyut nedeniyle repoya eklenmez |",
           "| `youtube-aciklama.txt` · `youtube-bolumler.txt` | YouTube başlık/açıklama/etiketler ve bölüm zaman damgaları |",
           "| `altyazi.srt` | Türkçe altyazı (pozisyon numaraları rakamla) |",
           "| `narration/script.json` · `narration/display.json` | Seslendirme metni · alt yazıda rakama çevrilen ifadeler |",
           "| `tools/` | `kit.py` (sahne şablonları), `scenes.py` (bu dersin verisi), `video.py` (ayarlar), `build_timing.py`, `build.py`, `docs.py` |",
           "", "## Yeniden üretmek", "", "```bash", "python3 tools/build_timing.py", "cd tools && python3 build.py && python3 docs.py && cd ..",
           "npx hyperframes check", f"npx hyperframes render -o renders/{name}.mp4", "```", ""]
(ROOT / "README.md").write_text("\n".join(readme))

brief = ["---", "workflow: general-video", "flow: automation", "storyboard: no", f'message: "{DOC["message"]}"', "destination: youtube",
         "aspect: 1920x1080", "language: tr", "audience: gümrük müşavirliği / muavinliği sınavına hazırlananlar, gümrük öğrencileri (ders kanalı)",
         f"length: ~{total / 60:.1f} dk".replace(".", ","), "angle: örnek soru çözümü / ders serisi (her videoda 3 soru)", "---", "", "## Intent", "",
         f"Gümrük Koçu tarife dersleri serisinin {NUM}. videosu. {DOC['intent']} Soru kökleri, şıklar ve çeldiriciler bize ait; 5 şıklı;",
         "videonun hiçbir yerinde soruların bir sınavdan alındığı ima edilmez. Soru hazırlama ilkeleri: 2027-GM- reposundaki",
         "\"Soru Hazırlama Kurgusu ve Kuralları\" belgesi.", "", "## Assets", "",
         "- assets/img/koc-*.png — Gümrük Koçu (ana karakter) ve tepki görselleri.",
         "- assets/img/stajyer-cut.png, yardimci-cut.png, cano-cut.png, baba-crop.png — ekip.", "- assets/img/logo-crop.png — logo.", "",
         "## Customizations", "", "- Seslendirme: ElevenLabs **eleven_v4**, ses **Cem** (voice_id D1xRw7f8ZHedI7xJgfvz).",
         "- Maskot titremez; tepki görselleri arasında yumuşak geçiş.", "", "## Notes", "", f"- Doğrulama kaynakları: {DOC['sources']}", ""]
(ROOT / "BRIEF.md").write_text("\n".join(brief))

sb = ["---", "mode: autonomous", f'message: "{DOC["message"]}"', "canvas: 1920x1080", f"duration: {total}s (sesten türetildi — timing.json)", "---", "",
      f"# Tarife dersi {NUM} — sahne planı", ""]
for s in T["scenes"]:
    sb += [f"## {s['id']} · {s['title']}", f"- {s['start']:.1f}s → {s['start'] + s['dur']:.1f}s · src: compositions/{s['id']}.html",
           f"- {DOC['scenes'][s['id']]}", ""]
(ROOT / "STORYBOARD.md").write_text("\n".join(sb))

yt = ["BAŞLIK", DOC["yt_title"], "", "AÇIKLAMA", DOC["yt_intro"], "", "Bu derste:"]
yt += [f"• Soru {i} — {q['yt']}" for i, q in enumerate(qs, 1)]
yt += ["", "BÖLÜMLER"] + [f"{ts(t)} {n}" for n, t in chap]
yt += ["", f"Cevap anahtarı: 1-{qs[0]['answer']} · 2-{qs[1]['answer']} · 3-{qs[2]['answer']}. Kaç tanesini bildiniz? Yorumlara yazın!", "",
       "Videodaki sorular eğitim amaçlı hazırlanmış özgün örneklerdir. Somut sınıflandırma işlemlerinde güncel Türk Gümrük Tarife Cetveli, izahname ve idarenin görüşleri esas alınmalıdır.",
       "", "ETİKETLER", DOC["tags"], "", DOC["hashtags"], ""]
(ROOT / "youtube-aciklama.txt").write_text("\n".join(yt))
print("docs written", name)
