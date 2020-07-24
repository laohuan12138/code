import sys
import queue
import threading
from subprocess import Popen, PIPE


class DoRun(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            ip = self._queue.get()
            check_ping  = Popen("ping {0} \n".format(ip),stdin=PIPE,stdout=PIPE,shell=True)
            data = check_ping.stdout.read()
            if str.encode("ttl") in data:
                sys.stdout.write(ip + 'is UP \n')


def main():
    threads = []
    threads_count = 10
    queu = queue.Queue()

    for i in range(1,10):
        queu.put('39.108.146.' + str(i))

    for i in range(threads_count):
        threads.append(DoRun(queu))

    for i in threads:
        i.start()

    for i in threads:
        i.join()


if __name__ == '__main__':
    main()