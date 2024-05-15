from flask import request, render_template #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.produto import Produto


# #Irá rodar o pag WEB a fim de exibir o CRUD do banco
# def produtoHtmlController():
#     if request.method == 'GET':
#          return render_template('*******')


#Essa função contém o CRUD completo da tabela "produto"
def produtoController():


    #Com o método POST, será possível criar um produto colocando as informações na tabela
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Produto(data['codigo'], data['descricao'], data['codCategoria'], data['codClassificacao'], data['codMarca'], data['preco'], data['foto1'])
                db.session.add(user)
                db.session.commit()  #manda as informações para o banco de dados
                return 'Produto cadastrado com sucesso', 200
            except Exception as e:
                return 'Não foi possível criar um novo produto{}'.format(str(e)), 405
    

    #O método GET vai puxar todos as informações da tabela "produto" e exibi-las na pag WEB "*******"
    elif request.method == 'GET':
            try:
                    data = Produto.query.all()
                    print([produto.to_dict() for produto in data])
                    return render_template('*******', data={'produtos': [produto.to_dict() for produto in data]}) #Carregando o site
            except Exception as e:
                return 'Não foi possível pesquisar os produtos cadastrados. Error: {}'.format(str(e)), 405
    

    #Permite a atualização das informações presentes no banco
    elif request.method == 'PUT':
          try:
              #Incialmente, o produto será localizado pelo seu código
              data = request.get.json()
              put_produto_id = data['codigo']
              produto = Produto.query.get(put_produto_id)
              if produto in None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'Produto não encontrado'}, 404
              #Se não, os campos da tabela "produto" serão atualizados com novas informações digitadas
              produto.codigo = data.get('codigo', produto.codigo)
              produto.descricao = data.get('descricao', produto.descricao)
              produto.codCategoria = data.get('codCategoria', produto.codCategoria)
              produto.codClassificacao = data.get('codClassificacao', produto.codClassificacao)
              produto.codMarca = data.get('codMarca', produto.codMarca)
              produto.preco = data.get('preco', produto.preco)
              produto.foto1 = data.get('descricao', produto.descricao)
              print(produto.codigo, produto.descricao, produto.codCategoria, produto.codClassificacao, produto.codMarca, produto.preco, produto.foto1)
              db.session.commit() #Finaliza o processo
          except Exception as e:
              return 'Não foi possível atualizar os produtos. ERRO:{}'.format(str(e)),405


    #O DELETE é responsável por remover informações do banco
    elif request.method == 'DELETE':
        try:
             data = request.get.json() 
             delete_produto_id = data['codigo'] #Vai deletar o produto a partir do codigo informado
             produto = Produto.query.get(delete_produto_id)
             if produto in None:
                  return {'error': 'Produto não encontrado'}, 404 #caso o id seja inválido, um erro é informado
             #Caso contrário, a ação de delete é executada
             db.session.delete(produto)
             db.session.commit()
             return 'Produto deletado com sucesso', 200
        except Exception as e: #Mensagem de erro caso não seja possível concluir a ação
              return 'Não foi possível atualizar o produto. ERRO:{}'.format(str(e)),405