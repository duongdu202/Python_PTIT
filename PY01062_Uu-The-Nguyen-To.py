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
    dem = 0
    for i in n:
        if i == "2" or i == "3" or i == "5" or i == "7":
            dem += 1
    if SNT(len(n)) and dem > len(n) - dem:  print("YES")
    else:   print("NO")