from ultralytics import YOLO

model = YOLO("runs/classify/train/weights/best.pt")

image_path = "datasets/test/positive/00001.jpg"

results = model.predict(image_path)

classes = ["negative", "positive"]

for r in results:
    probs = r.probs
    predicted = classes[probs.top1]
    confidence = probs.top1conf

    print("Prediction:", predicted)
    print("Confidence:", float(confidence))