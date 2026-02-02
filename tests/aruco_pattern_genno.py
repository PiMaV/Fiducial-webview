import cv2
import cv2.aruco as aruco
import numpy as np
from PIL import Image

# --- Config ---
MARKER_PX = 60
PADDING = 5
# One dict: 0–249 = real (DICT_250), 250–999 = fake (no collision)
DICT = aruco.getPredefinedDictionary(aruco.DICT_4X4_1000)
FAKE_ID_MIN = 250  # Real = 0..249, Fake = 250..999

# --- 1. Symmetric 11x11 matrix ---
# 1 = real (ID 0..249), 0 = fake (ID 250..999)
X = 1
_ = 0

base_matrix = [
    [0,0,0,0,0,0,0,0,0,0,0],  # R1
    [0,X,X,X,0,0,0,X,X,X,0],  # R2 eye top
    [0,X,0,X,0,0,0,X,0,X,0],  # R3 eye middle (hole)
    [0,X,X,X,0,0,0,X,X,X,0],  # R4 eye bottom
    [0,0,0,0,0,0,0,0,0,0,0],  # R5
    [0,0,0,0,0,0,0,0,0,0,0],  # R6
    [X,0,0,0,0,0,0,0,0,0,X],  # R7 mouth corners
    [0,X,0,0,0,0,0,0,0,X,0],  # R8
    [0,0,X,0,0,0,0,0,X,0,0],  # R9
    [0,0,0,X,X,X,X,X,0,0,0],  # R10 mouth bottom
    [0,0,0,0,0,0,0,0,0,0,0],  # R11
]

rows = len(base_matrix)
cols = len(base_matrix[0])

# --- 2. Generate image ---
canvas_size = rows * MARKER_PX + (rows + 1) * PADDING
canvas = np.full((canvas_size, canvas_size), 255, dtype=np.uint8)

s_id = 0
f_id = 0
fake_range = 1000 - FAKE_ID_MIN
for r in range(rows):
    for c in range(cols):
        y = r * MARKER_PX + (r + 1) * PADDING
        x = c * MARKER_PX + (c + 1) * PADDING
        
        if base_matrix[r][c] == 1:
            img = aruco.generateImageMarker(DICT, s_id % FAKE_ID_MIN, MARKER_PX)
            s_id += 1
        else:
            img = aruco.generateImageMarker(DICT, FAKE_ID_MIN + (f_id % fake_range), MARKER_PX)
            f_id += 1
        canvas[y:y+MARKER_PX, x:x+MARKER_PX] = img

# Save
final_img = Image.fromarray(canvas)
final_img.save('aruco_11x11_symmetric.png')