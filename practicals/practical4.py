
# there is a new barn with n stalls and c cows. the stalls are located on a straight line at position stall1, stall2, stall3, ..., stalln. we wantto assign the cows to the stalls so that the minimum distance between any two of them is as large as possible. what is the largest minimum distance?return the maximum possible distance between the cows.

# input: n = 5, c = 3, stall = [1, 2, 8, 4, 9]
# output: 3

def minimum_distance(n, c, stall):
    stall.sort()
    low, high = 0, stall[-1] - stall[0]
    while low < high:
        mid = low + (high - low + 1) // 2
        count = 1
        start = stall[0]
        for i in range(1, n):
            if stall[i] - start >= mid:
                count += 1
                start = stall[i]
        if count >= c:
            low = mid
        else:
            high = mid - 1
    return low