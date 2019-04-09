import proxy
import log
import sys
import console

port = 8888

if (len(sys.argv) == 1):
    print('Port argv is empty, use default port 8888')
elif (len(sys.argv) == 2):
    port = int(sys.argv[1])

console.start(proxy.Proxy('127.0.0.1', port, 'blacklist.conf'))
log.close()
