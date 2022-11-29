from ctypes import sizeof
from queue import Empty


str = input().split()
a,k,n = [int(i) for i in str]
b = []
i = int(a/k)*k+k
while i <= n:
    b.append(i-a)
    i += k
for i in b:
    print(i,end=' ')
if len(b) == 0 : print("-1")
