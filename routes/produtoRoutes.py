from controllers.produtoController import produtoController
from controllers.produtoController import produtoHtmlController

#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def produtoRoutes(app):
    app.route('/', methods=['POST', 'GET', 'DELETE', 'PUT'])(produtoHtmlController)
    app.route('/produto', methods=['POST', 'GET', 'DELETE', 'PUT'])(produtoController)