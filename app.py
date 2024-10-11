from flask import (Flask, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): # função responsável pela página
 nome = request.args.get('nome') # use seu nome
 return f"""<h1>Página inicial</h1> 
    <p>Oi {nome}, Que nome bonito!</p> 
    <hr>
 """ # HTML retornado

@app.route("/area", methods=('GET',)) # Assina uma rota
def area(): # função responsável pela página
 altura = float(request.args.get('a'))  # use seu nome
 largura = float(request.args.get('l')) # use seu nome
 return f"""<h1>Area</h1> 
    <p>Altura: {altura}</p> 
    <p>Largura: {largura}</p>
    <p>Area: {altura * largura}</p>
    <hr>
 """ # HTML retornado

@app.route("/parimpar", methods=('GET',)) # Assina uma rota
def parimpar(): # função responsável pela página
 numero = float(request.args.get('n'))  # use seu nome
 identificador = None
 if numero % 2 == 0:
  identificador = "par"
 else:
  identificador = "impar"
 return f"""<h1>Area</h1> 
    <p>Numero: {numero}</p> 
    <p>Este numero é {identificador}.</p>
    <hr>
 """ # HTML retornado

@app.route("/nomesobrenome", methods=('GET',)) # Assina uma rota
def nomesobrenome(): # função responsável pela página
 nome = request.args.get('nome')  # use seu nome
 sobrenome = request.args.get('sobrenome') # use seu nome
 return f"""<h1>Citação bibliográfica do nome</h1> 
    <p>{str.upper(sobrenome)}, {str.capitalize(nome)}.</p> 
    <hr>
 """ # HTML retornado



@app.route("/galeria", methods=('GET',)) # Assina uma rota
def galeria(): # função responsável pela página
 return "<h1>Galeria</h1>" # HTML retornado

@app.route("/contato", methods=('GET',)) # Assina uma rota
def contato(): # função responsável pela página
 return "<h1>Contato</h1>" # HTML retornado

@app.route("/sobre", methods=('GET',)) # Assina uma rota
def sobre(): # função responsável pela página
 return "<h1>Sobre</h1>" # HTML retornado