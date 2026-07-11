from flask import Flask, render_template, request
import os

from utils.image_detector import detect_image
from utils.video_detector import detect_video

app = Flask(__name__)

# -----------------------------
# Folders
# -----------------------------

IMAGE_UPLOAD = os.path.join("static", "uploads", "images")
VIDEO_UPLOAD = os.path.join("static", "uploads", "videos")

IMAGE_OUTPUT = os.path.join("static", "outputs", "images")
VIDEO_OUTPUT = os.path.join("static", "outputs", "videos")

os.makedirs(IMAGE_UPLOAD, exist_ok=True)
os.makedirs(VIDEO_UPLOAD, exist_ok=True)
os.makedirs(IMAGE_OUTPUT, exist_ok=True)
os.makedirs(VIDEO_OUTPUT, exist_ok=True)


# -----------------------------
# Home
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Image Detection
# -----------------------------

@app.route("/upload_image", methods=["POST"])
def upload_image():

    if "image" not in request.files:
        return "No image uploaded."

    file = request.files["image"]

    if file.filename == "":
        return "No image selected."

    image_path = os.path.join(
        IMAGE_UPLOAD,
        file.filename
    )

    file.save(image_path)

    output_path = detect_image(image_path)

    print("Original Image:", image_path)
    print("Detected Image:", output_path)

    return render_template(
        "image_result.html",
        original=os.path.relpath(image_path, "static").replace("\\", "/"),
        detected=os.path.relpath(output_path, "static").replace("\\", "/")
    )


# -----------------------------
# Video Detection
# -----------------------------

@app.route("/upload_video", methods=["POST"])
def upload_video():

    if "video" not in request.files:
        return "No video uploaded."

    file = request.files["video"]

    if file.filename == "":
        return "No video selected."

    video_path = os.path.join(
        VIDEO_UPLOAD,
        file.filename
    )

    file.save(video_path)

    output_path = detect_video(video_path)

    print("Original Video:", video_path)
    print("Detected Video:", output_path)

    return render_template(
        "video_result.html",
        original=os.path.relpath(video_path, "static").replace("\\", "/"),
        detected=os.path.relpath(output_path, "static").replace("\\", "/")
    )


# -----------------------------
# Run
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)