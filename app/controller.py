from app import app
from models.modelconn import ClienteModel

@app.route('/Cadastrar/', methods=["GET"])

def index():
    return ClienteModel.cadastrarUser()
