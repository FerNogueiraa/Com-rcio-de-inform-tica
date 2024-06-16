from controllers.menuControllers import menuHtmlController

def menuRoutes(app):
    app.route('/resultadoPesquisaProduto', methods=['GET', 'POST'])(menuHtmlController)