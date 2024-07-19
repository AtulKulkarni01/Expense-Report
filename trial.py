# import easyocr
# import time


# from PIL import Image
# import pytesseract
# import cv2
# import os

# class ImageTextExtractor:
#     def __init__(self, preprocess=["thresh", "blur"]):
#         self.preprocess = preprocess

#     def preprocess_image(self, image):
        
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
#         if self.preprocess[0] == "thresh":
#             gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#         else:
#             gray = cv2.medianBlur(gray, 3)
        
#         return gray

#     def read_text_from_image(self, image):
#         gray = self.preprocess_image(image)
#         text = pytesseract.image_to_string(gray)
#         print(text)
#         return text
    

# img = cv2.imread("bill4.jpg")
# ex = ImageTextExtractor()

# ex.read_text_from_image(img)


import pytesseract
import cv2

# Update this path to where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Your existing code
res = pytesseract.image_to_string(cv2.imread("bill5.jpg"))

print(res)

# pytesseract.image_to_string(cv2.imread("bill4.jpg"))