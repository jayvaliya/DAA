# insertion sort
# Time complexity: O(n^2)

def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        temp = array[i]
        j = i-1
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp
        # print(array)
    return array

array= [9,8,7,6,5,4,3,2,1]

print(insertionSort(array)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
