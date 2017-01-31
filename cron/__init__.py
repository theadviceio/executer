import threading
import time
# import logging

__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'

__lock = threading.Lock()
__cron_storage = {}



class NotFoundError(Exception):

    """Raised when an operation attempts a state transition that's not allowed."""

    def __init__(self, message):
        """Attributes:

        _previous -- state at beginning of transition
        _next -- attempted new state
        message -- explanation of why the specific transition is not allowed
        """
        super(NotFoundError, self).__init__(message)
        self.message = message

    def __str__(self):
        return self.message


def add_cron(cron_name):
    global __lock
    global __cron_storage
    with __lock:
        if cron_name not in __cron_storage:
            __cron_storage[cron_name] = {}
            # curr_lock = threading.Lock()
            # __cron_storage[cron_name]["lock"] = curr_lock
            __cron_storage[cron_name]["jobs"] = []
            __cron_storage[cron_name]["cron_runned_times"] = 0
            __cron_storage[cron_name]["cron_failed_times"] = 0


def add_job(cron_job, cron_name):
    global __lock
    global __cron_storage
    with __lock:
        if cron_name not in __cron_storage:
            raise NotFoundError("No such cron name: %s job" % cron_name)
        __cron_storage[cron_name]["jobs"].append(cron_job)


def run_job(cron_job, cron_name):
    """Run any job and increment jobs counters
    :param cron_job: function
    :param cron_name: place to find counters
    :return:
    """
    global __cron_storage
    if cron_name not in __cron_storage:
        raise KeyError("No such cron job")

    try:
        cron_runned_times = 0
        with __lock:
            cron_runned_times = __cron_storage[cron_name]["cron_runned_times"]
        cron_job(cron_runned_times=cron_runned_times)
        with __lock:
            __cron_storage[cron_name]["cron_runned_times"] += 1
    except Exception as error:
        # logging.critical("error %s " % error)
        with __lock:
            __cron_storage[cron_name]["cron_failed_times"] += 1


def run_cron(cron_name, period=1, num=0):
    """Run cron with sleep period and number of times
    :param period:
    :param num: if num > 0 then this cron is limited by number of steps
                else: it's infinite cron
    :return:
    """
    global __lock
    global __cron_storage
    add_cron(cron_name=cron_name)

    if num > 0:
        run_it = 0
        while run_it < num:
            # cron
            jobs = []
            with __lock:
                jobs = __cron_storage[cron_name]["jobs"]
            for cron_job in jobs:
                run_job(cron_job=cron_job, cron_name=cron_name)
            run_it += 1
            time.sleep(period)

    else:
        while True:
        # cron
            jobs = []
            with __lock:
                jobs = __cron_storage[cron_name]["jobs"]
            for cron_job in jobs:
                run_job(cron_job=cron_job, cron_name=cron_name)
            time.sleep(period)
        # sleep
        time.sleep(period)
