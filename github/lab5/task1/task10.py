import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    return snake

camel = "thisIsACamelCaseString"
snake = camel_to_snake(camel)
print("Snake Case:", snake)