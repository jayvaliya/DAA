# write a program to determine whether a given number is prime or not.

def is_prime(n):
    if n < 2:
        return False
    
    # for i in range(2, n): # this is O(n)
    # for i in range(2, n//2 + 1): # this is O(n/2)
    for i in range(2, int(n**0.5)+1): # this is O(sqrt(n)) [Best]
        if n % i == 0:
            return False
    return True


print(is_prime(4))
print(is_prime(37))

# time complexity of is_prime is O(sqrt(n))
# space complexity of is_prime is O(1)