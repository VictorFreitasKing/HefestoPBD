from ..entidades import faturista
from ..views import faturistas_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('faturistas', __name__)

@app.route('/api/faturistas/', methods=['GET', 'POST'])
def url_geral_faturistas():
    if (request.method == "GET"):
        return faturistas_view.faturistas_view().getAll()
    if (request.method == "POST"):
        faturistasTemp = faturista.faturistas(
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )

        return faturistas_view.faturistas_view().post(faturistasTemp)


@app.route('/api/faturistas/<int:id>/', methods=['GET', 'POST'])
def url_unico_faturistas(id):
    if request.method == 'GET':
        return faturistas_view.faturistas_view().get(id)
    if request.method == 'POST':
        faturistasTemp = faturista.faturistas(
            codigo=id,
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )
        return faturistas_view.faturistas_view().patch(id, faturistasTemp)
    else:
        return make_response({}, 404)
