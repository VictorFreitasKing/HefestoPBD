from ..entidades import loja_conveniada
from ..views import lojas_conveniadas_view
from flask import request, Blueprint, make_response, render_template
from api import app

urls = Blueprint('lojas_conveniadas', __name__)

@app.route('/api/lojas_conveniadas/', methods=['GET', 'POST'])
def url_geral_lojas_conveniadas():
    if (request.method == "GET"):
        return lojas_conveniadas_view.lojas_conveniadas_view().getAll()
    if (request.method == "POST"):
        lojas_conveniadasTemp = loja_conveniada.Lojas_Conveniadas(
            cnpj=request.json["cnpj"],
            razao_social=request.json["razao_social"],
            IE=request.json["IE"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"]
        )

        return lojas_conveniadas_view.lojas_conveniadas_view().post(lojas_conveniadasTemp)


@app.route('/api/lojas_conveniadas/<int:id>/', methods=['GET', 'POST'])
def url_unico_lojas_conveniadas(id):
    if request.method == 'GET':
        return lojas_conveniadas_view.lojas_conveniadas_view().get(id)
    if request.method == 'POST':
        lojas_conveniadasTemp = loja_conveniada.Lojas_Conveniadas(
            codigo=id,
            cnpj=request.json["cnpj"],
            razao_social=request.json["razao_social"],
            IE=request.json["IE"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"]
        )
        return lojas_conveniadas_view.lojas_conveniadas_view().patch(id, lojas_conveniadasTemp)
    else:
        return make_response({}, 404)
