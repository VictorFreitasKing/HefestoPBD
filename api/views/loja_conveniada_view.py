import json
from flask import make_response, Blueprint
from ..entidades import loja_conveniada
from ..services import loja_conveniada_service

#views = Blueprint('views', __name__)

class loja_conveniada_view():
    def getAll(self):
        lojas_conveniadas = loja_conveniada_service.getAll()
        if lojas_conveniadas is not None:
            loja_conveniadaJson = [lojas_conveniada.toJson() for lojas_conveniada in lojas_conveniadas]

            return make_response(loja_conveniadaJson, 200)
        else:
            return make_response({}, 200)

    def post(self, loja_conveniada):
        if loja_conveniada_service.cadastrar(loja_conveniada):
            return make_response(loja_conveniada_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        lojas_conveniadas = loja_conveniada_service.get(id)
        if lojas_conveniadas is not None:
            return make_response(lojas_conveniadas.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, loja_conveniada):
        loja_conveniada_service.editar(codigo=id, loja_conveniada=loja_conveniada)
        return make_response(loja_conveniada.toJson(), 201)