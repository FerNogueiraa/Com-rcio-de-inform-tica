from database.db import db

class Produto(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'descricao': self.descricao,
            'codCategoria': self.codCategoria,
            'codClassificacao': self.codClassificacao,
            'codMarca': self.codMarca,
            'preco': self.preco,
            'foto1': self.foto1,
        }
    codigo = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    descricao  = db.Column(db.String(100))
    codCategoria  = db.Column(db.Integer)
    codClassficacao = db.Column(db.Integer)
    codMarca = db.Column(db.Integer)
    preco = db.Column(db.String(50))
    foto1 = db.Column(db.String(1000))

    def __init__(self, descricao, codCategoria, codClassificacao, codMarca, preco, foto1):
        self.descricao = descricao
        self.codCategoria = codCategoria
        self.codClassificacao = codClassificacao
        self.codMarca = codMarca
        self.preco = preco
        self.foto1 = foto1

    