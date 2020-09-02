def order(sentence):
  # code here  
    arr = sentence.split(' ')
    sol = ['']*len(arr)
    for i in arr:
        for j in i:
            if j.isnumeric():
                print(j)
                sol[int(j)-1] = i
    return ' '.join(sol)