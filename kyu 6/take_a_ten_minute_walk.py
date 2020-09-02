def is_valid_walk(walk):
    #determine if walk is valid
    h = 0
    v = 0
    if len(walk) == 10:
        for i in walk:
            if i=='n':
                v+=1
            elif i=='s':
                v-=1
            elif i=='w':
                h-=1
            elif i=='e':
                h+=1
        if h==0 and v==0:
            return True
        
    return False