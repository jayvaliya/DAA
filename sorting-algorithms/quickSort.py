# Function to perform quick sort on an array
# Time complexity: O(nlogn)
# Space complexity: O(logn) - for recursion stack
def quickSort(arr):
    # Base case: If the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element (middle element in this case)
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three parts: left, middle (equal to pivot), and right
    left = [x for x in arr if x < pivot]      # Elements less than pivot
    middle = [x for x in arr if x == pivot]   # Elements equal to pivot
    right = [x for x in arr if x > pivot]     # Elements greater than pivot
    
    # Recursively sort the left and right parts
    return quickSort(left) + middle + quickSort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print(quickSort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]
