from flask import make_response, Blueprint
from ..entidades import veiculo
from ..services import veiculos_service

#views = Blueprint('views', __name__)

class veiculos_view():
    def getAll(self):
        veiculoss = veiculos_service.getAll()
        if veiculoss is not None:
            veiculossJson = [veiculos.toJson() for veiculos in veiculoss]

            return make_response(veiculossJson, 200)
        else:
            return make_response({}, 200)

    def post(self, veiculos):
        if veiculos_service.cadastrar(veiculos):
            return make_response(veiculos_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        veiculos = veiculos_service.get(id)
        if veiculos is not None:
            return make_response(veiculos.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, veiculos):
        veiculos_service.editar(codigo=id, veiculos=veiculos)
        return make_response(veiculos.toJson(), 201)