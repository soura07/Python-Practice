# tup = (1,2,3,56)
# # tup[2] = 5
# print(type(tup))

def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Found a factor, not a prime number
    return True  # No factors found, it's a prime number

# Example usage:
num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
