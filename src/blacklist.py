import log

class Blacklist:

    __filename = ''
    __blacklist = ['']

    def __init__(self, filename):
        self.__filename = filename
        self.refresh()

    def refresh(self):
        log.log('refresh blacklist\n')
        f = open(self.__filename, 'r')
        self.__blacklist = f.read().splitlines()
        f.close()

    def isBanned(self, webserver):
        # wwwpos = webserver.find('www.')
        # webserver = webserver[(wwwpos + 4):]
        # print(webserver)

        for sv in self.__blacklist:
            if (webserver == sv):
                return True

        return False