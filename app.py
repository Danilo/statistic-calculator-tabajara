import os, math
from flask import Flask, request, render_template
app = Flask(__name__)
# discreta examples
# 3 4 3.5 5 3.5 4 5 5.5 4 5
# 18 26 21 24 26 18 19 21 18 21 24 26 28 26 21 18 19 21 21 20 21 22 18 19 21 22 18 19 21 19

#continua
# 111 90 121 105 122 61 128 112 128 93 108 138 88 110 112 112 97 128 102 125 87 119 104 116 96 114 107 113 80 113 123 95 115 70 115 101 114 127 92 103 78 118 100 115 116 98 119 72 125 109 79 139 75 109 123 124 108 125 116 83 94 106 117 82 122 99 124 84 91 130
# 01  61|--71   02   2.86%  02    2.86%
# 02  71|--81   05   7.14%  07   10.00%
# 03  81|--91   06   8.57%  13   18.57%
# 04  91|--101  10  14.29%  23   32.86%
# 05 101|--111  12  17.14%  35   50.00%
# 06 111|--121  18  25.71%  53   75.71%
# 07 121|--131  15  21.43%  68   97.14%
# 08 131|--141  02   2.86%  70  100.00%

@app.route('/')
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
			discreta.insert_fi(dados_brutos)
			discreta.insert_Efi(discreta.fi)
			discreta.insert_fr(discreta.fi, discreta.Efi)
			discreta.insert_F(discreta.fi)
			discreta.insert_Fr(discreta.fr)
			discreta.insert_media(discreta.xi, discreta.fi)
			discreta.insert_Exi_fi(discreta.media)
			discreta.insert_moda(discreta.xi, discreta.fi)
			discreta.lines = len(discreta.xi)
			return render_template('discreta.html', statistic=discreta, rol=dados_brutos)
		elif request.form['form_id'] == 'continua':
			dados_brutos = data_to_rol(request.form['dados'].encode('UTF8').split())
			continua = Continua()
			continua.indice = 8
			continua.intervalo = [61, 71, 81, 91, 101, 111, 121, 131, 141]
			continua.fi = [2, 5, 6, 10, 12, 18, 15, 02]
			continua.fr = [2.86, 7.14, 8.57, 14.29, 17.14, 25.71, 21.43, 2.86]
			continua.F = [2, 7, 13, 23, 35, 53, 68, 70]
			continua.Fr = [2.86, 10.00, 18.57, 32.86, 50.00, 75.71, 97.14, 100.00]
			return render_template('continua.html', statistic=continua, rol=dados_brutos)
		else:
			return """
				<h1>Statistic Calculator Tabajara v1.0 - Flask Edition</h1>
				<br/>
				<h1>Request error!!!</h1>
				"""

def data_to_rol(my_list):
	rol = []
	
	for x in my_list:
		rol.append(x)
	rol.sort()
	return rol

class Discreta(object):
	lines = 0
	Efi = 0
	xi = []
	fi = []
	fr = []
	F = []
	Fr = []
	media = []
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
		self.media = []
		self.Exi_fi = 0
		self.moda = []

	def insert_xi(self, my_list):
		xi = []
		
		for x in my_list:
			if xi.count(x) == 0:
				xi.append(x)
		
		self.xi = xi
		return xi

	def insert_fi(self, my_list):
		fi = []
		xi = []

		for x in my_list:
			if xi.count(x) == 0:
				xi.append(x)
				fi.append(my_list.count(x))
		
		self.fi = fi
		return fi
	
	def insert_Efi(self, my_list):
		Efi = 0
		
		for x in my_list:
			Efi += int(x)
		
		self.Efi = Efi
		return Efi
	
	def insert_fr(self, my_list, total):
		fr = []
		num = 0.0
		
		for x in my_list:
			num = ((float(x) / float(total)) * 100)
			fr.append(float("{0:6.2f}".format(num)))
		
		self.fr = fr
		return fr
	
	def insert_F(self, my_list):
		F = []
		i = 0
		
		for x in my_list:
			i += int(x)
			F.append(i)
		
		self.F = F
		return F
	
	def insert_Fr(self, my_list):
		i = 0
		Fr = []

		for x in my_list:
			i += float(x)
			Fr.append(i)

		self.Fr = Fr
		return Fr
	
	def insert_media(self, my_xi_list, my_fi_list):
		media = []
		i = len(my_xi_list)
		
		for x in range(i):
			media.append(float(my_xi_list[x]) * float(my_fi_list[x]))
		
		self.media = media
		return media
	
	def insert_Exi_fi(self, my_list):
		Exi_fi = 0
		
		for x in my_list:
			Exi_fi += float(x)
		
		self.Exi_fi = Exi_fi
		return Exi_fi
	
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
	at = 0
	fi = []
	k = 0
	fr = []
	F = []
	Fr = []
	
	def __init__(self):
		self.indice = 0
		self.at = 0
		self.fi = []
		self.k
		self.fr = []
		self.F = []
		self.Fr = []
	
	def insert_at(self, my_list):
		at = 0
		at = float(my_list[len(my_list)-1] - my_list[0])
		self.at = at
		return at
	
	def insert_fi(self, my_list):
		fi = []
		xi = []
		
		for x in my_list:
			if xi.count(x) == 0:
				xi.append(x)
				fi.append(my_list.count(x))
		
		self.fi = fi
		return fi
	
	def insert_k(self, my_list):
		k = 0
		total = 0.0
		
		for x in my_list:
			total += float(x)
		k = round(math.sqrt(total))
		self.k = k
		return k
	
	def insert_xi(self, my_list, at, k):
		xi = []
		
		ic = round(at / int(math.sqrt(k)))
		xi.append(my_list[0])
		
		for x in range(int(math.sqrt(k))):
			if x != my_list[0]:
				xi.append(int(xi[len(xi) - 1] + ic))
		
		self.xi = xi
		return xi
	

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	# app.run(debug=True)
	app.run(host='0.0.0.0', port=port)
