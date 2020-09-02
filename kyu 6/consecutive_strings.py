def longest_consec(strarr, k):
    # your code
    l = len(strarr)
    prev_max_len = 0
    max_len = 0
    max_str = ''
    if len == 0 or k > l or  k<= 0:
        return ""
    for i in range(l-k+1):
        max_len = 0
        for j in range(k):
            max_len += len(strarr[i+j])
            #print(strarr[i+j])
            #max_str += strarr[i+j]
        #print(strarr[i])
        #print(prev_max_len, max_len)
        #print(max_str)
        if max_len > prev_max_len:
            prev_max_len = max_len
            max_len = 0
            max_str = ''
            for m in range(k):
                max_str += strarr[i+m]
            #print(max_str)
    return max_str