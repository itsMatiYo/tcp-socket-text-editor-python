import socket
from datetime import datetime
import threading
import asyncio

# server Configs
HOST, PORT = '127.0.0.1', 65432

# text
txt = ''

# users
USERS = {}
editor = ''

# last edit
last_edit = datetime(2001, 2, 3, 4, 5, 6)


def send_all(data):
    """send the str(data) to all connections"""
    global USERS
    for i in USERS.keys():
        i.write(data.encode())


class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('socknet')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        # self.transport.write(data)
        """Handler for conncetions"""
        global last_edit, editor, USERS, txt
        print('Connected by', self.transport.get_extra_info('sockname'))
        data = message
        if data != 'dc':
            if data.split(':')[0] == 'name':
                # input should be in form of "name:<name>"
                name = data.split(':')[1]
                if USERS.get(self.transport):
                    self.transport.write(b'You have already chosen a name')
                else:
                    if name in USERS.values():
                        self.transport.write(b'This name is already taken')
                    else:
                        USERS[self.transport] = name
                        send_all(f'{name} joined.')

            # editing txt
            # ? input in form of "edit:<txt>"
            elif data.split(':')[0] == 'edit':
                # check registered or not
                if self.transport not in USERS.keys():
                    self.transport.write(b'You are not registered')
                else:
                    # check last_Edit time less than 5 seconds
                    if editor == self.transport or (datetime.now() -
                                                    last_edit).seconds > 5:
                        if editor != self.transport:
                            editor = self.transport
                            send_all(f'editor:{USERS[self.transport]}')
                        last_edit = datetime.now()
                        # edit
                        txt = data.split(':')[1]
                        send_all(f'txt:{txt}')

                    else:
                        self.transport.write(b'status:Editing is on cooldown')
        else:
            # disconnecting
            name = USERS.get(self.transport)
            USERS.pop(self.transport)
            self.transport.write(b'dc')
            send_all(f'user {name} disconnected')
            self.transport.close()

            # print('Close the client socket')
            # self.transport.close()


async def run_server():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(lambda: EchoServerProtocol(), HOST, PORT)

    async with server:
        await server.serve_forever()


# try:
asyncio.run(run_server())
# except:
#     print('Error')
