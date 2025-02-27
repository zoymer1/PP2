import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = "SplitThisStringAtUppercaseLetters"
parts = re.split(r'(?=[A-Z])', text)
parts = [part for part in parts if part]
print("Splitted Parts:", parts)