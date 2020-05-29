import time
import logging
from functools import wraps 

def myLogger(f):
    logging.basicConfig(filename='{}.log'.format(f.__name__), level=logging.INFO)
    @wraps(f)
    def wrapper(*args, **kwargs):
        logging.info('{} ran with args: {} , and kwargs:{}'.format(f.__name__, args, kwargs))
        return f(*args, **kwargs)
    return wrapper


def myTimer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = f(*args, **kwargs)
        total = time.time()-start
        print("{}-> Time : {}".format(f.__name__, total))
        return rv
    return wrapper


@myLogger
@myTimer
def test(z:int):
    print("Printing Test: ")
    time.sleep(z)
    

@myLogger
@myTimer
def test2(z:int):
    print("Printing Test 2: ")
    for _ in range(z*100000):
        pass

test(2)

test2(6)
