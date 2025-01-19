import logging ## logging package is imported here, this comes inbuilt with python


def test_loggingDemo(): ## logging method defined here
    logger = logging.getLogger(__name__) ## __name__ is givem to capture the file name of the test execution

    fileHandler = logging.FileHandler('logfile.log') ## here log file name has been passed
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")##log format has been defined here
    fileHandler.setFormatter(formatter) ## log format and file name has been attached in one object

    logger.addHandler(fileHandler)  #filehandler object has been attached with our logger object

    logger.setLevel(logging.CRITICAL) ## level of log has been set here so only critical and above critical logs will be saved
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")

## above are all level of logs which goes in top to bottom heirarchy only,


