def pig_it(text):
    #your code here
    arr = text.split(' ')
    sol = []
    for i in arr:
        if len(i) == 1 and i.isalpha() == False:
            sol.append(i)
        else:
            sol.append(i[1:]+i[0]+'ay')
        
    return ' '.join(sol)