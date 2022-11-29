k = 1
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while k:
    str = input().split()
    k = str[0]
    k = int(k)
    if k == 0:   break
    s = str[1]
    a = []
    for i in range(len(s)):
        a.append(P[(P.find(s[len(s)-i-1]) + k ) % 28])
    for i in a: print(i,end='')
    print()
