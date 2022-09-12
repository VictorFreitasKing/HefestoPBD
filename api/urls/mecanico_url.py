from ..entidades import mecanico
from ..views import mecanico_view
from flask import request, Blueprint, make_response
from api import app

urls = Blueprint('mecanicos', __name__)

@app.route('/api/mecanicos/', methods=['GET', 'POST'])
def url_geral_mecanico():
    if (request.method == "GET"):
        return mecanico_view.mecanico_view().getAll()
    if (request.method == "POST"):
        mecanicoTemp = mecanico.Mecanico(
            matriculaFuncionario=request.json["matriculaFuncionario"],
            especialidade=request.json["especialidade"]
        )

        return mecanico_view.mecanico_view().post(mecanicoTemp)


@app.route('/api/mecanicos/<int:id>/', methods=['GET', 'POST'])
def url_unico_mecanico(id):
    if request.method == 'GET':
        return mecanico_view.mecanico_view().get(id)
    if request.method == 'POST':
        mecanicoTemp = mecanico.Mecanico(
            codigo=id,
            matriculaFuncionario=request.json["matriculaFuncionario"],
            especialidade=request.json["especialidade"]
        )
        return mecanico_view.mecanico_view().patch(id, mecanicoTemp)
    else:
        return make_response({}, 404)
