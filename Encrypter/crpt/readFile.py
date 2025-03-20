import ntpath
def readFile(path):
    with open(path, "rb") as file:
        return file.read().hex(), ntpath.basename(path)

def splitData(data):
    hex = map("".join, zip(*[iter(data)]*2))
    return list(hex)
