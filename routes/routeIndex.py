#Importação de todos os Routes criados, pois esse é o arquivo que vai gerenciar todos os outros
from routes.categoriaRoutes import categoriaRoutes
from routes.classificacaoRoutes import classificacaoRoutes
from routes.marcaRoutes import marcaRoutes
from routes.produtoRoutes import produtoRoutes
from routes.usuarioRoutes import usuarioRoutes

from routes.homeRoutes import homeRoutes
from routes.loginRoutes import loginRoutes
from routes.menuRoutes import menuRoutes


def routeIndex(app):
    homeRoutes(app=app)
    loginRoutes(app=app)
    menuRoutes(app=app)

    categoriaRoutes(app=app)
    classificacaoRoutes(app=app)
    marcaRoutes(app=app)
    usuarioRoutes(app=app)
    produtoRoutes(app=app)

    
 