#The Thread class can be extended for tasks that may involve multiple functions and maintain state.
#This can be achieved by extending the Thread object and overriding the run() function. 
#The overridden run() function is then executed when the start() function of the thread is called.

import threading
import logging
import time

t_start = time.perf_counter()

FORMAT = '%(levelname)s - %(asctime)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt='%H:%M:%S')

class CustomThread(threading.Thread):

    def __init__(self, delay):
        # Call the Thread class's init function
       threading.Thread.__init__(self)
       self.delay = delay

    #Override the run
    def run(self):
        t_id = threading.get_ident()
        t_name =  threading.current_thread().getName()
        logging.info(f"\t{t_name} sleeping for {self.delay} second(s)")
        time.sleep(self.delay)
        logging.info(f"\t{t_name} done sleep")


if __name__ == "__main__":
    threads = []
    for i in range(10):
        t = CustomThread(i)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")