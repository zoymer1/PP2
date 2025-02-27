import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"ab{2,3}"
tests = ["abb", "abbb", "ab", "abbbb"]

for s in tests:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches")
    else:
        print(f"'{s}' does not match")