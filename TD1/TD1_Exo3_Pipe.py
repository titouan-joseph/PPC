
from multiprocessing import Process, Pipe

def child(parent_conn, child_conn):
    while True:
        phrase = child_conn.recv()
        child_conn.send(phrase[::-1])

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(parent_conn, child_conn))
    p.start()

    phrase = input("give me a phrase")

    while phrase.lower() != "end":
        parent_conn.send(phrase)
        print(parent_conn.recv())
        phrase = input("give me a phrase")

    child_coon.close()
    parent_conn.close()
    p.terminate()
    p.join()
