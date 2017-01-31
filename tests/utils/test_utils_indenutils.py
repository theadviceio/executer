import sys
import os
import unittest
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)) + "/../../"))

import utils.identutils


class TestTimeUtilsClass(unittest.TestCase):

    def test_gen_uuid_format(self):
        """ test that function return current time in right format """
        data = utils.identutils.gen_uuid()
        refilter = "^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$"
        search = re.findall(refilter, data)
        self.assertEqual(search[0], data)

    def test_gen_uuid_uniq(self):
        """ test that function return current time in right format """
        data = utils.identutils.gen_uuid()
        data1 = utils.identutils.gen_uuid()
        self.assertNotEqual(data, data1)

if __name__ == '__main__':
    unittest.main()
