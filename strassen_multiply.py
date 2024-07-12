# strassen multiply

def strassen_multiply(a,b):
    if len(a) == 1:
        return[a[0][0] * b[0][0]]
    
    mid = len(a)//2
    a11,a12, a21,a22 = split_matrix(a)
    b11,b12, b21,b22 = split_matrix(b)
    
    
    m1  = strassen_multiply(add(a11,a22), add(b11,b22))
    m2  = strassen_multiply(add(a21,a22), b11)
    m3  = strassen_multiply(a11, sub(b12,b22))
    m4  = strassen_multiply(a22, sub(b21,b11))
    m5  = strassen_multiply(add(a11,a12), b22)
    m6  = strassen_multiply(sub(a21,a11), add(b11,b12))
    m7  = strassen_multiply(sub(a12,a22), add(b21,b22))
    
    c11 = add(sub(add(m1,m4),m5),m7)
    c12 = add(m3,m5)
    c21 = add(m2,m4)
    c22 = add(sub(add(m1,m3),m2),m6)
    
    return combine_matrix(c11,c12,c21,c22)

def add(a,b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]

def sub(a,b):
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]

def split_matrix(a):
    n = len(a)//2
    a11 = [[a[i][j] for j in range(n)] for i in range(n)]
    a12 = [[a[i][j] for j in range(n,len(a))] for i in range(n)]
    a21 = [[a[i][j] for j in range(n)] for i in range(n,len(a))]
    a22 = [[a[i][j] for j in range(n,len(a))] for i in range(n,len(a))]
    
    return a11,a12,a21,a22

def combine_matrix(a11,a12,a21,a22):
    n = len(a11)
    a = [[0 for j in range(2*n)] for i in range(2*n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = a11[i][j]
            a[i][j+n] = a12[i][j]
            a[i+n][j] = a21[i][j]
            a[i+n][j+n] = a22[i][j]
    return a

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(len(a)):
    print(a[i])
    # print()

for i in range(len(b)):
    print(b[i])
    # print()
    
ans = strassen_multiply(a,b)
for i in range(len(ans)):
    print(ans[i])
    print()