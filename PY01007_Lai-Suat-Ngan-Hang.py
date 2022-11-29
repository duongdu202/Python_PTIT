t = int(input())
while t :
    a = input().split()
    n,x,m = [float(i) for i in a]
    i = 1
    while  (n*pow(1+x/100,i)) < m :
        i += 1
    print(i)
    t -= 1
