import logging

class Logging:

    @staticmethod
    def log():
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        fhandler=logging.FileHandler(".//Logs//OrangeHRM_Logs")
        formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        return logger

