cache = {}

def log(func):
    def wrapper(*args):
        print(f"\nFunction Called : {func.__name__}")
        print(f"Arguments : {args}")

        result = func(*args)

        print(f"Return Value : {result}")
        return result
    return wrapper


def memoize(func):
    def wrapper(*args):
        if args in cache:
            print("Result fetched from cache.")
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@log
@memoize
def add(a, b):
    return a + b


@log
@memoize
def subtract(a, b):
    return a - b


@log
@memoize
def multiply(a, b):
    return a * b


@log
@memoize
def divide(a, b):
    return a / b


@log
@memoize
def power(a, b):
    return a ** b


@log
@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("Addition:", add(10, 20))
print("Addition Again:", add(10, 20))

print("\nSubtraction:", subtract(20, 10))

print("\nMultiplication:", multiply(5, 6))

print("\nDivision:", divide(20, 5))

print("\nPower:", power(2, 5))

print("\nFactorial:", factorial(5))