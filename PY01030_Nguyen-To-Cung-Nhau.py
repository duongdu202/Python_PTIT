def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)

str = input().split()
n = int(str[0])
k = int(str[1])
if k == 2:
    dem = 0
    for i in range(10,100):
        if USCLN(n,i) == 1:
            print(i,end=' ')
            dem += 1
            if dem%10 == 0:
                print("")
if k == 3:
    dem = 0
    for i in range(100,1000):
        if USCLN(n,i) == 1:
            print(i,end=' ')
            dem += 1
            if dem%10 == 0:
                print("")
if k == 4:
    dem = 0
    for i in range(1000,10000):
        if USCLN(n,i) == 1:
            print(i,end=' ')
            dem += 1
            if dem%10 == 0:
                print("")
if k == 5:
    dem = 0
    for i in range(10000,100000):
        if USCLN(n,i) == 1:
            print(i,end=' ')
            dem += 1
            if dem%10 == 0:
                print("")