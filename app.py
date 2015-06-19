import os, math
from flask import Flask, request, render_template
app = Flask(__name__)
#discreta
# 3 4 3.5 5 3.5 4 5 5.5 4 5
# 18 26 21 24 26 18 19 21 18 21 24 26 28 26 21 18 19 21 21 20 21 22 18 19 21 22 18 19 21 19

#continua
# 111 90 121 105 122 61 128 112 128 93 108 138 88 110 112 112 97 128 102 125 87 119 104 116 96 114 107 113 80 113 123 95 115 70 115 101 114 127 92 103 78 118 100 115 116 98 119 72 125 109 79 139 75 109 123 124 108 125 116 83 94 106 117 82 122 99 124 84 91 130
# 28 06 17 48 63 47 27 21 03 07 12 39 50 54 33 45 15 24 01 07 36 53 46 27 05 10 32 50 52 11 42 22 03 17 34 56 25 02 30 10 33 01 49 13 16 08 31 21 06 09 02 11 32 25 00 55 23 41 29 04 51 01 06 31 05 05 11 04 10 26 12 06 16 08 02 04 28

#desvio padrao
# 1000 3000 2000 5000
# 12 11 10 9 8.5 11.5

#distribuicao normal
# media 300
# desvio padrao 20

#distribuicao binomial
# p = 0.4 q = 0.6 n = 10 k = 10 total 0.0001 0.01%
# p = 0.75 q = 0.25 n = 80 k = 12
# Media 60.000000 - Variancia 15.000000 - Desvio 3.872983

