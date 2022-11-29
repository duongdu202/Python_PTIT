t = int(input())
for i in range(t):
    n = input()
    check = 1
    if n[0] == n[1]: check = 0
    for i in range(0,len(n),2):
        if n[i] != n[0]:   check = 0
    if check == 1 and len(n)%2 == 1:    print("YES")
    else:   print("NO")