mon = ['TOAN', 'LY', 'HOA']
cong = [1.5, 1, 0]

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
    id = 'TS{0:0>2}'.format(id)
    ten = input()
    ten = cht(ten)
    diem = float(input())
    dt = input()
    kv = int(input())
    diem += cong[kv-1]
    if dt != 'Kinh': diem += 1.5
    if diem >= 20.5 : s = ' Do'
    else : s = ' Truot'
    ds.append([id,ten,diem,s])
ds = sorted(ds, key = lambda x : -x[2])
for i in range(0,n):
    print(ds[i][0],end=' ')
    print(ds[i][1],end=' ')
    print("{:.1f}".format(ds[i][2]),end='')
    print(ds[i][3],end='\n')