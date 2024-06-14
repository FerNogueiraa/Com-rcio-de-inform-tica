from controllers.homeControllers import homeHtmlController

def homeRoutes(app):
    app.route('/',  methods=['GET'])(homeHtmlController)