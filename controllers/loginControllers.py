from flask import render_template, request, redirect, url_for, flash
from database.db import db
from models.usuario import Usuario

def loginHtmlController():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        
        # Verificação no banco de dados
        user = Usuario.query.filter_by(login=login, senha=senha).first()
        if user:
            # Login bem-sucedido
            return redirect(url_for('menuHtmlController'))
        else:
            # Login falhou
            flash('Login ou senha incorretos')
            return redirect(url_for('loginHtmlController'))
    return render_template('FrontEnd/login.html')
