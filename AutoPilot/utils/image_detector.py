import os
from ultralytics import YOLO

# ----------------------------------
# Load trained model (loads only once)
# ----------------------------------
MODEL_PATH = "models/best.pt"
model = YOLO(MODEL_PATH)


def detect_image(image_path):
    """
    Detect objects in an uploaded image
    and save the annotated image.
    """

    # Run prediction
    results = model.predict(
        source=image_path,
        conf=0.25,
        save=False,
        verbose=False
    )

    # Annotated image
    annotated = results[0].plot()

    # Output path
    filename = os.path.basename(image_path)

    output_path = os.path.join(
        "static",
        "outputs",
        "images",
        filename
    )

    # Save image
    import cv2
    cv2.imwrite(output_path, annotated)

    return output_path