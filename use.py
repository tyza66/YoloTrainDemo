from ultralytics import YOLO

model = YOLO("best.pt")
model.predict(source="test.jpg",save=True)
