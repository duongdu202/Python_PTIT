def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)

def TCS(a):
    sum = 0
    while a :
        sum += a%10
        a = int(a/10)
    return sum

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
    str = input().split()
    a, b = [int(i) for i in str]
    if SNT(TCS(USCLN(a,b))) == 1: print("YES")
    else:   print("NO")
    t -= 1