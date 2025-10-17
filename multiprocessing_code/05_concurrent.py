from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import os
import logging
from unittest import result

t_start = time.perf_counter()

FORMAT = '%(levelname)s - %(asctime)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt='%H:%M:%S')

def work(delay):
    p_id = os.getpid()
    parent_id = os.getppid()
    logging.info(f"\tProcess: {p_id} sleeping for {delay} second(s)")
    time.sleep(delay)
    # logging.info(f"\tProcess: {p_id} done sleep")
    return(f"Process: {p_id} done sleep {delay} second(s)")

if __name__ == "__main__":
    
    with ProcessPoolExecutor() as executor:
        results = []
        for i in reversed(range(10)):
            p = executor.submit(work,i)
            results.append(p)
        
        # as_completed prints the results in the order the processes are completed
        for f in as_completed(results):
            logging.info(f"{f.result()}")

    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")