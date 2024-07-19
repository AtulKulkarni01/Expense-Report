import easyocr
import time


from PIL import Image
import pytesseract
import cv2
import os

class ImageTextExtractor:
    def __init__(self, preprocess=["thresh", "blur"]):
        self.preprocess = preprocess

    def preprocess_image(self, image):
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        if self.preprocess[0] == "thresh":
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        else:
            gray = cv2.medianBlur(gray, 3)
        
        return gray

    def read_text_from_image(self, image):
    
        # Update this path to where Tesseract is installed
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Your existing code
        gray = self.preprocess_image(image)
        text = pytesseract.image_to_string(gray)
        print(text)
        return text
    


    
class OCRHandler:
    def __init__(self, language='en'):
        self.reader = easyocr.Reader([language]) 

    def read_text_from_image(self, image_path, detail=0):
        start_time = time.perf_counter()
        result = self.reader.readtext(image_path, detail=detail)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print("Result: ", result)
        print("Total Time: ", "%.2f" % total_time, " seconds")
        return result
