from controllers.classificacaoControllers import classificacaoController
from controllers.classificacaoControllers import classificacaoHtmlController

#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def classificacaoRoutes(app):
    app.route('/', methods=['POST', 'GET', 'DELETE', 'PUT'])(classificacaoHtmlController)
    app.route('/classificacao', methods=['POST', 'GET', 'DELETE', 'PUT'])(classificacaoController)