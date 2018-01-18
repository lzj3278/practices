# -*- coding:utf-8 -*-

from multiprocessing import Pool
import os, time


def getFile(path):
    file_list = []
    for root, dirs, files in list(os.walk(path)):
        for i in files:
            # if i.endswith('py') or i.endswith('csv'):
            file_list.append(root + '\\' + i)
    return file_list


def openfile(filepath):
    with open(filepath) as f:
        content = f.readlines()
    lines = len(content)
    word_num = 0
    for i in content:
        word_num += len(i.strip('\n'))
    return lines, word_num, filepath


if __name__ == '__main__':
    start = time.time()
    filepath = 'E:/www/data_treating'
    file_list = getFile(filepath)
    p = Pool()
    resultlist = p.map(openfile, file_list)
    p.close()
    p.join()
    end = time.time()
    print resultlist
    print '{:0.2f}'.format(end - start)