table = {
0.00 : 0.0000, 0.01 : 0.0040, 0.02 : 0.0080, 0.03 : 0.0120, 0.04 : 0.0160, 0.05 : 0.0199, 0.06 : 0.0239, 0.07 : 0.0279, 0.08 : 0.0319, 0.09 : 0.0359,
0.10 : 0.0398, 0.11 : 0.0438, 0.12 : 0.0478, 0.13 : 0.0517, 0.14 : 0.0557, 0.15 : 0.0596, 0.16 : 0.0636, 0.17 : 0.0675, 0.18 : 0.0714, 0.19 : 0.0753,
0.20 : 0.0793, 0.21 : 0.0832, 0.22 : 0.0871, 0.23 : 0.0910, 0.24 : 0.0948, 0.25 : 0.0987, 0.26 : 0.1026, 0.27 : 0.1064, 0.28 : 0.1103, 0.29 : 0.1141,
0.30 : 0.1179, 0.31 : 0.1217, 0.32 : 0.1255, 0.33 : 0.1293, 0.34 : 0.1331, 0.35 : 0.1368, 0.36 : 0.1406, 0.37 : 0.1443, 0.38 : 0.1480, 0.39 : 0.1517,
0.40 : 0.1554, 0.41 : 0.1591, 0.42 : 0.1628, 0.43 : 0.1664, 0.44 : 0.1700, 0.45 : 0.1736, 0.46 : 0.1772, 0.47 : 0.1808, 0.48 : 0.1844, 0.49 : 0.1879,
0.50 : 0.1915, 0.51 : 0.1950, 0.52 : 0.1985, 0.53 : 0.2019, 0.54 : 0.2054, 0.55 : 0.2088, 0.56 : 0.2123, 0.57 : 0.2157, 0.58 : 0.2190, 0.59 : 0.2224,
0.60 : 0.2257, 0.61 : 0.2291, 0.62 : 0.2324, 0.63 : 0.2357, 0.64 : 0.2389, 0.65 : 0.2422, 0.66 : 0.2454, 0.67 : 0.2486, 0.68 : 0.2517, 0.69 : 0.2549,
0.70 : 0.2580, 0.71 : 0.2611, 0.72 : 0.2642, 0.73 : 0.2673, 0.74 : 0.2704, 0.75 : 0.2734, 0.76 : 0.2764, 0.77 : 0.2794, 0.78 : 0.2823, 0.79 : 0.2852,
0.80 : 0.2881, 0.81 : 0.2910, 0.82 : 0.2939, 0.83 : 0.2967, 0.84 : 0.2995, 0.85 : 0.3023, 0.86 : 0.3051, 0.87 : 0.3078, 0.88 : 0.3106, 0.89 : 0.3133,
0.90 : 0.3159, 0.91 : 0.3186, 0.92 : 0.3212, 0.93 : 0.3238, 0.94 : 0.3264, 0.95 : 0.3289, 0.96 : 0.3315, 0.97 : 0.3340, 0.98 : 0.3365, 0.99 : 0.3389,
1.00 : 0.3413, 1.01 : 0.3438, 1.02 : 0.3461, 1.03 : 0.3485, 1.04 : 0.3508, 1.05 : 0.3531, 1.06 : 0.3554, 1.07 : 0.3577, 1.08 : 0.3599, 1.09 : 0.3621,
1.10 : 0.3643, 1.11 : 0.3665, 1.12 : 0.3686, 1.13 : 0.3708, 1.14 : 0.3729, 1.15 : 0.3749, 1.16 : 0.3770, 1.17 : 0.3790, 1.18 : 0.3810, 1.19 : 0.3830,
1.20 : 0.3849, 1.21 : 0.3869, 1.22 : 0.3888, 1.23 : 0.3907, 1.24 : 0.3925, 1.25 : 0.3944, 1.26 : 0.3962, 1.27 : 0.3980, 1.28 : 0.3997, 1.29 : 0.4015,
1.30 : 0.4032, 1.31 : 0.4049, 1.32 : 0.4066, 1.33 : 0.4082, 1.34 : 0.4099, 1.35 : 0.4115, 1.36 : 0.4131, 1.37 : 0.4147, 1.38 : 0.4162, 1.39 : 0.4177,
1.40 : 0.4192, 1.41 : 0.4207, 1.42 : 0.4222, 1.43 : 0.4236, 1.44 : 0.4251, 1.45 : 0.4265, 1.46 : 0.4279, 1.47 : 0.4292, 1.48 : 0.4306, 1.49 : 0.4319,
1.50 : 0.4332, 1.51 : 0.4345, 1.52 : 0.4357, 1.53 : 0.4370, 1.54 : 0.4382, 1.55 : 0.4394, 1.56 : 0.4406, 1.57 : 0.4418, 1.58 : 0.4429, 1.59 : 0.4441,
1.60 : 0.4452, 1.61 : 0.4463, 1.62 : 0.4474, 1.63 : 0.4484, 1.64 : 0.4495, 1.65 : 0.4505, 1.66 : 0.4515, 1.67 : 0.4525, 1.68 : 0.4535, 1.69 : 0.4545,
1.70 : 0.4554, 1.71 : 0.4564, 1.72 : 0.4573, 1.73 : 0.4582, 1.74 : 0.4591, 1.75 : 0.4599, 1.76 : 0.4608, 1.77 : 0.4616, 1.78 : 0.4625, 1.79 : 0.4633,
1.80 : 0.4641, 1.81 : 0.4649, 1.82 : 0.4656, 1.83 : 0.4664, 1.84 : 0.4671, 1.85 : 0.4678, 1.86 : 0.4686, 1.87 : 0.4693, 1.88 : 0.4699, 1.89 : 0.4706,
1.90 : 0.4713, 1.91 : 0.4719, 1.92 : 0.4726, 1.93 : 0.4732, 1.94 : 0.4738, 1.95 : 0.4744, 1.96 : 0.4750, 1.97 : 0.4756, 1.98 : 0.4761, 1.99 : 0.4767,
2.00 : 0.4772, 2.01 : 0.0040, 2.02 : 0.4783, 2.03 : 0.4788, 2.04 : 0.4793, 2.05 : 0.4798, 2.06 : 0.4803, 2.07 : 0.4808, 2.08 : 0.4812, 2.09 : 0.4817,
2.10 : 0.4821, 2.11 : 0.4778, 2.12 : 0.4830, 2.13 : 0.4834, 2.14 : 0.4838, 2.15 : 0.4842, 2.16 : 0.4846, 2.17 : 0.4850, 2.18 : 0.4854, 2.19 : 0.4857,
2.20 : 0.4861, 2.21 : 0.4864, 2.22 : 0.4868, 2.23 : 0.4871, 2.24 : 0.4875, 2.25 : 0.4878, 2.26 : 0.4881, 2.27 : 0.4884, 2.28 : 0.4887, 2.29 : 0.4890,
2.30 : 0.4893, 2.31 : 0.4896, 2.32 : 0.4898, 2.33 : 0.4901, 2.34 : 0.4904, 2.35 : 0.4906, 2.36 : 0.4909, 2.37 : 0.4911, 2.38 : 0.4913, 2.39 : 0.4916,
2.40 : 0.4918, 2.41 : 0.4920, 2.42 : 0.4922, 2.43 : 0.4925, 2.44 : 0.4927, 2.45 : 0.4929, 2.46 : 0.4931, 2.47 : 0.4932, 2.48 : 0.4934, 2.49 : 0.4936,
2.50 : 0.4938, 2.51 : 0.4940, 2.52 : 0.4941, 2.53 : 0.4943, 2.54 : 0.4945, 2.55 : 0.4946, 2.56 : 0.4948, 2.57 : 0.4949, 2.58 : 0.4951, 2.59 : 0.4952,
2.60 : 0.4953, 2.61 : 0.4955, 2.62 : 0.4956, 2.63 : 0.4957, 2.64 : 0.4959, 2.65 : 0.4960, 2.66 : 0.4961, 2.67 : 0.4962, 2.68 : 0.4963, 2.69 : 0.4964,
2.70 : 0.4965, 2.71 : 0.4966, 2.72 : 0.4967, 2.73 : 0.4968, 2.74 : 0.4969, 2.75 : 0.4970, 2.76 : 0.4971, 2.77 : 0.4972, 2.78 : 0.4973, 2.79 : 0.4974,
2.80 : 0.4974, 2.81 : 0.4975, 2.82 : 0.4976, 2.83 : 0.4977, 2.84 : 0.4977, 2.85 : 0.4978, 2.86 : 0.4979, 2.87 : 0.4979, 2.88 : 0.4980, 2.89 : 0.4981,
2.90 : 0.4981, 2.91 : 0.4982, 2.92 : 0.4982, 2.93 : 0.4983, 2.94 : 0.4984, 2.95 : 0.4984, 2.96 : 0.4985, 2.97 : 0.4985, 2.98 : 0.4986, 2.99 : 0.4986,
3.00 : 0.4987, 3.01 : 0.4987, 3.02 : 0.4987, 3.03 : 0.4988, 3.04 : 0.4988, 3.05 : 0.4989, 3.06 : 0.4989, 3.07 : 0.4989, 3.08 : 0.4990, 3.09 : 0.4990,
3.10 : 0.4999}

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():

	if request.method == 'POST':

		if request.form['form'] == 'discreta':
			dados_brutos = data_to_rol(request.form['dados'].encode('UTF8').split())
			discreta = Discreta()
			discreta.xi = insert_xi(dados_brutos)
			discreta.fi = insert_fi(dados_brutos)
			discreta.Efi = insert_Efi(discreta.fi)
			discreta.fr = insert_fr(discreta.fi, discreta.Efi)
			discreta.F = insert_F(discreta.fi)
			discreta.Fr = insert_Fr(discreta.fr)
			discreta.xi_fi = insert_xi_fi(discreta.xi, discreta.fi)
			discreta.Exi_fi = insert_Exi_fi(discreta.xi_fi)
			discreta.moda = insert_moda(discreta.xi, discreta.fi)
			discreta.lines = len(discreta.xi)
			return render_template('discreta.html', statistic=discreta, rol=dados_brutos)
		elif request.form['form'] == 'continua':
			dados_brutos = data_to_rol(request.form['dados'].encode('UTF8').split())
			continua = Continua()
			continua.fi = insert_fi(dados_brutos)
			continua.Efi = insert_Efi(continua.fi)
			continua.insert_at(dados_brutos)
			continua.insert_k(dados_brutos, continua.Efi)
			continua.insert_intervalo_do_xi(dados_brutos, continua.at, continua.k)
			continua.insert_fi_do_intervalo(dados_brutos, continua.xi, continua.ic)
			continua.fr = insert_fr(continua.new_fi, continua.Efi)
			continua.F = insert_F(continua.new_fi)
			continua.Fr = insert_Fr(continua.fr)
			continua.xi_fi = insert_xi_fi(continua.xi, continua.new_fi)
			continua.Exi_fi = insert_Exi_fi(continua.xi_fi)
			continua.lines = (len(continua.new_fi) - 1)
			return render_template('continua.html', statistic=continua, rol=dados_brutos)
		elif request.form['form'] == 'desvio_padrao':
			dados_brutos = data_to_rol(request.form['dados'].encode('UTF8').split())
			desvio_padrao = DesvioPadrao()
			desvio_padrao.xi = insert_xi(dados_brutos)
			desvio_padrao.fi = insert_fi(dados_brutos)
			desvio_padrao.Efi = insert_Efi(desvio_padrao.fi)
			desvio_padrao.xi_fi = insert_xi_fi(desvio_padrao.xi, desvio_padrao.fi)
			desvio_padrao.Exi_fi = insert_Exi_fi(desvio_padrao.xi_fi)
			desvio_padrao.insert_soma(dados_brutos, desvio_padrao.Exi_fi, desvio_padrao.Efi)
			desvio_padrao.lines  = len(desvio_padrao.xi)
			return render_template('desvio_padrao.html', statistic=desvio_padrao, rol=dados_brutos, math=math)
		elif request.form['form'] == 'distribuicao_normal':
			x = float(request.form['x'])
			media = float(request.form['media'])
			desvio_padrao = float(request.form['desvio_padrao'])
			z = float((x - media) / desvio_padrao)
			dn = get_dn(abs(z))
			return render_template('distribuicao_normal.html', x=x, media=media, desvio_padrao=desvio_padrao, z=z, dn=dn)
		elif request.form['form'] == 'distribuicao_binomial':
			p = float(request.form['p'])
			q = float(request.form['q'])
			n = float(request.form['n'])
			k = float(request.form['k'])
			total = distribuicao_binomial(p, q, n, k)
			return render_template('distribuicao_binomial.html', p=p, q=q, n=n, k=k, total=total, math=math)
		else:
			return """
				<h1>Statistic Calculator Tabajara v1.0 - Flask Edition</h1>
				<br/>
				<h1>Request error!!!</h1>
				"""

