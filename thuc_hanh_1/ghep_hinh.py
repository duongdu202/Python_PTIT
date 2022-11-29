t = int(input())
while t:
    str = input().split()
    a,b,x,y,z,l,r = [int(i) for i in str]
    s = []
    for i in range(1,int(min(a,b)/2),1):
        s.append(i*(a-2*i)*(b-2*i))
    s.sort(reverse=True)
    if l%s[0] < x:
        start = l + x-l%s[0]
    else:   start = l + s[0] - l%s[0] + x
    for i in range(start ,r+1,s[0]):
        if i%s[0]==x and i%s[1]==y and i%s[2]==z:
            print(i)
            break
    t -= 1