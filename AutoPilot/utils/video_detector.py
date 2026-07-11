import os
import cv2
from ultralytics import YOLO


MODEL_PATH = "models/best.pt"

model = YOLO(MODEL_PATH)


def detect_video(video_path):

    input_frames = "frames/input"
    output_frames = "frames/output"

    os.makedirs(input_frames, exist_ok=True)
    os.makedirs(output_frames, exist_ok=True)
    os.makedirs("static/outputs/videos", exist_ok=True)


    # Clear old frames

    for folder in [input_frames, output_frames]:

        for file in os.listdir(folder):

            path = os.path.join(folder, file)

            if os.path.isfile(path):
                os.remove(path)



    # -----------------------------
    # Read video
    # -----------------------------

    cap = cv2.VideoCapture(video_path)


    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30


    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


    print("FPS:", fps)
    print("Resolution:", width, height)



    frame_count = 0


    # -----------------------------
    # Extract frames
    # -----------------------------

    while True:

        ret, frame = cap.read()

        if not ret:
            break


        cv2.imwrite(
            os.path.join(
                input_frames,
                f"{frame_count:06d}.jpg"
            ),
            frame
        )


        frame_count += 1


    cap.release()


    print("Extracted:", frame_count)



    # -----------------------------
    # Detection
    # -----------------------------

    for frame_name in sorted(os.listdir(input_frames)):


        frame_path = os.path.join(
            input_frames,
            frame_name
        )


        results = model.predict(
            source=frame_path,
            conf=0.25,
            verbose=False
        )


        annotated = results[0].plot()


        cv2.imwrite(
            os.path.join(
                output_frames,
                frame_name
            ),
            annotated
        )


    print("Detection completed")



    # -----------------------------
    # Create browser compatible video
    # -----------------------------

    filename = os.path.splitext(
        os.path.basename(video_path)
    )[0]


    output_video = os.path.join(
        "static",
        "outputs",
        "videos",
        filename + ".mp4"
    )


    # H264 codec for browser

    fourcc = cv2.VideoWriter_fourcc(
        *"avc1"
    )


    writer = cv2.VideoWriter(
        output_video,
        fourcc,
        fps,
        (width, height)
    )


    if not writer.isOpened():

        print("avc1 failed, using mp4v")

        fourcc = cv2.VideoWriter_fourcc(
            *"mp4v"
        )

        writer = cv2.VideoWriter(
            output_video,
            fourcc,
            fps,
            (width, height)
        )



    for frame_name in sorted(os.listdir(output_frames)):


        img = cv2.imread(
            os.path.join(
                output_frames,
                frame_name
            )
        )


        writer.write(img)



    writer.release()


    print("Video created:")
    print(output_video)


    return output_video