from ultralytics import YOLO
import cv2
model = YOLO("best (1).pt")
import numpy
import pytesseract as py
results = model.predict("C:\\Users\\2707109\\Desktop\\project_yolo\\class2.v1i.yolov8 (1)\\Logical_07200.jpeg", save=True)
print(type(results))
print(results)
for result in results:
    print(type(result.boxes))
    boxes = result.boxes
boxes= boxes.numpy()
print(boxes.xyxy)

image=  cv2.imread("C:\\Users\\2707109\\Desktop\\project_yolo\\class2.v1i.yolov8 (1)\\Logical_07200.jpeg")
py.pytesseract.tesseract_cmd = r'C:\Users\2707109\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
window_name=  'image'
# from PIL import Image

# Image.fromarray(image).show()
# cv2.imshow(window_name, image)
# cv2.waitKey(0)
print("Shape of the image", image.shape) 
temp =0
A= []
for index in boxes.xyxy:
    
    temp+=1
    x = int(index[0])
    y = round(index[1])
    w = round(index[2])
    h = round(index[3])
    print("x, y ,w ,h\n",index[0],index[1],index[2],index[3])
# x,y,w,h= [1167 ,     1685 ,    1429  ,      1859]
    h= h-y
    w= w-x
    print("h, w",x,y)
    crop_img = image[y:y+h, x:x+w]
# cv2.imshow(window_name, crop_img)
    cv2.imwrite("Cropped_img/crop__" + str(temp) + ".jpg",crop_img)
  
    #passing to tesseract

    c = py.image_to_string(crop_img)
    A.append(c)
print(A)

