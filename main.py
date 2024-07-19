from OCR import OCRHandler
from OCR import ImageTextExtractor
import spacy
import regex as re
from categorize import Categorize
import cv2

class expense_report:
    def __init__(self) -> None:
        # self.ocr = OCRHandler()
        self.ocr = ImageTextExtractor()
        self.nlp = spacy.load("en_core_web_trf")


    def get_expense(self, image_path):

        res = cv2.imread(image_path)
        result = self.ocr.read_text_from_image(res)

        doc = self.nlp("".join(result))
        joined_text = "".join(result)


        print(joined_text)
        company_name = self.get_company_name(doc)
        date = self.get_date(joined_text)
        date = set(date).pop()
        print("THis is the date :", date)

        price = self.get_price(joined_text)
        print("this is the total amount : ", price)

        self.categorize(joined_text, date, company_name, price)

    def get_company_name(self, doc):
        
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        company_name = None
        # Print the named entities
        for entity, label in entities:
            if label == 'ORG':
                print(f"Company: {entity}")
                company_name = entity
                break
        return company_name
    def get_date(self, text):
    
        date_pattern = r'\b\d{1,2}/\d{1,2}/\d{1,4}\b'

        # Find all matches in the text
        dates = re.findall(date_pattern, text)

        # Print the extracted dates
        print("Dates:", dates)
        return dates
    
    def get_price(self, text):
        pattern = r'\b*\d+\.\d{2}\b'

        # Find all matches in the string
        prices = re.findall(pattern, text)

        maxi = float(prices[0])
        print(prices)
        for i in range(1, len(prices)):
            maxi = max(float(prices[i]), maxi)

        return maxi

    def categorize(self, text, date_time, company, total_price):
        categorizer = Categorize()
        row_contents = categorizer.categorize(text, date_time, company, total_price)
        categorizer.append_list_as_row('expenditure.csv', row_contents)