def data_to_rol(my_list):
	rol = []

	for x in my_list:
		rol.append(float(x))
	rol.sort()
	return rol

def insert_xi(my_list):
	xi = []

	for x in my_list:
		if xi.count(x) == 0:
			xi.append(x)

	return xi

def insert_fi(my_list):
	fi = []
	xi = []

	for x in my_list:
		if xi.count(x) == 0:
			xi.append(x)
			fi.append(my_list.count(x))

	return fi

def insert_Efi(my_list):
	Efi = 0

	for x in my_list:
		Efi += int(x)

	return Efi

def insert_fr(my_list, list_size):
	fr = []
	num = 0.0

	for x in my_list:
		num = ((float(x) / float(list_size)) * 100)
		fr.append(float("{0:6.2f}".format(num)))

	return fr

def insert_F(my_list):
	F = []
	i = 0

	for x in my_list:
		i += int(x)
		F.append(i)

	return F

def insert_Fr(my_list):
	i = 0
	Fr = []

	for x in my_list:
		i += float(x)
		Fr.append(i)

	return Fr

def insert_xi_fi(my_xi_list, my_fi_list):
	xi_fi = []
	i = len(my_xi_list)

	for x in range(i):
		xi_fi.append(float(my_xi_list[x]) * float(my_fi_list[x]))

	return xi_fi

