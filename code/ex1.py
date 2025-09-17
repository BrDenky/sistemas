# great_grandchild.py
import os
import time

print(f"Padre: PID={os.getpid()}")

pid1 = os.fork()
if pid1 == 0:  # Inside child
    print(f"\nI'm the child: PID = {os.getpid()}")
    print(f"\nParent's:  PID = {os.getppid()}")

    pid2 = os.fork()  # Inside grandchild
    if pid2 == 0:
        print(f"\nGrandchild: PID={os.getpid()}")
        print(f"\nChild's : PID={os.getppid()}")

        pid3 = os.fork()  # Inside great-grandchild
        if pid3 == 0:
            print(f"Great-grandchild: PID={os.getpid()}")
            print(f"Grandchild's: PPID={os.getppid()}")
            time.sleep(30)
        else:
            time.sleep(30)
    else:
        time.sleep(30)      
else:
    time.sleep(30)             
