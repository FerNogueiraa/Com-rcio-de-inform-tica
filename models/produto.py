from database.db import db

class Produto(db.model):
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
    descricao  = db.column(db.String(100))
    codCategoria  = db.column(db.Int(5))
    codClassficacao = db.column(db.Int(5))
    codMarca = db.column(db.Int(5))
    preco = db.column(db.String(50))
    foto1 = db.column(db.String(1000))

    def __init__(self, descricao, codCategoria, codClassificacao, codMarca, preco, foto1):
        self.descricao = descricao
        self.codCategoria = codCategoria
        self.codClassificacao = codClassificacao
        self.codMarca = codMarca
        self.preco = preco
        self.foto1 = foto1

    