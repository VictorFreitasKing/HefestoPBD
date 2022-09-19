from ..entidades import auxiliar_de_faturista
from ..views import auxiliar_de_faturista_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('auxiliares_de_faturistas', __name__)

@app.route('/api/auxiliares_de_faturistas/', methods=['GET', 'POST'])
def url_geral_auxiliares_de_faturistas():
    if (request.method == "GET"):
        return auxiliar_de_faturista_view.auxiliares_de_faturistas_view().getAll()
    if (request.method == "POST"):
        auxiliares_de_faturistasTemp = auxiliar_de_faturista.Auxiliar_de_Faturista(
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )

        return auxiliar_de_faturista_view.auxiliares_de_faturistas_view().post(auxiliares_de_faturistasTemp)


@app.route('/api/auxiliares_de_faturistas/<int:id>/', methods=['GET'])
def url_unico_auxiliares_de_faturistas(id):
    if request.method == 'GET':
        return auxiliar_de_faturista_view.auxiliares_de_faturistas_view().get(id)
    else:
        return make_response({}, 404)
