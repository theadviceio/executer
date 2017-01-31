import datetime
import utils.logs
import time

__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


# pylint: disable=logging-not-lazy
def curtime_to_isoformat():
    """return current time in iso format"""
    try:
        return datetime.datetime.now().isoformat()
    # pylint: disable=broad-except
    except Exception as error:
        utils.logs.critical(
            "Can't datetime.now().isoformat() because '%s' " % error)
        return None


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.start = time.time()
        self.end = time.time()

    def __enter__(self):
        self.start = time.time()
        self.start_all = self.start
        return self

    def reset(self):
        self.start = time.time()

    def get_secs(self):
        self.end = time.time()
        secs = self.end - self.start
        return secs

    def get_msecs(self):
        self.end = time.time()

        msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print ('elapsed time: %f ms' % msecs)
        return msecs

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print ('elapsed time: %f ms' % self.msecs)

        self.secs_all = self.end - self.start_all
        self.msecs_all = self.secs_all * 1000  # millisecs
        if self.verbose:
            print ('elapsed time: %f ms' % self.msecs_all)
