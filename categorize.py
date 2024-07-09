import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from csv import writer
import csv

class Categorize:
    def __init__(self) -> None:
        self.tokenizer = nltk.RegexpTokenizer(r"\w+")
        self.stop_words = set(nltk.corpus.stopwords.words('english'))
        self.categories = self.build_categories()

    def build_categories(self):
        categories = {
            "entertainment": self.get_synonyms("entertainment") + ['happy', 'restaurant', 'food', 'kitchen', 'hotel', 'room', 'park', 'movie', 'cinema', 'popcorn', 'combo meal'],
            "home_utility": self.get_synonyms("home") + ['internet', 'telephone', 'electricity', 'meter', 'wifi', 'broadband', 'consumer', 'reading', 'gas', 'water', 'postpaid', 'prepaid'],
            "grocery": self.get_synonyms("grocery") + ['bigbasket', 'milk', 'atta', 'sugar', 'sunflower', 'oil', 'bread', 'vegetable', 'fruit', 'salt', 'paneer'],
            "investment": self.get_synonyms("investment") + ['endowment', 'grant', 'loan', 'applicant', 'income', 'expenditure', 'profit', 'interest', 'expense', 'finance', 'property', 'money', 'fixed', 'deposit', 'kissan', 'vikas'],
            "transport": self.get_synonyms("car") + ['cab', 'ola', 'uber', 'autorickshaw', 'railway', 'air', 'emirates', 'aerofloat', 'taxi', 'booking', 'road', 'highway'],
            "shopping": self.get_synonyms("dress") + ['iphone', 'laptop', 'saree', 'max', 'pantaloons', 'westside', 'vedic', 'makeup', 'lipstick', 'cosmetics', 'mac', 'facewash', 'heels', 'crocs', 'footwear', 'purse']
        }
        return categories

    def get_synonyms(self, word):
        synonyms = []
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
        return synonyms

    def categorize(self, text, st, head, x):
        new_words = self.tokenizer.tokenize(text)
        filtered_list = [w for w in new_words if w not in self.stop_words]

        # Check which category the words belong to
        category = "others"
        for word in filtered_list:
            for cat, words in self.categories.items():
                if word in words:
                    category = cat
                    break
            if category != "others":
                break

        row_contents = [st, head, x, category]
        self.append_list_as_row('expenditure.csv', row_contents)

    def append_list_as_row(self, file, list_of_elem):
        with open(file, 'a+', newline='', encoding='utf-8') as write_obj:
            csv_writer = writer(write_obj)
            if write_obj.tell() == 0:  # Check if the file is empty
                csv_writer.writerow(["Start Time", "Head", "Total", "Category"])  # Write headers if the file is empty
            csv_writer.writerow(list_of_elem)

# Example usage
text = "Logan's Auto Repair Shop AUTO SHOP 154 Repair Avenue, London, UK +44 779 5633 875 VAT: 123 4567 89 Part no. Description Price Customer and Vehicle Information Ref # 6430 22541 Oil E50.00 Name  Sarah Brown Date1/1/21 22431 Oil Filter E20.00 Adaress:220 Customer Road, London, UK Due on: 3/1/21 44367 Air Filter {25.00 Year 2019 MakelModel Mercedes A Class VIN 4Y1SL658482411439 Phone: 07539891714 48908 Cabin Filter {25.00 Maior Service Oil change Minor overhaul Part Refitment Other 76532 Front Pads E90.00 No; InstructioniLabour Amount 2 43898 Rear Tyre E180.00 Oil, Oil filter, Air filter , cabin filter replaced E50.00 Front pads replaced {40.00 Rear tyres fitted, balanced and disposal of old tyres {45.00 Subject to terms and conditions as required by law. Total Parts {390.00 Total parts {390.00 Total Labor E135.00 The warranties as applicable for the parts will be as provided by the hereby authorize the company to perform the repair work Other Charges E0.00 manufacturer. The company' s liability will be limited to what is expressly as detailed above and to operateldrive the vehicle for the required by the applicable laws and will not extend beyond. purpose of inspection or testing: Tax E105.00 Signature: Sarah Brown Total Due E630.00 aty"
st = "08:00 AM"
head = "John Doe"
x = "Total: $100"
categorizer = Categorize()
categorizer.categorize(text, st, head, x)
