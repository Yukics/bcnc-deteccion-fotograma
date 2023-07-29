import logging
import datetime
import os

def setupLogging():

    if not os.path.exists("./logs"):
        os.makedirs("./logs")

    logPath = "./logs"
    logFileName = "output-" + datetime.datetime.now().strftime("%Y%m%d-%H%M")
    logLevel = "DEBUG"

    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()

    fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, logFileName))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
    rootLogger.setLevel(logLevel)