import unittest
import sys
import os
import psycopg2

path = os.path.abspath("database")
sys.path.append(path)


from connect_to_db import Database

class TestValidPass(unittest.TestCase):
	def test_valid_pass(self):
            self.assertRaises(psycopg2.DatabaseError, Database.__enter__(self), ' ')

     
     
     
if __name__=='__main__':
	unittest.main()