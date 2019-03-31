
def log(str):
    logfile = open('log.txt', 'a+')
    print(str, '\n')
    logfile.write(str + '\n')
    logfile.close()

def close():
    open('log.txt', 'w')