def spin_words(sentence):
    # Your code goes here
    l = sentence.split(' ')
    sol = []
    for i in l:
        if len(i) >= 5:
            sol.append(i[::-1])
        else:
            sol.append(i)
    
    return ' '.join(sol)