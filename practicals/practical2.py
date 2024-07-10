# given a sorted array and targate value find the index of the targate value using binary search and return it, If not found return the index where the targate value should be inserted(array must remian sorted).

# time complexity of binary search is O(log(n))
# space complexity of binary search is O(1)
# binary search is a divide and conquer algorithm

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 5))