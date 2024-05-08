from controllers.marcaControllers import marcaController, marcaHtmlController

#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def marcaRoutes(app):
    app.route('/**********', methods=['GET'])(marcaHtmlController)
    app.route('/cargos', methods=['GET', 'POST', 'PUT', 'DELETE'])(marcaController)
    #Aqui, dependendo do método citado, a função "cargosRoutes" irá exibir/modificar o Banco