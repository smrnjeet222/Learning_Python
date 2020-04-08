import threading
import time

def count(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.01)

for _ in range(2):
    x = threading.Thread(target=count, args=(5,))
    x.start()

print("Done") 