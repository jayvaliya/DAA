# quick sort
# Time complexity: O(nlogn)
# Space complexity: O(logn)

def quickSort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x ==pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

arr = [3, 6, 8, 10, 1, 2, 1]
print(quickSort(arr)) # Output: [1, 1, 2, 3, 6, 8, 10]
