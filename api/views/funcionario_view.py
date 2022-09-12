import json
from flask import make_response, Blueprint
from ..entidades import funcionario
from ..services import funcionario_service

#views = Blueprint('views', __name__)

class Funcionario_view():
    def getAll(self):
        funcionarios = funcionario_service.getAll()
        if funcionarios is not None:
            funcionarios = [funcionario.toJson() for funcionario in funcionarios]

            return make_response(funcionarios, 200)
        else:
            return make_response({}, 200)

    def post(self, funcionario):
        if funcionario_service.cadastrar(funcionario):
            return make_response(funcionario_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        funcionario = funcionario_service.get(id)
        if funcionario is not None:
            return make_response(funcionario.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, funcionario):
        funcionario_service.editar(matricula=id, funcionario=funcionario)
        return make_response(funcionario.toJson(), 201)