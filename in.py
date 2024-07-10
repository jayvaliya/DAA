
arr = [6,3,4,2,1,5]

for i in range(1,len(arr)-1):
    temp = arr[i]
    j=i-1
    while temp<arr[j] and j >=0:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
    
    
print(arr)

