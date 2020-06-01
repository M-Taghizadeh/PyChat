import socket
import threading

client = socket.socket()
client.connect(('localhost', 12345))

def send_data():
    while True:
        message = str.encode("client: " + input())
        client.send(message)

def recv_data():
    while True:
        message_recv = client.recv(1024)
        print("\033[92m {}\033[00m" .format(message_recv.decode()))

threading.Thread(target=send_data).start()
threading.Thread(target=recv_data).start()