def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


for t in range(int(input())):
    n = int(input())
    l1 = [int(i) for i in input().split()]
    l1 = sorted(set(l1))
    a = sorted(l1, key=sum_digits)
    for i in a:
        print(i,end=' ')
    print()
