import multiprocessing
import time
import os
import logging

t_start = time.perf_counter()

FORMAT = '%(levelname)s - %(asctime)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt='%H:%M:%S')

def work(delay):
    p_id = os.getpid()
    parent_id = os.getppid()
    logging.info(f"\tProcess: {p_id} sleeping for {delay} second(s)")
    time.sleep(delay)
    logging.info(f"\tProcess: {p_id} done sleep")

if __name__ == "__main__":
    processes = []
    for i in range(50):
        p = multiprocessing.Process(target=work,args=(1,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")