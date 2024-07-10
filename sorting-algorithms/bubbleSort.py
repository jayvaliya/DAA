# Function to perform bubble sort on an array
# Time complexity: O(n^2)

def bubbleSort(array):
    n = len(array)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
    return array

# Example usage
array = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(array))  # Output: [11, 12, 22, 25, 34, 64, 90]
