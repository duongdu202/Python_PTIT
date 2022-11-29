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
    check = 1
    for i in range(len(n)):
        if SNT(i) and not(SNT(int(n[i]))) : check = 0
        if not(SNT(i)) and SNT(int(n[i])): check = 0
    if check == 1:    print("YES")
    else:   print("NO")