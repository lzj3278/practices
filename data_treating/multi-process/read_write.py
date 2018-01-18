from multiprocessing import Process, Queue
import time


def reader(q):
    while True:
        msg = q.get()
        if msg == 'DONE':
            break


def write(count, q):
    for i in xrange(0, count):
        q.put(i)
    q.put('DONE')


if __name__ == '__main__':
    for count in [10 ** 4, 10 ** 5, 10 ** 6]:
        q = Queue()
        reader_p = Process(target=reader, args=(q,))
        # reader_p.daemon = True
        reader_p.start()
        _start = time.time()
        write(count, q)
        reader_p.join()
        print "Sending %s numbers to Queue() took %s seconds" % (count, (time.time() - _start))
