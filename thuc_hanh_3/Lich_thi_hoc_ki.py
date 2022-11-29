import re

n,m = [int(x) for x in input().split()]
a = [0]*n
b = [0]*n
for i in range(0,n):
    a[i] = input()
    b[i] = input()

listThi = []
for i in range(0,m):
    stt = i+1
    txt = input()
    ma, dd, mm, yy, hh, ss, nhom = [x for x in re.split(' |/|:',txt)]
    listThi.append([stt,ma, dd, mm, yy, hh, ss, nhom])
listThi = sorted(listThi, key=lambda x: (x[4],x[3],x[2],x[5],x[6],x[2]))
for i in range(0,m):
    if listThi[i][0] < 10:
        print("T00",end='')
    else:    print("T0",end='')
    print(listThi[i][0],end=' ')
    print(listThi[i][1],end=' ')
    print(b[a.index(listThi[i][1])],end=' ')
    print(listThi[i][2],end='/')
    print(listThi[i][3],end='/')
    print(listThi[i][4],end=' ')
    print(listThi[i][5],end=':')
    print(listThi[i][6],end=' ')
    print(listThi[i][7],end='\n')
    