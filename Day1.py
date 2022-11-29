t = int(input())
while t:
    str = input().split()
    a, b = [int(i) for i in str]
    str = input()
    dem = 0
    if b >= 0:
        print((a+b)*len(str))
    else:
        for i in range(len(str) - 1):
            if str[i] != str[i+1]:
                dem += 1
        dem += 1
        dem = int(dem / 2) +1
        print(a*len(str) + dem*b)
    t -= 1
