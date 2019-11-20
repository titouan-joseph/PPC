import threading
from queue import Queue
import statistics
import sys


def calcul(fonction, data_ready):
    print("Starting thread:", threading.current_thread().name)
    data_ready.wait()
    data = queue.get()
    print(fonction.__name__ + " : " + str(fonction(data)))
    print("Ending thread:", threading.current_thread().name)


if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)

    queue = Queue()
    data_ready = threading.Event()

    data = []
    n = input("entrer liste de nb")
    input_str = n.split()
    for s in input_str:
        try:
            x = float(s)
        except ValueError:
            print("bad number", s)
        else:
            data.append(x)

    queue.put(data)
    data_ready.set()

    for f in [min, max, statistics.median, statistics.mean, statistics.stdev]:
        queue.put(data)
        thread = threading.Thread(target=calcul, args=(f, data_ready))
        thread.start()
        thread.join()

    print("Ending thread:", threading.current_thread().name)
