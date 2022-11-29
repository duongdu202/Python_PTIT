t = int(input())
while t :
    a = input()
    check = 1
    for i in range(1,int(len(a)/2)+1):
        if abs(ord(a[i]) - ord(a[i-1])) != abs(ord(a[len(a)-i-1]) - ord(a[len(a)-i])):
            check = 0
            break
    if check == 1: print("YES")
    else: print("NO")
    t -= 1
