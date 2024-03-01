import socket

s = socket.socket()
s.connect(('localhost',7070))

message = s.recv(1024)

print("This is receive message on client",message.decode())