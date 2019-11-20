import sys
import threading


def fibonacci(n):
    print("Starting thread:", threading.current_thread().name)
    res = [0]
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        res.append(a)
        i += 1
    print(res)
    print("Ending thread:", threading.current_thread().name)


if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)
    index = int(sys.argv[1])
    thread = threading.Thread(target=fibonacci, args=(index,))
    thread.start()
    thread.join()
    print("Ending thread:", threading.current_thread().name)