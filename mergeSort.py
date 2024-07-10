# merge sort
# Time complexity: O(nlogn)
# Space complexity: O(n)


def mergeSort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

arr = [3, 6, 8, 10, 1, 2, 1]
print(mergeSort(arr)) # Output: [1, 1, 2, 3, 6, 8, 10]