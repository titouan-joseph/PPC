import time
import random
import multiprocessing


def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


if __name__ == "__main__":
    indexes = [random.randint(10**3, 10**6) for i in range(100)]

    with multiprocessing.Pool(processes=4) as pool:  #Creation d'une pool de 4 processus nomé pool

        print("*** Synchronous call in one process")
        start = time.time()
        result = pool.apply(is_prime, (10,))
        print(result)
        end = time.time()
        print("Time : {}".format(end - start))

        print("*** Asynchronous call in one process")
        start = time.time()
        result = pool.apply_async(is_prime, (10,))
        print(result.get())
        end = time.time()
        print("Time : {}".format(end - start))

        print("*** Synchronous map")
        start = time.time()
        for x in pool.map(is_prime, indexes):
            print(x)
        end = time.time()
        print("Time : {}".format(end - start))

        print("*** Asynchronous map")
        start = time.time()
        for x in pool.map_async(is_prime, indexes).get():
            print(x)
        end = time.time()
        print("Time : {}".format(end - start))
