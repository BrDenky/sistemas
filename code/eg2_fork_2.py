
import os
import time

# first child
pid_f1 = os.fork()

# - second child
# - The first child also creates 
# a child (parent's grandchild)
pid_f2 = os.fork()

if pid_f1 > 0 and pid_f2 > 0:
    print("\nI'm the Parent, PID:",os.getpid())
    print("\tChild's PID:",pid_f1)
    print("\tChild's PID:",pid_f2)
elif pid_f1 == 0 and pid_f2 > 0:
    print("\nI'm the first child, PID:",os.getpid())
    print("\tParent's PID:",os.getppid())
elif pid_f2 == 0 and pid_f1 >0:
    print("\nI'm the second child, PID:",os.getpid())
    print("\tParent's PID:",os.getppid())
else:
    print("\nI'm the grandchild, PID:",os.getpid())
    print("\tParent's PID:",os.getppid())

time.sleep(20)
