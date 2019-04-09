import socket
import log
import blacklist
import requestparser
import _thread

class Proxy:
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
    Day la proxy client
    Su dung de giao tiep voi webserver
    '''
    @staticmethod
    def __communicate(self, host, conn, requests):
        log.log('connect to ', host, ':', str(80), '\n')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.__REQUEST_TIMEOUT)

        # TODO: make this block more clearly
        try:
            s.connect((host, 80))
            s.send(requests)

            while True:
                data = bytes(s.recv(self.__MAX_DATA))
                if (len(data) > 0):
                    try:
                        conn.sendall(data)
                    except BrokenPipeError:
                        log.log('Broken pipe error\n')
                else:
                    break

            s.close()
        except socket.timeout:
            log.log(host, ', request timed out!\n')
            s.close()

    '''
    Day la proxy client
    Su dung de kiem tra xem webserver co nam trong baclklist.conf khong
    Neu' co', gui cho webbrowser noi dung 403.html
    '''
    @staticmethod
    def __client_thread(self, conn, addr):
        request = conn.recv(self.__MAX_DATA)
        parser = requestparser.RequestParser(request) # Day la request parser ne, su dung cho no' tien. thoi

        if (parser.is_close_request()):
            self.__shouldclose = True
            conn.close()
            return

        if (self.__blacklist.isBanned(parser.getwebserver())):
            # TODO: send file
            f = open('403.html', 'r')
            conn.sendall(f.read().encode('utf-8'))
            f.close()
            conn.close()
            return

        self.__communicate(self, parser.getwebserver(), conn, request)
        conn.close()

    '''
    Khoi dong proxy server len
    '''
    
    def start(self):
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server.bind((self.__host, self.__port))
        self.__server.listen(False)

        while self.__shouldclose == False:
            conn, addr = self.__server.accept()
            # Su dung thread de giu~ cac' ket' noi' con
            _thread.start_new_thread(self.__client_thread, (self, conn, addr))
        
        self.__server.close()

    def close(self):
        # Day la doan code gui Close Request
        temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        temp.connect((self.__host, self.__port))
        temp.sendall(b'MYCLOSEREQUEST')
        temp.close()

    def refresh(self):
        self.__blacklist.refresh()

    

