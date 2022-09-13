from flask import make_response, Blueprint
from ..entidades import produto
from ..services import produto_service

#views = Blueprint('views', __name__)

class produto_view():
    def getAll(self):
        produtos = produto_service.getAll()
        if produtos is not None:
            produtosJson = [produto.toJson() for produto in produtos]

            return make_response(produtosJson, 200)
        else:
            return make_response({}, 200)

    def post(self, produto):
        if produto_service.cadastrar(produto):
            return make_response(produto_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        produto = produto_service.get(id)
        if produto is not None:
            return make_response(produto.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, produto):
        produto_service.editar(codigo=id, produto=produto)
        return make_response(produto.toJson(), 201)