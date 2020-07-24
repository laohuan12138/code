import _thread
import time
from subprocess import Popen, PIPE
import sys

def ping_check(ip):
    check = Popen("ping {0} -c 2 \n".format(ip),stdin=PIPE,stdout=PIPE,shell=True)
    data = check.stdout.read()
    if str.encode("ttl") in data:
        sys.stdout.write('%s is UP \n' % ip)




if __name__ == '__main__':
    start = time.time()
    for i in range(1,255):
        ip = '39.108.146.' + str(i)
        _thread.start_new_thread(ping_check,(ip,))
        time.sleep(0.1)
    end = time.time()
    print("用时 %.2f秒" % (end-start))