t = int(input())
while t:
    str = input()
    check = 1
    a = []
    for i in range(len(str)):
        a.append( int(str[i]) )
    for i in range(len(a)-1):
        i = int(i)
        if int(a[len(a)-i-1]) >= 5:
            a[len(a)-i-2] += 1
            a[len(a)-i-1] = 0
        else:
            a[len(a)-i-1] = 0
    for i in a: print(i, end='')
    print()
    t -= 1