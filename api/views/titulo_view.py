from flask import make_response, Blueprint
from ..entidades import titulo
from ..services import titulos_service

#views = Blueprint('views', __name__)

class titulos_view():
    def getAll(self):
        tituloss = titulos_service.getAll()
        if tituloss is not None:
            titulossJson = [titulos.toJson() for titulos in tituloss]

            return make_response(titulossJson, 200)
        else:
            return make_response({}, 200)

    def post(self, titulos):
        if titulos_service.cadastrar(titulos):
            return make_response(titulos_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        titulos = titulos_service.get(id)
        if titulos is not None:
            return make_response(titulos.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, titulos):
        titulos_service.editar(codigo=id, titulo=titulos)
        return make_response(titulos.toJson(), 201)