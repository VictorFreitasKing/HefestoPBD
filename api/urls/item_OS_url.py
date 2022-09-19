from ..entidades import item_OS
from ..views import item_OS_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('item_OSs', __name__)

@app.route('/api/itens_OS/', methods=['GET', 'POST'])
def url_geral_item_OS():
    if (request.method == "GET"):
        return item_OS_view.item_OS_view().getAll()
    if (request.method == "POST"):
        item_OSTemp = item_OS.Item_OS(
            preco=request.json["preco"],
            status=request.json["status"]
        )

        return item_OS_view.item_OS_view().post(item_OSTemp)


@app.route('/api/itens_OS/<int:id>/', methods=['GET', 'POST'])
def url_unico_item_OS(id):
    if request.method == 'GET':
        return item_OS_view.item_OS_view().get(id)
    if request.method == 'POST':
        item_OSTemp = item_OS.Item_OS(
            codigo=id,
            preco=request.json["preco"],
            status=request.json["status"]
        )
        return item_OS_view.item_OS_view().patch(id, item_OSTemp)
    else:
        return make_response({}, 404)
