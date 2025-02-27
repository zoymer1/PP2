import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = "InsertSpacesBetweenWordsStartingWithCapitals"
result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
print("Result:", result)