t = int(input())
while t:
    n = input()
    sum = int(n)
    dem = 0
    while 1 :
        if sum%7 == 0:
            print(sum)
            break
        sum = int(n) + int(n[::-1])
        n = str(sum)
        dem += 1
        if dem == 1000:
            print("-1")
            break
    t -= 1