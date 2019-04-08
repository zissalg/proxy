

class Blacklist:
    '''
    Load from blacklist.txt
    '''

    blacklist = ['']

    def __init__(self, filename):
        f = open(filename, 'r')
        self.blacklist = f.read().splitlines()
        f.close()

    def isBan(self, webserver):
        # wwwpos = webserver.find('www.')
        # webserver = webserver[(wwwpos + 4):]
        # print(webserver)

        for elm in self.blacklist:
            if (elm == webserver):
                return True

        return False