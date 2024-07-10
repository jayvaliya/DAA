
# selection sort
# Time complexity: O(n^2)

def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

array = [64, 34, 25, 12, 22, 11, 90]
print(selectionSort(array)) # output: [11, 12, 22, 25, 34, 64, 90]