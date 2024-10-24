from flask import (Flask, render_template, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/sobre", methods=('GET',)) # Assina uma rota
def index(): # função responsável pela página
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
 return f"""<h1>Area</h1> 
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

@app.route("/tabuada/<int:num>", methods=['GET'])
def tabuada(num: int):
  return render_template('tabuada.html', num=num)


@app.route("/galeria", methods=('GET',)) # Assina uma rota
def galeria(): # função responsável pela página
 return "<h1>Galeria</h1>" # HTML retornado

@app.route("/contato", methods=('GET',)) # Assina uma rota
def contato(): # função responsável pela página
 return "<h1>Contato</h1>" # HTML retornado

@app.route("/sobre", methods=('GET',)) # Assina uma rota
def sobre(): # função responsável pela página
 return "<h1>Sobre</h1>" # HTML retornado
