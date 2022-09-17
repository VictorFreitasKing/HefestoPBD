from flask import make_response, Blueprint
from ..entidades import servico
from ..services import servicos_service

#views = Blueprint('views', __name__)

class servicos_view():
    def getAll(self):
        servicoss = servicos_service.getAll()
        if servicoss is not None:
            servicossJson = [servicos.toJson() for servicos in servicoss]

            return make_response(servicossJson, 200)
        else:
            return make_response({}, 200)

    def post(self, servicos):
        if servicos_service.cadastrar(servicos):
            return make_response(servicos_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        servicos = servicos_service.get(id)
        if servicos is not None:
            return make_response(servicos.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, servicos):
        servicos_service.editar(codigo=id, servicos=servicos)
        return make_response(servicos.toJson(), 201)