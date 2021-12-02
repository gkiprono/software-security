
'''
Gabriel Kiprono
logs.py
Sept 23 2021
'''

import logging
import os


log = logging.getLogger()
log.info("Hello, world")


if __name__ == "__main__":
    print("Hello World")
    logging.basicConfig(filename="mlPY.log", filemode="a",format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logging.warning("this will get logged to a file")