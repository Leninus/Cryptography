lowercaseAlphabet = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26
}
uppercaseAlphabet = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26
}
others = {
    " " : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "0" : 10,
    "." : 11, 
    "!" : 12,
    "?" : 13,
    "," : 14 
}
def getVectors(text):
    text = list(text)
    chars = []
    for char in text:
        data = (0,0)
        if char.isupper():
            data = (2, uppercaseAlphabet.get(char))
        elif char.islower():
            data = (1, lowercaseAlphabet.get(char))
        else:
            try:
                data = (3, others.get(char))
            except KeyError:
                data = (3, 0)
        chars.append(data)
    return chars

def combineString(vectors):
    text = []
    for char in vectors:
        if char[0] == 1:
            text.append(lowercaseAlphabet.get(char[1]))
print(getVectors("TeSt , 1234567890"))