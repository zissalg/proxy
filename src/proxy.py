import socket
import log
import _thread

class Proxy:
    '''
    Nhận requests từ web browser
    Kiểm tra tính hợp lệ
    Gửi requests đi cho web server
    Khi có được dữ liệu từ web server thì gửi lại cho trình duyệt
    '''
    MAX_DATA = 4096
    host = ""
    port = 0
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def parse_url(self, requests):
        first_line = requests.split('\n')[0]

        if (len(first_line) <= 1):
            return ""

        url = first_line.split(' ')[1]
        http_pos = url.find("://")
        if (http_pos == -1):
            temp = url
        else:
            temp = url[(http_pos + 3):]
        port_pos = temp.find(":")
        webserver_pos = temp.find("/")
        if (webserver_pos == -1):
            webserver_pos = len(temp)
    
        webserver = temp[:webserver_pos]

        return webserver

    def __init__(self, host, port):
        self.host = host
        self.port = port

    @staticmethod
    def __communicate(self, host, conn, requests):
        print('Connect to ', host, ':', 80)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)

        try:
            s.connect((host, 80))
            s.send(requests)

            while True:
                data = bytes(s.recv(self.MAX_DATA))
                if (len(data) > 0):
                    conn.sendall(data)
                else:
                    break

            s.close()
        except socket.timeout:
            print(host, ':', 80, ' requests timed out!')
            s.close()

    @staticmethod
    def __client_thread(self, conn, addr):
        requests = conn.recv(self.MAX_DATA)
        webserver = self.parse_url(requests.decode('ASCII'))
        self.__communicate(self, webserver, conn, requests)
        conn.close()

    def start(self):
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(False)

        while True:
            conn, addr = self.server.accept()
            _thread.start_new_thread(self.__client_thread, (self, conn, addr))

    def close(self):
        sefl.server.close()

    

