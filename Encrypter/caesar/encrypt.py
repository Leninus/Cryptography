from alphabet import *
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
            text.append(lowercaseValues.get(char[1]))
        elif char[0] == 2:
            text.append(uppercaseValues.get(char[1]))
        elif char[0] == 3:
            text.append(othersValues.get(char[1]))
    return "".join(text)

def shiftString(vectors, shift):
    newVectors = []
    for char in vectors:
        if char[0] != 3:
            tempNum = char[1] + shift
            tempNum = tempNum % 26
            newVectors.append((char[0], tempNum))
        else:
            newVectors.append(char)
    return newVectors

def main():
    textStart = input("Input text to cypher: ")
    shift = int(input("Input shift value (whole number): "))
    vectors = getVectors(textStart)
    vectors = shiftString(vectors, shift)
    textEnd = combineString(vectors)
    print(textEnd)

if __name__ == "__main__":
    main()