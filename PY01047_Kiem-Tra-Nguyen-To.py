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
    str = input()
    n = int(str[-4:])
    if SNT(n):  print("YES")
    else:   print("NO")