from OCR import OCRHandler
import spacy
import regex as re

class expense_report:
    def __init__(self) -> None:
        self.ocr = OCRHandler()
        self.nlp = spacy.load("en_core_web_trf")


    def get_expense(self, image_path):
        result = self.ocr.read_text_from_image(image_path=image_path)

        doc = self.nlp(" ".join(result))
        joined_text = " ".join(result)

        company_name = self.get_company_name(doc)
        date = self.get_date(joined_text)
        print("THis is the date :", set(date).pop())

        price = self.get_price(joined_text)
        print("this is the total amount : ", price)

    def get_company_name(self, doc):
        
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Print the named entities
        for entity, label in entities:
            if label == 'ORG':
                print(f"Company: {entity}")
                break

    def get_date(self, text):
    
        date_pattern = r'\b\d{1,2}/\d{1,2}/\d{2}\b'

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

