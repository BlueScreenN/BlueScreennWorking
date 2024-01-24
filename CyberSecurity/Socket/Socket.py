import socket

myConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myConnection.connect(("192.168.1.134", 8080))

myConnection.send("Connection OK")