import socket
import log
import requestparser
import blacklist
import _thread

class ProxyClient:
    __MAX_DATA = 4096
    __REQUEST_TIMEOUT = 1
    '''
    '''
    def __init__(self, conn, blacklist):
        _thread.start_new_thread(self.__client_thread, (self, conn, blacklist))
    
    @staticmethod
    def __client_thread(self, conn, blacklist):
        request = conn.recv(self.__MAX_DATA)
        parser = requestparser.RequestParser(request)

        if (blacklist.isBanned(parser.getwebserver())):
            f = open('403.html', 'r')
            conn.sendall(f.read().encode('utf-8'))
            f.close()
            conn.close()
            return

        self.__communicate(self, conn, parser.getwebserver(), request)
    
    @staticmethod
    def __communicate(self, conn, host, request):
        log.log('connect to ', host, '\n')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.__REQUEST_TIMEOUT)

        try:
            s.connect((host, 80))
            s.send(request)

            while True:
                data = bytes(s.recv(self.__MAX_DATA))
                if (len(data) > 0):
                    conn.sendall(data)
                else:
                    s.close()
                    break
        except socket.timeout:
            log.log(host, ', request timed out!')
            s.close()

        conn.close()