import bisect
import string
str = input().split()
n, m = [int(i) for i in str]
a = []
b = []
str = input().split()
for i in str:   a.append(i)
str = input().split()
for i in str:   b.append(i)
a.sort()
b.sort()
b.append(10000000)
min = 1000000 
for i in a:
    j = 0
    while b[j] < a[i]:
        j += 1
    if(min < abs(int(b[j])-int(a[i]))):   min =   abs(int(b[j])-int(a[i]))
    j -= 1
    if(min < abs(int(b[j])-int(a[i]))):   min =   abs(int(b[j])-int(a[i]))
print(min)