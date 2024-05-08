from flask import Flask   
from database.db import db   
from routes import routeIndex


#Faz a conexão com o banco da dados
class MyServer():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/comercioonline' #Caminho para localizar o banco
        db.init_app(self.app)
        routeIndex(self.app)
    def run(self):
        self.app.run(port=3000, debug=True, host='localhost')
    
if __name__ == "__main__":
    app = MyServer() #Inicia o servidor
    app.run