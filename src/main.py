import proxyserver
import log
import sys
import console

port = 8888

if (len(sys.argv) == 1):
    print('Port argv is empty, use default port 8888')
elif (len(sys.argv) == 2):
    port = int(sys.argv[1])

proxyserver = proxyserver.ProxyServer('127.0.0.1', port, 'blacklist.conf')
console.start(proxyserver)
log.close()
