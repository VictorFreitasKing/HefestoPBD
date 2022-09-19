from flask import make_response, Blueprint
from ..entidades import auxiliar_de_faturista
from ..services import auxiliar_de_faturista_service

#views = Blueprint('views', __name__)

class auxiliares_de_faturistas_view():
    def getAll(self):
        auxiliares_de_faturistas = auxiliar_de_faturista_service.getAll()
        if auxiliares_de_faturistas is not None:
            auxiliares_de_faturistasJson = [auxiliares_de_faturista.toJson() for auxiliares_de_faturista in auxiliares_de_faturistas]

            return make_response(auxiliares_de_faturistasJson, 200)
        else:
            return make_response({}, 200)

    def post(self, auxiliar_de_faturista):
        if auxiliar_de_faturista_service.cadastrar(auxiliar_de_faturista):
            return make_response(auxiliar_de_faturista_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)

    def get(self, id):
        auxiliares_de_faturistas = auxiliar_de_faturista_service.get(id)
        if auxiliares_de_faturistas is not None:
            return make_response(auxiliares_de_faturistas.toJson(), 200)
        else:
            return make_response({}, 200)