import os   

fileList = []

for file in os.listdir():
    if file == "ransom.py":
        continue
    if os.path.isfile(file):
        fileList.append(file)
    

print(fileList)


