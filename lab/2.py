# q2_zombie.py
import os, time

pid = os.fork()
if pid == 0:              # Hijo: termina de inmediato
    os._exit(0)
else:                     # Padre: NO hace wait()
    print(f"[PARENT] PID={os.getpid()} childPID={pid} (no wait)")
    time.sleep(30)        # durante este tiempo el hijo queda <defunct>/Z
