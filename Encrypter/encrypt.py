import random as rand
from pathlib import Path
import string

def getText():
    path = input("Give path to file for encryption, leave empty for your own text:")
    if not path:
        text = input("Give text for encryption: ")
        name = "text"
    else:
        name = Path(path).stem
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
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
    end = []
    for key in text:
        key = ord(key)
        key = key + rand.randint(0,1000)
        key = chr(key)
        end.append(key)
    return "".join(end)

def outputToFile(text, seed, name = "text",):
    with open(name + ".crpt", "w", encoding="utf-8") as file:
        file.write(text)
    if seed == "0000":
        pass
    else:
        with open(name + ".key", "w", encoding="utf-8") as file:
            file.write(seed)

def main():
    text = getText()
    seed = generateSeed()
    encryptedText = encrypt(text[0], seed)
    outputToFile(encryptedText, seed, text[1])

if __name__ == "__main__":
    main()
    