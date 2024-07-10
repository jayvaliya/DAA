# Function to perform selection sort on an array
# Time complexity: O(n^2)
def selectionSort(array):
    n = len(array)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

# Example usage
array = [64, 34, 25, 12, 22, 11, 90]
print(selectionSort(array))  # Output: [11, 12, 22, 25, 34, 64, 90]
