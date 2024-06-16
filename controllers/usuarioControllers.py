from flask import request, render_template, jsonify #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.usuario import Usuario


#Irá rodar o pag WEB a fim de exibir o CRUD do banco
def usuarioHtmlController():
    if request.method == 'GET':
         return render_template('FrontEnd/cadastroUsuario.html')
    return render_template('FrontEnd/cadastroUsuario.html')


#Essa função contém o CRUD completo da tabela "usuario"
def usuarioController():

    # POST
    # ----------------------------------------------------------------------------------------------------------------------------------
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Usuario(data['codigo'], data['nome'], data['login'], data['senha'])
                db.session.add(user)
                db.session.commit()  #manda as informações para o banco de dados
                return 'Usuário criada com sucesso', 200
            except Exception as e:
                return 'Não foi possível criar um novo usuário{}'.format(str(e)), 405
    

    #GET
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'GET':
        try:
            codigo = request.args.get('codigo')
            nome = request.args.get('nome')
            login = request.args.get('login')
            senha = request.args.get('senha')
            query = Usuario.query

            if codigo:
                query = query.filter_by(codigo=codigo)
            if nome:
                query = query.filter(Usuario.nome.like(f"%{nome}%"))
                query = query.filter(Usuario.login.like(f"%{login}%"))
                query = query.filter(Usuario.senha.like(f"%{senha}%"))

            usuario = query.all()
            results = [{'codigo': cat.codigo, 'nome': cat.nome, 'login': cat.login, 'senha': cat.senha} for cat in usuario]
            return jsonify(results), 200
        except Exception as e:
            return 'Erro ao buscar por usuários: {}'.format(str(e)), 405
    

    # PUT
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'PUT':
          try:
              id_usuario = int(request.args.to_dict().get('codigo'))
              data = request.get_json()
              print(id_usuario)

              usuario = Usuario.query.get(id_usuario)
              if usuario is None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'Usuario não encontrada'}, 404
              print(data)
              #Se não, os campos de codigo e descrição são atualizados com novas informações digitadas pelo usuário
              usuario.nome = data.get('nome', usuario.nome)
              usuario.login = data.get('login', usuario.login)
              usuario.senha = data.get('senha', usuario.senha)
              print(usuario.codigo, usuario.nome, usuario.login, usuario.senha)
              db.session.commit() #Finaliza o processo
              return {
                   "message": "Usuario atualizado com sucesso",
                   "status": 200
              }
          except Exception as e:
              return 'Não foi possível atualizar o usuário. ERRO:{}'.format(str(e)),405


    # DELETE
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'DELETE':
        try:
            data = int(request.args.to_dict().get('codigo'))
            usuario = Usuario .query.get(data)
            if usuario is None: 
                return {'error': 'Classificação não encontrada'}, 404
            db.session.delete(usuario)
            db.session.commit()
            return 'Usuario deletada com sucesso', 200
        except Exception as e:
            return 'Não foi possível deletar o usuario. ERRO: {}'.format(str(e)), 405 