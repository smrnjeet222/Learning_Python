import socket
import threading
from queue import Queue

target = '127.0.0.1'
queue = Queue()
open_ports = []


def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except Exception:
        return False


def fill_queue(port_lst):
    for port in port_lst:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print(f"Port: {port}")
            open_ports.append(port)


port_lst = range(1, 1024)
fill_queue(port_lst)

thread_lst = []

for t in range(1000):
    thread = threading.Thread(target=worker)
    thread_lst.append(thread)

for thread in thread_lst:
    thread.start()

for thread in thread_lst:
    thread.join()

print(f"Open ports are: {open_ports}")
