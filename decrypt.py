import sys
import os

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
    if o-n < 0:
        getNewIndex(l, n)
    else:
        return o-n

def decryptFile(key,message):
    res = []
    i = 0
    for s in message:
        if s == "\n":
            return ''.join(res)
        indexOfs = alphabets.index(s)
        res.append(alphabets[getNewIndex(indexOfs,key[i])])
        if i >= (len(key) - 1):
            i = 0
        else:
            i += 1
    return ''.join(res)

def getOGName(f:str):
    l = f.split("_")
    return l[1]
    

def createNewFile(data,file,key):
    newFileName = getOGName(file)
    def writeToFile(msg):
        with open(newFileName, 'a') as f:
            f.write(msg + "\n")
    for d in data:
        msg = decryptFile(key, d)
        writeToFile(msg)
    print("File decrypted as: "+newFileName)


        


if __name__ == "__main__":
    args = sys.argv
    file = args[1]
    data = getFileData(file)
    createNewFile(data, file, key=[1,2,3,4])