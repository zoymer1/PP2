import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"[ ,\.]"
text = "Hello, world. How are you?"
result = re.sub(pattern, ":", text)
print("Result:", result)