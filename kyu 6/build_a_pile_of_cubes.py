def find_nb(m):
    # your code
    n = 1
    sum = 0
    while sum<m:
        sum = sum + (n*n*n)
        if sum == m:
            return n
        n+=1
    return -1