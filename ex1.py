def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) +  fib(n - 2)

def fib_iter(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return b


print(fib(40))