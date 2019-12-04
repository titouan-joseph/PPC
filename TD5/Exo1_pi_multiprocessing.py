import sys
import multiprocessing
import random

pointInside = multiprocessing.Value('d', 0.0)


def pi(n, lock):
    print("Starting thread:", multiprocessing.current_process().name)
    global pointInside
    for i in range(n):
        x = -1 + 2 * random.random()
        y = -1 + 2 * random.random()
        if x ** 2 + y ** 2 <= 1:
            with lock:
                pointInside.value += 1

    print("Ending thread:", multiprocessing.current_process().name)


if __name__ == "__main__":
    print("Starting thread:", multiprocessing.current_process().name)
    points = int(sys.argv[1])
    nProcess = 100
    lock = multiprocessing.Lock()

    process = [multiprocessing.Process(target=pi, args=(points, lock)) for i in range(nProcess)]

    for p in process:
        p.start()

    for p in process:
        p.join()

    print("Approximation de pi : {}".format((4 * pointInside.value) / (nProcess * points)))
    print("Ending thread:", multiprocessing.current_process().name)
