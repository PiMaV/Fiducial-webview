"""
AprilTag 36h11: PNG-Tags erzeugen und Codes in TXT schreiben.
Liest CODE_LIST_36H11 + Bit-Layout aus generator.html (eine Quelle).
Run: python apriltag36h11_gen.py
Output: Ordner apriltag36h11_out/ mit tag_000.png .. tag_586.png, plus codes_36h11.txt
"""
import os
import re

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Bitte installieren: pip install Pillow")
    raise SystemExit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
# generator.html liegt im Repo-Root (bei Skript in tests/)
GENERATOR_HTML = os.path.join(REPO_ROOT, "generator.html")
OUT_DIR = os.path.join(SCRIPT_DIR, "apriltag36h11_out")
CODES_TXT = os.path.join(SCRIPT_DIR, "codes_36h11.txt")

# Bit-Layout 8x8: 1 Zelle Rahmen, 6x6 Daten (BIT_X/BIT_Y 1..6) – wie offiziell 1-bit border
APRILTAG_BIT_X = [1, 2, 3, 4, 5, 2, 3, 4, 3, 6, 6, 6, 6, 6, 5, 5, 5, 4, 6, 5, 4, 3, 2, 5, 4, 3, 4, 1, 1, 1, 1, 1, 2, 2, 2, 3]
APRILTAG_BIT_Y = [1, 1, 1, 1, 1, 2, 2, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 3, 6, 6, 6, 6, 6, 5, 5, 5, 4, 6, 5, 4, 3, 2, 5, 4, 3, 4]
BORDER_START = 0  # Daten direkt bei BIT_X/BIT_Y (1..6) → 1 Zelle Rahmen links/oben/unten/rechts
SIZE_CELLS = 8


def load_codes_from_generator():
    """Liest CODE_LIST_36H11 aus generator.html."""
    if not os.path.isfile(GENERATOR_HTML):
        raise FileNotFoundError("generator.html nicht gefunden (im Repo-Root, z. B. von dort: python tests/apriltag36h11_gen.py).")
    with open(GENERATOR_HTML, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.search(r"var CODE_LIST_36H11 = \[([^\]]+)\]", content)
    if not m:
        raise ValueError("CODE_LIST_36H11 in generator.html nicht gefunden.")
    codes = [int(x.strip(), 16) for x in m.group(1).split(",")]
    return codes


def draw_tag_36h11(code, cell_px=8):
    """Zeichnet einen AprilTag 36h11: schwarzer Hintergrund, weiße Zellen wo Bit=1, MSB=Bit0."""
    size = SIZE_CELLS * cell_px
    img = Image.new("RGB", (size, size), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    white = (255, 255, 255)
    for i in range(36):
        if (code >> (35 - i)) & 1:
            x = APRILTAG_BIT_X[i] * cell_px
            y = APRILTAG_BIT_Y[i] * cell_px
            draw.rectangle([x, y, x + cell_px - 1, y + cell_px - 1], fill=white)
    return img


def main():
    codes = load_codes_from_generator()
    n = len(codes)
    print(f"AprilTag 36h11: {n} Codes aus generator.html geladen.")

    os.makedirs(OUT_DIR, exist_ok=True)
    cell_px = 12

    for tag_id, code in enumerate(codes):
        img = draw_tag_36h11(code, cell_px=cell_px)
        path = os.path.join(OUT_DIR, f"tag_{tag_id:03d}.png")
        img.save(path)
    print(f"PNGs gespeichert: {OUT_DIR}/tag_000.png .. tag_{n-1:03d}.png")

    with open(CODES_TXT, "w", encoding="utf-8") as f:
        f.write("# AprilTag 36h11 – ID : 36-bit-Code (hex)\n")
        f.write("# Gleiche Quelle wie generator.html (CODE_LIST_36H11)\n\n")
        for tag_id, code in enumerate(codes):
            f.write(f"{tag_id}\t{code:09x}\n")
        f.write("\n# JavaScript-Array (zum Kopieren):\n")
        hex_codes = ",".join(f"0x{c:010x}" for c in codes)
        f.write(f"var CODE_LIST_36H11 = [{hex_codes}];\n")
    print(f"Codes geschrieben: {CODES_TXT}")


if __name__ == "__main__":
    main()
