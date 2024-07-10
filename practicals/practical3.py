# There are N children standing in a line. Each child is assigned a rating value. You are giving candies to these children subjected to the following requirements: Each child must have at least one candy. Children with a higher rating get more candies than their neighbors. What is the minimum candies you must give/have?

def min_candies(ratings):
    n = len(ratings)
    candies = [1] * n  # Step 1: Give each child 1 candy initially

    # Traverse from left to right
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1  # If current child has higher rating, give more candies than the previous child

    # Traverse from right to left
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)  # Ensure the current child has more candies than the next child if higher rating

    return sum(candies)  # Return the total number of candies

# Example 1
ratings1 = [1, 0, 2]
print(min_candies(ratings1))  # Output: 5
# Explanation:
# Initial candies: [1, 1, 1]
# Left to right: [1, 1, 2]
# Right to left: [2, 1, 2]

# Example 2
ratings2 = [1, 2, 2]
print(min_candies(ratings2))  # Output: 4
# Explanation:
# Initial candies: [1, 1, 1]
# Left to right: [1, 2, 1]
# Right to left: [1, 2, 1]

# Example 3
ratings3 = [1, 3, 4, 5, 2]
print(min_candies(ratings3))  # Output: 11
# Explanation:
# Initial candies: [1, 1, 1, 1, 1]
# Left to right: [1, 2, 3, 4, 1]
# Right to left: [1, 2, 3, 4, 1]

# Example 4
ratings4 = [1, 2, 87, 87, 87, 2, 1]
print(min_candies(ratings4))  # Output: 13
# Explanation:
# Initial candies: [1, 1, 1, 1, 1, 1, 1]
# Left to right: [1, 2, 3, 1, 1, 2, 1]
# Right to left: [1, 2, 3, 1, 2, 1, 2]
