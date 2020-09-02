def narcissistic( value ):
    # Code away
    count = 0
    sum = 0
    num = value
    dig = 0
    while num != 0: 
        num //= 10
        count+= 1
    num = value
    while num != 0:
        dig = num%10
        sum += dig**count
        num //= 10
    if sum == value:
        return True
    return False