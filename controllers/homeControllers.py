from flask import request, render_template

def homeHtmlController():
    if request.method == 'GET':
         return render_template('FrontEnd/home.html')
    return render_template('FrontEnd/home.html')