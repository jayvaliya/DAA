
# li=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

li=[[0,0,0],[0,0,0],[0,0,0]]

n=3

i=0
j=n//2

for x in range(1,n*n+1):
    li[i][abs(j)]=x
    if x%n==0:
        i=(i+1)%n
    else:
        i=abs((i-1)%n)
        j=(j+1)%n

# Print the Matrix
for i in range(n):
    print(li[i])
