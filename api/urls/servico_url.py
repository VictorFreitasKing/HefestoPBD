from ..entidades import servico
from ..views import servico_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('servicoss', __name__)

@app.route('/api/servicoss/', methods=['GET', 'POST'])
def url_geral_servicos():
    if (request.method == "GET"):
        return servico_view.servicos_view().getAll()
    if (request.method == "POST"):
        servicosTemp = servico.servicos(
            descreicao=request.json["descricao"]
        )

        return servico_view.servicos_view().post(servicosTemp)


@app.route('/api/servicoss/<int:id>/', methods=['GET', 'POST'])
def url_unico_servicos(id):
    if request.method == 'GET':
        return servico_view.servicos_view().get(id)
    if request.method == 'POST':
        servicosTemp = servico.servicos(
            codigo=id,
            descreicao=request.json["descricao"]
        )
        return servico_view.servicos_view().patch(id, servicosTemp)
    else:
        return make_response({}, 404)
