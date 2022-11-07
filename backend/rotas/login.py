from importacoes import *
from geral.cripto import *

@app.route("/")
def r_login():
    return "Rota padrão de login"

@app.route("/teste", methods = ["GET"])
def teste():
    print("Funcioando")
    resposta = ("Funcionando")
    return resposta

# curl -X POST localhost:5000/login -d '{"login":"lauraprof@gmail.com","senha":"lauraprof123"}' -H 'Content-Type: application/json'
@app.route("/login", methods=['POST'])
def login():
    dados = request.get_json(force=True) # requisita os dados

    login = dados['login']
    senha = dados['senha']
    
    encontrado = Pessoa.query.filter_by(email=login, senha=cifrar(senha)).first()
    
    if encontrado is None: 
        resposta = jsonify({"resultado": "erro", "detalhes":"usuario ou senha incorreto(s)"})
    else:
        access_token = create_access_token(identity=login)
        resposta = jsonify({"resultado":"ok", "detalhes": "TOKEN: "+access_token}) 
    
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta