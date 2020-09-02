from math import log, sqrt

def fast_fib(n, cache={0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    m = (n + 1) // 2
    a, b = fast_fib(m - 1), fast_fib(m)
    fib = a * a + b * b if n & 1 else (2 * a + b) * b
    cache[n] = fib
    return fib

logroot5 = log(5) / 2
logphi = log((1 + 5 ** 0.5) / 2)

def nearest_fibonacci(n):
    if n == 0:
        return 0
    # Approximate by inverting the large term of Binet's formula
    y = int((log(n) + logroot5) / logphi)
    lo = fast_fib(y)
    hi = fast_fib(y + 1)
    return lo if n - lo <= hi - n else hi