from flask import make_response, Blueprint
from ..entidades import veiculo
from ..services import veiculos_service

#views = Blueprint('views', __name__)

class veiculos_view():
    def getAll(self):
        veiculoss = veiculos_service.getAll()
        if veiculoss is not None:
            veiculosJson = [veiculos.toJson() for veiculos in veiculoss]

            return make_response(veiculosJson, 200)
        else:
            return make_response({}, 200)

    def post(self, veiculo):
        if veiculos_service.cadastrar(veiculo):
            return make_response(veiculos_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        veiculo = veiculos_service.get(id)
        if veiculo is not None:
            return make_response(veiculo.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, veiculo):
        veiculos_service.editar(codigo=id, veiculo=veiculo)
        return make_response(veiculo.toJson(), 201)