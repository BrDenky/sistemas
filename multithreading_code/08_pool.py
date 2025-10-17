# from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time
import logging

t_start = time.perf_counter()

FORMAT = '%(levelname)s - %(asctime)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt='%H:%M:%S')

def work(delay):
    t_id = threading.get_ident()
    t_name =  threading.current_thread().getName()
    logging.info(f"\t{t_name} sleeping for {delay} second(s)")
    time.sleep(delay)
    # logging.info(f"\t{t_name} done sleep")
    return (f"{t_name} done sleep {delay} second(s)")

if __name__ == "__main__":
    n_threads = 10
    with ThreadPoolExecutor(max_workers=n_threads) as executor:

        # items = range(10)
        items = reversed(range(10))

        # call a function on each item in a list and process results
        for result in executor.map(work, items):
            #the result are returned in the order that they wre started
            logging.info(result)
        
        
    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")