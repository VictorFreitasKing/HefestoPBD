import json
from flask import make_response, Blueprint
from ..entidades import oficina
from ..services import oficina_service

#views = Blueprint('views', __name__)

class oficinas_view():
    def getAll(self):
        oficinas = oficina_service.getAll()
        if oficinas is not None:
            oficinaJson = [oficina.toJson() for oficina in oficinas]

            return make_response(oficinaJson, 200)
        else:
            return make_response({}, 200)

    def post(self, oficina):
        if oficina_service.cadastrar(oficina):
            return make_response(oficina_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        oficinas = oficina_service.get(id)
        if oficinas is not None:
            return make_response(oficinas.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, oficina):
        oficina_service.editar(codigo=id, oficina=oficina)
        return make_response(oficina.toJson(), 201)