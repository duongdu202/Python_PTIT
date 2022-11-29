def cht(tin):
    temp1 = tin.split()
    temp2 = []
    for j in temp1:
        ten = ''
        for i in j:
            if i.isalpha():
                ten = ten + i
        ten = ten.lower()
        ten = ten.capitalize()
        if ten.isalpha():
            temp2.append(ten)
    tout=' '.join(temp2)
    return tout

n = int(input())
ds = []
for i in range(n) :
    id = i+1
    id = 'SV{0:0>2}'.format(id)
    ten = input()
    ten = cht(ten)
    diem1 = float(input())
    diem2 = float(input())
    diem3 = float(input())
    tb = (diem1*3 +diem2*3 +diem3*2)/8
    if tb*1000%10 == 5: tb = tb-0.005+0.01
    ds.append([id,ten,tb])
ds = sorted(ds, key = lambda x : -x[2])
dem = -1
nho = ds[0][2]
for i in range(0,n):
    print(ds[i][0],end=' ')
    print(ds[i][1],end=' ')
    print("{:.2f}".format(ds[i][2]),end=' ')
    if nho == ds[i][2]: dem+=1
    else:
        dem = 0
        nho = ds[i][2]
    print(i+1-dem,end='\n')
    