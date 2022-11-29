t = int(input())
for i in range(t):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    sum = str(sum)
    if sum == sum[::-1] and len(sum) > 1:    print("YES")
    else:   print("NO")