import sys

alphabets = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ?.,';:]}[{!@#$%^&*()_-+=") # same to be used in encrypt and decrypt

def getFileData(file):
    data = []
    f = open(file, 'r')
    for x in f:
        data.append(x)
    f.close()
    return data

def getNewIndex(o,n):
    l = len(alphabets)
    if o+n >= l:
        getNewIndex(0, n-1)
    else:
        return o+n

# key is going to be 5 digit number usign ceasar cipher
def useCipher(key, message):
    res = []
    i = 0
    for s in message:
        indexOfs = alphabets.index(s)
        res.append(alphabets[getNewIndex(indexOfs,key[i])])
        if i >= (len(key) - 1):
            i = 0
        else:
            i += 1
    return res
    
def createNewFile(data,file,key):
    def writeToFile(msg):
        with open('encrypted_'+file, 'a') as f:
            f.write(msg + "\n")
    for d in data:
        msg = useCipher(key, d)
        writeToFile(''.join(msg))
    print("File Encrypted as: encrypted_"+file)



if __name__ == "__main__":
    args = sys.argv
    file = args[1]
    data = getFileData(file)
    createNewFile(data, file, key=[1,2,3,4])
    