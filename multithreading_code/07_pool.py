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

        results = []
        for i in reversed(range (10)):
            t = executor.submit(work,i)
            results.append(t)

        for f in as_completed(results):
            logging.info(f"{f.result()}")
        
        
    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")