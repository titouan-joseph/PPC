import random
import concurrent.futures


def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return (n, a)


if __name__ == "__main__":
    indexes = [random.randint(0, 100) for i in range(10)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        print("Results returned via asynchronous map:")
        for result in executor.map(fibonacci, indexes):
            print(result)

        print("Results returned as Future objects as they complete:")
        futures = [executor.submit(fibonacci, index) for index in indexes]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())