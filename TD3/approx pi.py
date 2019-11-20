import sys
import threading
import random


pointInside = 0

def pi(n):
    print("Starting thread:", threading.current_thread().name)
    global pointInside
    for i in range(n):
        x = -1 + 2 * random.random()
        y = -1 + 2 * random.random()
        if x**2 + y**2 <= 1:
            pointInside += 1
    print("Ending thread:", threading.current_thread().name)

if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)
    points = int(sys.argv[1])
    thread = threading.Thread(target=pi, args=(points,))
    thread.start()
    thread.join()
    print("Approximation de pi : {}".format((4*pointInside)/points))
    print("Ending thread:", threading.current_thread().name)