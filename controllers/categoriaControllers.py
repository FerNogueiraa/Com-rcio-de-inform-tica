from flask import request, render_template #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.categoria import Categoria


#Irá rodar o pag WEB a fim de exibir o CRUD do banco
def categoriaHtmlController():
    if request.method == 'GET':
         return render_template('CRUDCategoria.html')


#Essa função contém o CRUD completo da tabela "categoria"
def categoriaController():

    # POST
    # ----------------------------------------------------------------------------------------------------------------------------------
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
    

    #O método GET vai puxar todos as informações da tabela "categoria" e exibi-las na pag WEB "teste.html"
    # elif request.method == 'GET':
    #     try:
    #         data = int(request.args.to_dict().get('codigo'))
    #         categoria = Categoria.query.all(data)
    #         if categoria is None:  # Usando 'is' para verificar se a categoria é None
    #             return {'error': 'Categoria não encontrada'}, 404
    #         categorias = [{'codigo': categoria.codigo, 'descricao': categoria.descricao} for categoria in data]
    #         print(categorias)
    #     except Exception as e:
    #         return 'Não foi possível buscar pelas categorias. Error: {}'.format(str(e)), 405
            

    # PUT
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'PUT':
          try:
              #Incialmente, a categoria será localizado pelo seu código
              id_categoria = int(request.args.to_dict().get('codigo'))
              data = request.get_json()
              print(id_categoria)

              categoria = Categoria.query.get(id_categoria)
              if categoria is None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'Categoria não encontrada'}, 404
              print(data)
              #Se não, os campos de codigo e descrição são atualizados com novas informações digitadas pelo usuário
              categoria.descricao = data.get('descricao', categoria.descricao)
              print(categoria.codigo, categoria.descricao)
              db.session.commit() #Finaliza o processo
              return {
                   "message": "Categoria atualizada com sucesso",
                   "status": 200
              }
          except Exception as e:
              return 'Não foi possível atualizar a categoria. ERRO:{}'.format(str(e)),405


    # DELETE
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'DELETE':
        try:
            data = int(request.args.to_dict().get('codigo'))
            categoria = Categoria.query.get(data)
            if categoria is None:  # Usando 'is' para verificar se a categoria é None
                return {'error': 'Categoria não encontrada'}, 404
            # Se a categoria for encontrada, a excluímos
            db.session.delete(categoria)
            db.session.commit()
            return 'Categoria deletada com sucesso', 200
        except Exception as e:
            return 'Não foi possível deletar a categoria. ERRO: {}'.format(str(e)), 405
