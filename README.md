# ArUco & AprilTag Web Scanner

HTML-based ArUco and AprilTag scanner and pattern generator. Runs in the browser, no server. Works on GitHub Pages and any static host.

**Live:** [https://fiducials.mess.engineering](https://fiducials.mess.engineering)

## What it does

- **ArUco 4×4** – Dictionary DICT_4X4_1000 (built-in, byte-swapped like OpenCV). Filled cells = ID 0–250, empty = 250+.
- **AprilTag 36h11** – 587 IDs, 8×8 layout with 1-cell border; same codes as official 36h11 family.
- **In-browser detection** via [js-aruco2](https://github.com/damianofalcioni/js-aruco2); dictionaries embedded (no external fetch).
- **Camera** – Live video, cyan overlay with marker IDs, optional gray/binary debug view with pseudo-3D boxes (magenta).
- **Generator** – Grid layout (click filled/empty), Smiley preset, PNG download for ArUco and AprilTag.
- **Mobile-friendly** – Throttled on small screens; works in mobile browsers over HTTPS.

## Requirements

- **HTTPS or localhost** – `getUserMedia` (camera) only works in a secure context.
  - Use the GitHub Pages link above (HTTPS), or
  - Run locally: `npx serve . -p 8080` then open **http://localhost:8080**.

## Project

| File             | Purpose |
|------------------|--------|
| **index.html**   | Landing page (links to Scanner & Generator). |
| **scanner.html** | Camera-based ArUco/AprilTag scanner. |
| **generator.html** | Pattern generator: ArUco 4×4 or AprilTag 36h11, grid, Smiley preset, PNG download. |

## Tests / dev tools

The **tests/** folder contains optional dev and verification files:

| File | Purpose |
|------|--------|
| **apriltag36_test.html** | Visual check: AprilTag IDs 0–4 with 36-bit bit dump (verifies rendering vs. PNG). |
| **apriltag36h11_gen.py** | Generates AprilTag 36h11 PNGs and **codes_36h11.txt** from `generator.html` (needs Pillow). Run from repo root: `python tests/apriltag36h11_gen.py`. |
| **dump_aruco_1000.py** | Dumps DICT_4X4_1000 codes to JS array (for reference). |
| **codes_36h11.txt** / **codes_1000.txt** | Code lists (hex + JS array) for copy/paste. |

You can **commit tests/** (small, useful for future checks) or leave it out; generated PNGs in `tests/apriltag36h11_out/` are ignored via `.gitignore`.

## License

**MIT** – see [LICENSE](LICENSE).

Uses [js-aruco2](https://github.com/damianofalcioni/js-aruco2); its license applies. ArUco dictionary: built-in OpenCV-style. AprilTag 36h11: 587 codes, same layout as official family.
