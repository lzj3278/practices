# -*- coding:utf-8 -*-

from SocketServer import StreamRequestHandler, ThreadingTCPServer
from time import ctime


class My_Hander(StreamRequestHandler):
    def handle(self):
        print('connected from ', self.client_address)
        self.wfile.write('[{}] {}'.format(ctime(), self.rfile.readline()))


if __name__ == '__main__':
    s = ThreadingTCPServer(('', 20001), My_Hander)
    s.serve_forever()
