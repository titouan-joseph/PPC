import random
import threading
import time


class State:
    THINKING = 1
    HUNGRY = 2
    EATING = 3


N = 5


def mutex():
    return threading.Lock()


state = [State() for i in range(N)]
sem = [threading.Semaphore(0) for i in range(N)]
chopstick = [mutex() for i in range(N)]


def philosopher(i):
    print("Starting thread:", threading.current_thread().name)
    while True:

        print("{} est en train de manger".format(i))
        time.sleep(2)

        with lock:
            state[i]= State.HUNGRY
            print("{} a faim".format(i))
            if (state[(i + N - 1) % N] != State.EATING) and (state[(i + 1) % N] != State.EATING):
                state[i] = State.EATING
                sem[i].release()

        sem[i].acquire()
        print("")



if __name__ == "__main__":

    print("Starting thread:", threading.current_thread().name)

    philosopher_list = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]

    for t in philosopher_list:
        t.start()

    for t in philosopher_list:
        t.join()

    print("Ending thread:", threading.current_thread().name)
