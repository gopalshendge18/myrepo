# import cv2
# import pytesseract
# import numpy as np

# def mask_text(image_path):
#     # Load the image
#     pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#     image = cv2.imread(image_path)

#     # Convert the image to grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Use Tesseract OCR to extract text from the image
#     extracted_text = pytesseract.image_to_string(gray_image)

#     # Get the bounding boxes of the text regions
#     boxes = pytesseract.image_to_boxes(gray_image)

#     # Create a mask with the same size as the image
#     mask = np.zeros(gray_image.shape, dtype=np.uint8)

#     # Loop over the bounding boxes and draw rectangles around the text regions
#     for b in boxes.splitlines():
#         b = b.split()
#         x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#         cv2.rectangle(image, (x, image.shape[0] - y), (w, image.shape[0] - h), (0, 0, 0), 2)
#         cv2.rectangle(mask, (x, image.shape[0] - y), (w, image.shape[0] - h), (255, 255, 255), -1)

#     # Apply the mask to the image
#     masked_image = cv2.bitwise_and(image, image, mask=mask)

#     return masked_image

# # Example usage
# image_path = 'Logical_03000.jpeg'
# masked_image = mask_text(image_path)

# # Display the masked image
# cv2.imshow('Masked Image', masked_image)
# cv2.imwrite("result.jpg", masked_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
  
  
import cv2
import numpy as np

# Read the image
image = cv2.imread("right_angles_line.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(image, 50, 150)

# Create a structuring element for morphological operations
kernel = np.ones((1,1), np.uint8)

# Perform erosion to thin the edges
thinned_edges = cv2.erode(edges, kernel, iterations=1)

# Display the thinned edges
cv2.imshow("Thinned Edges", thinned_edges)
cv2.imwrite("erod_image.jpg",thinned_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
