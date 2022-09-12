from flask import make_response, Blueprint
from ..entidades import mecanico
from ..services import mecanico_service

#views = Blueprint('views', __name__)

class mecanico_view():
    def getAll(self):
        mecanicos = mecanico_service.getAll()
        if mecanicos is not None:
            mecanicosJson = [mecanico.toJson() for mecanico in mecanicos]

            return make_response(mecanicosJson, 200)
        else:
            return make_response({}, 200)

    def post(self, mecanico):
        if mecanico_service.cadastrar(mecanico):
            return make_response(mecanico_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        mecanico = mecanico_service.get(id)
        if mecanico is not None:
            return make_response(mecanico.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, mecanico):
        mecanico_service.editar(codigo=id, mecanico=mecanico)
        return make_response(mecanico.toJson(), 201)