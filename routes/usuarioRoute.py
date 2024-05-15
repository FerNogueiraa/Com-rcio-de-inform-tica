from controllers.usuarioControllers import usuarioController
#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def usuarioRoutes(app):
    # app.route('/**********', methods=['GET'])(usuarioHtmlController)
    app.route('/cargos', methods=['GET', 'POST', 'PUT', 'DELETE'])(usuarioController)
    #Aqui, dependendo do método citado, a função "cargosRoutes" irá exibir/modificar o Banco