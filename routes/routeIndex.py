#Importação de todos os Routes criados, pois esse é o arquivo que vai gerenciar todos os outros
from routes.categoriaRoute import categoriaRoutes
from routes.classificacaoRoute import classificacaoRoutes
from routes.marcaRoute import marcaRoutes
from routes.produtoRoute import produtoRoutes
from routes.usuarioRoute import usuarioRoutes

def routeIndex(app):
    categoriaRoutes(app=app)
    classificacaoRoutes(app=app)
    marcaRoutes(app=app)
    produtoRoutes(app=app)
    usuarioRoutes(app=app)
 