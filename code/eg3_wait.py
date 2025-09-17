
import os
import time

pid_f1 = os.fork()

if pid_f1 == 0: #it means inside the child process
    print("\nI'm the child, PID:",os.getpid())
    print("\tParent's PID:",os.getppid())
    time.sleep(10)
elif pid_f1 > 0: #it means inside the parent process
    w = os.waitpid(pid_f1,0)
    print("\nI'm the parent, PID:",os.getpid())
    print("\tChild's PID:",pid_f1)
    print("\tChild's PID:",w[0],"Child's status code:",w[1])
else:
    print("\nFork operation failed")