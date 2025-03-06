import time
import math
number = float(input())
milliseconds = int(input())
time.sleep(milliseconds / 1000.0)
result = math.sqrt(number)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")