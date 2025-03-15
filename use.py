from ultralytics import YOLO

model = YOLO("XXX.pt")
model.predictor("test.jpg",save=True)
