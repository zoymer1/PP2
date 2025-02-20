n = int(input())
def squares_up_to_n(n):
    for i in range(n+1):
        yield i*i
for x in squares_up_to_n(n):
    print(x)