import time
import random
import threading

N = 5


def mutex():
    return threading.Lock()


chopstick = [mutex() for i in range(N)]


def philosopher(i):
    print("Starting thread:", threading.current_thread().name)
    while True:

        print("{}, est en train de pense".format(i))
        time.sleep(random.randint(0, 10))

        left_stick = i
        right_stick = (i + 1) % N

        min_stick = min(left_stick, right_stick)

        chopstick[min_stick].acquire()
        print("{}, prend le plus petit stick".format(i))

        if min_stick == left_stick:
            chopstick[right_stick].acquire()
        else:
            chopstick[left_stick].acquire()
        print("{}, prend un stick".format(i))

        time.sleep(random.randint(0, 15))
        print("{}, dit: j'ai bien manger".format(i))

        chopstick[left_stick].release()
        chopstick[right_stick].release()
        print("Ending thread:", threading.current_thread().name)


if __name__ == "__main__":


    print("Starting thread:", threading.current_thread().name)

    philosopher_list = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]

    for t in philosopher_list:
        t.start()

    for t in philosopher_list:
        t.join()

    print("Ending thread:", threading.current_thread().name)
