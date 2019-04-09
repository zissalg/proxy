import socket
import log
import blacklist
import requestparser
import proxyclient

class ProxyServer:
    '''
    Nhận requests từ web browser
    Kiểm tra tính hợp lệ
    Gửi requests đi cho web server
    Khi có được dữ liệu từ web server thì gửi lại cho trình duyệt
    '''
    __MAX_DATA = 4096
    __REQUEST_TIMEOUT = 1
    __host = ''
    __port = 0
    __server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __shouldclose = False

    def __init__(self, host, port, blacklist_filename):
        self.__host = host
        self.__port = port
        self.__blacklist = blacklist.Blacklist(blacklist_filename)

    '''
    Khoi dong proxy server len
    '''
    
    def start(self):
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server.bind((self.__host, self.__port))
        self.__server.listen(False)

        while self.__shouldclose == False:
            conn, addr = self.__server.accept()
            proxyclient.ProxyClient(conn, self.__blacklist)
        
        self.__server.close()

    def close(self):
        # Day la doan code gui Close Request
        temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        temp.connect((self.__host, self.__port))
        temp.close()

    def refresh(self):
        self.__blacklist.refresh()

    

