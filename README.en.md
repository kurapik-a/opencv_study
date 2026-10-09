# OpenCV Learning Notes

A collection of hands-on OpenCV practice scripts in Python. Each script covers a single topic, progressing from basic image I/O through interactive controls, video processing, filtering, edge detection, and finally motion-based vehicle counting.

## Repository Structure

```
opencv/
├── LICENSE
├── README.md              # Chinese documentation
├── README.en.md           # English documentation (this file)
└── OpenCV入门/            # All practice scripts
    ├── first.py           # Read and display an image
    ├── mouse.py           # Mouse event callbacks
    ├── TrackBar.py        # Trackbar controls
    ├── video_read.py      # Read video frames
    ├── video_write.py     # Write video to file
    ├── test.py            # Capture from webcam and save
    ├── aftrer.py          # Drawing primitives (lines, ellipses, polygons, text)
    ├── drewshape.py       # Interactive drawing with the mouse
    ├── drewshape copy.py  # Drawing mode switching (line / circle)
    ├── thresh.py          # Six thresholding methods
    ├── blur.py            # Filtering and edge detection
    ├── contours.py        # Contour detection and drawing
    ├── addlogo.py         # Image watermarking (alpha blending)
    └── car_count.py       # Vehicle counting via motion detection
```

## Requirements

| Dependency | Version |
|---|---|
| Python | 3.8+ |
| opencv-python | 4.x |
| numpy | any recent version |
| matplotlib | required only by `car_count.py` |

```bash
pip install opencv-python numpy matplotlib
```

## Scripts Overview

| Script | Topic | Key APIs |
|---|---|---|
| `first.py` | Image loading, display, key interaction, saving | `imread` / `imshow` / `waitKey` / `imwrite` |
| `mouse.py` | Mouse event callbacks | `setMouseCallback` |
| `TrackBar.py` | Trackbars for live parameter tuning | `createTrackbar` / `getTrackbarPos` |
| `video_read.py` | Reading and displaying video frame by frame | `VideoCapture` |
| `video_write.py` | Capturing from webcam and recording to file | `VideoWriter` / `VideoWriter_fourcc` |
| `test.py` | Reading capture properties and saving video | `cap.get(3)` / `cap.get(4)` |
| `aftrer.py` | Drawing primitives | `line` / `ellipse` / `polylines` / `putText` |
| `drewshape.py` | Drag-to-draw with live preview | Event callback + ROI restore |
| `drewshape copy.py` | Switching drawing mode via keys | Global state + key branching |
| `thresh.py` | Six thresholding variants | `threshold` + `THRESH_OTSU` |
| `blur.py` | Smoothing filters and edge detection | `blur` / `GaussianBlur` / `medianBlur` / `bilateralFilter` / `Sobel` / `Scharr` / `Laplacian` / `Canny` |
| `contours.py` | Contour detection and rendering | `findContours` / `drawContours` |
| `addlogo.py` | Watermark overlay with alpha blending | `multiply` / `add` / ROI assignment |
| `car_count.py` | Motion-based vehicle detection and counting | `createBackgroundSubtractorKNN` + morphology + area filtering |

## Detailed Notes

### Basic Image Operations

**`first.py`** — Loads an image and displays it in a resizable window. Press `q` to quit, `s` to save the frame as `cat.png`; any other key prints its character. A minimal template for keyboard-driven interaction.

**`aftrer.py`** — Draws a single red line on a blank canvas using `cv2.line` (color `(0,0,255)`, thickness 5). Commented-out hints cover `ellipse()`, `polylines()`, `fillPoly()` and `putText()`.

### Interactive Controls

**`TrackBar.py`** — Creates three trackbars (R / G / B, range 0–255) over a 480×640 black canvas. The color updates in real time as the sliders move, making it the most intuitive demonstration of live parameter tuning.

**`mouse.py`** — Registers a mouse callback that prints every event (type, coordinates, flags, user data) to the console. Useful for understanding OpenCV's event model.

