from ultralytics import YOLO

model = YOLO("best (2).pt")


results =  model.predict("C:\\Users\\Rahul -hp\\Desktop\\Internship\\TRDDC\\Internship 2\\Logical_07000.jpeg", save=True)



