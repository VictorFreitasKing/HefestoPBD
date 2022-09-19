from flask import make_response, Blueprint
from ..entidades import recepcionista
from ..services import recepcionista_service

#views = Blueprint('views', __name__)

class recepcionistas_view():
    def getAll(self):
        recepcionistas = recepcionista_service.getAll()
        if recepcionistas is not None:
            recepcionistasJson = [recepcionistas.toJson() for recepcionistas in recepcionistas]

            return make_response(recepcionistasJson, 200)
        else:
            return make_response({}, 200)

    def post(self, recepcionista):
        if recepcionista_service.cadastrar(recepcionista):
            return make_response(recepcionista_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        recepcionistas = recepcionista_service.get(id)
        if recepcionistas is not None:
            return make_response(recepcionistas.toJson(), 200)
        else:
            return make_response({}, 200)