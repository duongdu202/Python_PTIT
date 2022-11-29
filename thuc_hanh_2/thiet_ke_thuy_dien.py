t = int(input())
for g in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    h = [int(x) for x in input().split()]
    temp = [0]
    print(type(temp))
    s = [0] * n
    s[0] = h[0] * l[0]
    max = 0
    for i in range(1,n):
        if h[i] > h[i-1]:
            if h[i] < h[max]:
                temp[0] = h[i]*(l[i]-l[max])-h[i-1]
                s[i] = s[max] + temp
            else:
                sum = 0
                for k in range(l[max],l[i]):
                    sum += h[k]
                temp[0] = l[i]*(h[i] - h[max]) + (l[i]-l[max])*h[max] - sum
                s[i] = s[max] + temp
                max = i
        else:
            temp[0] = h[i]*[l[i]-l[i-1]]
            s[i] = s[i-1] + temp
        print(type(temp))
        print(type(s[i]))
    for i in s: print(i)

        