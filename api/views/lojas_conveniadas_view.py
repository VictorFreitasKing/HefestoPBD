import json
from flask import make_response, Blueprint
from ..entidades import lojas_conveniadas
from ..services import lojas_conveniadas_service

#views = Blueprint('views', __name__)

class lojas_conveniadas_view():
    def getAll(self):
        lojas_conveniadas = lojas_conveniadas_service.getAll()
        if lojas_conveniadas is not None:
            lojas_conveniadasJson = [lojas_conveniadas.toJson() for lojas_conveniadas in lojas_conveniadas]

            return make_response(lojas_conveniadasJson, 200)
        else:
            return make_response({}, 200)

    def post(self, lojas_conveniadas):
        if lojas_conveniadas_service.cadastrar(lojas_conveniadas):
            return make_response(lojas_conveniadas_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        lojas_conveniadas = lojas_conveniadas_service.get(id)
        if lojas_conveniadas is not None:
            return make_response(lojas_conveniadas.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, lojas_conveniadas):
        lojas_conveniadas_service.editar(codigo=id, lojas_conveniadas=lojas_conveniadas)
        return make_response(lojas_conveniadas.toJson(), 201)