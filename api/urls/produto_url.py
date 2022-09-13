from ..entidades import produto
from ..views import produto_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('produto', __name__)

@app.route('/api/produto/', methods=['GET', 'POST'])
def url_geral_produto():
    if (request.method == "GET"):
        return produto_view.produto_view().getAll()
    if (request.method == "POST"):
        produtoTemp = produto.produto(
            descricao=request.json["descricao"],
        )

        return produto_view.produto_view().post(produtoTemp)


@app.route('/api/produto/<int:id>/', methods=['GET', 'POST'])
def url_unico_produto(id):
    if request.method == 'GET':
        return produto_view.produto_view().get(id)
    if request.method == 'POST':
        produtoTemp = produto.produto(
            codigo=id,
            descricao=request.json["descricao"],
        )
        return produto_view.produto_view().patch(id, produtoTemp)
    else:
        return make_response({}, 404)
