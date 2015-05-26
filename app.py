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

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():

	if request.method == 'POST':

		if len(request.form['dados']) == 0:
			return """
				<h1>Statistic Calculator Tabajara v1.0 - Flask Edition</h1>
				<br/>
				<h1>Data error!!!</h1>
				"""

		if request.form['form_id'] == 'discreta':
			dados_brutos = data_to_rol(request.form['dados'].encode('UTF8').split())
			discreta = Discreta()
			discreta.insert_xi(dados_brutos)
			discreta.fi = insert_fi(dados_brutos)
			discreta.Efi = insert_Efi(discreta.fi)
			discreta.fr = insert_fr(discreta.fi, discreta.Efi)
			discreta.F = insert_F(discreta.fi)
			discreta.Fr = insert_Fr(discreta.fr)
			discreta.xi_fi = insert_xi_fi(discreta.xi, discreta.fi)
			discreta.Exi_fi = insert_Exi_fi(discreta.xi_fi)
			discreta.insert_moda(discreta.xi, discreta.fi)
			discreta.lines = len(discreta.xi)
			return render_template('discreta.html', statistic=discreta, rol=dados_brutos)
		elif request.form['form_id'] == 'continua':
			dados_brutos = data_to_rol(request.form['dados'].encode('UTF8').split())
			continua = Continua()
			continua.fi = insert_fi(dados_brutos)
			continua.Efi = insert_Efi(continua.fi)
			continua.insert_at(dados_brutos)
			continua.insert_k(dados_brutos, continua.Efi)
			continua.insert_xi(dados_brutos, continua.at, continua.k)
			continua.insert_new_fi(dados_brutos, continua.xi, continua.ic)
			continua.fr = insert_fr(continua.new_fi, continua.Efi)
			continua.F = insert_F(continua.new_fi)
			continua.Fr = insert_Fr(continua.fr)
			continua.xi_fi = insert_xi_fi(continua.xi, continua.new_fi)
			continua.Exi_fi = insert_Exi_fi(continua.xi_fi)
			continua.lines = (len(continua.new_fi) - 1)
			return render_template('continua.html', statistic=continua, rol=dados_brutos)
		elif request.form['form_id'] == 'desvio_padrao':
			dados_brutos = data_to_rol(request.form['dados'].encode('UTF8').split())
			desvio_padrao = DesvioPadrao()
			desvio_padrao.insert_xi(dados_brutos)
			desvio_padrao.fi = insert_fi(dados_brutos)
			desvio_padrao.Efi = insert_Efi(desvio_padrao.fi)
			desvio_padrao.xi_fi = insert_xi_fi(desvio_padrao.xi, desvio_padrao.fi)
			desvio_padrao.Exi_fi = insert_Exi_fi(desvio_padrao.xi_fi)
			desvio_padrao.insert_soma(dados_brutos, desvio_padrao.Exi_fi, desvio_padrao.Efi)
			desvio_padrao.lines  = len(desvio_padrao.xi)
			return render_template('desvio_padrao.html', statistic=desvio_padrao, rol=dados_brutos)
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

	def insert_xi(self, my_list):
		xi = []

		for x in my_list:
			if xi.count(x) == 0:
				xi.append(x)

		self.xi = xi
		return xi

	def insert_moda(self, my_xi_list, my_fi_list):
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
		self.moda = moda
		return moda


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

	def insert_xi(self, my_list, at, k):
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

	def insert_new_fi(self, my_list, xi, ic):
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

	def insert_xi(self, my_list):
		xi = []

		for x in my_list:
			if xi.count(x) == 0:
				xi.append(x)

		self.xi = xi
		return xi

	def insert_soma(self, my_list, Exi_fi, Efi):
		soma = 0

		for x in my_list:
			soma += ((float(x) - (Exi_fi/Efi)) ** 2)

		self.soma = round(soma, 4)
		return round(soma, 4)

	def do_sqrt(self, number):
		return round(math.sqrt(number), 4)


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True)
	# app.run(host='0.0.0.0', port=port)
