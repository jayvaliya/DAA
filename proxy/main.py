
# given an array use bubble sort to sort only the even numbers in ascending order while leaving the odd numbers in their original positions.

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[i]%2==0 and arr[j]%2==0):
                if(arr[i]>arr[j]):
                    temp = arr[j]
                    arr[j]=arr[i]
                    arr[i]=temp
    return arr

arr = [10,7,4,1,2,8,9,1,3]
print(BubbleSort(arr))


# given an array of int find the starting and ending position of a target value if target is not found, return [-1, -1]

arr = [10,7,4,1,2,8,1,9,3]
def findTargate(arr,targate):
    l=-1
    r=-1
    for i in range(len(arr)):
        if(arr[i]==targate):
            l = i
            break

    for j in range(len(arr) - 1, l, -1):
        if(arr[j]==targate):
            r=j
    return [l,r]
print(findTargate(arr,1))

