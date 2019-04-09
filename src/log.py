FILENAME = 'log.txt'
logfile = open(FILENAME, 'w+')

def log(*obj, useprint = True):
    global logfile
    str = ''
    for o in obj:
        str += o

    if useprint:
        print(str)

    logfile = open(FILENAME, 'a+')
    logfile.write(str)
    logfile.close()

def close():
    global logfile
    logfile.close()