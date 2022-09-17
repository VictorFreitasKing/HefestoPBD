import json
from flask import make_response, Blueprint
from ..entidades import oficina
from ..services import oficinas_service

#views = Blueprint('views', __name__)

class oficinas_view():
    def getAll(self):
        oficinas = oficinas_service.getAll()
        if oficinas is not None:
            oficinasJson = [oficinas.toJson() for oficinas in oficinas]

            return make_response(oficinasJson, 200)
        else:
            return make_response({}, 200)

    def post(self, oficinas):
        if oficinas_service.cadastrar(oficinas):
            return make_response(oficinas_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        oficinas = oficinas_service.get(id)
        if oficinas is not None:
            return make_response(oficinas.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, oficinas):
        oficinas_service.editar(codigo=id, oficinas=oficinas)
        return make_response(oficinas.toJson(), 201)