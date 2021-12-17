import socket
from datetime import datetime
import threading

# server Configs
HOST, PORT = '127.0.0.1', 65432

# text
txt = ''

# users
USERS = {}
CONNS = []
editor = ''

# last edit
last_edit = datetime(2001, 2, 3, 4, 5, 6)


def send_all(data):
    global CONNS
    for i in CONNS:
        i.sendall(data.encode())


# python client.py
def handler(conn, addr):
    global last_edit, editor, USERS, CONNS, txt
    print('Connected by', addr)
    while True:
        # parsing data
        data = conn.recv(2048)
        in_data = data.decode()

        # registering user
        if in_data.split(':')[0] == 'name':
            # input should be in form of "name:<name>"
            name = in_data.split(':')[1]
            if USERS.get(addr):
                conn.send(b'You have already chosen a name')
            else:
                if name in USERS.values():
                    conn.send(b'This name is already taken')
                else:
                    USERS[addr] = name
                    CONNS.append(conn)
                    send_all(f'{name} with ip {addr} joined.')

        # disconnecting
        # ! fix this
        if in_data == 'dc':
            name = USERS.get(addr)
            USERS.pop(addr)
            CONNS.remove(conn)
            conn.sendall(b'dc')
            send_all(f'user {name} with ip "{addr}" disconnected')
            conn.close()
            break

        # editing txt
        # ? input in form of "edit:<txt>"
        elif in_data.split(':')[0] == 'edit':
            # check registered or not
            if addr not in USERS.keys():
                conn.send(b'You are not registered')
            else:
                # check last_Edit time less than 5 seconds
                if editor == addr or (datetime.now() - last_edit).seconds > 5:
                    editor = addr
                    send_all(f'editor:{USERS[addr]}')
                    last_edit = datetime.now()
                    # edit
                    txt = in_data.split(':')[1]
                    send_all(f'txt:{txt}')
                else:
                    conn.send(b'status:Editing is on cooldown')
        if not data:
            break


# starting server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=handler, args=(conn, addr))
    thread.start()
    print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')
