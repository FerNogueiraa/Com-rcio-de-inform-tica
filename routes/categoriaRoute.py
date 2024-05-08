from controllers.categoriaControllers import categoriaController, categoriaHtmlController

#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def categoriaRoutes(app):
    app.route('/**********', methods=['GET'])(categoriaHtmlController)
    app.route('/cargos', methods=['GET', 'POST', 'PUT', 'DELETE'])(categoriaController)
    #Aqui, dependendo do método citado, a função "cargosRoutes" irá exibir/modificar o Banco