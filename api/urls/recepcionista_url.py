from ..entidades import recepcionista
from ..views import recepcionista_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('recepcionistas', __name__)

@app.route('/api/recepcionistas/', methods=['GET', 'POST'])
def url_geral_recepcionistas():
    if (request.method == "GET"):
        return recepcionista_view.recepcionistas_view().getAll()
    if (request.method == "POST"):
        recepcionistaTemp = recepcionista.Recepcionista(
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )

        return recepcionista_view.recepcionistas_view().post(recepcionistaTemp)


@app.route('/api/recepcionistas/<int:id>/', methods=['GET'])
def url_unico_recepcionistas(id):
    if request.method == 'GET':
        return recepcionista_view.recepcionistas_view().get(id)
    else:
        return make_response({}, 404)
