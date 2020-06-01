import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(16)
conn, addr = server.accept()

def send_data():
    while True:
        message = str.encode("server: " + input())
        conn.send(message)

def recv_data():
    while True:
        message_recv = conn.recv(1024)
        print("\033[96m {}\033[00m" .format(message_recv.decode()))

threading.Thread(target=send_data).start()
threading.Thread(target=recv_data).start()