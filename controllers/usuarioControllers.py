from flask import request, render_template #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.usuario import Usuario


# #Irá rodar o pag WEB a fim de exibir o CRUD do banco
# def usuarioHtmlController():
#     if request.method == 'GET':
#          return render_template('*******')


#Essa função contém o CRUD completo da tabela "usuario"
def usuarioController():


    #Com o método POST, será possível criar um usuario com codigo, nome, login e senha
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Usuario(data['codigo'], data['nome'], data['login'], data['senha'])
                db.session.add(user)
                db.session.commit()  #manda as informações para o banco de dados
                return 'Usuário cadastrado com sucesso', 200
            except Exception as e:
                return 'Não foi possível criar um novo usuário{}'.format(str(e)), 405
    

    #O método GET vai puxar todos as informações da tabela "usuario" e exibi-las na pag WEB "*******"
    elif request.method == 'GET':
            try:
                    data = Usuario.query.all()
                    print([usuario.to_dict() for usuario in data])
                    return render_template('*******', data={'usuarios': [usuario.to_dict() for usuario in data]}) #Carregando o site
            except Exception as e:
                return 'Não foi possível pesquisar os usuário cadastrados. Error: {}'.format(str(e)), 405
    

    #Permite a atualização das informações presentes no banco
    elif request.method == 'PUT':
          try:
              #Incialmente, o usuário será localizado pelo seu código
              data = request.get.json()
              put_usuario_id = data['codigo']
              usuario = Usuario.query.get(put_usuario_id)
              if usuario in None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'Usuário não encontrado'}, 404
              #Se não, os campos de codigo, nome, login e senha serão atualizados com novas informações digitadas
              usuario.codigo = data.get('codigo', usuario.codigo)
              usuario.nome = data.get('nome', usuario.nome)
              usuario.login = data.get('login', usuario.login)
              usuario.senha = data.get('senha', usuario.senha)
              print(usuario.codigo, usuario.nome, usuario.login, usuario.senha)
              db.session.commit() #Finaliza o processo
          except Exception as e:
              return 'Não foi possível atualizar os usuários cadastrados. ERRO:{}'.format(str(e)),405


    #O DELETE é responsável por remover informações do banco
    elif request.method == 'DELETE':
        try:
             data = request.get.json() 
             delete_usuario_id = data['codigo'] #Vai deletar a usuario a partir do codigo informado
             usuario = Usuario.query.get(delete_usuario_id)
             if usuario in None:
                  return {'error': 'Usuário não encontrado'}, 404 #caso o id seja inválido, um erro é informado
             #Caso contrário, a ação de delete é executada
             db.session.delete(usuario)
             db.session.commit()
             return 'Cadastro de usuário deletado com sucesso', 200
        except Exception as e: #Mensagem de erro caso não seja possível concluir a ação
              return 'Não foi possível atualizar as informações do usuário. ERRO:{}'.format(str(e)),405
    