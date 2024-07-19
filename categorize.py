import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from csv import writer,reader
import csv

class Categorize:
    def __init__(self):
        self.tokenizer = nltk.RegexpTokenizer(r"\w+")
        self.stop_words = set(nltk.corpus.stopwords.words('english'))
        self.categories = self.build_categories()

    def build_categories(self):
        categories = {
            "entertainment": self.get_synonyms("entertainment") + ['happy', 'restaurant', 'food', 'kitchen', 'hotel', 'room', 'park', 'movie', 'cinema', 'popcorn', 'combo meal'],
            "home_utility": self.get_synonyms("home") + ['internet', 'telephone', 'electricity', 'meter', 'wifi', 'broadband', 'consumer', 'reading', 'gas', 'water', 'postpaid', 'prepaid'],
            "grocery": self.get_synonyms("grocery") + ['bigbasket', 'milk', 'atta', 'sugar', 'sunflower', 'oil', 'bread', 'vegetable', 'fruit', 'salt', 'paneer', 'walmart'],
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
        new_words = self.tokenizer.tokenize(text.lower())  # Convert text to lowercase for case-insensitive matching
        filtered_list = [w for w in new_words if w not in self.stop_words]

        category = "others"
        for word in filtered_list:
            for cat, words in self.categories.items():
                if word in words:
                    category = cat
                    break
            if category != "others":
                break

        row_contents = [st, head, x, category]
        
        return row_contents


    def append_list_as_row(self, file, list_of_elem):
        with open(file, 'a+', newline='', encoding='utf-8') as write_obj:
            csv_writer = writer(write_obj)
            if write_obj.tell() == 0:  # Check if the file is empty
                csv_writer.writerow(["Date", "Company", "Total", "Category"])  # Write headers if the file is empty
            csv_writer.writerow(list_of_elem)



        
        # with open(file, 'r', encoding='utf-8') as read_obj:
        #     self.existing_content = read_obj.readlines()

        # # Open the file in write mode to overwrite the content
        # with open(file, 'w', newline='', encoding='utf-8') as write_obj:
        #     csv_writer = csv.writer(write_obj)
            
        #     # Write the header only if the file was previously empty
        #     if not self.existing_content:
        #         csv_writer.writerow(["Start Time", "Head", "Total", "Category"])
            
        #     # Write the new entry at the top
        #     csv_writer.writerow(list_of_elem)
            
        #     # Write the existing content back to the file, skipping the header
        #     if self.existing_content:
        #         write_obj.writelines(self.existing_content[1:])

# Example usage
text = "Walmart Save money. Live better. 386 - 6 72 2104 Mgr ROBERT   ROGERS 1521 GRANADA BLVD ORMOND BEACH FL 32174 ST# 00613 OP# 007671 TE# 07 TR# 02619 STB ALL PIN 002200001988 0 . 78 CABLE POUCH 068113118178 3 . 50 TRVL PILLOW 075057602322 9 . 97 SUBTOTAL 14.25 TAX 500 93 TOTAL 15.18 DEBIT TEND 15.18 CHANGE DUE 00 EFT DEBIT PAY FROM PRIMARY 15.18 TOTAL PURCHASE US DEBIT - 7641 REF 831600869690 NETWORK ID 0081 APPR CODE 870411 US DEBIT AID Aoooo00o980840 TC 9DE3EC353C6D6ADB *Pin Verified TERMINAL MX716047 11/11/18 23:37:13 ITEMS SOLD TC# 4903 0007 3123 6600 8297 11/11/18 23 : 37:18 WATCH OVER 6,000 FOR FREE MOVIES & TV Only at Vudu.com/WatchFree VUDU Walmart 's Digital Video Service"
st = "10:00 AM"
head = "Natalie"
x = "Total: $200"

categorizer = Categorize()
# row_contents = categorizer.categorize(text, st, head, x)
# categorizer.append_list_as_row('expenditure.csv', row_contents)
