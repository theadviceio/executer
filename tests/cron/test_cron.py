import unittest
import sys
import os
import signal

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)) + "/../../"))

import cron

__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'

if sys.version_info > (3,0,0):
    basestring = (str, bytes)
    unicode = str


class TimeoutError(Exception):
    pass

test_cron_job_runned_times = 0

def test_cron_job(cron_runned_times=0):
    global test_cron_job_runned_times
    test_cron_job_runned_times = cron_runned_times + 1




class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)


class TestApiCronClass(unittest.TestCase):
    def test_run_job_nonexist_cron(self):
        cron_job= ""
        cron_name = "non-exist"
        with self.assertRaises(KeyError):

            cron.run_job(cron_job, cron_name)

    def test_run_job(self):
        global test_cron_job_runned_times
        cron_name = "exists"
        with timeout(seconds=3):
            cron.add_cron(cron_name=cron_name)


        test_cron_job_runned_times = 0
        with timeout(seconds=5):
            cron.run_job(cron_job=test_cron_job, cron_name=cron_name)
        self.assertEqual(test_cron_job_runned_times, 1)
        test_cron_job_runned_times = 0


    def test_run_cron(self):
        global test_cron_job_runned_times
        cron_name = "test_run_cron"
        with timeout(seconds=3):
            cron.add_cron(cron_name=cron_name)


        test_cron_job_runned_times = 0
        with timeout(seconds=5):
            cron.add_job(cron_job=test_cron_job, cron_name=cron_name)

        with timeout(seconds=5):
            cron.run_cron(cron_name, period=1, num=2)
        self.assertEqual(test_cron_job_runned_times, 2)
        test_cron_job_runned_times = 0


    def test_run_cron_infinity(self):
        global test_cron_job_runned_times
        cron_name = "test_run_cron_infinity"
        with timeout(seconds=3):
            cron.add_cron(cron_name=cron_name)

        test_cron_job_runned_times = 0
        with timeout(seconds=5):
            cron.add_job(cron_job=test_cron_job, cron_name=cron_name)

        with self.assertRaises(TimeoutError):
            with timeout(seconds=4):
                cron.run_cron(cron_name, period=1, num=0)

        self.assertIn(test_cron_job_runned_times, [3, 4, 5])
        test_cron_job_runned_times = 0


if __name__ == '__main__':
    unittest.main()
