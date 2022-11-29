from cmath import sqrt


t = int(input())
while t:
    n = int(input())
    print("1",end='')
    for i in range(2,(n)+1,1):
        dem = 0
        while n%i == 0:
            n /= i
            dem += 1
        if dem != 0:
            print(" * ",end='')
            print(i,end='^')
            print(dem,end='')
    print()
    t -= 1