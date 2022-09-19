from flask import make_response, Blueprint
from ..entidades import chefe
from ..services import chefe_service

#views = Blueprint('views', __name__)

class chefe_view():
    def getAll(self):
        chefes = chefe_service.getAll()
        if chefes is not None:
            chefesJson = [chefe.toJson() for chefe in chefes]
            return make_response(chefesJson, 200)
        else:
            return make_response({}, 200)

    def post(self, chefe):
        if chefe_service.cadastrar(chefe):
            return make_response(chefe_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        chefes = chefe_service.get(id)
        if chefes is not None:
            return make_response(chefes.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, chefe):
        chefe_service.editar(codigo=id, chefe=chefe)
        return make_response(chefe.toJson(), 201)