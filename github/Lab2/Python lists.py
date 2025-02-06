thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist111 = ["apple", "banana", "cherry"]
print(len(thislist111))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thislist2 = list(("apple", "banana", "cherry"))  # обратите внимание на двойные круглые скобки
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
print(thislist3[1])

thislist4 = ["apple", "banana", "cherry"]
print(thislist4[-1])

thislist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[2:5])

thislist6 = ["apple", "banana", "cherry"]
if "apple" in thislist6:
    print("Yes, 'apple' is in the fruits list")

thislist7 = ["apple", "banana", "cherry"]
thislist7[1] = "blackcurrant"
print(thislist7)

thislist8 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist8[1:3] = ["blackcurrant", "watermelon"]
print(thislist8)

thislist9 = ["apple", "banana", "cherry"]
thislist9.insert(2, "watermelon")
print(thislist9)

thislist10 = ["apple", "banana", "cherry"]
thislist10.append("orange")
print(thislist10)

thislist11 = ["apple", "banana", "cherry"]
tropical11 = ["mango", "pineapple", "papaya"]
thislist11.extend(tropical11)
print(thislist11)

thislist12 = ["apple", "banana", "cherry"]
thislist12.remove("banana")
print(thislist12)

thislist13 = ["apple", "banana", "cherry"]
thislist13.pop(1)
print(thislist13)

thislist14 = ["apple", "banana", "cherry"]
thislist14.clear()
print(thislist14)

thislist15 = ["apple", "banana", "cherry"]
for x15 in thislist15:
    print(x15)

thislist16 = ["apple", "banana", "cherry"]
for i16 in range(len(thislist16)):
    print(thislist[i16])

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist17 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist17.sort()
print(thislist17)

thislist18 = ["banana", "orange", "kiwi", "cherry"]
thislist18.reverse()
print(thislist18)

thislist19 = ["apple", "banana", "cherry"]
mylist19 = thislist19.copy()
print(mylist19)

list11 = ["a", "b", "c"]
list222 = [1, 2, 3]
list333 = list11 + list222
print(list333)