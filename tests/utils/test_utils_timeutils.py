import unittest
import sys
import os
import unittest
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)) + "/../../"))

import utils.timeutils


class TestTimeUtilsClass(unittest.TestCase):

    def test_curtime_to_isoformat(self):
        """ test that function return current time in right format """
        data = utils.timeutils.curtime_to_isoformat()
        refilter = "^\d{4}-\d{2}-\d{2}\w{1}\d{2}:\d{2}:\d{2}[.]\d{6}$"
        search = re.findall(refilter, data)
        self.assertEqual(search[0], data)

if __name__ == '__main__':
    unittest.main()
