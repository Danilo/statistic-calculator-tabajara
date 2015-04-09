import unittest
from app import data_to_rol, Discreta

class TestDiscretaClass(unittest.TestCase):
	def setUp(self):
		self.discreta = Discreta()
	
	def test_data_to_rol(self):
		self.assertEqual(data_to_rol([1, 2, 3, 2, 1]), [1, 1, 2, 2, 3])
	
	def test_insert_xi(self):
		self.assertEqual(self.discreta.insert_xi([1, 2, 3, 2, 1]), [1, 2, 3])
	
	def test_insert_fi(self):
		self.assertEqual(self.discreta.insert_fi([1, 2, 3, 2, 1]), [2, 2, 1])
	

if __name__ == '__main__':
	unittest.main()