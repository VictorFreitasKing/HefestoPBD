from flask import make_response, Blueprint
from ..entidades import recepcionista
from ..services import recepcionista_service

#views = Blueprint('views', __name__)

class recepcionistas_view():
    def getAll(self):
        recepcionistass = recepcionista_service.getAll()
        if recepcionistass is not None:
            recepcionistassJson = [recepcionistas.toJson() for recepcionistas in recepcionistass]

            return make_response(recepcionistassJson, 200)
        else:
            return make_response({}, 200)

    def post(self, recepcionistas):
        if recepcionista_service.cadastrar(recepcionistas):
            return make_response(recepcionista_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        recepcionistas = recepcionista_service.get(id)
        if recepcionistas is not None:
            return make_response(recepcionistas.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, recepcionistas):
        recepcionista_service.editar(codigo=id, recepcionistas=recepcionistas)
        return make_response(recepcionistas.toJson(), 201)