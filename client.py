# import asyncio

# HOST, PORT = '127.0.0.1', 65432

# async def tcp_echo_client():
#     reader, writer = await asyncio.open_connection(HOST, PORT)

#     # while True:
#     global message
#     # message = input('command:')
#     writer.write('name:ssda'.encode())
#     await writer.drain()
#     data = await reader.read(2048)
#     print(f'Received: {data.decode()!r}')
#     writer.write('edit:ok'.encode())
#     print('sd')
#     print('sd')

#     data = await reader.read(2048)
#     print(f'Received: {data.decode()!r}')

#     print('Closing the connection')
#     writer.close()

# asyncio.run(tcp_echo_client())

# 2nd sol

# import socket, threading

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
HOST, PORT = '127.0.0.1', 65432
# try:
#     s.connect((HOST, PORT))
#     print('Connected')
# except:
#     print('Couldnt connect')

# s.send(b'test')

# def reciever():
#     while True:
#         data = s.recv(2048).decode()
#         if data:
#             print(data)
#         if data == 'dc':
#             s.close()
#             quit()

# thread = threading.Thread(target=reciever)
# thread.start()

# while True:
#     message = input()
#     s.send(message.encode())

import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(HOST, PORT)

    print(f'Send: {message!r}')
    while True:
        if message != 'l':
            message = input('::')
            writer.write(message.encode())

        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()


asyncio.run(tcp_echo_client('Hello World!'))