def product(numbers):
    prod=1
    for n in numbers:
        prod=prod*n
    return prod
def factorial(n):
    fact=1
    numbers = list(range(1, n + 1))
    return product(numbers)


print(factorial(4))