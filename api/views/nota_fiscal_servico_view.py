from flask import make_response, Blueprint
from ..entidades import nota_fiscal_servico
from ..services import nota_fiscal_servico_service

#views = Blueprint('views', __name__)

class notas_fiscais_servico_view():
    def getAll(self):
        notas_fiscais_servicos = nota_fiscal_servico_service.getAll()
        if notas_fiscais_servicos is not None:
            notas_fiscais_servicosJson = [notas_fiscais_servico.toJson() for notas_fiscais_servico in notas_fiscais_servicos]

            return make_response(notas_fiscais_servicosJson, 200)
        else:
            return make_response({}, 200)

    def post(self, notas_fiscais_servico):
        if nota_fiscal_servico_service.cadastrar(notas_fiscais_servico):
            return make_response(nota_fiscal_servico_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        notas_fiscais_servico = nota_fiscal_servico_service.get(id)
        if notas_fiscais_servico is not None:
            return make_response(notas_fiscais_servico.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, notas_fiscais_servico):
        nota_fiscal_servico_service.editar(codigo=id, nota_fiscal_servico=notas_fiscais_servico)
        return make_response(notas_fiscais_servico.toJson(), 201)