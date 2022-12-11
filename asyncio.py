import time
import threading
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)

executor.submit()


def myTaask():
    print(f' hello world: {threading.current_thread()}')


myThread = threading.Thread(target=myTaask)

myThread.start()
