t = int(input())
for i in range(t):
    n = input()
    sum = 1
    for i in n:
        if i!='0':  sum *= int(i)
    print(sum)