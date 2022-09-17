from flask import make_response, Blueprint
from ..entidades import item_NF
from ..services import itens_NF_service

#views = Blueprint('views', __name__)

class itens_NF_view():
    def getAll(self):
        itens_NFs = itens_NF_service.getAll()
        if itens_NFs is not None:
            itens_NFsJson = [itens_NF.toJson() for itens_NF in itens_NFs]

            return make_response(itens_NFsJson, 200)
        else:
            return make_response({}, 200)

    def post(self, itens_NF):
        if itens_NF_service.cadastrar(itens_NF):
            return make_response(itens_NF_service.get_ultimo().toJson(), 201)
        else:
            return make_response({}, 200)
    def get(self, id):
        itens_NF = itens_NF_service.get(id)
        if itens_NF is not None:
            return make_response(itens_NF.toJson(), 200)
        else:
            return make_response({}, 200)
    def patch(self, id, itens_NF):
        itens_NF_service.editar(codigo=id, itens_NF=itens_NF)
        return make_response(itens_NF.toJson(), 201)