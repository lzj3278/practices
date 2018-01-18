# -*- coding:utf-8 -*-
from multiprocessing import Pool

import time


def run(fn):
    time.sleep(1)
    return fn * fn


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]
    start = time.time()
    for i in test_list:
        run(i)
    end = time.time()
    print('顺序执行花费时间{:0.4f}'.format((end - start)))

    start1 = time.time()
    p = Pool(4)
    for i in test_list:
        p.apply_async(run, args=(i,))
    p.close()
    p.join()
    end1 = time.time()
    print('多进程花费时间{:0.4f}'.format((end1 - start1)))
