# exit.py

import os
import time
import sys

pid_f1 = os.fork()

if pid_f1 == 0: #it means inside the child process
    print("\nI'm the child, PID:",os.getpid())
    time.sleep(2)
    sys.exit("some error")
elif pid_f1 > 0: #it means inside the parent process
    w = os.waitpid(pid_f1,0)
    print("\nI'm the parent, PID:",os.getpid())
else:
    print("\nFork operation failed")