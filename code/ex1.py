import os
import time

pid1 = os.fork()

if pid1 == 0:  # primer hijo
    print(f"Soy el primer hijo, PID={os.getpid()}, padre={os.getppid()}")

    pid2 = os.fork()
    if pid2 == 0:  # segundo hijo (nieto)
        print(f"Soy el segundo hijo (nieto), PID={os.getpid()}, padre={os.getppid()}")

        pid3 = os.fork()
        if pid3 == 0:  # tercer hijo (bisnieto)
            print(f"Soy el tercer hijo (bisnieto), PID={os.getpid()}, padre={os.getppid()}")
            time.sleep(20)
        else:
            time.sleep(20)
    else:
        time.sleep(20)
else:
    print(f"Soy el padre, PID={os.getpid()}, hijo={pid1}")
    time.sleep(20)
