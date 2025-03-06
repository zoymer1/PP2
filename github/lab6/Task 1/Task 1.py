import math
numbers_str = input().split()
numbers = list(map(int, numbers_str))
result = math.prod(numbers)
print(result)