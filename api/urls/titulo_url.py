from ..entidades import titulo
from ..views import titulo_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('tituloss', __name__)

@app.route('/api/tituloss/', methods=['GET', 'POST'])
def url_geral_titulos():
    if (request.method == "GET"):
        return titulo_view.titulos_view().getAll()
    if (request.method == "POST"):
        titulosTemp = titulo.titulos(
            valor=request.json["valor"],
            vencimento=request.json["vencimento"],
            data_baixa=request.json["data_baixa"]
        )

        return titulo_view.titulos_view().post(titulosTemp)


@app.route('/api/tituloss/<int:id>/', methods=['GET', 'POST'])
def url_unico_titulos(id):
    if request.method == 'GET':
        return titulo_view.titulos_view().get(id)
    if request.method == 'POST':
        titulosTemp = titulo.titulos(
            codigo=id,
            valor=request.json["valor"],
            vencimento=request.json["vencimento"],
            data_baixa=request.json["data_baixa"]
        )
        return titulo_view.titulos_view().patch(id, titulosTemp)
    else:
        return make_response({}, 404)
