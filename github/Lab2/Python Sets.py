thisset1 = {"apple", "banana", "cherry"}
print(thisset1)

thisset2 = {"apple", "banana", "cherry"}
print("banana" in thisset2)

thisset3 = {"apple", "banana", "cherry"}
thisset3.add("orange")
print(thisset3)

thisset4 = {"apple", "banana", "cherry"}
tropical4 = {"pineapple", "mango", "papaya"}
thisset4.update(tropical4)
print(thisset4)

thisset5 = {"apple", "banana", "cherry"}
mylist5 = ["kiwi", "orange"]
thisset5.update(mylist5)
print(thisset5)

thisset6 = {"apple", "banana", "cherry"}
thisset6.remove("banana")
print(thisset6)

thisset7 = {"apple", "banana", "cherry"}
thisset7.discard("banana")
print(thisset7)

thisset8 = {"apple", "banana", "cherry"}
x8 = thisset8.pop()
print(x8)
print(thisset8)

thisset9 = {"apple", "banana", "cherry"}
thisset9.clear()
print(thisset9)

thisset10 = {"apple", "banana", "cherry"}
del thisset10

thisset11 = {"apple", "banana", "cherry"}
for x11 in thisset11:
    print(x11)

set111 = {"a", "b", "c"}
set222 = {1, 2, 3}
set333 = set111.union(set222)
print(set333)

set1111 = {"a", "b", "c"}
set2222 = {1, 2, 3}
set1111.update(set2222)
print(set1111)

set11111 = {"apple", "banana", "cherry"}
set22222 = {"google", "microsoft", "apple"}
set33333 = set11111.intersection(set22222)
print(set33333)

set12 = {"apple", "banana", "cherry"}
set21 = {"google", "microsoft", "apple"}
set32 = set12.difference(set21)
print(set32)

set13 = {"apple", "banana", "cherry"}
set23 = {"google", "microsoft", "apple"}
set31 = set13.symmetric_difference(set23)
print(set31)