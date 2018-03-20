
def fib(n):
"""Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
