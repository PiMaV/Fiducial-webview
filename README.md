# ArUco 4×4 Web Scanner

Simple HTML-based ArUco live view to test markers in the browser. One file, no server. Works on GitHub Pages and any static host.

**Live:** [https://PiMaV.github.io/aruco-webview/](https://PiMaV.github.io/aruco-webview/)

## What it does

- **4×4 ArUco** – Dictionary sizes 50, 250, or 1000 (same codes as [arucogen](https://chev.me/arucogen/)).
- **In-browser detection** via [js-aruco2](https://github.com/damianofalcioni/js-aruco2); marker codes loaded from [okalachev/arucogen](https://github.com/okalachev/arucogen).
- **Camera** – Live video, green overlay with marker IDs, optional gray/binary debug view with pseudo-3D boxes.
- **Mobile-friendly** – Throttled on small screens; works in mobile browsers over HTTPS.

## Requirements

- **HTTPS or localhost** – `getUserMedia` (camera) only works in a secure context.
  - Use the GitHub Pages link above (HTTPS), or
  - Run locally: `npx serve . -p 8080` then open **http://localhost:8080**.

## Project

| File        | Purpose                    |
|------------|----------------------------|
| **index.html** | The scanner (single file). |

## License

**MIT** – see [LICENSE](LICENSE).

Uses [js-aruco2](https://github.com/damianofalcioni/js-aruco2) and [arucogen](https://github.com/okalachev/arucogen) dictionary data; their licenses apply to those parts.
