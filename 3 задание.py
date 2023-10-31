# 3 задание
def decorator_function(func):
    fib = {}

    def wrapper(*args):
        if args in fib:
            return fib.get(args)
        else:
            result = func(*args)
            fib[args] = result
            return result
    return wrapper


@decorator_function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))
print(fibonacci(2))
print(fibonacci(7))
