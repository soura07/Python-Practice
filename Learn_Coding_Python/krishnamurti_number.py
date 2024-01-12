def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def isKrishnamurthy(n):
    sum = 0
    temp = n

    while temp != 0:
        rem = temp % 10
        sum += factorial(rem)
        temp //= 10

    return sum == n

n = 145
print("YES" if isKrishnamurthy(n) else "NO")
