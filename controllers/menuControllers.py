from flask import request, render_template

def menuHtmlController():
    if request.method == 'GET':
         return render_template('FrontEnd/MenuCadastro.html')
    return render_template('FrontEnd/MenuCadastro.html')