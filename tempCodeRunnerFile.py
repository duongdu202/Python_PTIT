str = input().split()
n, m = [int(i) for i in str]
a = []
b = []
str = input().split()
for i in str:   a.append(i)
str = input().split()
for i in str:   b.append(i)
a.sort()
b.sort()
min = 1000000 
for i in range(n):
    for j in range(m):
        temp = abs(a[i] - b[j])
        if(temp > min):
            min = temp
print(min)