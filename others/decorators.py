import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = f(*args, **kwargs)
        total = time.time()-start
        print("Time : ", total)
        return rv
    return wrapper


@timer
def test():
    for _ in range(100000):
        pass

@timer
def test2():
    time.sleep(2)

test()
test2()

