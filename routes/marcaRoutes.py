from controllers.marcaControllers import marcaController
from controllers.marcaControllers import marcaHtmlController

#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def marcaRoutes(app):
    app.route('/', methods=['POST', 'GET', 'DELETE', 'PUT'])(marcaHtmlController)
    app.route('/marca', methods=['POST', 'GET', 'DELETE', 'PUT'])(marcaController)