from flask import make_response, Blueprint
from ..entidades import faturista
from ..services import faturistas_service

#views = Blueprint('views', __name__)

class faturistas_view():
    def getAll(self):
        faturistass = faturistas_service.getAll()
        if faturistass is not None:
            faturistassJson = [faturistas.toJson() for faturistas in faturistass]

            return make_response(faturistassJson, 200)
        else:
            return make_response({}, 200)

    def post(self, faturistas):
        if faturistas_service.cadastrar(faturistas):
            return make_response(faturistas_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        faturistas = faturistas_service.get(id)
        if faturistas is not None:
            return make_response(faturistas.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, faturistas):
        faturistas_service.editar(codigo=id, faturistas=faturistas)
        return make_response(faturistas.toJson(), 201)