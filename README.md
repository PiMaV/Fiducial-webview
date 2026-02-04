# fiducial-webview

Browser-based **AprilTag** and **ArUco** scanner and pattern generator — no server, no build step. Works on GitHub Pages and any static host.

**Live:** [fiducials.mess.engineering](https://fiducials.mess.engineering) · **GitHub Pages:** [pimav.github.io/fiducial-webview](https://pimav.github.io/fiducial-webview/)

## Features

- **AprilTag 36h11** — 587 IDs, 8×8 layout; same codes as official 36h11 family
- **ArUco 4×4** — DICT_4X4_1000 (built-in, byte-swapped like OpenCV)
- **In-browser detection** — [js-aruco2](https://github.com/damianofalcioni/js-aruco2); dictionaries embedded
- **Live camera** — Video feed with cyan overlay, optional gray/binary debug view
- **Pattern generator** — Grid layout (click to fill/clear), Smiley & Logo presets, PNG download
- **Mobile-friendly** — Throttled on small screens; works over HTTPS

## Quick Start

Camera requires **HTTPS or localhost** (secure context). Options:

1. Use the live link above, or
2. Run locally: `npx serve . -p 8080` → open **http://localhost:8080**

## Project Structure

| File | Description |
|------|-------------|
| **index.html** | Landing page |
| **scanner.html** | Camera-based scanner (AprilTag / ArUco) |
| **generator.html** | Pattern generator (grid, presets, PNG export) |

## Tests

| File | Purpose |
|------|---------|
| **apriltag36_test.html** | AprilTag IDs 0–4 visual check + bit dump |
| **apriltag36h11_gen.py** | Generate PNGs from `generator.html` codes (requires Pillow) |
| **dump_aruco_1000.py** | Export DICT_4X4_1000 to JS array |
| **codes_36h11.txt** / **codes_1000.txt** | Code lists for reference |

Run generator: `python tests/apriltag36h11_gen.py` from repo root. Output: `tests/apriltag36h11_out/` (gitignored).

## License

**MIT** — see [LICENSE](LICENSE). Uses [js-aruco2](https://github.com/damianofalcioni/js-aruco2); ArUco dictionary: OpenCV-style; AprilTag 36h11: official family layout.
