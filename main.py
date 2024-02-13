from twisted.internet import reactor
from twisted.web import http, proxy


class MyProxyRequest(proxy.ProxyRequest):

    def process(self):
        print(f"Received request for {self.uri}")
        super().process()


class MyProxy(proxy.Proxy):
    requestFactory = MyProxyRequest


class ProxyFactory(http.HTTPFactory):
    protocol = MyProxy


reactor.listenTCP(10026, ProxyFactory())
reactor.run()
