import cv2
import numpy as np
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================
# VIDEO SOURCES
# =========================
caps = [
    cv2.VideoCapture(os.path.join(BASE_DIR, "videos/lane1.mp4")),
    cv2.VideoCapture(os.path.join(BASE_DIR, "videos/lane2.mp4")),
    cv2.VideoCapture(os.path.join(BASE_DIR, "videos/lane3.mp4")),
    cv2.VideoCapture(os.path.join(BASE_DIR, "videos/lane4.mp4")),
]

# =========================
# GLOBAL STATE
# =========================
latest_frames = [None, None, None, None]

current_lane = 0
green_time = 10
state = "GREEN"


# =========================
# FRAME LOOP
# =========================
def update_frames_loop():
    global latest_frames

    while True:
        frames = []

        for i in range(4):
            ret, frame = caps[i].read()

            if not ret:
                # fallback image (TEST)
                frame = np.zeros((240, 320, 3), dtype=np.uint8)
                cv2.putText(
                    frame,
                    f"Lane {i}",
                    (50, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )
            else:
                frame = cv2.resize(frame, (320, 240))

            frames.append(frame)

        latest_frames = frames
        time.sleep(0.1)  # 🔥 LOW LOAD
