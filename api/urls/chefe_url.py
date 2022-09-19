from ..entidades import chefe
from ..views import chefe_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('chefes', __name__)

@app.route('/api/chefes/', methods=['GET', 'POST'])
def url_geral_chefes():
    if (request.method == "GET"):
        return chefe_view.chefe_view().getAll()
    if (request.method == "POST"):
        chefeTemp = chefe.Chefe(
            matriculaFuncionario=request.json["matriculaFuncionario"]
        )
        return chefe_view.chefe_view().post(chefeTemp)


@app.route('/api/chefes/<int:id>/', methods=['GET', 'POST'])
def url_unico_chefes(id):
    if request.method == 'GET':
        return chefe_view.chefe_view().get(id)
    if request.method == 'POST':
        chefeTemp = chefe.Chefe(
            codigo=id,
            matriculaFuncionario=request.json["matriculaFuncionario"],
        )
        return chefe_view.chefe_view().patch(id, chefeTemp)
    else:
        return make_response({}, 404)
