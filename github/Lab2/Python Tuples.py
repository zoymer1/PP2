thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[1])

thistuple3 = ("apple", "banana", "cherry")
print(thistuple3[-1])

thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple4[2:5])

thistuple5 = ("apple", "banana", "cherry")
if "apple" in thistuple5:
    print("Yes, 'apple' is in the fruits tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple6 = ("apple", "banana", "cherry")
y6 = list(thistuple6)
y6.append("orange")
thistuple6 = tuple(y6)
print(thistuple6)

thistuple7 = ("apple", "banana", "cherry")
y7 = ("orange",)
thistuple7 += y7
print(thistuple7)

thistuple8 = ("apple", "banana", "cherry")
y8 = list(thistuple8)
y8.remove("apple")
thistuple8 = tuple(y8)
print(thistuple8)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green1, yellow2, *red3) = fruits1
print(green1)
print(yellow2)
print(red3)

thistuple9 = ("apple", "banana", "cherry")
for x9 in thistuple9:
    print(x9)
    
thistuple10 = ("apple", "banana", "cherry")
for i in range(len(thistuple10)):
    print(thistuple10[1])

thistuple11 = ("apple", "banana", "cherry")
i11 = 0
while i11 < len(thistuple11):
    print(thistuple11[i11])
    i11 = i11 + 1

tuple11 = ("a", "b", "c")
tuple22 = (1, 2, 3)
tuple33 = tuple11 + tuple22
print(tuple33)

fruits12 = ("apple", "banana", "cherry")
mytuple12 = fruits12 * 2
print(mytuple12)

thistuple13 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x13 = thistuple13.count(5)
print(x13)

thistuple14 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x14 = thistuple14.index(8)
print(x14)