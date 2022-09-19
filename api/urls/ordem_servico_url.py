from ..entidades import ordem_servico
from ..views import ordem_servico_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('os', __name__)

@app.route('/api/os/', methods=['GET', 'POST'])
def url_geral_OS():
    if (request.method == "GET"):
        return ordem_servico_view.ordem_servico_view.getAll()
    if (request.method == "POST"):
        osTemp = ordem_servico.Ordem_servico(
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
