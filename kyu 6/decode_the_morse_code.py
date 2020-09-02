
def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    #morse_code = morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    words = morse_code.split('   ')
    sol = []
    for i in range(len(words)):
        words[i] = words[i].split(' ')
        length = len(words[i])
        while("" in words[i]) : 
            words[i].remove("")
            length -= 1
        print(length)
        for j in range(length):
            words[i][j] = str(MORSE_CODE.get(words[i][j]))
            print(words[i])
        sol.append("".join(words[i]))
        print(sol)
        while("" in sol) : 
            sol.remove("")
    return " ".join(sol)
    #print(words)