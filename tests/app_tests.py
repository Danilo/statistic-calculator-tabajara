import unittest
from app import data_to_rol, Discreta, Continua

class TestDiscretaClass(unittest.TestCase):
	def setUp(self):
		self.discreta = Discreta()

	def test_data_to_rol(self):
		self.assertEqual(data_to_rol([1, 2, 3, 2, 1]), [1, 1, 2, 2, 3])

	def test_insert_xi(self):
		self.assertEqual(self.discreta.insert_xi([1, 2, 3, 2, 1]), [1, 2, 3])

	def test_insert_fi(self):
		self.assertEqual(self.discreta.insert_fi([1, 2, 3, 2, 1]), [2, 2, 1])

	def test_insert_Efi(self):
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


class TestContinuaClass(unittest.TestCase):
	def setUp(self):
		self.continua = Continua()

	def test_data_to_rol(self):
		self.assertEqual(data_to_rol([1, 2, 3, 2, 1]), [1, 1, 2, 2, 3])

	def test_insert_at(self):
		self.assertEqual(self.continua.insert_at([1000, 1500, 2000, 2100, 2800, 3000, 3900, 4000, 4100, 5000]), 4000)

	def test_insert_fi(self):
		self.assertEqual(self.continua.insert_fi([1, 2, 3, 2, 1]), [2, 2, 1])

	def test_insert_Efi(self):
		self.assertEqual(self.continua.insert_Efi([2, 2, 1]), 5)

	def test_insert_k(self):
		self.assertEqual(self.continua.insert_k([3, 3, 2, 2], 5), 2)

	def test_get_intervalo(self):
		self.assertEqual(self.continua.get_intervalo(4000, 10), [1000, 2265, 3530, 4795])

if __name__ == '__main__':
	unittest.main()
