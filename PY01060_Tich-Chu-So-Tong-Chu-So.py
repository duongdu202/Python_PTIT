t = int(input())
for i in range(t):
    n = input()
    sum = 0
    tich = 1
    check = 0
    for i in range(len(n)):
        if i%2 != 0:
            sum += int(n[i])
        elif n[i] != '0':
            check = 1
            tich *= int(n[i])
    if check == 0:  tich = 0
    print(tich,sum)