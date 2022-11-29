from re import I


t = int(input())
for j in range(t):
    n = int(input())
    m = {}
    s = 0
    a = [int(x) for x in input().split()]
    for i in a:
        m[i] = i
    Min = min(a)
    Max = max(a)
    for i in range(Min, Max):
        if not(i in m): s += 1
    print(s) 