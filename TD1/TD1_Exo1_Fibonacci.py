import time
from multiprocessing import Process

fibanacciList = [0, 1]
def suitefibonacci(nb):
    print(fibanacciList)
    i = 1
    while i < nb:
        fibanacciList.append(fibanacciList[i]+fibanacciList[i-1])
        i += 1

    print(fibanacciList)

if __name__ == "__main__":
    p = Process(target=suitefibonacci, args=(128,))
    p.start()
    p.join()