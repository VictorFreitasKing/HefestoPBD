from ..entidades import loja_conveniada
from ..views import loja_conveniada_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('loja_conveniada', __name__)

@app.route('/api/loja_conveniada/', methods=['GET', 'POST'])
def url_geral_lojas_conveniadas():
    if (request.method == "GET"):
        return loja_conveniada_view.loja_conveniada_view().getAll()
    if (request.method == "POST"):
        lojas_conveniadasTemp = loja_conveniada.Loja_Conveniada(
            cnpj=request.json["cnpj"],
            razao_social=request.json["razao_social"],
            IE=request.json["IE"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"],
            inicio_vigencia=request.json["inicio_vigencia"],
            fim_vigencia=request.json["fim_vigencia"]
        )

        return loja_conveniada_view.loja_conveniada_view().post(lojas_conveniadasTemp)


@app.route('/api/loja_conveniada/<int:id>/', methods=['GET', 'POST'])
def url_unico_lojas_conveniadas(id):
    if request.method == 'GET':
        return loja_conveniada_view.loja_conveniada_view().get(id)
    if request.method == 'POST':
        lojas_conveniadasTemp = loja_conveniada.Loja_Conveniada(
            razao_social=request.json["razao_social"],
            cnpj=request.json["cnpj"],
            IE=request.json["IE"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"],
            inicio_vigencia=request.json["inicio_vigencia"],
            fim_vigencia=request.json["fim_vigencia"]
        )
        return loja_conveniada_view.loja_conveniada_view().patch(id, lojas_conveniadasTemp)
    else:
        return make_response({}, 404)
