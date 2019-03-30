import socket
import _thread
import sys
import os

HOST=''
PORT=8888
MAX_DATA=4096

shouldClose = False
proxyServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def proxyStart():
    global shouldClose

    proxyServer.bind((HOST, PORT))
    proxyServer.listen(False)

    _thread.start_new_thread(inputThread, ())
    
    while (shouldClose == False):
        conn, addr = proxyServer.accept()
        _thread.start_new_thread(proxyThread, (conn, addr))


    proxyServer.close()
    print('Proxy was closed')

def inputThread():
    global shouldClose

    while shouldClose == False:
        issue = input('User: ')
        if issue == 'terminate':
            print("Terminate detected!")
            shouldClose = True
            proxyServer.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.close()
            break
            

def proxyThread(conn, addr):
    requests = conn.recv(4096)
    webserver = socket.gethostbyname('phimmoi.net')
    port = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((webserver, port))
    s.send(requests)

    while 1:
        data = s.recv(MAX_DATA)
        if (len(data) > 0):
            conn.send(data)
        else:
            break

    s.close()
    conn.close()

proxyStart()
