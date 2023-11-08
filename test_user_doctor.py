import unittest
import sys
import os


path = os.path.abspath("database")
sys.path.append(path)


from user.Doctor import doctor_register

class TestValidPass(unittest.TestCase):
	def test_valid_pass(self):
            self.assertRaises(AlreadyExist, doctor_register, ' ')

     
     
     
if __name__=='__main__':
	unittest.main()