import unittest
import sys
import os

path = os.path.abspath("database")
sys.path.append(path)


from validations import valid_datetime

class TestValidPass(unittest.TestCase):
	def test_valid_pass(self):
            self.assertRaises(NotExistDateTime, valid_datetime, ' ')

     
     
     
if __name__=='__main__':
	unittest.main()