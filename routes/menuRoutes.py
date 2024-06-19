from controllers.menuControllers import menuHtmlController

def menuRoutes(app):
    app.route('/menuCadastro', methods=['GET', 'POST'])(menuHtmlController) 