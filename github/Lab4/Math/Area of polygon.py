import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = (n * s**2) / (4 * math.tan(math.pi/n))
print("The area of the polygon is: {:.0f}".format(area))