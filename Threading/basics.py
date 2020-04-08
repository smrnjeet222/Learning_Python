import threading
import time

def foo():
    print("ran")
    time.sleep(1)
    print("done")

x = threading.Thread(target=foo)
x.start()
print(threading.activeCount())
