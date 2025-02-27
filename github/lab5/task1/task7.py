with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake = "this_is_a_test_string"
camel = snake_to_camel(snake)
print("Camel Case:", camel)