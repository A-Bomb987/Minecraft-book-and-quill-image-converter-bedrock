from PIL import Image
import os

MC_COLORS = {
    "0": (0, 0, 0),
    "1": (0, 0, 170),
    "2": (0, 170, 0),
    "3": (0, 170, 170),
    "4": (170, 0, 0),
    "5": (170, 0, 170),
    "6": (255, 170, 0),
    "7": (170, 170, 170),
    "8": (85, 85, 85),
    "9": (85, 85, 255),
    "a": (85, 255, 85),
    "b": (85, 255, 255),
    "c": (255, 85, 85),
    "d": (255, 85, 255),
    "e": (255, 255, 85),
    "f": (255, 255, 255),
}

SHADE_CHARS = ["█", "▓", "▒", "░"]

def closest_mc_color(rgb):
    r, g, b = rgb
    best_code = "f"
    best_dist = float("inf")
    for code, (cr, cg, cb) in MC_COLORS.items():
        dr = r - cr
        dg = g - cg
        db = b - cb
        dist = dr*dr + dg*dg + db*db
        if dist < best_dist:
            best_dist = dist
            best_code = code
    return best_code

def shade_char(rgb):
    r, g, b = rgb
    brightness = (r + g + b) / 3
    if brightness < 64:
        return SHADE_CHARS[0]
    elif brightness < 128:
        return SHADE_CHARS[1]
    elif brightness < 192:
        return SHADE_CHARS[2]
    else:
        return SHADE_CHARS[3]

def convert_image(path, out_width=50, out_height=25):
    img = Image.open(path).convert("RGB")
    img = img.resize((out_width, out_height), Image.Resampling.LANCZOS)

    lines = []
    for y in range(img.height):
        line = ""
        for x in range(img.width):
            rgb = img.getpixel((x, y))
            code = closest_mc_color(rgb)
            ch = shade_char(rgb)
            line += f"§{code}{ch}"
        lines.append(line)

    base, ext = os.path.splitext(path)
    out_path = base + "_mc_text.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"Done! Saved to: {out_path}")

if __name__ == "__main__":
    img_name = input("Enter image file name: ").strip()
    if not os.path.isfile(img_name):
        print("File not found.")
        exit()

    try:
        w = input("Output width (default 50): ").strip()
        h = input("Output height (default 25): ").strip()
        w = int(w) if w else 50
        h = int(h) if h else 25
    except ValueError:
        w, h = 50, 25

    convert_image(img_name, w, h)
