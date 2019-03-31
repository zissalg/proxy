import proxy
import log

proxy = proxy.Proxy('127.0.0.1', 8889)
proxy.start()
proxy.close()
log.close()