def thapHaNoi(n, A, B, C):
    if n == 1:
        print(A + " -> " + C )
    else:
        thapHaNoi(n-1, A, C, B)
        print(A + " -> " + C )
        thapHaNoi(n-1, B, A, C)
n = int(input())
thapHaNoi(n,'A','B','C')