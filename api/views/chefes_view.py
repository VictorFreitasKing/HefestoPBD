from flask import make_response, Blueprint
from ..entidades import chefe
from ..services import chefe_service

#views = Blueprint('views', __name__)

class chefes_view():
    def getAll(self):
        chefess = chefe_service.getAll()
        if chefess is not None:
            chefessJson = [chefes.toJson() for chefes in chefess]

            return make_response(chefessJson, 200)
        else:
            return make_response({}, 200)

    def post(self, chefes):
        if chefe_service.cadastrar(chefes):
            return make_response(chefe_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        chefes = chefe_service.get(id)
        if chefes is not None:
            return make_response(chefes.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, chefes):
        chefe_service.editar(codigo=id, chefes=chefes)
        return make_response(chefes.toJson(), 201)