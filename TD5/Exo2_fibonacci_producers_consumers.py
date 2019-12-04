import array
from multiprocessing import Process, Value, Array, Semaphore, RLock, current_process

MEMORY_SIZE = 100
consFlag = True

def fibonacci_pro(n, buffer , full, empty, mutex):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        empty.acquire()
        with mutex:
            buffer[p] = a
            print(current_process().name, "produces:",a ,'in:', p, flush=True)
            p = (p+1)% MEMORY_SIZE
            i += 1
            full.release()

def fibonacci_cons(buffer, full, empty, mutex):
    i =0
    while consFlag:
        full.acquire()
        with mutex:
            res = buffer[i]
            print(current_process().name, "consumes:", res, "from:", i, flush=True)
            i = (i+1)%MEMORY_SIZE
            empty.release()


if __name__ == "__main__":

    buffer = array.array('l', range(MEMORY_SIZE))
    full = Semaphore(0)
    empty = Semaphore(MEMORY_SIZE)
    mutex = RLock()

    cons = Process(target=fibonacci_cons() args=(buffer))


