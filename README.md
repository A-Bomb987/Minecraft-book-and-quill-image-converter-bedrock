# 🎮 Minecraft Image-to-Text Art Converter

Convert any image into Minecraft-formatted text art using color codes and Unicode block characters — ready to paste directly into chat, books, or signs.

---

## 📸 How It Works

Each pixel in your image is mapped to one of Minecraft's 16 chat colors (the closest match by RGB distance), and its brightness determines which Unicode block character represents it (`█ ▓ ▒ ░`). The result is a `.txt` file full of lines like `§a▓§f░§3█...` that Minecraft renders as a pixelated, color-shaded version of your image.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- [Pillow](https://python-pillow.org/) imaging library

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**
   ```bash
   pip install Pillow
   ```

---

## 🖼️ Usage

Run the script and follow the prompts:

```bash
python mc_image_converter.py
```

You will be asked for:

| Prompt | Description | Default |
|---|---|---|
| `Image file name` | Path to your input image (JPG, PNG, etc.) | *(required)* |
| `Output width` | Number of characters wide | `50` |
| `Output height` | Number of character rows tall | `25` |

### Example

```
Enter image file name: sunset.png
Output width (default 50): 80
Output height (default 40): 40
Done! Saved to: sunset_mc_text.txt
```

The output file (`sunset_mc_text.txt`) will be created in the **same directory** as your input image.

---

## 📋 Output Format

Each line of the output file contains a sequence of Minecraft color codes and block characters:

```
§c█§4▓§6▒§e░§f█...
```

- `§` — Minecraft's color escape prefix
- The character after `§` (e.g. `a`, `f`, `3`) — one of 16 color codes
- The block character (`█ ▓ ▒ ░`) — represents pixel brightness

### Supported Color Codes

| Code | Color | RGB |
|---|---|---|
| `0` | Black | `(0, 0, 0)` |
| `1` | Dark Blue | `(0, 0, 170)` |
| `2` | Dark Green | `(0, 170, 0)` |
| `3` | Dark Aqua | `(0, 170, 170)` |
| `4` | Dark Red | `(170, 0, 0)` |
| `5` | Dark Purple | `(170, 0, 170)` |
| `6` | Gold | `(255, 170, 0)` |
| `7` | Gray | `(170, 170, 170)` |
| `8` | Dark Gray | `(85, 85, 85)` |
| `9` | Blue | `(85, 85, 255)` |
| `a` | Green | `(85, 255, 85)` |
| `b` | Aqua | `(85, 255, 255)` |
| `c` | Red | `(255, 85, 85)` |
| `d` | Light Purple | `(255, 85, 255)` |
| `e` | Yellow | `(255, 255, 85)` |
| `f` | White | `(255, 255, 255)` |

---

## ⚙️ Function Reference

### `closest_mc_color(rgb)`
Finds the nearest Minecraft color to a given RGB pixel using squared Euclidean distance.

- **Parameters:** `rgb` — a `(R, G, B)` tuple
- **Returns:** a single-character Minecraft color code string (e.g. `"a"`)

### `shade_char(rgb)`
Selects a Unicode block character based on average pixel brightness.

- **Parameters:** `rgb` — a `(R, G, B)` tuple
- **Returns:** one of `█ ▓ ▒ ░` (darkest to lightest)

| Brightness Range | Character |
|---|---|
| 0 – 63 | `█` |
| 64 – 127 | `▓` |
| 128 – 191 | `▒` |
| 192 – 255 | `░` |

### `convert_image(path, out_width=50, out_height=25)`
Orchestrates the full conversion pipeline.

- **Parameters:**
  - `path` — file path to the input image
  - `out_width` — target character width (default `50`)
  - `out_height` — target character height (default `25`)
- **Output:** writes a `_mc_text.txt` file next to the input image

---

## 💡 Tips

- **Aspect ratio:** Terminal characters are taller than they are wide. For images that look correct in Minecraft chat, try using roughly **2× the width vs. height** (e.g. `80 × 40`).
- **Image choice:** High-contrast images with bold colors convert best. Detailed or low-contrast photos may lose clarity at small sizes.
- **Pasting in Minecraft:** The output is designed for use with mods or plugins (e.g. Carpet, chat editors) that support `§` color codes. Vanilla chat may not render colors depending on your server settings.
- **File encoding:** The output is saved as UTF-8 to preserve the Unicode block characters.

---

## 📁 Project Structure

```
your-repo-name/
├── mc_image_converter.py   # Main script
└── README.md               # This file
```

---

## 📄 License

This project is open source. Add your preferred license here (e.g. [MIT](https://choosealicense.com/licenses/mit/)).

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to improve color matching, add dithering, or support additional output formats, feel free to open an issue or submit a PR.
