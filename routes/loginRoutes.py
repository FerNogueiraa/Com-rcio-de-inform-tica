from controllers.loginControllers import loginHtmlController

def loginRoutes(app):
    app.route('/login', methods=['GET', 'POST'])(loginHtmlController)