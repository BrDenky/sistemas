import os
import time
import sys

#/usr/share/dict/words
with open("/usr/share/dict/words","r") as f:

    pid_f1 = os.fork()

    if pid_f1 == 0: #it means inside the child process
        print("\nI'm the child, PID:",os.getpid())
        for line in f:
            print('reading from child', line, end='')

    elif pid_f1 > 0: #it means inside the parent process
        print("\nI'm the Parent, PID:",os.getpid())
        for line in f:
            print('reading from parent:', line, end='')

    else:
        print("\nFork operation failed")


sys.exit()