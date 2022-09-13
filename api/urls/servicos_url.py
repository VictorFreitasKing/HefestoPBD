from ..entidades import servicos
from ..views import servicos_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('servicoss', __name__)

@app.route('/api/servicoss/', methods=['GET', 'POST'])
def url_geral_servicos():
    if (request.method == "GET"):
        return servicos_view.servicos_view().getAll()
    if (request.method == "POST"):
        servicosTemp = servicos.servicos(
            descreicao=request.json["descricao"]
        )

        return servicos_view.servicos_view().post(servicosTemp)


@app.route('/api/servicoss/<int:id>/', methods=['GET', 'POST'])
def url_unico_servicos(id):
    if request.method == 'GET':
        return servicos_view.servicos_view().get(id)
    if request.method == 'POST':
        servicosTemp = servicos.servicos(
            codigo=id,
            descreicao=request.json["descricao"]
        )
        return servicos_view.servicos_view().patch(id, servicosTemp)
    else:
        return make_response({}, 404)
