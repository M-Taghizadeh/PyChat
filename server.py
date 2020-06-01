import socket

# 1-Define Server:
# IPv4: AF_INET, IPv6: AF_INET6
# TCP: SOCK_STREAM, UDP: SOCK_DGRAM
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2-Binding:
server_ip = ('localhost', 1234) # ip and port
server.bind(server_ip)

# 3-Listening
server.listen(2) # 2 client cant connect to this server

# 4-Connection
con, addr = server.accept()

# 5-Send Data (Bytes Stream)
# con.send(b"This is a message.")
while True:
    send_data = str.encode("response: " + input(">> "))
    con.send(send_data)
