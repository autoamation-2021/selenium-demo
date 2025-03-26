import logging
import os

class LogGen():

    @staticmethod
    def loggen():
        logging.basicConfig(filename = os.path.abspath(os.curdir)+"\\logs\\automation.log",format = '%(asctime)s:%(levelname)s:%(message)s',datefmt = '%m/%d/%Y %I:%M:%S:%p',filemode = 'a')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

    def log_generator():
        logging.basicConfig(fielename= "",format)    

