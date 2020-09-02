def productFib(prod):
    # your code
    i, j = 0,1
    
    while True:
        if i*j == prod:
            return [i,j,True]
        elif i*j > prod:
            return [i,j,False]
        i, j = j, j+i
    return 