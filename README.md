# 🚗 AutoPilot - AI-Based Object Detection for Autonomous Driving

An AI-powered web application that detects road objects from images and videos using a custom-trained YOLOv8 model on the BDD100K dataset.

The application allows users to upload an image or video, performs object detection, and returns the annotated output through an easy-to-use Flask web interface.

---

## 📌 Features

- Upload and detect objects in images
- Upload and detect objects in videos
- Automatic frame extraction from uploaded videos
- Object detection on every frame using YOLOv8
- Reconstruct detected frames into a video
- Supports GPU acceleration (CUDA)
- User-friendly Flask web interface
- Download processed images and videos

---

## 🛠 Technologies Used

### Backend
- Python 3.14
- Flask

### Deep Learning
- YOLOv8 (Ultralytics)
- PyTorch
- CUDA

### Computer Vision
- OpenCV
- Pillow

### Dataset
- BDD100K (Berkeley DeepDrive Dataset)

---

## 📂 Project Structure

```
AutoPilot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── best.pt
│
├── utils/
│   ├── image_detector.py
│   └── video_detector.py
│
├── templates/
│   ├── index.html
│   ├── image_result.html
│   └── video_result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── uploads/
│   │   ├── images/
│   │   └── videos/
│   │
│   └── outputs/
│       ├── images/
│       └── videos/
│
├── frames/
│   ├── input/
│   └── output/
│
└── venv/
```

---

# Dataset

This project uses the **BDD100K Dataset**, one of the largest datasets available for autonomous driving research.

Dataset contains:

- 100,000 road images
- Bounding box annotations
- Traffic signs
- Traffic lights
- Cars
- Trucks
- Buses
- Motorcycles
- Riders
- Pedestrians

Official Website:

https://bdd-data.berkeley.edu/

---

# Classes Used

The model detects the following objects:

| Class ID | Object |
|-----------|---------|
| 0 | Pedestrian |
| 1 | Rider |
| 2 | Car |
| 3 | Truck |
| 4 | Bus |
| 5 | Train |
| 6 | Motorcycle |
| 7 | Bicycle |
| 8 | Traffic Light |
| 9 | Traffic Sign |

---

# Model Training

The YOLOv8 model was trained using the converted BDD100K dataset.

Training configuration:

- Model: YOLOv8 Nano
- Epochs: 30
- Image Size: 640 × 640
- Batch Size: 6
- GPU: NVIDIA RTX 3050 Laptop GPU (CUDA)

Example training command:

```bash
yolo detect train model=yolov8n.pt data=dataset.yaml epochs=30 imgsz=640 batch=6 device=0 workers=6 amp=False
```

---

# Performance

Validation results after training:

| Metric | Value |
|---------|-------|
| Precision | 0.704 |
| Recall | 0.418 |
| mAP@50 | 0.458 |
| mAP@50-95 | 0.263 |

---


## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# How It Works

## Image Detection

1. Upload an image
2. YOLO model detects objects
3. Bounding boxes are drawn
4. Detected image is displayed

---

## Video Detection

1. Upload a video
2. Extract every frame
3. Perform YOLO detection on each frame
4. Save detected frames
5. Reconstruct video
6. Display detected video

---

# Sample Workflow

```
Video
   │
   ▼
Frame Extraction
   │
   ▼
YOLOv8 Detection
   │
   ▼
Detected Frames
   │
   ▼
Video Reconstruction
   │
   ▼
Detected Output Video
```


---

# Requirements

Major Python libraries:

- Flask
- OpenCV
- Ultralytics
- Torch
- Torchvision
- Pillow
- NumPy

---

