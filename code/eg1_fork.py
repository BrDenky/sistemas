import os
import time

pid_f1 = os.fork()

if pid_f1 == 0: #it means inside the child process
    print("\nI'm the child, PID:",os.getpid())
    print("\tParent's PID:",os.getppid())
elif pid_f1 > 0: #it means inside the parent process
    print('hello world')
    print("\nI'm the parent, PID:",os.getpid())
    print("\tChild's PID:",pid_f1)
else:
    print("\nFork operation failed")

time.sleep(30)

