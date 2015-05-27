import unittest
from app import data_to_rol, insert_fi, insert_Efi, insert_fr, insert_F, insert_Fr, insert_xi_fi, insert_Exi_fi, Discreta, Continua

class TestCommonFunctions(unittest.TestCase):
	def test_data_to_rol(self):
		data   = [1, 2, 3, 2, 1]
		result = [1, 1, 2, 2, 3]
		self.assertEqual(data_to_rol(data), result)
		data   = [3, 4, 3.5, 5, 3.5, 4, 5, 5.5, 4, 5]
		result = [3.0, 3.5, 3.5, 4.0, 4.0, 4.0, 5.0, 5.0, 5.0, 5.5]
		self.assertEqual(data_to_rol(data), result)
		data   = [18, 26, 21, 24, 26, 18, 19, 21, 18, 21, 24, 26, 28, 26, 21, 18, 19, 21, 21, 20, 21, 22, 18, 19, 21, 22, 18, 19, 21, 19]
		result = [18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 19.0, 19.0, 19.0, 19.0, 19.0, 20.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 22.0, 22.0, 24.0, 24.0, 26.0, 26.0, 26.0, 26.0, 28.0]
		self.assertEqual(data_to_rol(data), result)
		data   = [6, 9, 2, 7, 0, 8, 2, 5, 4, 2, 5, 4, 4, 4, 4, 2, 5, 6, 3, 7, 3, 8, 8, 4, 4, 4, 7, 7, 6, 5, 4, 7, 5, 3, 3, 1, 3, 8, 0, 6, 5, 1, 2, 3, 3, 0, 5, 6, 6, 3]
		result = [0.0, 0.0, 0.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 7.0, 7.0, 8.0, 8.0, 8.0, 8.0, 9.0]
		self.assertEqual(data_to_rol(data), result)
		data   = [111, 90, 121, 105, 122, 61, 128, 112, 128, 93, 108, 138, 88, 110, 112, 112, 97, 128, 102, 125, 87, 119, 104, 116, 96, 114, 107, 113, 80, 113, 123, 95, 115, 70, 115, 101, 114, 127, 92, 103, 78, 118, 100, 115, 116, 98, 119, 72, 125, 109, 79, 139, 75, 109, 123, 124, 108, 125, 116, 83, 94, 106, 117, 82, 122, 99, 124, 84, 91, 130]
		result = [61.0, 70.0, 72.0, 75.0, 78.0, 79.0, 80.0, 82.0, 83.0, 84.0, 87.0, 88.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 108.0, 109.0, 109.0, 110.0, 111.0, 112.0, 112.0, 112.0, 113.0, 113.0, 114.0, 114.0, 115.0, 115.0, 115.0, 116.0, 116.0, 116.0, 117.0, 118.0, 119.0, 119.0, 121.0, 122.0, 122.0, 123.0, 123.0, 124.0, 124.0, 125.0, 125.0, 125.0, 127.0, 128.0, 128.0, 128.0, 130.0, 138.0, 139.0]
		self.assertEqual(data_to_rol(data), result)

	def test_insert_fi(self):
		data   = [1, 2, 3, 2, 1]
		result = [2, 2, 1]
		self.assertEqual(insert_fi(data), result)

	def test_insert_Efi(self):
		data   = [2, 2, 1]
		result = 5
		self.assertEqual(insert_Efi(data), result)

	def test_insert_fr(self):
		data   = [2, 2, 1]
		size   = 5
		result = [40.00, 40.00, 20.00]
		self.assertEqual(insert_fr(data, size), result)

	def test_insert_F(self):
		data   = [2, 2, 1]
		result = [2, 4, 5]
		self.assertEqual(insert_F(data), result)

	def test_insert_Fr(self):
		data   = [40.00, 40.00, 20.00]
		result = [40.00, 80.00, 100.00]
		self.assertEqual(insert_Fr(data), result)

	def test_insert_xi_fi(self):
		data_xi = [1, 2, 3]
		data_fi = [2, 2, 1]
		result  = [2, 4, 3]
		self.assertEqual(insert_xi_fi(data_xi, data_fi), result)

	def test_insert_Exi_fi(self):
		data   = [0]
		result = 0
		self.assertEqual(insert_Exi_fi(data), result)
		data = [2, 4, 3]
		result = 9
		self.assertEqual(insert_Exi_fi(data), result)


class TestDiscretaClass(unittest.TestCase):
	def setUp(self):
		self.discreta = Discreta()

	def test_insert_xi(self):
		self.assertEqual(self.discreta.insert_xi([1, 2, 3, 2, 1]), [1, 2, 3])

	def test_insert_moda(self):
		self.assertEqual(self.discreta.insert_moda([17, 18, 19, 20, 21], [3, 18, 17, 8, 4]), [18])


class TestContinuaClass(unittest.TestCase):
	def setUp(self):
		self.continua = Continua()

	def test_insert_at(self):
		self.assertEqual(self.continua.insert_at([1000, 1500, 2000, 2100, 2800, 3000, 3900, 4000, 4100, 5000]), 4000)

	def test_insert_k(self):
		self.assertEqual(self.continua.insert_k([3, 3, 2, 2], 5), 2)

	def insert_fi_do_intervalo(self):
		data_rol = [61.0, 70.0, 72.0, 75.0, 78.0, 79.0, 80.0, 82.0, 83.0, 84.0, 87.0, 88.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 108.0, 109.0, 109.0, 110.0, 111.0, 112.0, 112.0, 112.0, 113.0, 113.0, 114.0, 114.0, 115.0, 115.0, 115.0, 116.0, 116.0, 116.0, 117.0, 118.0, 119.0, 119.0, 121.0, 122.0, 122.0, 123.0, 123.0, 124.0, 124.0, 125.0, 125.0, 125.0, 127.0, 128.0, 128.0, 128.0, 130.0, 138.0, 139.0]
		data_xi  = [61.0, 71.0, 81.0, 91.0, 101.0, 111.0, 121.0, 131.0, 141.0]
		ic = 10
		result   = [2, 5, 6, 10, 12, 18, 15, 2, 0]
		self.assertEqual(self.continua.insert_fi_do_intervalo(data_rol, data_xi, ic), result)


if __name__ == '__main__':
	unittest.main()
