from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Visitantes(db.Model):
	_tablename_= 'visitante'
	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String)
	documentação = db.Column(db.String)
	instituição = db.Column(db.String)
	data = db.Column(db.String)
	entrada = db.Column(db.String)
	saida = db.Column(db.String)

	def __init__(self, nome, documentação, instituição, data, entrada, saida):
		self.nome = nome
		self.documentação = documentação
		self.instituição = instituição
		self.data = data
		self.entrada = entrada
		self.saida = saida

db.create_all()





@app.route('/')
def index():
	return render_template('index.html')



@app.route('/visitantes')
def visitantes():
	all_data = Visitantes.query.all()
	return render_template("visitantes.html", visitantes = all_data)



@app.route('/transportadoras')
def fornecedores():
	return render_template('transportadoras.html')



@app.route("/inserir", methods = ['POST'])
def inserir():

	if request.method == 'POST':
		nome = request.form.get('nome').upper()
		documentação = request.form.get('documentação').upper()
		instituição = request.form.get('instituição').upper()
		data = request.form.get('data').upper()
		entrada = request.form.get('entrada').upper()
		saida = request.form.get('saida').upper()

		dados = Visitantes(nome, documentação, instituição, data, entrada, saida)
		db.session.add(dados)
		db.session.commit()

		flash("Registro salvo com sucesso")

		return redirect(url_for('visitantes'))



@app.route('/atualizar', methods = ['GET', 'POST'])
def atualizar():	
	if request.method == 'POST':
		v = Visitantes.query.get(request.form.get('_id'))

		v.nome = request.form['nome'].upper()
		v.documentação = request.form['documentação'].upper()
		v.instituição = request.form['instituição'].upper()
		v.data = request.form['data'].upper()
		v.entrada = request.form['entrada'].upper()
		v.saida = request.form['saida'].upper()

		db.session.commit()
		flash("Registro Atualizado com Sucesso")

		return redirect(url_for('visitantes'))


@app.route('/deletar/<int:id>')
def deletar(id):
	v = Visitantes.query.get(id)
	db.session.delete(v)
	db.session.commit()

	flash("Registro deletado com sucesso")

	return redirect(url_for('visitantes'))








if __name__=='__main__':
	app.run(debug=True)
