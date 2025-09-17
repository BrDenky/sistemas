import os
import time

pid1 = os.fork()
pid2 = os.fork()
pid3 = os.fork()

time.sleep(20)
