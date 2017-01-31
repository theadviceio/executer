#import utils
import logging
# import status.log

__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


def critical(msg="", store_log=True):
    try:
        log(error=msg, logging_type="critical", store_log=store_log)
    except Exception as error:
        # print "Can't log, because %s" % error
        logging.critical("Can't log, because %s" % error)


def debug(msg="", store_log=True):
    try:
        log(error=msg, logging_type="debug", store_log=store_log)
    except Exception as error:
        # print "Can't log, because %s" % error
        logging.critical("Can't log, because %s" % error)


def info(msg="", store_log=True):
    try:
        log(error=msg, logging_type="info", store_log=store_log)
    except Exception as error:
        # print "Can't log, because %s" % error
        logging.critical("Can't log, because %s" % error)


def log(error, logging_type="critical", store_log=True):
    # try:
    #     if store_log:
    #         status.log.add(msg=error, level=logging_type)
    # except Exception as error_add:
    #     logging.critical("<LOG ADD ERROR:status.log.add:%s>" % error_add)

    if logging_type == "debug":
        logging.debug("<DEBUG>%s" % error)
    elif logging_type == "info":
        logging.info("<INFO>%s" % error)
    elif logging_type == "critical":
        logging.critical("<CRITICAL>%s" % error)
    else:
        logging.critical("<UNKNOWN_LOG_LEVEL>%s" % error)