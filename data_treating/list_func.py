def output_result(result, log=None):
    if log is not None:
        log.debug('got: %r', result)


def add(x, y):
    return x + y


if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')
    p = Pool()
    # p.apply_async(add, (5, 6), callback=partial(output_result, log=log))
    p.apply_async(add, (5, 6), callback=lambda result: output_result(result, log))
    p.close()
    p.join()
