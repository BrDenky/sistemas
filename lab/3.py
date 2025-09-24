# q3_orphan.py
import os, time

pid = os.fork()
if pid == 0:                     # Hijo vive más tiempo
    time.sleep(5)
    print(f"[CHILD ] PID={os.getpid()} new PPID={os.getppid()}")  # debería ser 1 (init/systemd)
else:                            # Padre muere primero
    os._exit(0)
