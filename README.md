# ArUco 4×4 Web Scanner

Web-based ArUco marker scanner using **4×4** markers (OpenCV `DICT_4X4_50`). **Runs entirely in the browser** — no server. Deploy to your website or GitHub Pages.

## Primary: Standalone (no server)

- **`index.html`** – Single HTML file. ArUco detection runs in the browser via [js-aruco2](https://github.com/damianofalcioni/js-aruco2) with a custom **DICT_4X4_50** dictionary.
- **Camera**: `getUserMedia` only works in a **secure context** (HTTPS or `localhost`).  
  - ✅ **GitHub Pages** (HTTPS) — ideal for testing on **mobile** (phone needs HTTPS).  
  - ✅ **Your site over HTTPS**  
  - ✅ **http://localhost** (e.g. with `npx serve .` or Python `http.server`) — desktop only.  
  - ❌ **file://** or plain HTTP (e.g. `http://192.168.x.x`) — camera unavailable; **mobile cannot use a local HTTP server** without HTTPS.

### Deploy to GitHub Pages

1. Push this repo to GitHub.
2. **Settings → Pages → Source**: Deploy from branch (e.g. `main`), root.
3. Open `https://<your-username>.github.io/<repo-name>/` (or your custom domain). The camera will work over HTTPS.

### Run locally (HTTPS or localhost)

```bash
# Option A: localhost with a simple server
npx serve . -p 8080
# Open http://localhost:8080

# Option B: Python
python -m http.server 8080
# Open http://localhost:8080
```

Then open **http://localhost:8080** and click “Start camera”.

## Features

- **4×4 ArUco** – DICT_4X4_50 (50 markers, 16 bits), same as OpenCV.
- **HTML-native** – No backend; works on GitHub Pages and any static host.
- **Auto-scan** – Continuous detection and overlay of marker IDs/corners.
- **Mobile-friendly** – Works in mobile browsers over HTTPS.

## Generate 4×4 markers (for printing)

Use the Python script (requires OpenCV):

```bash
pip install opencv-contrib-python
python generate_markers.py --ids 0 1 2 3 --size 200 --out markers
```

Images go to `markers/` (e.g. `aruco_4x4_id_0.png`). Use these with the web scanner; dictionary is **DICT_4X4_50**.

## Optional: Python server (backend detection)

If you prefer server-side OpenCV detection (e.g. for pose estimation later):

```bash
pip install -r requirements.txt
python server.py
```

- Serves **http://localhost:5000** (and `static/index.html` there uses the server’s `/api/detect`).
- The **root `index.html`** is standalone and does **not** use the server; use it for GitHub Pages.

## Project layout

| File | Purpose |
|------|--------|
| **index.html** | Standalone scanner (browser-only, 4×4). Use this for GitHub Pages / your site. |
| **server.py** | Optional Flask backend with OpenCV ArUco (for server-side detection). |
| **static/index.html** | Alternative UI that posts frames to the server (used when running `server.py`). |
| **generate_markers.py** | Generate printable DICT_4X4_50 marker images. |
| **requirements.txt** | Dependencies for the optional server. |

Dictionary: **DICT_4X4_50** (4×4 bits, 50 markers). The standalone page injects this dictionary into js-aruco2 so it matches OpenCV’s 4×4 markers.
