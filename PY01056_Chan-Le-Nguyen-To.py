import math
from tabnanny import check

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
    check = 1
    for i in range(len(n)):
        if i%2 == 1 and int(n[i])%2 == 0: check = 0
        if i%2 == 0 and int(n[i])%2 == 1: check = 0
        sum += int(n[i])
    if SNT(sum) and check == 1:    print("YES")
    else:   print("NO")