"""Dump DICT_4X4_1000 raw 16-bit codes (rotation 0) for use in generator/scanner.
   Run: python dump_aruco_1000.py
   Output: JavaScript array of 1000 hex codes (same format as CODE_LIST_4X4_250).
"""
import cv2.aruco as aruco

d = aruco.getPredefinedDictionary(aruco.DICT_4X4_1000)
# bytesList: (nMarkers, nBytes*4) where nBytes=2 for 4x4. Rotation 0 = first 2 bytes.
# Our CODE_LIST uses raw code = byte0 | (byte1<<8) to match OpenCV 0x32b5 for ID 0.
codes = []
bl = d.bytesList  # shape (1000, 2, 4): rot0 bytes at [i,0,0] and [i,0,1] -> 0x32b5 for id0
for i in range(1000):
    b0, b1 = int(bl[i, 0, 0]), int(bl[i, 0, 1])
    code = b0 | (b1 << 8)
    codes.append(hex(code))
# Print as single line for pasting
line = "var CODE_LIST_4X4_1000 = [" + ",".join(codes) + "];"
print(line)
