from controllers.produtoController import produtoController
#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def produtoRoutes(app):
    # app.route('/**********', methods=['GET'])(produtoHtmlController)
    app.route('/cargos', methods=['GET', 'POST', 'PUT', 'DELETE'])(produtoController)
    #Aqui, dependendo do método citado, a função "cargosRoutes" irá exibir/modificar o Banco