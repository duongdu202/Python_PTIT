str = input().split()
n,m,k = [int(i) for i in str]
a = []
i = 0
while i<n:
    a.append([])
    j=0
    while j<m:
        a[i].append(i*m+j+1)
        j+=1
    i+=1
while k:
    str = input().split()
    sr,x,y = [i for i in str]
    x = int(x)
    y = int(y)
    i=0
    if sr == 'R':
        while i<m:
            a[x-1][i] *= y
            i+=1
    else:
        while i<n:
            a[i][x-1] *= y
            i+=1
    k-=1
sum = 0
i=0
while i<n:
    j=0
    while j<m:
        sum += a[i][j]
        j+=1
    i+=1
a.clear()
print(sum)