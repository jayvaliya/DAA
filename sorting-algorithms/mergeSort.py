# Function to perform merge sort on an array
# Time complexity: O(nlogn)
# Space complexity: O(n)
def mergeSort(arr):
    # Base case: If the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])    # Recursively sort the left half
    right = mergeSort(arr[mid:])   # Recursively sort the right half
    
    # Merge the sorted halves
    return merge(left, right)

# Function to merge two sorted arrays into one sorted array
def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from left and right arrays and merge them into result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements from left or right arrays
    result += left[i:]
    result += right[j:]
    
    return result

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print(mergeSort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]
