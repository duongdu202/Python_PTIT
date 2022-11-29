from tabnanny import check

t = int(input())
while t:
    t -= 1
    n = input()
    check = 1
    for i in n:
        if i != '1' and i != '2' and i != '0':
            print("NO")
            check = 0
            break
    if check == 1:  print("YES")