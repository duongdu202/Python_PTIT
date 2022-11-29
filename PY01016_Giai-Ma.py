t = int(input())
while t :
    a = input()
    for i in range(1,len(a),2):
        dem = int(a[i])
        for j in range(dem):
            print(a[i-1],end='')
    print()
    t -= 1
