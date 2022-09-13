from flask import make_response, Blueprint
from ..entidades import chefes
from ..services import chefes_service

#views = Blueprint('views', __name__)

class chefes_view():
    def getAll(self):
        chefess = chefes_service.getAll()
        if chefess is not None:
            chefessJson = [chefes.toJson() for chefes in chefess]

            return make_response(chefessJson, 200)
        else:
            return make_response({}, 200)

    def post(self, chefes):
        if chefes_service.cadastrar(chefes):
            return make_response(chefes_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        chefes = chefes_service.get(id)
        if chefes is not None:
            return make_response(chefes.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, chefes):
        chefes_service.editar(codigo=id, chefes=chefes)
        return make_response(chefes.toJson(), 201)