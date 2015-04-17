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
	
	def test_inster_Efi(self):
		self.assertEqual(self.discreta.insert_Efi([2, 2, 1]), 5)
	
	def test_insert_fr(self):
		self.assertEqual(self.discreta.insert_fr([2, 2, 1], 5), [40.00, 40.00, 20.00])
	
	def test_insert_F(self):
		self.assertEqual(self.discreta.insert_F([2, 2, 1]), [2, 4, 5])
	
	def test_insert_Fr(self):
		self.assertEqual(self.discreta.insert_Fr([40.00, 40.00, 20.00]), [40.00, 80.00, 100.00])
	
	def test_insert_media(self):
		self.assertEqual(self.discreta.insert_media([1, 2, 3], [2, 2, 1]), [2, 4, 3])
	
	def test_insert_Exi_fi(self):
		self.assertEqual(self.discreta.insert_Exi_fi([2, 4, 3]), 9)
	
	def test_insert_moda(self):
		self.assertEqual(self.discreta.insert_moda([17, 18, 19, 20, 21], [3, 18, 17, 8, 4]), [18])
	

if __name__ == '__main__':
	unittest.main()