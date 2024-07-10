# Function to perform insertion sort on an array
# Time complexity: O(n^2)

def insertionSort(array):
    n = len(array)
    
    # Traverse through 1 to n elements
    for i in range(1, n):
        temp = array[i]
        j = i - 1
        
        # Move elements of array[0..i-1], that are greater than temp, to one position ahead of their current position
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        # Place the temp (current element being compared) in its correct position
        array[j + 1] = temp
    
    return array

# Example usage
array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(insertionSort(array))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
