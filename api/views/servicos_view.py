from flask import make_response, Blueprint
from ..entidades import servico
from ..services import servico_service

#views = Blueprint('views', __name__)

class servicos_view():
    def getAll(self):
        servicoss = servico_service.getAll()
        if servicoss is not None:
            servicossJson = [servicos.toJson() for servicos in servicoss]

            return make_response(servicossJson, 200)
        else:
            return make_response({}, 200)

    def post(self, servicos):
        if servico_service.cadastrar(servicos):
            return make_response(servico_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        servicos = servico_service.get(id)
        if servicos is not None:
            return make_response(servicos.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, servicos):
        servico_service.editar(codigo=id, servicos=servicos)
        return make_response(servicos.toJson(), 201)