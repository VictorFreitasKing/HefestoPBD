from flask import make_response, Blueprint
from ..entidades import item_OS
from ..services import item_OS_service

#views = Blueprint('views', __name__)

class item_OS_view():
    def getAll(self):
        item_OSs = item_OS_service.getAll()
        if item_OSs is not None:
            item_OSsJson = [item_OS.toJson() for item_OS in item_OSs]

            return make_response(item_OSsJson, 200)
        else:
            return make_response({}, 200)

    def post(self, item_OS):
        if item_OS_service.cadastrar(item_OS):
            return make_response(item_OS_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        item_OS = item_OS_service.get(id)
        if item_OS is not None:
            return make_response(item_OS.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, item_OS):
        item_OS_service.editar(codigo=id, item_OS=item_OS)
        return make_response(item_OS.toJson(), 201)