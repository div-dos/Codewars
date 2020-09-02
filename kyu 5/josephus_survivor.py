def josephus_survivor(n,k):
    #your code here
    lst = list(range(1,n+1))
    #print(lst)
    i = 0
    while len(lst)>1:
        #print(lst)
        if i+k > len(lst):
            i = i+k - len(lst)-1
        else:
            i += k-1
        #print(i, len(lst))
        while(i>len(lst)-1):
            i -= len(lst)
        lst.pop(i)
    return lst[0]