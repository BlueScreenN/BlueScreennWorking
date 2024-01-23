import os   
from cryptography.fernet import Fernet

fileList = []

for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomedecrypter.py":
        continue
    if os.path.isfile(file):
        fileList.append(file)

with open("generatedkey.key", "rb") as generatedkey:
    secretKey = generatedkey.read()

for file in fileList:
    with open(file, "rb") as theFile:
        contents = theFile.read()
    contentsDecrypted = Fernet(secretKey).decrypt(contents)
    with open (file, "wb") as theFile:
        theFile.write(contentsDecrypted)
