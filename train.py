from ultralytics import YOLO
import cv2
model = YOLO("best (1).pt")
import numpy

results = model.predict("C:\\Users\\2707109\\Desktop\\project_yolo\\class2.v1i.yolov8 (1)\\Logical_07200.jpeg", save=True)
print(type(results))
print(results)
for result in results:
    print(type(result.boxes))
    boxes = result.boxes
boxes= boxes.numpy()
print(boxes.xyxy)

image=  cv2.imread("C:\\Users\\2707109\\Desktop\\project_yolo\\class2.v1i.yolov8 (1)\\Logical_07200.jpeg")

window_name=  'image'
# from PIL import Image

# Image.fromarray(image).show()
# cv2.imshow(window_name, image)
# cv2.waitKey(0)
print("Shape of the image", image.shape) 
temp =0
# for index in boxes.xywh:
    
#     temp+=1
#     x = round(index[0])
#     y = round(index[1])
#     w = round(index[2])
#     h = round(index[3])
#     print("x, y ,w ,h\n",index[0],index[1],index[2],index[3])
x,y,w,h= {1167 ,     1685 ,    1429  ,      1859}
h= 1859-1685
w= 1429-1167
crop_img = image[y:y+h, x:x+w]
cv2.imwrite("Cropped_img/crop__" + str(temp) + ".jpg",crop_img)


