import sys
import random
import statistics
import threading
from queue import Queue

def worker(task_queue, data, data_ready):
    print("Starting thread:", threading.current_thread().name)
    data_ready.wait()
    function = task_queue.get()
    res = function(data)
    print(function.__name__, "(", data, ")", res)
    print("Ending thread:", threading.current_thread().name)

if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)

    data = []
    tasks = [min, max, statistics.median, statistics.mean, statistics.stdev]

    task_queue = Queue()
    for t in tasks:
        task_queue.put(t)

    data_ready = threading.Event()

    threads = [threading.Thread(target=worker, args=(task, data, data_ready)) for task in tasks]

    for t in threads:
        t.start()

    print("enter values, ctrl+d to end")
    input_str = sys.stdin.read().split()
    for s in input_str:
        try:
            x = float(s)
        except ValueError:
            print("bad number", s)
        else:
            data.append(x)