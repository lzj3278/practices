# -*- coding:utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM

while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('127.0.0.1', 20001))
    data = raw_input('> ')
    if not data:
        break
    s.send('{}\r\n'.format(data))
    data = s.recv(8192)
    if not data:
        break
    print(data.strip())
    s.close()
