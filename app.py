from flask import (Flask, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): # função responsável pela página
 nome = request.args.get('nome') # use seu nome
 return f"""<h1>Página inicial</h1> 
    <p>Oi {nome}, Que nome bonito!</p> 
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