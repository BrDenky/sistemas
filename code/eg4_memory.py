# memory.py

import os
import time

names = ['maria','juan','lucia']

pid_f1 = os.fork()

if pid_f1 == 0: #it means inside the child process
    print("\nI'm the child, PID:",os.getpid())
    names.append('pedro')
    names.append('ana')
elif pid_f1 > 0: #it means inside the parent process
    print("\nI'm the parent, PID:",os.getpid())
    names.pop()
else:
    print("\nFork operation failed")

print(names)