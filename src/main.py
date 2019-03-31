import socket
import _thread
import sys
import os

# CHÚ Ý:
# Đây chỉ là bản demo thử nên không tuân thủ các quy định về tên trong python
# Sau khi viết thật sự thì sẽ PHẢI tuân thủ

HOST=''
PORT=8889
MAX_DATA=4096

shouldClose = False
# Tạo global socket cho proxy server
proxyServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def proxyStart():
    global shouldClose

    # Gắn địa chỉ IP và PORT cho proxy server
    proxyServer.bind((HOST, PORT))
    proxyServer.listen(False)
    
    # Thêm tiến trình nhận input từ người dùng
    _thread.start_new_thread(inputThread, ())
    
    # Lắn nghe thông tin kết nối từ trình duyệt
    # Mỗi lần truy cập trang web http thì trình duyệt sẽ gửi cho mình một đống GET http://www.xxx.com/
    while (shouldClose == False):
        conn, addr = proxyServer.accept()
        _thread.start_new_thread(proxyThread, (conn, addr))

    # Tắt proxy server
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

def getURL(requests):
    decStr = requests.decode('ASCII')
    firstLine = decStr.split('\n')[0]
    fullURL = firstLine.split(' ')[1]
    print('Full URL: ', fullURL)
    URL = fullURL.split('/')[2]
    print('URL: ', URL)
    return URL

def proxyThread(conn, addr):
    global shouldClose
    # Nhận requests từ trình duyệt
    requests = conn.recv(MAX_DATA)
    # Lấy URL trong requests ra
    url = getURL(requests)
    # Lấy địa chỉ của web server từ url
    webserver = socket.gethostbyname(url)
    # Mặc định là port 80
    port = 80

    print('\nRequests from ', url, '\n')

    # Kết nối đến web server và nhận data từ server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((webserver, port))
    s.send(requests)
    
    # Sau khi kết nối xong chuyển dữ liệu từ data sang cho trình duyệt web
    while shouldClose == False:
        data = s.recv(MAX_DATA)
        if (len(data) > 0):
            conn.send(data)
        else:
            break
    
    # Hoàn tất rồi thì close
    
    s.close()
    conn.close()

proxyStart()
