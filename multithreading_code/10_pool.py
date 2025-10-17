# from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures.thread import _worker
import threading
import time
import logging
import requests 

t_start = time.perf_counter()

FORMAT = '%(levelname)s - %(asctime)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt='%H:%M:%S')

urls=[
    "https://pbs.twimg.com/media/FYooOeqWQAIwHzW.jpg",
    "https://pbs.twimg.com/media/FYmcCtsWAAE4wSK.jpg",
    "https://pbs.twimg.com/media/FYmcDG9WQAAJXSc.jpg",
    "https://pbs.twimg.com/media/FYRjxjGXkAc5fV5.jpg",
    "https://pbs.twimg.com/media/FYNyijRWQAQSmbQ.jpg",
    "https://pbs.twimg.com/media/FX9HqAHXwAANxPg.jpg",
    "https://pbs.twimg.com/media/FXt9EgmVQAA6j_d.jpg",
    "https://pbs.twimg.com/media/FXpFCEPUsAAwasG.jpg",
    "https://pbs.twimg.com/media/FXk5pKxWYAAwvUf.jpg",
    "https://pbs.twimg.com/media/FXk5p1RXkAEjuOs.jpg",
    "https://pbs.twimg.com/media/FXk5qR4X0AAFDx8.jpg",
    "https://pbs.twimg.com/media/FXk5qzIXoAACkY6.jpg",
    "https://pbs.twimg.com/media/FXgcBWnXkAAKjHA.jpg",
]

def download_url_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[4]
    with open("images/"+img_name,'wb') as img_file:
        img_file.write(img_bytes)
    
    return f"{img_url} was downloaded"

if __name__ == "__main__":
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        for result in executor.map(download_url_image,urls):
            logging.info(result)

    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")