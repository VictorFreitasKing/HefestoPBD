from flask import make_response, Blueprint
from ..entidades import faturista
from ..services import faturista_service

#views = Blueprint('views', __name__)

class faturistas_view():
    def getAll(self):
        faturistas = faturista_service.getAll()
        if faturistas is not None:
            faturistasJson = [faturista.toJson() for faturista in faturistas]

            return make_response(faturistasJson, 200)
        else:
            return make_response({}, 200)

    def post(self, faturista):
        if faturista_service.cadastrar(faturista):
            return make_response(faturista_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        faturistas = faturista_service.get(id)
        if faturistas is not None:
            return make_response(faturistas.toJson(), 200)
        else:
            return make_response({}, 200)