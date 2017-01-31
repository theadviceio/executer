import sys
import os
import unittest
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)) + "/../../"))
import utils.errors

# logname = "/tmp/test.log"
# print("-----------------------------")
# print((" current logs in %s" % logname))
# print("-----------------------------")



__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


def get_temp_filename(deleted=False):
    file = tempfile.NamedTemporaryFile(delete=deleted, prefix='_rde_logtmp')
    new_file_name = file.name
    #file.close
    return new_file_name



class TestUtilsErrorsClass(unittest.TestCase):
    

    def test_get_runtime_error(self):        
        logged_string = "sssssssASdAadDASdasD"
        with self.assertRaises(RuntimeError):
            utils.errors.get_runtime_error(error=logged_string)        

    def test_get_io_error(self):        
        logged_string = "get_io_error_sssssssASdAadDASdasD"
        with self.assertRaises(IOError):
            utils.errors.get_io_error(error=logged_string)        

    def test_get_notimplemented_error(self):
        
        logged_string = "get_notimplemented_error_sssssssASdAadDASdasD"
        with self.assertRaises(NotImplementedError):
            utils.errors.get_notimplemented_error(error=logged_string)
        
    def test_get_transition_error(self):        
        logged_string = "get_transition_error_sssssssASdAadDASdasD"
        with self.assertRaises(utils.errors.TransitionError):
            utils.errors.get_transition_error(error=logged_string)
        
    def test_get_key_error(self):        
        logged_string = "get_key_error_error_sssssssASdAadDASdasD"
        with self.assertRaises(KeyError):
            utils.errors.get_key_error(error=logged_string)
        
    def test_get_type_error(self):
        
        logged_string = "get_type_error_sssssssASdAadDASdasD"
        with self.assertRaises(TypeError):
            utils.errors.get_type_error(error=logged_string)
        
    def test_get_value_error(self):        
        logged_string = "get_value_error_sssssssASdAadDASdasD"
        with self.assertRaises(ValueError):
            utils.errors.get_value_error(error=logged_string)
        

if __name__ == '__main__':
    unittest.main()
