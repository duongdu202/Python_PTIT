t = int(input())
while t :
    b = []
    a = list(input())
    a.append(0)
    dem = 1
    i = 1
    nho = a[0]
    while i < len(a):
        if a[i] == nho:
            dem += 1
        else:
            b.append(dem)
            b.append(nho)
            nho = a[i]
            dem = 1
        i += 1
    for i in b: print(i,end='')
    print()
    t -= 1
