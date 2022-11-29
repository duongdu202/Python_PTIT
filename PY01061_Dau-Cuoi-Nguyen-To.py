
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
    if SNT(int(n[:3])) and SNT(int(n[len(n)-3:])):
        print("YES")
    else:   print("NO")