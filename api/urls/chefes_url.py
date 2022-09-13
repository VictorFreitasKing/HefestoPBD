from ..entidades import chefes
from ..views import chefes_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('chefes', __name__)

@app.route('/api/chefes/', methods=['GET', 'POST'])
def url_geral_chefes():
    if (request.method == "GET"):
        return chefes_view.chefes_view().getAll()
    if (request.method == "POST"):
        chefesTemp = chefes.chefes(
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )

        return chefes_view.chefes_view().post(chefesTemp)


@app.route('/api/chefes/<int:id>/', methods=['GET', 'POST'])
def url_unico_chefes(id):
    if request.method == 'GET':
        return chefes_view.chefes_view().get(id)
    if request.method == 'POST':
        chefesTemp = chefes.chefes(
            codigo=id,
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )
        return chefes_view.chefes_view().patch(id, chefesTemp)
    else:
        return make_response({}, 404)
