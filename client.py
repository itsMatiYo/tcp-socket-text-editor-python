import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
HOST, PORT = '127.0.0.1', 65432
try:
    s.connect((HOST, PORT))
    print('Connected')
except:
    print('Couldnt connect')

s.send(b'test')


def reciever():
    while True:
        data = s.recv(2048).decode()
        print(data)
        if data == 'dc':
            s.close()
            quit()


thread = threading.Thread(target=reciever)
thread.start()

while True:
    message = input()
    s.send(message.encode())
