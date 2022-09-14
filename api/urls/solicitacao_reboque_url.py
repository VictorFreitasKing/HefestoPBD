from ..entidades import solicitacao_reboque
from ..views import solicitacao_reboque_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('solicitacao_reboques', __name__)

@app.route('/api/solicitacao_reboques/', methods=['GET', 'POST'])
def url_geral_solicitacao_reboque():
    if (request.method == "GET"):
        return solicitacao_reboque_view.solicitacao_reboque_view().getAll()
    if (request.method == "POST"):
        solicitacao_reboqueTemp = solicitacao_reboque.solicitacao_reboque(
            latitude=request.json["latitude"],
            longitude=request.json["longitude"]
        )

        return solicitacao_reboque_view.solicitacao_reboque_view().post(solicitacao_reboqueTemp)


@app.route('/api/solicitacao_reboques/<int:id>/', methods=['GET', 'POST'])
def url_unico_solicitacao_reboque(id):
    if request.method == 'GET':
        return solicitacao_reboque_view.solicitacao_reboque_view().get(id)
    if request.method == 'POST':
        solicitacao_reboqueTemp = solicitacao_reboque.solicitacao_reboque(
            codigo=id,
            latitude=request.json["latitude"],
            longitude=request.json["longitude"]
        )
        return solicitacao_reboque_view.solicitacao_reboque_view().patch(id, solicitacao_reboqueTemp)
    else:
        return make_response({}, 404)
