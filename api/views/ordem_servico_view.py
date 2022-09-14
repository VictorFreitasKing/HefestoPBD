from flask import make_response, Blueprint
from ..entidades import ordem_servico
from ..services import ordem_servico_service

#views = Blueprint('views', __name__)

class ordem_servico_view():
    def getAll(self):
        ordem_servicos = ordem_servico_service.getAll()
        if ordem_servicos is not None:
            ordem_servicosJson = [ordem_servico.toJson() for ordem_servico in ordem_servicos]

            return make_response(ordem_servicosJson, 200)
        else:
            return make_response({}, 200)

    def post(self, ordem_servico):
        if ordem_servico_service.cadastrar(ordem_servico):
            return make_response(ordem_servico_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        ordem_servico = ordem_servico_service.get(id)
        if ordem_servico is not None:
            return make_response(ordem_servico.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, ordem_servico):
        ordem_servico_service.editar(codigo=id, ordem_servico=ordem_servico)
        return make_response(ordem_servico.toJson(), 201)