from ..entidades import oficina
from ..views import oficina_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('oficinas', __name__)

@app.route('/api/oficinas/', methods=['GET', 'POST'])
def url_geral_oficinas():
    if (request.method == "GET"):
        return oficina_view.oficinas_view().getAll()
    if (request.method == "POST"):
        oficinaTemp = oficina.Oficina(
            codigoChefe=request.json["codigoChefe"],
            razao_social=request.json["razao_social"],
            cnpj=request.json["cnpj"],
            IE=request.json["IE"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"]
        )

        return oficina_view.oficinas_view().post(oficinaTemp)


@app.route('/api/oficinas/<int:id>/', methods=['GET', 'POST'])
def url_unico_oficinas(id):
    if request.method == 'GET':
        return oficina_view.oficinas_view().get(id)
    if request.method == 'POST':
        oficinaTemp = oficina.Oficina(
            codigoChefe=request.json["codigoChefe"],
            razao_social=request.json["razao_social"],
            cnpj=request.json["cnpj"],
            IE=request.json["IE"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"]
        )
        return oficina_view.oficinas_view().patch(id, oficinaTemp)
    else:
        return make_response({}, 404)
