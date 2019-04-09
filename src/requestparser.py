import log


class RequestParser:
    __request = ''
    __url = ''
    __webserver = ''
    __close_request = False

    def __init__(self, request):
        self.__request = request.decode('ascii')
        log.log(self.__request, '\n')

        if (self.is_close_request()):
            return

        self.__parseurl()
        self.__parsewebserver()

    def __parseurl(self):
        lines = self.__request.split('\n')

        if (len(lines) == 0):
            log.log('parseurl(), error while parsing request!\n')
            return

        firstline = lines[0]
        self.__url = firstline.split(' ')[1]
    
    def __parsewebserver(self):
        http = 'http://'
        httppos = self.__url.find(http)
        if (httppos == -1):
            log.log('parserwebserver(), error while parsing request\n')

        temp = self.__url[(httppos + len(http)):]
        serverpos = temp.find('/')

        if (serverpos == -1):
            serverpos = len(temp)
        
        self.__webserver = temp[:serverpos]


    def getwebserver(self):
        return self.__webserver

    def geturl(self):
        return self.__url

    def is_close_request(self):
        return self.__request.find('MYCLOSEREQUEST') != -1

'''
parser = RequestParser(b'GET http://www.phimmoi.net/phim/phong-than-duong-tien-truyen-ky-6521/ HTTP/1.1 \
Host: www.phimmoi.net\
Proxy-Connection: keep-alive\
Cache-Control: max-age=0\
Upgrade-Insecure-Requests: 1\
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36 \
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\
Accept-Encoding: gzip, deflate\
Accept-Language: en-US,en;q=0.9,vi;q=0.8\
Cookie: __cfduid=da165af55e0881152180cd9d37655b7441554698237; __utmz=247746630.1554698239.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=0c2941138c1b62fc:T=1554698240:S=ALNI_MadmUNH0SMa-q1DMVTXlGxi_6okUQ; _ga=GA1.2.171894974.1554698239; _gid=GA1.2.1415228359.1554698240; __utma=247746630.171894974.1554698239.1554698239.1554725895.2; __utmc=247746630; uniad_preload_1032=2'
)

print('url: ',parser.geturl())
print('webserver: ',parser.getwebserver())
'''