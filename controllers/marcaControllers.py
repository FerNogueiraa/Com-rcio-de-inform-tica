from flask import request, render_template #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.marca import Marca


#Irá rodar o pag WEB a fim de exibir o CRUD do banco
def marcaHtmlController():
    if request.method == 'GET':
         return render_template('*******')


#Essa função contém o CRUD completo da tabela "marca"
def marcaController():


    #Com o método POST, será possível criar uma marca com codigo e nome
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Marca(data['codigo'], data['nome'])
                db.session.add(user)
                db.session.commit()  #manda as informações para o banco de dados
                return 'Marca criada com sucesso', 200
            except Exception as e:
                return 'Não foi possível criar uma nova marca{}'.format(str(e)), 405
    

    #O método GET vai puxar todos as informações da tabela "marca" e exibi-las na pag WEB "*******"
    elif request.method == 'GET':
            try:
                    data = Marca.query.all()
                    print([marca.to_dict() for marca in data])
                    return render_template('*******', data={'marcas': [marca.to_dict() for marca in data]}) #Carregando o site
            except Exception as e:
                return 'Não foi possível pesquisar as marcas. Error: {}'.format(str(e)), 405
    

    #Permite a atualização das informações presentes no banco
    elif request.method == 'PUT':
          try:
              #Incialmente, a marca será localizado pelo seu código
              data = request.get.json()
              put_marca_id = data['codigo']
              marca = Marca.query.get(put_marca_id)
              if marca in None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'Marca não encontrada'}, 404
              #Se não, os campos de codigo e nome são atualizados com novas informações digitadas pelo usuário
              marca.codigo = data.get('codigo', marca.codigo)
              marca.nome = data.get('nome', marca.nome)
              print(marca.codigo, marca.nome)
              db.session.commit() #Finaliza o processo
          except Exception as e:
              return 'Não foi possível atualizar as marcas. ERRO:{}'.format(str(e)),405


    #O DELETE é responsável por remover informações do banco
    elif request.method == 'DELETE':
        try:
             data = request.get.json() 
             delete_marca_id = data['codigo'] #Vai deletar a marca a partir do codigo informado
             marca = Marca.query.get(delete_marca_id)
             if marca in None:
                  return {'error': 'Marca não encontrada'}, 404 #caso o id seja inválido, um erro é informado
             #Caso contrário, a ação de delete é executada
             db.session.delete(marca)
             db.session.commit()
             return 'Marca deletada com sucesso', 200
        except Exception as e: #Mensagem de erro caso não seja possível concluir a ação
              return 'Não foi possível atualizar a marca. ERRO:{}'.format(str(e)),405
        