def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)

t = int(input())
while t:
    a = input()
    b = a[::-1]
    if USCLN(int(a),int(b)) == 1:
        print("YES")
    else:   print("NO")
    t -= 1