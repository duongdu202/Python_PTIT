from re import I


a = input()
b = a[::-1]
c = ''
dem = 0
for i in b:
    c += i
    dem += 1
    if dem%3 == 0 and dem != len(a):
        c += ','
print(c[::-1])