def to_camel_case(text):
    i = 0
    j = 0
    if len(text) == 0:
        return ''
    while i < len(text):
        print(text[i])
        
        
        if i == len(text) and text[len(text)].isalpha():
            new = text[len(text)].upper()
            text = text[:i-1]+new

        elif (text[i] == '-' or text[i] == '_') and text[i+1] != '\n':
            if text[i+1].islower():
                new = text[i+1].upper()
                text = text[:i]+new+text[i+2:]
            else:
                j += 1
                text = text[:i]+text[i+1:]
        
        
        print(text)
        i+=1
        
    if j == 0:
            if i == 0 and text[0].isalpha():
                new = text[i].upper()
                text = new+text[i+1:]
                
    return text