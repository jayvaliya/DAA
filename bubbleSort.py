# bubble sort
# Time complexity: O(n^2)

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(array)) # Output: [11, 12, 22, 25, 34, 64, 90]