import socket

s = socket.socket()
s.bind(('localhost',7070))
s.listen(5)
clie,addr = s.accept()
print(f"connection has estiblished to {addr}")

clie.send(bytes(f"this is send message from server","utf-8"))