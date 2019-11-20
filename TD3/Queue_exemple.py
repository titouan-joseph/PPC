import threading
from queue import Queue


def worker(queue, data_ready):
    print("Starting thread:", threading.current_thread().name)
    data_ready.wait()
    value = queue.get()
    print("got value:", value)
    print("Ending thread:", threading.current_thread().name)


if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)

    queue = Queue()
    data_ready = threading.Event()

    thread = threading.Thread(target=worker, args=(queue, data_ready))
    thread.start()

    value = input("\n give me some value:")
    queue.put(value)
    data_ready.set()

    thread.join()

    print("Ending thread:", threading.current_thread().name)