import random as rand
from pathlib import Path

def getText(file):
    name = Path(file).stem
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()
    return text, name

def getKey():
    type = input("Press [1] to decrypt with password, press [2] to decrypt with key, leave empty to decrypt without key")
    if type == "1":
        key = input("Decrypting using a password\nEnter password: ")
    elif type == "2":
        file = input("Decrypting with a key\nPath to key: ")
        with open(file, "r", encoding="utf-8") as file:
            key = file.read()
    else: 
        key = "0000"
    return key    

def decrypt(text, key):
    rand.seed(key)
    end = []
    for key in text:
        key = ord(key)
        key = key - rand.randint(0,1000)
        key = chr(key)
        end.append(key)
    return "".join(end) 
   
def createDecrypted(text, originName = "text", extension = ".txt"):
    fileCreated = False
    tries = ""
    att = 0
    while not fileCreated:
        try:
            with open(originName + tries +  "_decoded" + extension, "x") as file:
             file.write(text)
        except FileExistsError:
            tries = f"({att})"
            att += 1
        else:
            fileCreated = True
            pass


def main():
    text = getText(input("Path: "))
    key = getKey()
    decryptedText = decrypt(text[0], key)
    createDecrypted(decryptedText, text[1])

if __name__ == "__main__":
    main()