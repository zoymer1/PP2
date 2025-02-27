import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"[A-Z][a-z]+"
text = "Hello World This is a Test String"
matches = re.findall(pattern, text)
print("Matches:", matches)