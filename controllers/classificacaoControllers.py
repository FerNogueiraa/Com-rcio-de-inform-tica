from flask import request, render_template #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.classificacao import Classificacao


# #Irá rodar o pag WEB a fim de exibir o CRUD do banco
# def classificacaoHtmlController():
#     if request.method == 'GET':
#          return render_template('*******')


#Essa função contém o CRUD completo da tabela "classificacao"
def classificacaoController():


    #Com o método POST, será possível criar uma classificacao com codigo e nome
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Classificacao(data['codigo'], data['nome'])
                db.session.add(user)
                db.session.commit()  #manda as informações para o banco de dados
                return 'Classificação criada com sucesso', 200
            except Exception as e:
                return 'Não foi possível criar uma nova classificação{}'.format(str(e)), 405
    

    #O método GET vai puxar todos as informações da tabela "classificacao" e exibi-las na pag WEB "*******"
    elif request.method == 'GET':
            try:
                    data = Classificacao.query.all()
                    print([classificacao.to_dict() for classificacao in data])
                    return render_template('*******', data={'classificacoes': [classificacao.to_dict() for classificacao in data]}) #Carregando o site
            except Exception as e:
                return 'Não foi possível buscar por classificações. Error: {}'.format(str(e)), 405
    

    #Permite a atualização das informações presentes no banco
    elif request.method == 'PUT':
          try:
              #Incialmente, a classificação será localizado pelo seu código
              data = request.get.json()
              put_classificacao_id = data['codigo']
              classificacao = Classificacao.query.get(put_classificacao_id)
              if classificacao in None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'Classificação não encontrada'}, 404
              #Se não, os campos de codigo e nome são atualizados com novas informações digitadas pelo usuário
              classificacao.codigo = data.get('codigo', classificacao.codigo)
              classificacao.nome = data.get('nome', classificacao.nome)
              print(classificacao.codigo, classificacao.nome)
              db.session.commit() #Finaliza o processo
          except Exception as e:
              return 'Não foi possível atualizar a classificação. ERRO:{}'.format(str(e)),405


    #O DELETE é responsável por remover informações do banco
    elif request.method == 'DELETE':
        try:
             data = request.get.json() 
             delete_classificacao_id = data['codigo'] #Vai deletar a classificacao a partir do codigo informado
             classificacao = Classificacao.query.get(delete_classificacao_id)
             if classificacao in None:
                  return {'error': 'Classificação não encontrada'}, 404 #caso o id seja inválido, um erro é informado
             #Caso contrário, a ação de delete é executada
             db.session.delete(classificacao)
             db.session.commit()
             return 'Classificação deletada com sucesso', 200
        except Exception as e: #Mensagem de erro caso não seja possível concluir a ação
              return 'Não foi possível atualizar a classificação. ERRO:{}'.format(str(e)),405
        