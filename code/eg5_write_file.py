# write_file.py

import os
import time
import sys

with open("new_file.txt","w") as f:

    pid_f1 = os.fork()

    if pid_f1 == 0: #it means inside the child process
        print("\nI'm the child, PID:",os.getpid())
        for i in range(100):
            c_line = "\t\tchild"+str(i)+"\n"
            print(c_line)
            f.write(c_line)

    elif pid_f1 > 0: #it means inside the parent process
        print("\nI'm the Parent, PID:",os.getpid())
        for i in range(100):
            p_line = "parent"+str(i)+"\n"
            print(p_line)
            f.write(p_line)

    else:
        print("\nFork operation failed")
