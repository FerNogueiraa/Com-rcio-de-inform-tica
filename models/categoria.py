from database.db import db

class Categoria(db.model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'descricao': self.descricao
        }
    codigo = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    descricao = db.column(db.String(100))

    def __init__(self, descricao):
        self.descricao = descricao