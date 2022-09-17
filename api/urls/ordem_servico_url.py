from ..entidades import veiculo
from ..views import veiculos_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('ordem_servicoss', __name__)

@app.route('/api/os/', methods=['GET', 'POST'])
def url_geral_OS():
    if (request.method == "GET"):
        return veiculos_view.veiculos_view().getAll()
    if (request.method == "POST"):
        veiculosTemp = veiculo.veiculos(
            placa=request.json["placa"],
            marca=request.json["marca"],
            modelo=request.json["modelo"]
        )

        return veiculos_view.veiculos_view().post(veiculosTemp)


@app.route('/api/os/<int:id>/', methods=['GET', 'POST'])
def url_unico_OS(id):
    if request.method == 'GET':
        return veiculos_view.veiculos_view().get(id)
    if request.method == 'POST':
        veiculosTemp = veiculo.veiculos(
            codigo=id,
            placa=request.json["placa"],
            marca=request.json["marca"],
            modelo=request.json["modelo"]
        )
        return veiculos_view.veiculos_view().patch(id, veiculosTemp)
    else:
        return make_response({}, 404)
