import json
from flask import make_response, Blueprint
from ..entidades import cliente
from ..services import cliente_service

#views = Blueprint('views', __name__)

class Cliente_view():
    def getAll(self):
        clientes = cliente_service.getAll()
        if clientes is not None:
            clientesJson = [cliente.toJson() for cliente in clientes]

            return make_response(clientesJson, 200)
        else:
            return make_response({}, 200)

    def post(self, cliente):
        if cliente_service.cadastrar(cliente):
            return make_response(cliente_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        cliente = cliente_service.get(id)
        if cliente is not None:
            return make_response(cliente.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, cliente):
        cliente_service.editar(codigo=id, cliente=cliente)
        return make_response(cliente.toJson(), 201)