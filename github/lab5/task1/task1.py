import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"ab*"
tests = ["a", "ab", "abb", "ac", "b"]

for s in tests:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches")
    else:
        print(f"'{s}' does not match")