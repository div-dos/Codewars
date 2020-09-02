from math import floor, log

def elder_age(m,n,l,t):
    a = max(m, n)
    b = min(m, n)
    
    p = 2 ** floor(log(a, 2))
    q = min(p, b)
    
    f = max(0, -l)
    to = max(0, p - l - 1)

    sum = q * (to - f + 1) * (f + to) >> 1

    if a > p:
        sum += elder_age(a - p, q, l - p, t)

    if b > q:
        sum += elder_age(p, b - q, l - q, t)

    if b > q and a > p:
        sum += elder_age(a - p, b - q, l, t)

    return sum % t