**`drewshape.py`** — A complete mouse drawing program: press the left button to anchor the start point, drag to preview, release to commit. Supports both line and circle modes. The key implementation detail is using a temporary image for the drag preview to avoid leaving trails.

**`drewshape copy.py`** — A stripped-down variant that keeps the callback skeleton and adds key-based mode switching (`l` for line, `c` for circle), helpful for studying state management in isolation.

### Video Processing

**`video_read.py`** — Reads a video file (`103236.mp4` by default; switch to camera index `0` if preferred) and displays it frame by frame. Press `q` to quit, `s` to save the current frame.

**`video_write.py`** — Captures from the webcam and records to `out.avi` using MJPG encoding at 24 FPS. Frame dimensions are queried dynamically via `cap.get(3)` / `cap.get(4)` so the writer configuration always matches the source.

**`test.py`** — A compact end-to-end walkthrough of webcam capture and video writing: read properties → create `VideoWriter` → write frames in a loop → release resources.

### Image Processing

**`thresh.py`** — Demonstrates six thresholding methods: binary, binary inverse, truncate, to-zero, to-zero inverse, and Otsu's method (`THRESH_OTSU`) for automatic threshold selection.

**`blur.py`** — A combined exercise in filtering and edge detection, organized in three groups:

| Category | Methods |
|---|---|
| Smoothing | Mean, Gaussian, median, bilateral, box, custom kernel (`filter2D`) |
| First-order derivative | Sobel (x / y), Scharr |
| Second-order derivative / edges | Laplacian, Canny |

> Note: the median filter requires an odd kernel size. Bilateral filtering preserves edges while denoising, at the cost of higher runtime.

**`contours.py`** — Grayscale → Otsu threshold → `findContours` with `RETR_LIST` and `CHAIN_APPROX_SIMPLE` → `drawContours` in red.

**`addlogo.py`** — An image watermarking utility exposing three functions:

- `add_watermark_with_bitwise()` — overlays a watermark at a given position, supporting PNG watermarks with an alpha channel; blending is done with `multiply` + `add`, and out-of-bounds coordinates are clamped
- `create_text_watermark()` — generates a transparent text watermark image via `putText`
- `add_multiple_watermarks()` — applies a watermark at several positions in one pass

> The blending formula is `result = watermark × alpha + background × (1 - alpha)`, consistent with standard alpha compositing.

### End-to-End Example

**`car_count.py`** — Detects and counts vehicles in a video. Pipeline:

```
read frame → Gaussian denoise → KNN background subtraction → erosion → dilation (×3)
→ morphological closing (×2) → find contours → area and aspect-ratio filtering → draw boxes
```

Filtering rules: contour area > 700, and aspect ratio within `0.2 – 5.0` (the latter rejects thin false positives such as lane markings). Press `Esc` to quit, `s` to save the frame.

> Two quirks are kept as-is to reflect the actual learning process: `cv2.cvtColor(frame, ...)` discards its return value (the intent was grayscale conversion), and `findContours` receives the morphological flag `MORPH_CLOSE` as its second argument.

## Getting Started

1. Enter the script directory: `cd OpenCV入门`
2. Provide the required test assets — several scripts depend on external images or videos that are not tracked in this repository:
   - `first.py` → `cat.1.jpg`
   - `blur.py`, `contours.py` → `dog.293.jpg`
   - `thresh.py` → `cat.14.jpg`
   - `car_count.py` → `video.mp4`
   - `video_read.py` → `103236.mp4`
3. Run a script: `python first.py`

Key conventions across scripts: `q` / `Esc` to quit, `s` to save the current frame. Scripts block on `waitKey`, so press a key to exit before closing the window.

## Suggested Learning Path

The scripts follow roughly this progression:

```
Image I/O and display  →  Interactive controls (mouse / trackbars)
        ↓
Video I/O  →  Drawing primitives  →  Thresholding  →  Filtering and edge detection
        ↓
Contours  →  Image compositing (watermark)  →  Motion detection and counting
```

Working through the "Scripts Overview" table in order is recommended — run each script first to see the effect, then read the code.

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.
