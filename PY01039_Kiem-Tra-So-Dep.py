t = int(input())
while t:
    n = input()
    check = 1
    for i in range(0,len(n)):
        if i%2 == 0:
            if n[i] != n[0]:
                print("NO")
                check = 0
                break
        else:
            if n[i] != n[1]:
                print("NO")
                check = 0
                break
    if check == 1:  print("YES")
    t -= 1