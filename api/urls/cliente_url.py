from ..entidades import cliente
from ..views import cliente_view
from flask import request, Blueprint, make_response, render_template
from api import app

urls = Blueprint('clientes', __name__)

@app.route('/api/clientes/', methods=['GET', 'POST'])
def url_geral_cliente():
    if (request.method == "GET"):
        return cliente_view.Cliente_view().getAll()
    if (request.method == "POST"):
        clienteTemp = cliente.Cliente(
            nome=request.json["nome"],
            cpf=request.json["cpf"],
            rg=request.json["rg"],
            telefone=request.json["telefone"],
            celular=request.json["celular"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"],
            tipo=request.json["tipo"]
        )

        return cliente_view.Cliente_view().post(clienteTemp)


@app.route('/api/clientes/<int:id>/', methods=['GET', 'POST'])
def url_unico_cliente(id):
    if request.method == 'GET':
        return cliente_view.Cliente_view().get(id)
    if request.method == 'POST':
        clienteTemp = cliente.Cliente(
            codigo=id,
            nome=request.json["nome"],
            cpf=request.json["cpf"],
            rg=request.json["rg"],
            telefone=request.json["telefone"],
            celular=request.json["celular"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"],
            tipo=request.json["tipo"]
        )
        return cliente_view.Cliente_view().patch(id, clienteTemp)
    else:
        return make_response({}, 404)
