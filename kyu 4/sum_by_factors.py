def sum_for_list(lst):
    #find the largest number in the lst
    max = 0
    for i in lst:
        if abs(i) > max:
            max = abs(i)
    
    #find the list of all the prime factors
    factor = []
    for i in lst:
        #print(i)
        for j in range(2,abs(i)+1):
            #print(j)
            if i%j == 0 and j not in factor:
                factor.append(j)
    
    #print(factor)
    prime_factor = []

    for i in factor:
        if is_prime(i):
            prime_factor.append(i)

    prime_factor.sort()
    #print(prime_factor)
    sol = []
    for i in prime_factor:
        sum = 0
        #print(i)
        for j in lst:
            #print(j)
            if j%i == 0:
                #print('True')
                sum += j
        sol.append([i, sum])

    return sol

def is_prime(i):
    for m in range(2,i):
        if (i%m==0):
            return False
    return True