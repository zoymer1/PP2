temperature = 25
if temperature > 20:
    print("It's warm outside.")

score = 85
if score >= 50:
    print("You passed the exam.")
    print("Congratulations!")

age = 30
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

number = 15
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

height = 180
if height > 170: print("You are tall.")

weight = 70
print("Overweight") if weight > 75 else print("Normal weight")

time = 12
print("Morning") if time < 12 else print("Afternoon") if time < 18 else print("Evening")

x = 10
y = 20
z = 30
if x < y and y < z:
    print("x is less than y and y is less than z.")

a = 5
b = 10
c = 15
if a > b or c > b:
    print("At least one of the conditions is True.")

is_raining = False
if not is_raining:
    print("You don't need an umbrella.")

num = 50
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is negative or zero.")