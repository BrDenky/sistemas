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
    logging.info(f"\t{t_name} done sleep")

if __name__ == "__main__":
    work(5) #run once
    work(1) #run twice
    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")