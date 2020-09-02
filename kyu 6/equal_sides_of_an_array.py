def find_even_index(arr):
    #your code here
    i = 0
    
    while i != len(arr):
        sum = 0
        nsum = 0
        #print("working")
        for m in range(i):
            sum += arr[m]
        #print(sum)
        for n in range(i+1,len(arr)):
            nsum += arr[n]
        print(nsum)
        if(sum == nsum):
            return i
        i+=1
    
    return -1