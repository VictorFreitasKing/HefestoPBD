from ..entidades import notas_fiscais
from ..views import notas_fiscais_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('notas_fiscaiss', __name__)

@app.route('/api/notas_fiscaiss/', methods=['GET', 'POST'])
def url_geral_notas_fiscais():
    if (request.method == "GET"):
        return notas_fiscais_view.notas_fiscais_view().getAll()
    if (request.method == "POST"):
        notas_fiscaisTemp = notas_fiscais.notas_fiscais(
            total=request.json["total"]
        )

        return notas_fiscais_view.notas_fiscais_view().post(notas_fiscaisTemp)


@app.route('/api/notas_fiscaiss/<int:id>/', methods=['GET', 'POST'])
def url_unico_notas_fiscais(id):
    if request.method == 'GET':
        return notas_fiscais_view.notas_fiscais_view().get(id)
    if request.method == 'POST':
        notas_fiscaisTemp = notas_fiscais.notas_fiscais(
            codigo=id,
            total=request.json["total"],
            numero=request.json["numero"],
            serie=request.json["serie"]
          #  codigoOS=request.json["codigoOS"],
           # codigo_loja_conveniada=request.json["codigo_loja_conveniada"],
            #codigoAuxiliarFaturista=request.json["codigoAuxiliarFaturista"]

        )
        return notas_fiscais_view.notas_fiscais_view().patch(id, notas_fiscaisTemp)
    else:
        return make_response({}, 404)
