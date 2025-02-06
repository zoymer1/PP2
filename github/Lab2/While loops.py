i = 1
while i < 6:
  print(i)
  i += 1

i2 = 1
while i2 < 6:
  print(i2)
  if i2 == 3:
    break
  i2 += 1

i3 = 0
while i3 < 6:
  i3 += 1
  if i3 == 3:
    continue
  print(i3)

i4 = 1
while i4 < 6:
  print(i4)
  i4 += 1
else:
  print("i is no longer less than 6")