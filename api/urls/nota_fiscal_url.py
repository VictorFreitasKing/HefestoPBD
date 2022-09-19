from ..entidades import nota_fiscal
from ..views import nota_fiscal_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('notas_fiscais', __name__)

@app.route('/api/notas_fiscais/', methods=['GET', 'POST'])
def url_geral_notas_fiscais():
    if (request.method == "GET"):
        return nota_fiscal_view.notas_fiscais_view().getAll()
    if (request.method == "POST"):
        notas_fiscaisTemp = nota_fiscal.Nota_Fiscal(
            total=request.json["total"]
        )

        return nota_fiscal_view.notas_fiscais_view().post(notas_fiscaisTemp)


@app.route('/api/notas_fiscais/<int:id>/', methods=['GET', 'POST'])
def url_unico_notas_fiscais(id):
    if request.method == 'GET':
        return nota_fiscal_view.notas_fiscais_view().get(id)
    if request.method == 'POST':
        notas_fiscaisTemp = nota_fiscal.Nota_Fiscal(
            codigo=id,
            total=request.json["total"],
            numero=request.json["numero"],
            serie=request.json["serie"]
          #  codigoOS=request.json["codigoOS"],
           # codigo_loja_conveniada=request.json["codigo_loja_conveniada"],
            #codigoAuxiliarFaturista=request.json["codigoAuxiliarFaturista"]

        )
        return nota_fiscal_view.notas_fiscais_view().patch(id, notas_fiscaisTemp)
    else:
        return make_response({}, 404)
