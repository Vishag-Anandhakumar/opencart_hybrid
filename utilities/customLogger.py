import logging
import os

class LogGeneration():
    @staticmethod
    def logGen():
        path = os.path.abspath(os.curdir)+"\\logs\\automation.log"
        logging.basicConfig(filename=path, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        return logger