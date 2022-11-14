'''

Task 2

'''

import socket
import threading

HOST = '127.0.0.1'
PORT = 6161
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
thread_counter = 0

def client(connection):
    while True:
        data = connection.recv(1024)
        reply = f'[RECEIVED FROM CLIENT]:{data.decode("utf-8")}'
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()



server_socket.bind((HOST, PORT))
server_socket.listen(6)
print(HOST, PORT)

while True:
    connection,address = server_socket.accept()
    thread = threading.Thread(target=client, args=(connection,))
    thread.start()
    thread_counter+=1
    print(f'Threads: {thread_counter}')
