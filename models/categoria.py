from database.db import db

class Categoria(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'descricao': self.descricao
        }
    codigo = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    descricao = db.Column(db.String(100))

    def __init__(self, codigo, descricao):
        self.descricao = descricao,
        self.codigo = codigo