from flask import request, render_template #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.categoria import Categoria


#Irá rodar o pag WEB a fim de exibir o CRUD do banco
def categoriaHtmlController():
    if request.method == 'GET':
         return render_template('*******')


#Essa função contém o CRUD completo da tabela "categoria"
def categoriaController():


    #Com o método POST, será possível criar uma categoria com codigo e descrição
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Categoria(data['codigo'], data['descricao'])
                db.session.add(user)
                db.session.commit()  #mando as informações para o banco de dados
                return 'Categoria criada com sucesso', 200
            except Exception as e:
                return 'A categoria não foi criada {}'.format(str(e)), 405
    

    #O método GET vai puxar todos as informações da tabela "categoria" e exibi-las na pag WEB "*******"
    elif request.method == 'GET':
            try:
                    data = Categoria.query.all()
                    print([categoria.to_dict() for categoria in data])
                    return render_template('*******', data={'categorias': [categoria.to_dict() for categoria in data]}) #Carregando o site
            except Exception as e:
                return 'Não foi possível buscar pelas categorias. Error: {}'.format(str(e)), 405
    

    #Permite a atualização das informações presentes no banco
    elif request.method == 'PUT':
          try:
              #Incialmente, a categoria será localizado pelo seu código
              data = request.get.json()
              put_categoria_id = data['codigo']
              categoria = Categoria.query.get(put_categoria_id)
              if categoria in None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'Categoria não encontrada'}, 404
              #Se não, os campos de codigo e descrição são atualizados com novas informações digitadas pelo usuário
              categoria.codigo = data.get('codigo', categoria.codigo)
              categoria.descricao = data.get('descricao', categoria.descricao)
              print(categoria.codigo, categoria.descricao)
              db.session.commit() #Finaliza o processo
          except Exception as e:
              return 'Não foi possível atualizar a categoria. ERRO:{}'.format(str(e)),405


    #O DELETE é responsável por remover informações do banco
    elif request.method == 'DELETE':
        try:
             data = request.get.json() 
             delete_categoria_id = data['codigo'] #Vai deletar o categoria a partir do id informado
             categoria = Categoria.query.get(delete_categoria_id)
             if categoria in None:
                  return {'error': 'Categoria não encontrada'}, 404 #caso o id seja inválido, um erro é informado
             #Caso contrário, a ação de delete é executada
             db.session.delete(categoria)
             db.session.commit()
             return 'Categoria deletada com sucesso', 200
        except Exception as e: #Mensagem de erro caso não seja possível concluir a ação
              return 'Não foi possível atualizar a categoria. ERRO:{}'.format(str(e)),405
    