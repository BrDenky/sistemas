from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageFilter
import time
import os
import logging


t_start = time.perf_counter()

FORMAT = '%(levelname)s - %(asctime)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt='%H:%M:%S')

image_names=[
    "FYooOeqWQAIwHzW.jpg",
    "FYmcCtsWAAE4wSK.jpg",
    "FYmcDG9WQAAJXSc.jpg",
    "FYRjxjGXkAc5fV5.jpg",
    "FYNyijRWQAQSmbQ.jpg",
    "FX9HqAHXwAANxPg.jpg",
    "FXt9EgmVQAA6j_d.jpg",
    "FXpFCEPUsAAwasG.jpg",
    "FXk5pKxWYAAwvUf.jpg",
    "FXk5p1RXkAEjuOs.jpg",
    "FXk5qR4X0AAFDx8.jpg",
    "FXk5qzIXoAACkY6.jpg",
    "FXgcBWnXkAAKjHA.jpg",
]

def process_image(img_name):
    img = Image.open(f"images/{img_name}")
    img = img.filter(ImageFilter.GaussianBlur(15))
    new_size = (1200,1200)
    img = img.resize(new_size)
    img.save(f'images_processed/{img_name}')
    
    return f"{img_name} was processed"

if __name__ == "__main__":
    
    with ProcessPoolExecutor() as executor:
        for result in executor.map(process_image,image_names):
            logging.info(result)

    t_finish = time.perf_counter()
    logging.info(f"Finished in {round(t_finish-t_start,0)} second(s)")