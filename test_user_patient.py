import unittest
import sys
import os


path = os.path.abspath("database")
sys.path.append(path)


from user.Patient import patient_register

class TestValidPass(unittest.TestCase):
	def test_valid_pass(self):
            self.assertRaises(AlreadyExist, patient_register, ' ')

     
     
     
if __name__=='__main__':
	unittest.main()