def insert_Exi_fi(my_list):
	Exi_fi = 0

	for x in my_list:
		Exi_fi += float(x)

	return Exi_fi

def insert_moda(my_xi_list, my_fi_list):
	moda = []
	number = 0
	position = 0

	for x, s in enumerate(my_fi_list):
		if number < s:
			number = s
			position = x
	moda.append(my_xi_list[position])

	if my_fi_list.count(number) > 1:
		number = 0
		position = 0

		for j, t in enumerate(my_fi_list):
			if number <= t:
				if number != moda[len(moda)-1]:
					number = t
					position = j
		moda.append(my_xi_list[position])
	return moda

def distribuicao_binomial(p, q, n, k):
	total = 0.0
	fn = math.factorial(n)
	fk = math.factorial(k)
	fn_k = math.factorial(n-k)
	total = (fn / (fk * fn_k)) * (p ** k) * (q ** (n - k))
	return total

def get_dn(z):
	dn = table[z]
	return dn

class Discreta(object):
	lines = 0
	Efi = 0
	xi = []
	fi = []
	fr = []
	F = []
	Fr = []
	xi_fi = []
	Exi_fi = 0
	moda = []

	def __init__(self):
		self.lines = 0
		self.Efi = 0
		self.xi = []
		self.fi = []
		self.fr = []
		self.F = []
		self.Fr = []
		self.xi_fi = []
		self.Exi_fi = 0
		self.moda = []


