from ultralytics import YOLO

model = YOLO("best (1).pt")

# Perform object detection on the image
results = model.predict("C:\\Users\\Rahul -hp\\Desktop\\Internship\\TRDDC\\Internship 2\\Logical_07000.jpeg", save=True, save_txt=True)
for result in results:
    boxes = result.boxes

print(boxes.xyxy)
# Extract bounding box coordinates of all detected objects

