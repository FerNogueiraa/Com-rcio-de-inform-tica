from controllers.categoriaControllers import categoriaController

#Método GET: pega alguma informação do Banco de Dados a fim de exibi-la
#Método POST: manda informações para dentro do Banco, podendo criar ou modificar tabelas
def categoriaRoutes(app):
    # app.route('/clientesHTML')(categoriaHtmlController)
    app.route('/categoria', methods=['POST', 'GET', 'PUT', 'DELETE'])(categoriaController)

    #Aqui, dependendo do método citado, a função "categoriaRoutes" irá exibir/modificar o Banco

