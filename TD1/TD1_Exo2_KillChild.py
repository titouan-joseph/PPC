import os
import signal
import time
import sys
from multiprocessing import Process


def hander(sig, frmae):
    if sig == signal.SIGUSR1:
        os.kill(childPID, signal.SIGKILL)
        print("Die, soon!")

def child():
    time.sleep(5)
    os.kill(os.getppid(), signal.SIGUSR1)
    while True:
        print("get up dad!")


if __name__ == "__main__":
    signal.signal(signal.SIGUSR1, hander)

    ChildProcess = Process(target=child, args=())
    ChildProcess.start()
    global childPID
    childPID = ChildProcess.pid
    ChildProcess.join()
