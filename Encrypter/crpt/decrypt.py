import random as rand
import readFile


def getText(file):
    text, name = readFile.readFile(file)
    text = readFile.splitData(text)
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

def decrypt(text, seed):
    rand.seed(seed)
    trace = []
    end = []
    for key in text:
        key = int(key, 16)
        key = key - rand.randint(0, 255)
        key = key % 256
        key = hex(key)
        print(key)
        key = key.split("0x")[1]
        print(key)
        key = key.zfill(2)
        print(key)
        end.append(key)
    trace.append(rand.randbytes(15))
    return end, trace 
   
def createDecrypted(text, originName = "text", extension = ".txt"):
    fileCreated = False
    tries = ""
    att = 0
    hexData = []
    for i in text[0]:
        print(i)
        hexData.append(int(str(i),16))
    while not fileCreated:
        try:
            with open(originName + tries +  "_decoded" + extension, "wb") as file:
                file.write(bytes(hexData))
        except FileExistsError:
            tries = f"({att})"
            att += 1
        else:
            fileCreated = True
            pass
    with open(originName + "_decrypted.seedTrace", 'w') as file:
            file.write(str(text[1]))


def main():
    text = getText(input("Path: "))
    key = getKey()
    decryptedText = decrypt(text[0], key)
    createDecrypted(decryptedText, text[1])

if __name__ == "__main__":
    main()