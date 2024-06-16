from controllers.usuarioControllers import usuarioController
from controllers.usuarioControllers import usuarioHtmlController

#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def usuarioRoutes(app):
    app.route('/usuario', methods=['POST', 'GET', 'DELETE', 'PUT'])(usuarioHtmlController)
    app.route('/api/usuario', methods=['POST', 'GET', 'DELETE', 'PUT'])(usuarioController)
