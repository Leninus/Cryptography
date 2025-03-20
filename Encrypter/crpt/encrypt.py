import random as rand
import string
import readFile

def textToHex(text):
    data = []
    for char in text:
        data.append(hex(ord(char)))
    return list(data)

def getText():
    path = input("Give path to file for encryption, leave empty for your own text:")
    if not path:
        text = textToHex(input("Give text for encryption: "))
        name = "text"
    else:
        file = readFile.readFile(path)
        name = file[1]
        text = readFile.splitData(file[0])    
    return text, name

def generateSeed():
    type = input("Press [1] to use a password, press [2] to generate a random key, press [3] to use existing key, \nleave empty to encrypt without a key: ")
    if type == "1":
        seed = input("Encrypting with password\nCreate a password: ")
    elif type == "2":
        print ("Encrypting with randomly generated key")
        seed = "".join(rand.choices(string.ascii_letters + string.digits, k = 256))
    elif type == "3":
        with open(input("Encrypting with existing key\nPath to key: "), "r", encoding="utf-8") as file:
            seed = file.read()
    else:
        print("Encrypting without key")
        seed = "0000"
    return seed

def encrypt(text, seed):
    rand.seed(seed)
    nudgedData = []
    seedTrace = []
    for key in text:
        key = int(key, 16)
        key = key + rand.randint(0,255)
        key = key % 256
        key = hex(key)
        key = key.split("0x")[1]
        key = key.zfill(2)
        nudgedData.append(key)
    seedTrace.append(rand.randbytes(15))
    return nudgedData, seedTrace

def outputToFile(text, seed, name = "text"):
    hexData = []
    for thing in text[0]:
        print(thing)
        hexData.append(int(str(thing), 16))
    with open(name + ".crpt", "wb") as file:
        file.write(bytes(hexData))
    if seed == "0000":
        with open(name + ".seedTrace", 'w', encoding='utf8') as file:
            file.write(str(text[1]))
    else:
        with open(name + ".key", "w", encoding="utf-8") as file:
            file.write(seed)
        with open(name + ".seedTrace", 'w', encoding='utf8') as file:
            file.write(str(text[1]))

def main():
    text = getText()
    print(text)
    seed = generateSeed()
    encryptedText = encrypt(text[0], seed)
    print(encryptedText)
    outputToFile(encryptedText, seed, text[1])

if __name__ == "__main__":
    main()