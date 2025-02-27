import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"[a-z]+_[a-z]+"
text = "This is a test_string and another_example in the text."
matches = re.findall(pattern, text)
print("Matches:", matches)