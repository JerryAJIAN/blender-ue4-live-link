import socket
import threading

def startserver():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),8888))
    s.listen(1)

    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        clientsocket.send(bytes("welcome to the server", "utf-8"))

thread = threading.Thread(target=startserver)
thread.start()