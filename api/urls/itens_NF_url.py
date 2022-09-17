from ..entidades import item_NF
from ..views import itens_NF_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('itens_NFs', __name__)

@app.route('/api/itens_NFs/', methods=['GET', 'POST'])
def url_geral_itens_NF():
    if (request.method == "GET"):
        return itens_NF_view.itens_NF_view().getAll()
    if (request.method == "POST"):
        itens_NFTemp = item_NF.itens_NF(
            quantidade=request.json["quantidade"],
            preco=request.json["preco"]
        )

        return itens_NF_view.itens_NF_view().post(itens_NFTemp)


@app.route('/api/itens_NFs/<int:id>/', methods=['GET', 'POST'])
def url_unico_itens_NF(id):
    if request.method == 'GET':
        return itens_NF_view.itens_NF_view().get(id)
    if request.method == 'POST':
        itens_NFTemp = item_NF.itens_NF(
            codigo=id,
            quantidade=request.json["quantidade"],
            preco=request.json["preco"]
        )
        return itens_NF_view.itens_NF_view().patch(id, itens_NFTemp)
    else:
        return make_response({}, 404)
