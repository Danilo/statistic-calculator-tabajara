import os
from flask import Flask, request, render_template
app = Flask(__name__)

# 18,26,21,24,26,18,19,21,18,21,24,26,28,26,21,18,19,21,21,20,21,22,18,19,21,22,18,19,21,19
# 1	 18	 6	20.00	6   20.00
# 2	 19	 5	16.67  11   36.67
# 3	 20	 1	 3.33  12   40.00
# 4	 21	 9	30.00  21   70.00
# 5	 22	 2	 6.67  23   76.67
# 6	 24	 2	 6.67  25   83.33
# 7	 26	 4	13.33  29   96.67
# 8	 28	 1	 3.33  30  100.00

# 111,90,121,105,122,61,128,112,128,93,108,138,88,110,112,112,97,128,102,125,87,119,104,116,96,114,107,113,80,113,123,95,115,70,115,101,114,127,92,103,78,118,100,115,116,98,119,72,125,109,79,139,75,109,123,124,108,125,116,83,94,106,117,82,122,99,124,84,91,130
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
	discreta = Discreta()
	discreta.indice = 8
	discreta.xi = [18, 19, 20, 21, 22, 24, 26, 28]
	discreta.fi = [6, 5, 1, 9, 2, 2, 4, 1]
	discreta.fr = [20.00, 16.67, 3.33, 30.00, 6.67, 6.67, 13.33, 3.33]
	discreta.F = [6, 11, 12, 21, 23, 25, 29, 30]
	discreta.Fr = [20.00, 36.67, 40.00, 70.00, 76.67, 83.33, 96.67, 100.00]
	
	continua = Continua()
	continua.indice = 8
	continua.intervalo = [61, 71, 81, 91, 101, 111, 121, 131, 141]
	continua.fi = [2, 5, 6, 10, 12, 18, 15, 02]
	continua.fr = [2.86, 7.14, 8.57, 14.29, 17.14, 25.71, 21.43, 2.86]
	continua.F = [2, 7, 13, 23, 35, 53, 68, 70]
	continua.Fr = [2.86, 10.00, 18.57, 32.86, 50.00, 75.71, 97.14, 100.00]
	
	if request.method == 'POST':
		
		if request.form['form_id'] == 'discreta':
			return render_template('discreta.html', statistic=discreta)
		
		if request.form['form_id'] == 'continua':
			return render_template('continua.html', statistic=continua)

class Discreta(object):
	indice = 0
	xi = []
	fi = []
	fr = []
	F = []
	Fr = []
	
	def __init__(self):
		self.indice = 0
		self.xi = []
		self.fi = []
		self.fr = []
		self.F = []
		self.Fr = []

class Continua(object):
	indice = 0
	intervalo = []
	fi = []
	fr = []
	F = []
	Fr = []
	
	def __init__(self):
		self.indice = 0
		self.intervalo = []
		self.fi = []
		self.fr = []
		self.F = []
		self.Fr = []

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
