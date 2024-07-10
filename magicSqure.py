# Print magic squre

# Take user input for the size of the matrix
n = int(input("Enter the size of the matrix (n x n): "))

# Initialize a 2D list (matrix) with all zeros
li = [[0] * n for _ in range(n)]

# Initialize variables for matrix manipulation
i = 0
j = n // 2

# Fill the matrix with numbers from 1 to n*n in a specific pattern
for x in range(1, n*n+1):
    li[i][abs(j)] = x  # Place current number in the matrix
    
    # Update row index
    if x % n == 0:
        i = (i + 1) % n  # Move to the next row when a full row is filled
    else:
        i = abs((i - 1) % n)  # Move up one row
        j = (j + 1) % n  # Move right one column

# Print the Matrix
for row in li:
    print(row)
