def move_zeros(array):
    #your code here
    count = 0
    i = 0
    l = len(array)
    while i < l:
        #print(l)
        if (array[i] is not False) and array[i] == 0:
            l -=1
            array.pop(i)
            i -=1
            count +=1
        i+=1
            
        #print(array)
    
    #print(array)
    #print(count)
    for i in range(count):
        array.append(0)
    return array