def max_sequence(arr):
    # ... 
    max_sum = 0
    max_end = 0
    initial = 0
    end = 0
    if len(arr) == 0:
        return max_sum
    
    for i in range(len(arr)):
        
        if arr[i] > max_sum + arr[i]:
            initial = i
            max_sum = arr[i]
            

        else:
            max_sum += arr[i]

        if max_end < max_sum:
            max_end = max_sum
            end = i
    return max_end