import _thread
import os

def print_usage():
    print('------------------------------------------------')
    print('USAGE: ')
    print()
    print('    close: close proxy server and exit the program')
    print()
    print('    refresh: refresh our Blacklist')
    print()
    print('    help: print this usage:)')
    print('------------------------------------------------')

def loop():
    global proxy_server
    print('type \'help\' to see more infomation!')
        
    while True:
        req = input()
        if (req == 'close'):
            proxy_server.close()
            os._exit(0)
        elif (req == 'refresh'):
            proxy_server.refresh()
        elif (req == 'help'):
            print_usage()
        else:
            print_usage()

def start(proxy):
    _thread.start_new_thread(loop, ())
    global proxy_server
    proxy_server = proxy
    proxy_server.start()