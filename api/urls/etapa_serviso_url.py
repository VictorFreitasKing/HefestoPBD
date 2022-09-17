from ..entidades import servico
from ..views import servicos_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('etapa_servico', __name__)

@app.route('/api/etapa_servico/', methods=['GET', 'POST'])
def url_geral_etapa_servico():
    if (request.method == "GET"):
        return servicos_view.servicos_view().getAll()
    if (request.method == "POST"):
        servicosTemp = servico.servicos(
            descricao=request.json["descricao"]
        )

        return servicos_view.servicos_view().post(servicosTemp)


@app.route('/api/etapa_servico/<int:id>/', methods=['GET', 'POST'])
def url_unico_etapa_servico(id):
    if request.method == 'GET':
        return servicos_view.servicos_view().get(id)
    if request.method == 'POST':
        servicosTemp = servico.servicos(
            codigo=id,
            descricao=request.json["descricao"]
        )
        return servicos_view.servicos_view().patch(id, servicosTemp)
    else:
        return make_response({}, 404)
