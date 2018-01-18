# -*- coding:utf-8 -*-

from SocketServer import BaseRequestHandler, ThreadingTCPServer


class EchoHander(BaseRequestHandler):
    def handle(self):
        print('got connect from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            print msg
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    server = ThreadingTCPServer(('', 2000), EchoHander)
    server.serve_forever()
