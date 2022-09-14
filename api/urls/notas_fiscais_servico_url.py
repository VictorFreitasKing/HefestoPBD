from ..entidades import notas_fiscais_servico
from ..views import notas_fiscais_servico_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('notas_fiscais_servicos', __name__)

@app.route('/api/notas_fiscais_servicos/', methods=['GET', 'POST'])
def url_geral_notas_fiscais_servico():
    if (request.method == "GET"):
        return notas_fiscais_servico_view.notas_fiscais_servico_view().getAll()
    if (request.method == "POST"):
        notas_fiscais_servicoTemp = notas_fiscais_servico.notas_fiscais_servico(
            data_emissao=request.json["data_emissao"],
            total=request.json["total"]
        )

        return notas_fiscais_servico_view.notas_fiscais_servico_view().post(notas_fiscais_servicoTemp)


@app.route('/api/notas_fiscais_servicos/<int:id>/', methods=['GET', 'POST'])
def url_unico_notas_fiscais_servico(id):
    if request.method == 'GET':
        return notas_fiscais_servico_view.notas_fiscais_servico_view().get(id)
    if request.method == 'POST':
        notas_fiscais_servicoTemp = notas_fiscais_servico.notas_fiscais_servico(
            codigo=id,
            data_emissao=request.json["data_emissao"],
            total=request.json["total"]
        )
        return notas_fiscais_servico_view.notas_fiscais_servico_view().patch(id, notas_fiscais_servicoTemp)
    else:
        return make_response({}, 404)
