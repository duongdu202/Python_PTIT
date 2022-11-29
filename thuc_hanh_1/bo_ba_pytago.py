n = int(input())
a = [0]*n
for i in range(n):
    a[(i*i)%n]+=1
print(a)
index = 0
for i in range(n):
    dem=0
    for j in range(n):
        dem += a[j] * a[(i+n-j)%n]
    # dem /= 2
    index += dem * a[i]
print(index)
