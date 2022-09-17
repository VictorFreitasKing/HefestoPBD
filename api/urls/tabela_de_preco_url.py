from ..entidades import servico
from ..views import tabelas_de_precos_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('tabelas_de_precos', __name__)

@app.route('/api/tabelas_de_precos/', methods=['GET', 'POST'])
def url_geral_tabelas_de_precos():
    if (request.method == "GET"):
        return tabelas_de_precos_view.tabelas_de_precos_view().getAll()
    if (request.method == "POST"):
        tabelas_de_precosTemp = tabelas_de_precos_view.tabelas_de_precos(
            preco=request.json["preco"],
            inicio=request.json["inicio"],
            fim=request.json["fim"]
        )

        return tabelas_de_precos_view.tabelas_de_precos_view().post(tabelas_de_precosTemp)


@app.route('/api/tabelas_de_precos/<int:id>/', methods=['GET', 'POST'])
def url_unico_tabelas_de_precos(id):
    if request.method == 'GET':
        return tabelas_de_precos_view.tabelas_de_precos_view().get(id)
    if request.method == 'POST':
        tabelas_de_precosTemp = tabelas_de_precos.tabelas_de_precos(
            codigo=id,
            preco=request.json["preco"],
            inicio=request.json["inicio"],
            fim=request.json["fim"]
        )
        return tabelas_de_precos_view.servicos_view().patch(id, tabelas_de_precosTemp)
    else:
        return make_response({}, 404)
