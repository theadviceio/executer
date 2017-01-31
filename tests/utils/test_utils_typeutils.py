# -*- coding: utf-8 -*-
import sys
import os
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)) + "/../../"))
import utils.typeutils

__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


class TestUtilsTypeClass(unittest.TestCase):

    def tearDown(self):
        import glob
        import os
        filelist = glob.glob("/tmp/_rde_tmp*")
        for f in filelist:
            os.remove(f)

    def test_is_numeric_int(self):
        self.assertTrue(utils.typeutils.is_numeric(test_variable=1))

    def test_is_numeric_float(self):
        self.assertTrue(utils.typeutils.is_numeric(test_variable=1.1))

    def test_is_numeric_long(self):
        mylong_integer=(65536*65536*6666666666666666666666666)
        self.assertTrue(utils.typeutils.is_numeric(test_variable=mylong_integer))

    def test_is_string_string_hew(self):
        self.assertTrue(utils.typeutils.is_string(test_variable="לךגכשדלךגכלךגכד"))

    def test_is_string_string_rus(self):
        self.assertTrue(utils.typeutils.is_string(test_variable="символы — это символы, имеющ"))

    def test_is_string_string_asci(self):
        self.assertTrue(utils.typeutils.is_string(test_variable="asci12"))

    def test_is_string_string_asci_genarated(self):
        char_id = 0
        while char_id <256:
            asci_char = chr(char_id)
            # print asci_char
            self.assertTrue(utils.typeutils.is_string(test_variable=asci_char))
            char_id += 1

    def test_typeerror_on_not_string_notstaring_dict(self):
        with self.assertRaises(TypeError):
            utils.typeutils.typeerror_on_not_string(test_variable={})

    def test_typeerror_on_not_string_notstaring_none(self):
        with self.assertRaises(TypeError):
            utils.typeutils.typeerror_on_not_string(test_variable=None)

    def test_typeerror_on_not_string_notstaring_list(self):
        with self.assertRaises(TypeError):
            utils.typeutils.typeerror_on_not_string(test_variable=list)

    def test_typeerror_on_not_string_notstaring_rus(self):
        utils.typeutils.typeerror_on_not_string(test_variable="символы — это символы, имеющ")

    def test_typeerror_on_not_string_notstaring_heb(self):
        utils.typeutils.typeerror_on_not_string(test_variable="ךגכשדלךגכלךגכד")

    def test_typeerror_on_not_string_notstaring_asci(self):
        char_id = 0
        while char_id <256:
            asci_char = chr(char_id)
            # print asci_char
            utils.typeutils.typeerror_on_not_string(test_variable=asci_char)
            char_id += 1

    def test_is_none_return_list_none(self):
        data = utils.typeutils.is_none_return_list(test_variable=None)
        self.assertIsInstance(data, list)

    def test_is_none_return_list(self):
        test_data = [{}, [], dict, "No", NotImplementedError, False, True]
        for _data in test_data:
            data = utils.typeutils.is_none_return_list(test_variable=_data)
            self.assertEqual(data, _data)

    def test_is_none_return_dict_none(self):
        data = utils.typeutils.is_none_return_dict(test_variable=None)
        self.assertIsInstance(data, dict)

    def test_is_none_return_dict(self):
        test_data = [{}, [], dict, "No", NotImplementedError, False, True]
        for _data in test_data:
            data = utils.typeutils.is_none_return_dict(test_variable=_data)
            self.assertEqual(data, _data)

    def test_is_none_return_hosts_none(self):
        data = utils.typeutils.is_none_return_hosts(hosts=None)
        self.assertIsInstance(data, list)
        self.assertEqual(data, ['127.0.0.1'])

    def test_is_none_return_hosts(self):
        test_data = [{}, [], dict, "No", NotImplementedError, False, True]
        for _data in test_data:
            data = utils.typeutils.is_none_return_hosts(hosts=_data)
            self.assertEqual(data, _data)

    def test_get_from_kwargs_or_none_wrong_kwargs(self):
        test_data = [[], dict, "No", NotImplementedError, False, True]
        key = "somekey"
        for _data in test_data:
            result = utils.typeutils.get_from_kwargs_or_none(key=None, kwargs=_data)
            self.assertIs(result, None)
            result = utils.typeutils.get_from_kwargs_or_none(key=key, kwargs=_data)
            self.assertIs(result, None)

    def test_get_from_kwargs_or_none_wrong_kwargs_dict_without_key(self):
        key = "somekey"
        test_data = [{}, {"not_some_key": ""}]

        for _data in test_data:
            result = utils.typeutils.get_from_kwargs_or_none(key=key, kwargs=_data)
            self.assertIs(result, None)

    def test_get_from_kwargs_or_none_wrong_kwargs_dict_with_key(self):
        key = "somekey"
        test_data = ["", False, {}, [], NotImplementedError]
        for value in test_data:
            test_data = {key: value}
            result = utils.typeutils.get_from_kwargs_or_none(key=key, kwargs=test_data)
            self.assertIs(result, value)


    def test_to_list(self):
        key = "somekey"
        test_data = [{}, {"not_some_key": ""}, None, NotImplementedError]
        for value in test_data:

            result = utils.typeutils.to_list(value)
            self.assertNotIsInstance(value, list)
            print (result)
            self.assertIsInstance(result, list)
if __name__ == '__main__':
    unittest.main()
