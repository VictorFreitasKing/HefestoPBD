from flask import make_response, Blueprint
from ..entidades import auxiliar_de_faturista
from ..services import auxiliar_de_faturista_service

#views = Blueprint('views', __name__)

class auxiliares_de_faturistas_view():
    def getAll(self):
        auxiliares_de_faturistass = auxiliar_de_faturista_service.getAll()
        if auxiliares_de_faturistass is not None:
            auxiliares_de_faturistassJson = [auxiliares_de_faturistas.toJson() for auxiliares_de_faturistas in auxiliares_de_faturistass]

            return make_response(auxiliares_de_faturistassJson, 200)
        else:
            return make_response({}, 200)

    def post(self, auxiliares_de_faturistas):
        if auxiliar_de_faturista_service.cadastrar(auxiliares_de_faturistas):
            return make_response(auxiliar_de_faturista_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        auxiliares_de_faturistas = auxiliar_de_faturista_service.get(id)
        if auxiliares_de_faturistas is not None:
            return make_response(auxiliares_de_faturistas.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, auxiliares_de_faturistas):
        auxiliar_de_faturista_service.editar(codigo=id, auxiliares_de_faturistas=auxiliares_de_faturistas)
        return make_response(auxiliares_de_faturistas.toJson(), 201)