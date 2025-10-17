from concurrent.futures import ThreadPoolExecutor
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
    return f"{t_name} done sleep {delay} second(s)"

if __name__ == "__main__":
    n_threads = 4
    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        # submit() function takes the target function name and any arguments and returns a Future object.
        # The Future object can be used to query the status of the task (e.g. done(), running(), or cancelled()) 
        # and can be used to get the result or exception raised by the task once completed

        #submit(fn, /, *args, **kwargs)
        t1 = executor.submit(work,3)
        t2 = executor.submit(work,3)
        t3 = executor.submit(work,3)
        t4 = executor.submit(work,5)

        #the result() method returns the value of the function
        logging.info(f"Result {t1.result()}")
        logging.info(f"Result {t2.result()}")
        logging.info(f"Result {t3.result()}")
        logging.info(f"Result {t4.result()}")

        # shutdown is called automatically
        # executor.shutdown()

    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")