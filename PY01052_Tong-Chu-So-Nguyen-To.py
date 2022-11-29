import math

def SNT(n):
    if (n < 2):
        return False;
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True;

t = int(input())
for i in range(t):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if SNT(sum):    print("YES")
    else:   print("NO")