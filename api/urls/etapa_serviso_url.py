from ..entidades import etapa_servico
from ..views import etapa_servico_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('etapa_servico', __name__)

@app.route('/api/etapas_servico/', methods=['GET', 'POST'])
def url_geral_etapa_servico():
    if (request.method == "GET"):
        return etapa_servico_view.etapa_servico_view().getAll()
    if (request.method == "POST"):
        etapasTemp = etapa_servico.Etapa_Servico(
            descricao=request.json["descricao"]
        )

        return etapa_servico_view.etapa_servico_view().post(servicosTemp)


@app.route('/api/etapas_servico/<int:id>/', methods=['GET', 'POST'])
def url_unico_etapa_servico(id):
    if request.method == 'GET':
        return etapa_servico_view.etapa_servico_view().get(id)
    if request.method == 'POST':
        servicosTemp = etapa_servico.Etapa_Servico(
            codigo=id,
            descricao=request.json["descricao"]
        )
        return etapa_servico_view.etapa_servico_view().patch(id, servicosTemp)
    else:
        return make_response({}, 404)
