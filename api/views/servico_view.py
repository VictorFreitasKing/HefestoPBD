from flask import make_response, Blueprint
from ..entidades import servico
from ..services import servico_service

#views = Blueprint('views', __name__)

class servicos_view():
    def getAll(self):
        servicos = servico_service.getAll()
        if servicos is not None:
            servicosJson = [servico.toJson() for servico in servicos]

            return make_response(servicosJson, 200)
        else:
            return make_response({}, 200)

    def post(self, servico):
        if servico_service.cadastrar(servico):
            return make_response(servico_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        servicos = servico_service.get(id)
        if servicos is not None:
            return make_response(servicos.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, servico):
        servico_service.editar(codigo=id, servico=servico)
        return make_response(servico.toJson(), 201)