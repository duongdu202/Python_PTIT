t = int(input())
while t :
    a = input()
    check = 0
    nho = 0
    for i in a:
        if int(i) < nho :
            print("NO")
            check = 1
            break
        nho = int(i)
    if check == 0:
        print("YES")
    t -= 1
