from ..entidades import oficina
from ..views import oficinas_view
from flask import request, Blueprint, make_response, render_template
from api import app

urls = Blueprint('oficinass', __name__)

@app.route('/api/oficinass/', methods=['GET', 'POST'])
def url_geral_oficinas():
    if (request.method == "GET"):
        return oficinas_view.oficinas_view().getAll()
    if (request.method == "POST"):
        oficinasTemp = oficina.oficinas(
            cnpj=request.json["cnpj"],
            razao_social=request.json["razao_social"],
            IE=request.json["IE"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"],
            codigoChefe=request.json["codigoChefe"]
        )

        return oficinas_view.oficinas_view().post(oficinasTemp)


@app.route('/api/oficinass/<int:id>/', methods=['GET', 'POST'])
def url_unico_oficinas(id):
    if request.method == 'GET':
        return oficinas_view.oficinas_view().get(id)
    if request.method == 'POST':
        oficinasTemp = oficina.oficinas(
            codigo=id,
            cnpj=request.json["cnpj"],
            razao_social=request.json["razao_social"],
            IE=request.json["IE"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"],
            codigoChefe=request.json["codigoChefe"]
        )
        return oficinas_view.oficinas_view().patch(id, oficinasTemp)
    else:
        return make_response({}, 404)
