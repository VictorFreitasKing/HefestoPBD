from ..entidades import veiculos
from ..views import veiculos_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('veiculoss', __name__)

@app.route('/api/veiculoss/', methods=['GET', 'POST'])
def url_geral_veiculos():
    if (request.method == "GET"):
        return veiculos_view.veiculos_view().getAll()
    if (request.method == "POST"):
        veiculosTemp = veiculos.veiculos(
            placa=request.json["placa"],
            marca=request.json["marca"],
            modelo=request.json["modelo"]
        )

        return veiculos_view.veiculos_view().post(veiculosTemp)


@app.route('/api/veiculoss/<int:id>/', methods=['GET', 'POST'])
def url_unico_veiculos(id):
    if request.method == 'GET':
        return veiculos_view.veiculos_view().get(id)
    if request.method == 'POST':
        veiculosTemp = veiculos.veiculos(
            codigo=id,
            placa=request.json["placa"],
            marca=request.json["marca"],
            modelo=request.json["modelo"]
        )
        return veiculos_view.veiculos_view().patch(id, veiculosTemp)
    else:
        return make_response({}, 404)
