from flask import make_response, Blueprint
from ..entidades import etapa_servico
from ..services import etapa_servico_services

#views = Blueprint('views', __name__)

class etapa_servico_view():
    def getAll(self):
        etapa_servico = etapa_servico_services.getAll()
        if etapa_servico is not None:
            etapa_servico_Json = [servicos.toJson() for servicos in etapa_servico]

            return make_response(etapa_servico_Json, 200)
        else:
            return make_response({}, 200)

    def post(self, servicos):
        if etapa_servico_services.cadastrar(servicos):
            return make_response(etapa_servico_services.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        etapa_servico = etapa_servico_services.get(id)
        if etapa_servico is not None:
            return make_response(etapa_servico.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, servicos):
        etapa_servico_services.editar(codigo=id, etapa_servico=etapa_servico)
        return make_response(servicos.toJson(), 201)