vehicles = ["car", "bike", "bus"]
for vehicle in vehicles:
    print(vehicle)

word = "python"
for letter in word:
    print(letter)

colors = ["red", "green", "blue"]
for color in colors:
    if color == "green":
        break
    print(color)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)

for num in range(4):
    print(num)

for num1 in range(2, 5):
    print(num1)

for num2 in range(1, 10, 2):
    print(num2)

for num3 in range(3):
    print(num3)
else:
    print("Loop completed.")

adjectives4 = ["small", "large"]
items4 = ["table", "chair"]
for adjective4 in adjectives4:
    for item4 in items4:
        print(adjective4, item4)

for _ in [0, 1, 2]:
    pass  # Placeholder for future code