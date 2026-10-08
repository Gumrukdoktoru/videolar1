"""Bundle the rendered PNG slides into one PDF (raster; the vector print of the SVG filters is ~70 MB)."""
import pathlib
from PIL import Image

D = pathlib.Path(__file__).resolve().parent
pages = [Image.open(p).convert("RGB") for p in sorted((D / "png").glob("ozet-beyan-quiz-*.png"))]
out = D / "ozet-beyan-quiz-carousel.pdf"
pages[0].save(out, save_all=True, append_images=pages[1:], resolution=72, quality=92)
print(out, len(pages), "pages")
