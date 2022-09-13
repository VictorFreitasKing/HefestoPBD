from ..entidades import recepcionistas
from ..views import recepcionistas_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('recepcionistas', __name__)

@app.route('/api/recepcionistas/', methods=['GET', 'POST'])
def url_geral_recepcionistas():
    if (request.method == "GET"):
        return recepcionistas_view.recepcionistas_view().getAll()
    if (request.method == "POST"):
        recepcionistasTemp = recepcionistas.recepcionistas(
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )

        return recepcionistas_view.recepcionistas_view().post(recepcionistasTemp)


@app.route('/api/recepcionistas/<int:id>/', methods=['GET', 'POST'])
def url_unico_recepcionistas(id):
    if request.method == 'GET':
        return recepcionistas_view.recepcionistas_view().get(id)
    if request.method == 'POST':
        recepcionistasTemp = recepcionistas.recepcionistas(
            codigo=id,
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )
        return recepcionistas_view.recepcionistas_view().patch(id, recepcionistasTemp)
    else:
        return make_response({}, 404)
