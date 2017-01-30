# from __future__ import absolute_import
# from base import *

import unittest
import os
import tempfile


import glob
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)) + "/../../"))

import cache



__version__ = 1.0
__author__ = 'weldpua2008@gmail.com'

tmp_files=[]


class TestRepoClass(unittest.TestCase):

    def getTempFileName(self, deleted=True):
        f = tempfile.NamedTemporaryFile(delete=deleted, prefix='_tmp')
        config_file_path = f.name
        f.close
        # global tmp_files
        tmp_files.append(config_file_path)
        return config_file_path

    def tearDown(self):        
        # filelist = glob.glob("/tmp/_tmp*")
        # for f in filelist:
        #     os.remove(f)
        # global tmp_files
        for f in tmp_files:
            if os.path.isfile(f):
                os.remove(f)

    def test_dict_by_default(self):
        __cache_store = cache.get_cache_copy()
        self.assertIsInstance(__cache_store, dict)

    def test_set(self):
        cache.flush_cache()

        file_path = self.getTempFileName(deleted=False)
        statbuf = os.stat(file_path)
        access_time = statbuf.st_mtime

        key = 'key'
        value = 'value'
        cache_type = 'cache_type'
        cache.update(key=key, value=value, cache_type=cache_type, file_path=file_path)
        # cache.update(key=None, value=None, cache_type=None, file_path=None)
        __cache_store = cache.get_cache_copy()
        self.assertIsInstance(__cache_store, dict)
        self.assertIn(cache_type, __cache_store)
        self.assertIn(key, __cache_store[cache_type])
        self.assertIn(file_path, __cache_store[cache_type][key])
        self.assertIn('value', __cache_store[cache_type][key][file_path])
        self.assertIn('access_time', __cache_store[cache_type][key][file_path])
        self.assertEqual(value, __cache_store[cache_type][key][file_path]['value'])
        self.assertEqual(access_time, __cache_store[cache_type][key][file_path]['access_time'])
        # test that on change file it's the same value
        with open(file_path, 'a+') as file_content:
            file_content.write("sss")
        self.assertEqual(value, __cache_store[cache_type][key][file_path]['value'])
        self.assertEqual(access_time, __cache_store[cache_type][key][file_path]['access_time'])

        cache.flush_cache()

    def test_set_same_key(self):
        cache.flush_cache()

        file_path = self.getTempFileName(deleted=False)
        statbuf = os.stat(file_path)
        access_time = statbuf.st_mtime

        key = 'key'
        value = 'value'
        cache_type = 'cache_type'
        cache.update(key=key, value=value, cache_type=cache_type, file_path=file_path)

        file_path = self.getTempFileName(deleted=False)
        cache.update(key=key, value=value, cache_type=cache_type, file_path=file_path)
        statbuf = os.stat(file_path)
        access_time_2 = statbuf.st_mtime
        __cache_store = cache.get_cache_copy()
        self.assertEqual(value, __cache_store[cache_type][key][file_path]['value'])
        self.assertEqual(access_time, __cache_store[cache_type][key][file_path]['access_time'])
        # cache.update(key=None, value=None, cache_type=None, file_path=None)
        __cache_store = cache.get_cache_copy()
        # logging.critical("__cache_store: %s" % __cache_store)
        # test that on change file it's the same value
        with open(file_path, 'a+') as file_content:
            file_content.write("sss")
        self.assertEqual(value, __cache_store[cache_type][key][file_path]['value'])
        self.assertEqual(access_time_2, __cache_store[cache_type][key][file_path]['access_time'])
        cache.flush_cache()

    def test_get_exist(self):
        cache.flush_cache()

        file_path = self.getTempFileName(deleted=False)
        # statbuf = os.stat(file_path)
        # access_time = statbuf.st_mtime
        key = 'key'
        value = 'value'
        cache_type = 'cache_type'
        cache.update(key=key, value=value, cache_type=cache_type, file_path=file_path)
        _value = cache.get(key=key, cache_type=cache_type, file_path=file_path)
        self.assertEqual(value, _value)

    def test_get_non_exist(self):
        cache.flush_cache()
        file_path = self.getTempFileName(deleted=False)
        statbuf = os.stat(file_path)
        access_time = statbuf.st_mtime
        key = 'key'
        value = 'value'
        cache_type = 'cache_type'
        # cache.update(key=key, value=value, cache_type=cache_type, file_path=file_path)
        _value = cache.get(key=key, cache_type=cache_type, file_path=file_path)
        self.assertNotEqual(value, _value)

    def test_flush_cache(self):
        cache.flush_cache()

        file_path = self.getTempFileName(deleted=False)
        statbuf = os.stat(file_path)
        access_time = statbuf.st_mtime

        key='key'
        value='value'
        cache_type='cache_type'
        cache.update(key=key, value=value, cache_type=cache_type, file_path=file_path)
        __cache_store = cache.get_cache_copy()
        self.assertIsInstance(__cache_store, dict)
        num = len(__cache_store)
        self.assertGreater(num, 0)

        cache.flush_cache()
        __cache_store = cache.get_cache_copy()
        self.assertIsInstance(__cache_store, dict)
        num = len(__cache_store)
        self.assertLessEqual(num, 0)

        # file_path = self.getTempFileName(deleted=False)
        # cache.update(key=key, value=value, cache_type=cache_type, file_path=file_path)
        # statbuf = os.stat(file_path)
        # access_time_2 = statbuf.st_mtime
        # __cache_store = cache.get_cache_copy()
        # self.assertEqual(value, __cache_store[cache_type][key][file_path]['value'])
        # self.assertEqual(access_time, __cache_store[cache_type][key][file_path]['access_time'])
        # # cache.update(key=None, value=None, cache_type=None, file_path=None)
        # __cache_store = cache.get_cache_copy()
        # # test that on change file it's the same value
        # with open(file_path, 'a+') as file_content:
        #     file_content.write("sss")
        # self.assertEqual(value, __cache_store[cache_type][key][file_path]['value'])
        # self.assertEqual(access_time_2, __cache_store[cache_type][key][file_path]['access_time'])
        # cache.flush_cache()


if __name__ == '__main__':
    unittest.main()
