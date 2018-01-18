# -*- coding:utf-8 -*-

import os
import random
import time
from multiprocessing import Process, Queue


def write(q):
    print('process to write {}'.format(os.getpid()))
    for i in ['a', 'b', 'c']:
        print('put {} to queue'.format(i))
        q.put(i)
        time.sleep(random.random())


def read(q):
    print('process to read {}'.format(os.getpid()))
    while True:
        i = q.get()
        print('get {} from queue'.format(i))


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
