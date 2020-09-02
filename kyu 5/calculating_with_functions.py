def zero(fun = None):
    #your code here
    if fun == None:
        return 0
    else:
        return fun(0)
def one(fun = None): #your code here
    if fun == None:
        return 1
    else:
        return fun(1)
    
def two(fun = None): #your code here
    if fun == None:
        return 2
    else:
        return fun(2)
def three(fun = None): #your code here
    if fun == None:
        return 3
    else:
        return fun(3)
def four(fun = None): #your code here
    if fun == None:
        return 4
    else:
        return fun(4)
def five(fun = None): #your code here
    if fun == None:
        return 5
    else:
        return fun(5)
def six(fun = None): #your code here
    if fun == None:
        return 6
    else:
        return fun(6)
def seven(fun = None): #your code here
    if fun == None:
        return 7
    else:
        return fun(7)
def eight(fun = None): #your code here
    if fun == None:
        return 8
    else:
        return fun(8)
def nine(fun = None): #your code here
    if fun == None:
        return 9
    else:
        return fun(9)

def plus(y): #your code here
    return lambda x: x+y
def minus(y): #your code here
    return lambda x: x-y
def times(y): #your code here
    return lambda x: x*y
def divided_by(y): #your code here
    return lambda x: int(x/y)