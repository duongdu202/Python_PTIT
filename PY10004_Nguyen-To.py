def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)

def SNT(a):
    a = int(a)
    check = 0
    if a == 1: return check
    for i in range(2,a):
        if a%i == 0: return check
    check = 1
    return check

t = int(input())
while t:
    n = int(input())
    dem = 0
    for i in range(n):
        if USCLN(i,n) == 1:
            dem += 1
    if SNT(dem) == 1: print("YES")
    else:   print("NO")
    t -= 1