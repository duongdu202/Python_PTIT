t = int(input())
while t:
    n = int(input())
    sum = 0
    check = 1
    nho = n%10-2
    while n:
        sum += n%10
        if abs(n%10 - nho) != 2:
            check = 0
            break
        nho = n%10
        n = int(n/10)
    if check == 1 and sum%10 == 0: print("YES")
    else:    print("NO")
    t-=1