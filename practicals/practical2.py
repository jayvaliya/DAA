# Given a sorted array and target value, find the index of the target value using binary search and return it.
# If not found, return the index where the target value should be inserted (array must remain sorted).

# Time complexity of binary search is O(log(n))
# Space complexity of binary search is O(1)
# Binary search is a divide and conquer algorithm

def binary_search(arr, target):
    left = 0  # Initialize the left boundary of the search range
    right = len(arr) - 1  # Initialize the right boundary of the search range

    while left <= right:  # Continue searching while the search range is valid
        mid = (left + right) // 2  # Calculate the midpoint of the current range
        if arr[mid] == target:  # Check if the midpoint element is the target
            return mid  # Return the index if the target is found
        elif arr[mid] < target:  # If the target is greater, search in the right half
            left = mid + 1
        else:  # If the target is smaller, search in the left half
            right = mid - 1

    return left  # Return the insertion point if the target is not found

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 5))  # Output: 4
# Explanation: The target value 5 is found at index 4
