FILENAME = 'log.txt'
logfile = open(FILENAME, 'w+')

def log(*obj):
    global logfile
    str = ''
    for o in obj:
        str += o
    print(str)
    logfile = open(FILENAME, 'a+')
    logfile.write(str)
    logfile.close()

def close():
    global logfile
    logfile.close()