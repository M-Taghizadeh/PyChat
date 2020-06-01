import socket

# 1- Define Client 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2- Connect to server
server_ip = ('localhost', 1234) 
client.connect(server_ip)

# 3-Receive Data from server(GET Response) and print it.
# data = client.recv(1024) # receives blocks of size 1024 from the server
while True:
    data = client.recv(1024)
    print(data.decode())




