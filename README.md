# ArUco 4×4 Web Scanner

HTML-based ArUco scanner and pattern generator. Runs in the browser, no server. Works on GitHub Pages and any static host.

**Live:** [https://aruco.mess.engineering](https://aruco.mess.engineering)

## What it does

- **4×4 ArUco** – Dictionary sizes 50 and 250 (built-in, same codes as OpenCV DICT_4X4_250).
- **In-browser detection** via [js-aruco2](https://github.com/damianofalcioni/js-aruco2); dictionary embedded (no external fetch).
- **Camera** – Live video, cyan overlay with marker IDs, optional gray/binary debug view with pseudo-3D boxes (magenta).
- **Mobile-friendly** – Throttled on small screens; works in mobile browsers over HTTPS.

## Requirements

- **HTTPS or localhost** – `getUserMedia` (camera) only works in a secure context.
  - Use the GitHub Pages link above (HTTPS), or
  - Run locally: `npx serve . -p 8080` then open **http://localhost:8080**.

## Project

| File             | Purpose                                      |
|------------------|----------------------------------------------|
| **index.html**   | Landing page (links to Scanner & Generator). |
| **scanner.html** | Camera-based ArUco scanner.                  |
| **generator.html** | Pattern generator (grid, Smiley preset, PNG download). |

## License

**MIT** – see [LICENSE](LICENSE).

Uses [js-aruco2](https://github.com/damianofalcioni/js-aruco2); its license applies. Dictionary: built-in OpenCV DICT_4X4_250.
