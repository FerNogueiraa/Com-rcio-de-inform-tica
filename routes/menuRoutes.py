from controllers.menuControllers import menuHtmlController

def menuRoutes(app):
    app.route('/MenuCadastro', methods=['GET', 'POST'])(menuHtmlController)