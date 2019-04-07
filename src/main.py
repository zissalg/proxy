import proxy
import log
import sys

port = 8888

if (len(sys.argv) == 1):
    print('Port argv is empty, use default port 8888')
elif (len(sys.argv) == 2):
    port = int(sys.argv[1])

proxy = proxy.Proxy('127.0.0.1', port)
proxy.start()
proxy.close()
log.close()
