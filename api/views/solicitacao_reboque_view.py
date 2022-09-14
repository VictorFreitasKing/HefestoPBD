from flask import make_response, Blueprint
from ..entidades import solicitacao_reboque
from ..services import solicitacao_reboque_service

#views = Blueprint('views', __name__)

class solicitacao_reboque_view():
    def getAll(self):
        solicitacao_reboques = solicitacao_reboque_service.getAll()
        if solicitacao_reboques is not None:
            solicitacao_reboquesJson = [solicitacao_reboque.toJson() for solicitacao_reboque in solicitacao_reboques]

            return make_response(solicitacao_reboquesJson, 200)
        else:
            return make_response({}, 200)

    def post(self, solicitacao_reboque):
        if solicitacao_reboque_service.cadastrar(solicitacao_reboque):
            return make_response(solicitacao_reboque_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        solicitacao_reboque = solicitacao_reboque_service.get(id)
        if solicitacao_reboque is not None:
            return make_response(solicitacao_reboque.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, solicitacao_reboque):
        solicitacao_reboque_service.editar(codigo=id, solicitacao_reboque=solicitacao_reboque)
        return make_response(solicitacao_reboque.toJson(), 201)