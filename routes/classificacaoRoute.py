from controllers.classificacaoControllers import classificacaoController

#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def classificacaoRoutes(app):
    # app.route('/**********', methods=['GET'])(classificacaoHtmlController)
    app.route('/cargos', methods=['GET', 'POST', 'PUT', 'DELETE'])(classificacaoController)
    #Aqui, dependendo do método citado, a função "cargosRoutes" irá exibir/modificar o Banco