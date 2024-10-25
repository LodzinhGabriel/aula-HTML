from flask import (Flask, render_template, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/")
def index():
 return render_template('layout.html')

@app.route("/paginainicial", methods=('GET',)) # Assina uma rota
def paginainicial(): # função responsável pela página
 nome = request.args.get('nome') # use seu nome
 return f"""<h1>Página inicial</h1> 
    <p>Oi {nome}, Que nome bonito!</p> 
    <hr>
 """ # HTML retornado

@app.route("/area/<float:largura>/<float:altura>", methods=('GET',)) # Assina uma rota
def area(largura: float, altura: float): # função responsável pela página
 return f"""<h1>Area</h1> 
    <p>Altura: {altura}</p> 
    <p>Largura: {largura}</p>
    <p>Area: {altura * largura}</p>
    <hr>
 """ # HTML retornado

@app.route("/parimpar/<float:numero>", methods=('GET',)) # Assina uma rota
def parimpar(numero: float): # função responsável pela página
 identificador = None
 if numero % 2 == 0:
  identificador = "par"
 else:
  identificador = "impar"
 return f"""<h1>Par e ímpar</h1> 
    <p>Numero: {numero}</p> 
    <p>Este numero é {identificador}.</p>
    <hr>
 """ # HTML retornado

@app.route("/nomesobrenome/<string:nome>/<string:sobrenome>", methods=('GET',)) # Assina uma rota
def nomesobrenome(nome, sobrenome): # função responsável pela página
 return f"""<h1>Citação bibliográfica do nome</h1> 
    <p>{str.upper(sobrenome)}, {str.capitalize(nome)}.</p> 
    <hr>
 """ # HTML retornado

@app.route("/potencia/<float:base>/<float:expoente>")
def potencia(base: float, expoente:float):
  return f"""<h1>Potenciação</h1> 
    <p>Base: {base}</p>
    <p>Expoente: {expoente}</p>
    <p>Resultado: {base**expoente}.</p>
    <hr>
"""
@app.route("/tabuada/")
@app.route("/tabuada/<num>", methods=('GET',))
def tabuada(num = None):
  
  if 'num' in request.args:
   num = int(request.args.get('num')) 

  return render_template('tabuada.html', num=num)

@app.route("/juros")
def juros(i = None, j = None, t = None, d = None):
 
 if 'i' and 'j' and 't' and 'd' in request.args:
   i = int(request.args.get('i'))
   j = int(request.args.get('j'))
   t = int(request.args.get('t'))
   d = int(request.args.get('d'))
 
 return render_template('juros.html', i=i, j=j, t=t, d=d)

@app.route("/login")
def login(email = None, senha = None):
 
 if 'email' and 'senha' in request.args:
   email = request.args.get('email')
   senha = request.args.get('senha')
 
 return render_template('login.html', email=email, senha=senha)

@app.route("/imc")
def imc(peso = None, altura = None):
 
 if 'peso' and 'altura' in request.args:
   peso = float(request.args.get('peso'))
   altura = int(request.args.get('altura')) / 100
 
 return render_template('imc.html', peso=peso, altura=altura)


@app.route("/galeria", methods=('GET',)) # Assina uma rota
def galeria(): # função responsável pela página
 return "<h1>Galeria</h1>" # HTML retornado

@app.route("/contato", methods=('GET',)) # Assina uma rota
def contato(): # função responsável pela página
 return "<h1>Contato</h1>" # HTML retornado

@app.route("/sobre", methods=('GET',)) # Assina uma rota
def sobre(): # função responsável pela página
 return "<h1>Sobre</h1>" # HTML retornado
