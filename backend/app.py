from flask import Flask, Response, render_template, jsonify
import threading
import time
import cv2

from logic import latest_frames, update_frames_loop, current_lane, state, green_time

app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../frontend",
    static_url_path="",
)


# =========================
# STREAM FUNCTION
# =========================
def generate_lane(lane_id):
    while True:
        frame = latest_frames[lane_id]

        if frame is None:
            time.sleep(0.01)
            continue

        _, buffer = cv2.imencode(".jpg", frame)

        yield (
            b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
        )

        time.sleep(0.03)


# =========================
# ROUTES
# =========================
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed/<int:lane_id>")
def video_feed(lane_id):
    return Response(
        generate_lane(lane_id), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/status")
def status():
    return jsonify(
        {"current_lane": current_lane, "state": state, "green_time": green_time}
    )


# =========================
# RUN
# =========================
if __name__ == "__main__":
    threading.Thread(target=update_frames_loop, daemon=True).start()
    app.run(debug=False)
