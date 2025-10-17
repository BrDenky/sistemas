from concurrent.futures import ProcessPoolExecutor, as_completed
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
    # logging.info(f"\tProcess: {p_id} done sleep")
    return(f"Process: {p_id} done sleep {delay} second(s)")

if __name__ == "__main__":
    
    with ProcessPoolExecutor() as executor:
        p1 = executor.submit(work,1)
        p2 = executor.submit(work,1)
        p3 = executor.submit(work,1)
        p4 = executor.submit(work,1)

        #the result() method returns the value of the function
        logging.info(f"Result {p1.result()}")
        logging.info(f"Result {p2.result()}")
        logging.info(f"Result {p3.result()}")
        logging.info(f"Result {p4.result()}")


    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")