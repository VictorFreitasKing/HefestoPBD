from flask import make_response, Blueprint
from ..entidades import nota_fiscal
from ..services import nota_fiscal_service

#views = Blueprint('views', __name__)

class notas_fiscais_view():
    def getAll(self):
        notas_fiscaiss = nota_fiscal_service.getAll()
        if notas_fiscaiss is not None:
            notas_fiscaissJson = [notas_fiscais.toJson() for notas_fiscais in notas_fiscaiss]

            return make_response(notas_fiscaissJson, 200)
        else:
            return make_response({}, 200)

    def post(self, notas_fiscais):
        if nota_fiscal_service.cadastrar(notas_fiscais):
            return make_response(nota_fiscal_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        notas_fiscais = nota_fiscal_service.get(id)
        if notas_fiscais is not None:
            return make_response(notas_fiscais.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, notas_fiscais):
        nota_fiscal_service.editar(codigo=id, notas_fiscais=notas_fiscais)
        return make_response(notas_fiscais.toJson(), 201)