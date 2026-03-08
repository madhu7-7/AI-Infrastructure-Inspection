from ultralytics import YOLO

# load YOLOv8 classification model
model = YOLO("yolov8n-cls.pt")

# train classification model
model.train(
    data="datasets",
    epochs=5,
    imgsz=224,
    batch=8,
    device="cpu"
)