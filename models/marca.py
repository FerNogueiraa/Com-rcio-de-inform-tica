from database.db import db

class Marca(db.model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'nome': self.nome
        }
    codigo = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    nome = db.column(db.String(100))

    def __init__(self, nome):
        self.nome = nome