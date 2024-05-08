from database.db import db

class Usuario(db.model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'nome': self.nome,
            'login': self.login,
            'senha': self.senha,
        }
    codigo = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    nome = db.column(db.String(100))
    login = db.column(db.String(100))
    senha = db.column(db.String(50))

    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha