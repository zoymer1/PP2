elements_str = input().split()
elements_bool = tuple(bool(int(x)) for x in elements_str)
result = all(elements_bool)
print(result)