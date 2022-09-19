from ..entidades import veiculo
from ..views import veiculo_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('veiculos', __name__)

@app.route('/api/veiculo/', methods=['GET', 'POST'])
def url_geral_veiculos():
    if (request.method == "GET"):
        return veiculo_view.veiculos_view().getAll()
    if (request.method == "POST"):
        veiculoTemp = veiculo.Veiculo(
            placa=request.json["placa"],
            marca=request.json["marca"],
            modelo=request.json["modelo"]
        )

        return veiculo_view.veiculos_view().post(veiculoTemp)


@app.route('/api/veiculo/<int:id>/', methods=['GET', 'POST'])
def url_unico_veiculos(id):
    if request.method == 'GET':
        return veiculo_view.veiculos_service.get(id)
    if request.method == 'POST':
        veiculosTemp = veiculo.Veiculo(
            codigo=id,
            placa=request.json["placa"],
            marca=request.json["marca"],
            modelo=request.json["modelo"]
        )
        return veiculo_view.veiculos_view().patch(id, veiculosTemp)
    else:
        return make_response({}, 404)
