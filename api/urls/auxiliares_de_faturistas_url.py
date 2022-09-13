from ..entidades import auxiliares_de_faturistas
from ..views import auxiliares_de_faturistas_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('auxiliares_de_faturistas', __name__)

@app.route('/api/auxiliares_de_faturistas/', methods=['GET', 'POST'])
def url_geral_auxiliares_de_faturistas():
    if (request.method == "GET"):
        return auxiliares_de_faturistas_view.auxiliares_de_faturistas_view().getAll()
    if (request.method == "POST"):
        auxiliares_de_faturistasTemp = auxiliares_de_faturistas.auxiliares_de_faturistas(
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )

        return auxiliares_de_faturistas_view.auxiliares_de_faturistas_view().post(auxiliares_de_faturistasTemp)


@app.route('/api/auxiliares_de_faturistas/<int:id>/', methods=['GET', 'POST'])
def url_unico_auxiliares_de_faturistas(id):
    if request.method == 'GET':
        return auxiliares_de_faturistas_view.auxiliares_de_faturistas_view().get(id)
    if request.method == 'POST':
        auxiliares_de_faturistasTemp = auxiliares_de_faturistas.auxiliares_de_faturistas(
            codigo=id,
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )
        return auxiliares_de_faturistas_view.auxiliares_de_faturistas_view().patch(id, auxiliares_de_faturistasTemp)
    else:
        return make_response({}, 404)
