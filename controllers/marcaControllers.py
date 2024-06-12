from flask import request, render_template #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.marca import Marca


#Irá rodar o pag WEB a fim de exibir o CRUD do banco
def marcaHtmlController():
    if request.method == 'GET':
         return render_template('CRUDMarca.html')


#Essa função contém o CRUD completo da tabela "marca"
def marcaController():

    # POST
    # ----------------------------------------------------------------------------------------------------------------------------------
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
    


    # GET
    # ----------------------------------------------------------------------------------------------------------------------------------
    # elif request.method == 'GET':
    #     try:
    #         data = int(request.args.to_dict().get('codigo'))
    #         classificacao = Classificacao.query.all(data)
    #         if classificacao is None:  # Usando 'is' para verificar se a categoria é None
    #             return {'error': 'Categoria não encontrada'}, 404
    #         categorias = [{'codigo': categoria.codigo, 'descricao': categoria.descricao} for categoria in data]
    #         print(categorias)
    #     except Exception as e:
    #         return 'Não foi possível buscar pelas categorias. Error: {}'.format(str(e)), 405
    


    # PUT
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'PUT':
          try:
              id_marca = int(request.args.to_dict().get('codigo'))
              data = request.get_json()
              print(id_marca)

              marca = Marca.query.get(id_marca)
              if marca is None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'marca não encontrada'}, 404
              print(data)
              #Se não, os campos de codigo e descrição são atualizados com novas informações digitadas pelo usuário
              marca.nome = data.get('nome', marca.nome)
              print(marca.codigo, marca.nome)
              db.session.commit() #Finaliza o processo
              return {
                   "message": "Marca atualizada com sucesso",
                   "status": 200
              }
          except Exception as e:
              return 'Não foi possível atualizar a Marca. ERRO:{}'.format(str(e)),405



    # DELETE
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'DELETE':
        try:
            data = int(request.args.to_dict().get('codigo'))
            marca = Marca .query.get(data)
            if marca is None: 
                return {'error': 'Classificação não encontrada'}, 404
            db.session.delete(marca)
            db.session.commit()
            return 'Marca deletada com sucesso', 200
        except Exception as e:
            return 'Não foi possível deletar a marca. ERRO: {}'.format(str(e)), 405 
        