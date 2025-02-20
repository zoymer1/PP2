n = int(input())

def divisible_by_3_and_4(n):
    for i in range(0, n+1, 12):
        yield i

for x in divisible_by_3_and_4(n):
    print(x)