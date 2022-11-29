from ast import Str
from tabnanny import check


t = int(input())
while t:
    t -= 1
    n = input()
    check = 1
    m = n.index(max(n))
    if m == 0 or m == len(n)-1:
        print("NO")
        continue
    for i in range(m):
        if n[i] >= n[i+1]:
            print("NO")
            check = 0
            break
    if check == 0: continue
    for i in range(m,len(n)-1):
        if n[i] <= n[i+1]:
            print("NO")
            check = 0
            break
    if check == 1:  print("YES")