class Continua(object):
	indice = 0
	fi = []
	Efi = 0
	xmax = 0.0
	xmin = 0.0
	at = 0.0
	k = 0.0
	ic = 0.0
	xi = []
	new_fi = []
	fr = []
	F = []
	Fr = []
	xi_fi = []
	Exi_fi = 0
	moda = []

	def __init__(self):
		self.indice = 0
		self.fi = []
		self.xmax = 0
		self.xmin = 0
		self.at = 0.0
		self.k = 0.0
		self.ic = 0.0
		self.Efi = 0
		self.xi = []
		self.new_fi = []
		self.fr = []
		self.F = []
		self.Fr = []
		self.xi_fi = []
		self.Exi_fi = 0
		self.moda = []

	def insert_at(self, my_list):
		at = 0
		at = float(my_list[len(my_list)-1]) - float(my_list[0])
		self.at = at
		self.xmax = float(my_list[len(my_list)-1])
		self.xmin = float(my_list[0])
		return at

	def insert_k(self, my_list, Efi):
		k = 0
		k = round(math.sqrt(float(Efi)))
		self.k = k
		return k

	def insert_intervalo_do_xi(self, my_list, at, k):
		xi = []
		ic = round(float(at) / float(k))
		xi.append(my_list[0])

		for x in range(int(k)):
			if x != my_list[0]:
				xi.append(int(xi[len(xi) - 1]) + float(ic))

		while True:
			if xi[len(xi) - 1] <= my_list[len(my_list) - 1]:
				xi.append(int(xi[len(xi) - 1]) + float(ic))
			else:
				break

		self.xi = xi
		self.ic = ic
		return xi

	def insert_fi_do_intervalo(self, my_list, xi, ic):
		new_fi = []
		first_num = 0.0
		second_num = 0.0

		first_num = my_list[0]

		for y in xi:
			counter = 0
			second_num = first_num + ic

			for x in my_list:
				if x >= first_num:
					if x < second_num:
						counter += 1

			new_fi.append(counter)
			first_num = second_num

		self.new_fi = new_fi
		return new_fi


class DesvioPadrao(object):
	lines = 0
	xi = []
	fi = []
	Efi = 0
	xi_fi = 0
	Exi_fi = 0
	soma = 0

	def __init__(self):
		self.lines = 0
		self.xi = []
		self.fi = []
		self.Efi = 0
		self.xi_fi = 0
		self.Exi_fi = 0
		self.soma = 0

	def insert_soma(self, my_list, Exi_fi, Efi):
		soma = 0

		for x in my_list:
			soma += ((float(x) - (Exi_fi/Efi)) ** 2)

		self.soma = round(soma, 4)
		return round(soma, 4)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True)
	#app.run(host='0.0.0.0', port=port)
