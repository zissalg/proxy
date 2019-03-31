import socket

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b'asdfasdfasdfsdafsd')

connect('127.0.0.1', 8888)