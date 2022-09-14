from flask import make_response, Blueprint
from ..entidades import tabela_de_precos
from ..services import tabela_de_preco_service

#views = Blueprint('views', __name__)

class tabela_de_precos_view():
    def getAll(self):
        tabela_de_precos = tabela_de_preco_service.getAll()
        if tabela_de_precos is not None:
            tabela_de_precos_Json = [servicos.toJson() for servicos in tabela_de_precos]

            return make_response(tabela_de_precos_Json, 200)
        else:
            return make_response({}, 200)

    def post(self, servicos):
        if tabela_de_preco_service.cadastrar(servicos):
            return make_response(tabela_de_preco_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        tabela_de_preco = tabela_de_preco_service.get(id)
        if tabela_de_preco is not None:
            return make_response(tabela_de_preco.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, servicos):
        tabela_de_preco_service.editar(codigo=id, tabela_de_precos=tabela_de_precos)
        return make_response(servicos.toJson(), 201)