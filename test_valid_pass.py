import unittest
import sys
import os

path = os.path.abspath("database")
sys.path.append(path)


from validations import valid_pass

class TestValidPass(unittest.TestCase):
	def test_valid_pass(self):
            self.assertRaises(InvalidPassword, valid_pass, 'abc')

     
     
     
if __name__=='__main__':
	unittest.main()