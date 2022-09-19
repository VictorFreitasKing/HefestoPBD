from ..entidades import faturista
from ..views import faturista_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('faturistas', __name__)

@app.route('/api/faturistas/', methods=['GET', 'POST'])
def url_geral_faturistas():
    if (request.method == "GET"):
        return faturista_view.faturistas_view().getAll()
    if (request.method == "POST"):
        faturistasTemp = faturista.Faturista(
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )

        return faturista_view.faturistas_view().post(faturistasTemp)


@app.route('/api/faturistas/<int:id>/', methods=['GET'])
def url_unico_faturistas(id):
    if request.method == 'GET':
        return faturista_view.faturistas_view().get(id)
    else:
        return make_response({}, 404)
