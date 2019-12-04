from multiprocessing import Process, Value, Array

MEMORY_SIZE = 100


def fibonacci(n, mem):
    mem[0] = 0
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        mem[i + 1] = a
        i += 1

    if i + 1 < MEMORY_SIZE:
        mem[i + 1] = -1


if __name__ == "__main__":

    index = int(input("index please"))
    shared_memory = Array('i', MEMORY_SIZE)

    child = Process(target=fibonacci, args=(index, shared_memory))
    child.start()
    child.join()

    for x in shared_memory[:]:
        if x == -1:
            break
        print(x, end=" ")
    print()
